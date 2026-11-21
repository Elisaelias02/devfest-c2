# Desplegar el teamserver de la sala en Cloud Run (T-1h, antes de la charla)

El C2 vive en GCP **antes** de que empiece el workshop. Así los beacons de la
sala viajan por Internet desde el Paso 1 — con HTTPS y dominio `*.run.app`
real, y sin depender de la red local del venue.

```bash
cd c2/
gcloud run deploy c2-sala --source . \
  --region us-central1 --allow-unauthenticated
```

Anota la URL que devuelve (ej. `https://c2-sala-xxxx-uc.a.run.app`):

1. **Panel del proyector**: abre esa URL en el navegador, pantalla completa.
2. **Paso 1**: la sala pone esa URL como `C2` en su `agente.py`.
3. **Slide 04**: reemplaza el placeholder `https://TU-C2.run.app` por la URL real
   (o déjalo y dilo en voz alta — la URL está en el panel que proyectas).

## Plan B

Si el deploy falla o no hay Internet usable: corre `python3 c2.py` local y la
sala apunta a `http://TU-IP-LOCAL:8443` (o cada quien corre su propio `c2.py`
en otra terminal y apunta a `http://localhost:8443` — "felicidades, cada uno
es su propio operador").

## Limpieza post-charla

```bash
gcloud run services delete c2-sala mi-frente --region us-central1
```
