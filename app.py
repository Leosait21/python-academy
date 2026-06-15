from flask import Flask, render_template_string, request, Response
import os
from datetime import datetime

app = Flask(__name__)

HTML = """ ... ТВОЙ HTML БЕЗ ИЗМЕНЕНИЙ ... """

LOG_FILE = "visitors.txt"

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    agent = request.headers.get("User-Agent")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time} | {ip} | {agent}\n")

    return render_template_string(HTML)


ADMIN_PASSWORD = "Mustafosait"

@app.route("/admin")
def admin():
    password = request.args.get("password")

    if password != ADMIN_PASSWORD:
        return """... ТВОЙ HTML АДМИНКИ ..."""

    if not os.path.exists(LOG_FILE):
        return "<h2>Пока нет посетителей</h2>"

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html = """... ТВОЙ HTML ТАБЛИЦЫ ..."""

    for line in lines[::-1]:
        parts = line.strip().split(" | ")
        if len(parts) == 3:
            html += f"""
            <tr>
                <td>{parts[0]}</td>
                <td>{parts[1]}</td>
                <td>{parts[2]}</td>
            </tr>
            """

    html += "</table></body></html>"
    return html


# 🔥 ВАЖНО: НОРМАЛЬНЫЙ robots.txt (без 404 и без мусора)
@app.route("/robots.txt")
def robots():
    text = """User-agent: *
Allow: /

Sitemap: https://python-academy.onrender.com/sitemap.xml
"""
    return Response(text, mimetype="text/plain")


# 🔥 НОРМАЛЬНЫЙ sitemap.xml (чистый, без скриптов)
@app.route("/sitemap.xml")
def sitemap():
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://python-academy.onrender.com/</loc>
  </url>
</urlset>
"""
    return Response(xml, mimetype="application/xml")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
