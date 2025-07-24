# 🧩 The Spotify Shuffle Experiment
Análisis de la aleatoriedad y sesgos del modo aleatorio de Spotify.

## 🎯 2. Objetivo del proyecto
Evaluar empíricamente si el modo aleatorio (shuffle) de Spotify reproduce canciones de una playlist de forma realmente aleatoria o si existen sesgos en la selección del orden, y si dichos sesgos varían en función del historial de usuario o del dispositivo utilizado.

## 📦 4. Metodología
Voy a empezar haciendo un solo test llamado Mono-Artista, una playlist con 12 temas de un solo artista, dejando
fijas varias variables (todo esto esta siendo documentado en un excel el cual despues vere si subir)
### 📁 Dataset
Playlist con 12 canciones, armada desde una cuenta neutral.

### 👥 Cuentas utilizadas
Cuenta	Descripción
Cuenta B	Cuenta nueva sin historial
Cuenta C	Cuenta neutral (creadora)

### 🧪 Protocolo experimental
15 sesiones minimas de reproducción por cuenta.

Cada sesión reproduce 12 canciones en modo shuffle.

No se interactúa con el reproductor (no se pausan, ni se saltean, ni se repiten canciones).

### 📝 Registro de datos
Fecha, cuenta, Orden exacto de canciones reproducidas, Tiempos de reproducción, popularidad de la cancion, 
album, artista

## 📚 6. Resultados esperados
Detectar si existe un patrón de repetición o dispersión artificial.

Confirmar si el algoritmo penaliza agrupamientos.

Determinar si hay personalización según el usuario.

## 🧑‍💻 Autor
Ramiro Abadie
