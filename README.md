# 🧩 The Spotify Shuffle Experiment
Análisis de la aleatoriedad y sesgos del modo aleatorio de Spotify.

## 🎯 2. Objetivo del proyecto
Evaluar empíricamente si el modo aleatorio (shuffle) de Spotify reproduce canciones de una playlist de forma realmente aleatoria o si existen sesgos en la selección del orden, y si dichos sesgos varían en función del historial de usuario o del dispositivo utilizado.

## 📦 4. Metodología
### 📁 Dataset
Playlist con 75 canciones, armada desde una cuenta neutral.

Canciones variadas en género, artista y época, con duración homogénea.

Mismo orden inicial y sin cambios.

### 👥 Cuentas utilizadas
Cuenta	Descripción
Cuenta A	Cuenta personal con historial
Cuenta B	Cuenta nueva sin historial
Cuenta C	Cuenta neutral (creadora)

### 🧪 Protocolo experimental
10 sesiones de reproducción por cuenta.

Cada sesión reproduce 25 canciones en modo shuffle.

No se interactúa con el reproductor (no se pausan, ni se saltean, ni se repiten canciones).

Cada cuenta se rota entre dos dispositivos distintos (App de escritorio y reproductor web).

### 📝 Registro de datos
Fecha, cuenta, dispositivo

Orden exacto de canciones reproducidas

Tiempos de reproducción (opcional)

## 📚 6. Resultados esperados
Detectar si existe un patrón de repetición o dispersión artificial.

Confirmar si el algoritmo penaliza agrupamientos.

Determinar si hay personalización según el usuario.

## 🧑‍💻 Autor
Ramiro Abadie
