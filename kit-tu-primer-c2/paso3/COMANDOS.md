# Paso 3 — A la nube (Cloud Run)

El mismo código del Paso 2, sin tocar la lógica. Lo único que cambia es **dónde corre**.

## Despliegue en 3 comandos

```bash
# 1. Copia tu redirector junto al Procfile y requirements.txt de esta carpeta
cp ../paso2/redirector.py .

# 2. Apunta el frente a tu teamserver (el que escondiste detrás)
export C2_URL="https://TU-TEAMSERVER.run.app"

# 3. Despliega — Google construye el contenedor por ti
gcloud run deploy mi-frente --source . \
  --region us-central1 --allow-unauthenticated \
  --set-env-vars C2_URL=$C2_URL
```

Al terminar, `gcloud` te da una URL tipo `https://mi-frente-xxxx-uc.a.run.app`:

- **HTTPS con certificado válido de Google** — el candado verde, gratis.
- **Dominio `*.run.app`** — heredas la reputación de Google: nadie lo bloquea.
- Reapunta tu `agente.py` a esa URL y tu arquitectura está completa en la nube.

## Para el lunes (cuenta propia)

1. Activa un proyecto en <https://console.cloud.google.com> — los **$300 de crédito gratis** alcanzan de sobra.
2. Instala `gcloud` (<https://cloud.google.com/sdk/docs/install>) y haz `gcloud auth login`.
3. Repite los 3 comandos. Destruye con `gcloud run services delete mi-frente --region us-central1`.

> Cloud Run cobra solo mientras atiende peticiones; un lab de prueba cuesta centavos. Borra el servicio al terminar.
