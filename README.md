# Tu primer C2 en 3 pasos — DevFest

**"Offensive cloud architecture: Building adversarial infrastructure on GCP"** · DevFest 2026

En el workshop construimos juntos, paso a paso, una arquitectura de comando y control (C2) mínima — la misma forma que usan las campañas reales — y entendemos *por qué* cada pieza parece legítima.

## Qué vas a construir

```
tu agente  ──HTTPS──>  tu frente (redirector)  ──>  teamserver (C2)
 agente.py              paso2 → paso3 (Cloud Run)      c2.py (del presentador)
```

- **Paso 1 · El canal** — `paso1/agente.py`: un loop que beaconea por HTTPS. Aprendes: polling, JSON, por qué puerto 443, por qué la periodicidad te delata.
- **Paso 2 · El frente desechable** — `paso2/redirector.py`: reenvía beacons al C2. Aprendes: capas desechables, qué ve la víctima vs. qué ve el defensor.
- **Paso 3 · A la nube** — `paso3/`: el mismo código en Cloud Run, con candado verde y dominio de Google. Aprendes: por qué nadie bloquea `*.run.app`.

## Requisitos

- **Solo Python 3** (3.8+). Sin pip, sin dependencias: todo usa la librería estándar.
- Sin laptop: trabaja en pareja con alguien que tenga — así se hace en DevFest.
- Si te atrasas: cada carpeta `pasoN/` tiene el código completo de ese paso.

## Durante la sala

1. El presentador proyecta el **panel del teamserver** — ya desplegado en Cloud Run (`c2/DEPLOY.md`).
2. Editas la línea `C2 = ...` de tu `agente.py` con la URL `https://….run.app` que aparezca en pantalla.
3. Ejecutas: `python3 agente.py` → tu beacon viaja por Internet, con HTTPS y dominio de Google, hasta el C2. Tu nombre aparece en el panel. Ya eres parte de la botnet.
4. Paso 2: `python3 redirector.py` y reapuntas tu agente a `http://localhost:8080`. Tu tráfico ahora pasa por TU frente antes de salir a la nube.
5. Paso 3: el presentador despliega **ese mismo redirector** a Cloud Run en vivo — la cadena completa queda en GCP.

## Contexto 

Esta misma forma — frentes en servicios cloud legítimos, dominios de marca, TLS válido — fue la de la campaña documentada por Cisco Talos (feb-2024) que distribuyó Astaroth/Mekotio/Ousaban contra 300+ instituciones en 15 países de LATAM vía Google Cloud Run, y la de APT29 con servicios legítimos (MITRE ATT&CK T1583.006).

**Uso ético:** este kit es para aprender defensa construyendo. Úsalo solo en tus propias cuentas y laboratorios.
