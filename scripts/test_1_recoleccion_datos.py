import os
import time
import json
from datetime import datetime
from typing import List

import pandas as pd
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

# ---------- Config ----------
load_dotenv()

CLIENT_ID      = os.getenv("CLIENT_ID")
CLIENT_SECRET  = os.getenv("CLIENT_SECRET")
REDIRECT_URI   = os.getenv("REDIRECT_URI")
SCOPE          = ("user-read-playback-state "
                  "user-read-currently-playing "
                  "user-modify-playback-state "
                  "user-read-private")
PLAYLIST_URI   = os.getenv("PLAYLIST_URI")
SESSIONS       = int(os.getenv("SESSIONS", "8"))
CSV_BASE_PATH  = os.getenv("CSV_BASE_PATH", "data/raw/1")

sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=True
))

# ---------- Utilidades ----------
def esperar_dispositivo_activo() -> str:
    """Devuelve el device_id activo o levanta excepción si no hay ninguno."""
    devices = sp.devices().get("devices", [])
    if not devices:
        raise RuntimeError("No hay dispositivo activo con la sesion iniciada.")
    # Tomamos el primero; podés filtrar por name/type si querés algo específico
    return devices[0]["id"]

def reproducir_playlist(device_id: str):
    """Inicia la playlist en modo shuffle."""
    sp.shuffle(state=True, device_id=device_id)          # Activa shuffle
    sp.start_playback(device_id=device_id,               # Inicia lista desde cero
                      context_uri=PLAYLIST_URI)          # :contentReference[oaicite:1]{index=1}
    time.sleep(1)  # Pequeño respiro para asegurarnos de que arranque

def registrar_sesion(n: int) -> List[dict]:
    """Captura el orden de 12 temas para la sesión n y la devuelve como lista de dicts."""
    print(f"\nSesion {n}/{SESSIONS} - escuchando...")
    tracks = []
    prev_track_id = None

    while len(tracks) < 12:
        pb = sp.current_playback()
        if not (pb and pb.get("is_playing")):
            raise RuntimeError("La reproduccion se detuvo inesperadamente.")

        item = pb.get("item")
        if item and item["id"] != prev_track_id:
            tracks.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "session": n,
                "position": len(tracks) + 1,
                "track_name": item["name"],
                "artist": item["artists"][0]["name"],
                "album": item["album"]["name"],
                "duration_sec": round(item["duration_ms"] / 1000),
                "popularity": item["popularity"],
                "track_id": item["id"]
            })
            print(f"  {tracks[-1]['position']:02d}. {item['name']} - {item['artists'][0]['name']}")
            prev_track_id = item["id"]

        # Calculamos cuanto falta del track para optimizar el sleep
        remaining_ms = item["duration_ms"] - pb.get("progress_ms", 0)
        time.sleep(max(1, remaining_ms / 1000.0 * 0.5))  # 50 % del resto o al menos 1 s

    return tracks

def guardar_csv(tracks: List[dict], usuario: str):
    dt_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    artista_ref = tracks[0]['artist'].replace(" ", "_").replace("/", "-")
    path = os.path.join(CSV_BASE_PATH, artista_ref, usuario)
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, f"sesion_{dt_str}_{usuario}.csv")
    pd.DataFrame(tracks).to_csv(filename, index=False)
    print(f"CSV guardado en {filename}")

# ---------- Main ----------
def main():
    usuario = sp.current_user()["display_name"]
    device_id = esperar_dispositivo_activo()
    print(f"Analizando cuenta: {usuario}")
    print(f"Dispositivo activo: {device_id}")
    print(f"Playlist objetivo: {PLAYLIST_URI}\n")

    for sesion in range(1, SESSIONS + 1):
        try:
            reproducir_playlist(device_id)
            tracks = registrar_sesion(sesion)
            sp.pause_playback(device_id=device_id)
            guardar_csv(tracks, usuario)
        except Exception as e:
            # Siempre frena la música ante un problema
            try:
                sp.pause_playback(device_id=device_id)
            except Exception:
                pass
            print(f"Sesión {sesion} abortada: {e}")
            break  # salimos; si preferís continuar, reemplazá por 'continue'

    print("\n Prueba finalizada.")

if __name__ == "__main__":
    main()
