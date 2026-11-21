# c2.py — Teamserver de la sala (solo lo corre el presentador)
# Recibe los beacons de los agentes y muestra un panel en vivo para el proyector.
# Se despliega en Cloud Run antes de la charla (ver c2/DEPLOY.md): así los
# beacons de la sala viajan por Internet, con HTTPS y dominio *.run.app real.
from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os, time, html

PUERTO = int(os.environ.get("PORT", 8443))

beacons = {}  # id -> última vez que llamó

PANEL = """<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="3">
<title>C2 de la sala</title>
<body style="background:#0a0f14;color:#2ab95b;font-family:monospace;padding:2em">
<h1 style="font-size:2em">teamserver — agentes conectados: {n}</h1>
<table style="font-size:1.3em;border-spacing:1em 0.3em">{filas}</table>
</body>"""

class C2(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/beacon":
            datos = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            beacons[datos["id"]] = time.time()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"")
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        filas = "".join(
            "<tr><td>{}</td><td>hace {}s</td></tr>".format(html.escape(i), int(time.time() - t))
            for i, t in sorted(beacons.items(), key=lambda x: -x[1]))
        panel = PANEL.format(n=len(beacons), filas=filas).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(panel)

    def log_message(self, *args):
        pass

print(f"C2 escuchando en :{PUERTO} — abre el panel en el proyector")
HTTPServer(("0.0.0.0", PUERTO), C2).serve_forever()
