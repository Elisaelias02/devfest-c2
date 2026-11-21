# Paso a paso del presentador — desde cero

**"Tu primer C2 en 3 pasos" · DevFest · 30 min**
Todo lo que necesitas hacer, en orden, desde una cuenta de Google vacía hasta la limpieza final. Tiempos estimados entre paréntesis.

---

## PARTE 1 — Cuenta y proyecto GCP (15 min, una sola vez)

1. Entra a <https://console.cloud.google.com> con tu cuenta de Google.
2. Acepta la prueba gratuita: te piden tarjeta **pero no cobran** — son **$300 USD de crédito por 90 días**. De sobra para el workshop (lo que gastaremos: centavos).
   - **OJO**: si eliges verificar con **cuenta bancaria**, la validación puede tardar **días**. Elige **tarjeta** (crédito o débito Visa/Mastercard, no prepago): la verificación es **instantánea** — solo una retención temporal de hasta $1 que no es un cargo.
3. Arriba a la izquierda, selector de proyecto → **"Nuevo proyecto"** → nombre: `devfest-c2` → Crear.
4. Espera 30 segundos y asegúrate de que el proyecto `devfest-c2` quede seleccionado en la barra superior.

### PARTE 1B — ¿Sin tarjeta, o la verificación se atascó?

No necesitas tu propia cuenta de facturación: necesitas **acceso a un proyecto que ya tenga una**. Opciones en orden de velocidad:

1. **Créditos del DevFest (CONFIRMADO — ya los tienes)**: GDG LATAM envió los enlaces para DevFest 2026. Sin tarjeta ni verificación. Reglas:
   - Enlace: `https://g.dev/credits/gdg-guadalajara-1` (respaldo: `…-1-bkp`, solo si el primero falla — **un solo canje por cuenta**).
   - **Ventana de canje: 21/11/2026, 8:00–20:00** — canjea al llegar al registro, no esperes a la charla.
   - **Debe ser una cuenta @gmail.com personal** (no Google Workspace). Si tu correo habitual es corporativo, crea una Gmail nueva antes de llegar.
   - 1000 créditos por enlace para toda la sala: tu canje no afecta a los asistentes.
   - **OJO**: como el canje abre a las 8:00 del día del evento, el **ensayo en casa no puede usar estos créditos** — ensaya con tarjeta (verificación instantánea) o con el plan B local.
   - Flujo del día: 8:00 canjear → crear proyecto `devfest-c2` → seguir Parte 2 → ~10:00 deploy `c2-sala` → 11:00 charla.
2. **Un colega/amigo con GCP**: te agrega a su proyecto (Consola → IAM → Agregar → tu correo → rol **Editor**). Luego tú: `gcloud init` → eliges ESE proyecto → sigues con la Parte 2 igual. El gasto (centavos) cae en su crédito/tarjeta; al terminar borras los servicios y te quita el acceso.
3. **Créditos de Cloud Skills Boost**: en muchos DevFest reparten códigos gratis en el registro — dan acceso a proyectos sandbox temporales sin tarjeta.
4. **Plan B sin GCP**: el C2 corre local (`python3 c2/c2.py` + hotspot) y el paso 3 se narra con las slides. El workshop sobrevive, pero pierde el "esto es GCP de verdad" — último recurso.

## PARTE 2 — Instalar y conectar gcloud (10 min, una sola vez)

1. Instala el SDK: <https://cloud.google.com/sdk/docs/install> (hay instalador para macOS, Windows y Linux; en macOS también `brew install --cask google-cloud-sdk`).
2. Abre una terminal nueva y verifica:

```bash
   gcloud --version
```

3. Inicia sesión y apunta al proyecto:

```bash
   gcloud init
```

Elige tu cuenta de Google → elige el proyecto `devfest-c2` → región: `us-central1`.

4. Activa las APIs que Cloud Run necesita:

```bash
   gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
```

## PARTE 3 — Publicar el kit y el QR (15 min, días antes)

1. Descomprime `kit-tu-primer-c2-devfest.zip`.
2. Sube la carpeta a un repo público de GitHub (ej. `tu-usuario/kit-tu-primer-c2`): botón "New repository" → arrastra los archivos o `git push`.
3. Genera un QR apuntando al repo (cualquier generador; por ejemplo <https://qr-code-generator.com> o `qrencode`).
4. Pon el QR en la **slide 04** (caja `[QR]`) y en la **slide 14**; reemplaza `[tu-repo]` y `[tu handle]` en slide 14, guion y Canva.

## PARTE 4 — Ensayo (30 min, 1-2 días antes)

1. **Despliega el C2** (esto es lo único que corre entre el ensayo y la charla — cuesta centavos, no lo borres):

```bash
   cd kit-tu-primer-c2/c2
   gcloud run deploy c2-sala --source . --region us-central1 --allow-unauthenticated
```

Copia la URL que devuelve: `https://c2-sala-XXXXXXXX-uc.a.run.app`

2. Abre esa URL en el navegador → verás el panel "teamserver — agentes conectados: 0".
3. **Simula ser un asistente**: edita `paso1/agente.py`, pon la URL real en `C2 = "..."`, y ejecútalo:

```bash
   python3 paso1/agente.py
```

En 10-20 segundos tu `usuario@maquina` aparece en el panel. ✔

4. **Simula el paso 2**: edita `paso2/redirector.py` con la misma URL, ejecútalo en otra terminal, reapunta el agente a `http://localhost:8080` → el beacon sigue llegando al panel. ✔
5. **Ensaya el paso 3 (el momento en vivo)**:

```bash
   cd ../paso3
   cp ../paso2/redirector.py .
   gcloud run deploy mi-frente --source . --region us-central1 --allow-unauthenticated \
     --set-env-vars C2_URL="https://c2-sala-XXXXXXXX-uc.a.run.app"
```

Reapunta tu agente a la nueva URL `mi-frente-….run.app` → beacon llega **a través del frente en la nube**. ✔

6. Cronometra el deploy del paso 3 (típico: 60-120 s). Ese es el tiempo que tendrás que rellenar hablando en la charla — el guion ya lo cubre.

> La primera vez, `gcloud run deploy` puede tardar 3-5 min (crea el registro de contenedores). Por eso el ensayo importa: el día de la charla ya todo está caliente.

## PARTE 5 — Día del evento (checklist)

**Al llegar (T-1h)**

- [ ] **8:00–9:00, registro: canjea el crédito** (`g.dev/credits/gdg-guadalajara-1`, cuenta @gmail.com personal) si vas por la ruta de créditos del DevFest → crea el proyecto `devfest-c2` → Parte 2 (gcloud init + activar APIs).
- [ ] Conecta tu laptop al wifi del venue y verifica que el panel carga: abre la URL de `c2-sala`.
- [ ] Redeploy de calentamiento si hace falta (el servicio es estable; solo si cambiaste algo).
- [ ] Navegador con el panel a pantalla completa, listo en el escritorio del proyector.
- [ ] Terminal con fuente ≥20 pt, `cd kit-tu-primer-c2/paso3`, con el comando del paso 3 copiado en un bloc de notas junto a la URL del C2.
- [ ] Plan B listo: si el venue no da Internet, corre `python3 c2/c2.py` local + hotspot del teléfono.

**Durante (sigue el guion)**

- Paso 1: la sala escribe `agente.py` con la URL del panel → se llena la botnet en pantalla.
- Paso 2: `redirector.py` local → reapuntan a `localhost:8080`.
- Paso 3: ejecutas el deploy de `mi-frente` **en vivo** con el archivo que la sala escribió.

**Al terminar**

```bash
gcloud run services delete c2-sala mi-frente --region us-central1
```

Verifica en <https://console.cloud.google.com/run> que no queden servicios. Costo total esperado del workshop: **menos de $0.10 USD** (y sale del crédito gratis, no de tu tarjeta).

---

## Resumen en una línea

`gcloud init` → deploy `c2-sala` → repo + QR → ensayo → charla → `services delete`.