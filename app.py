from flask import Flask, render_template_string, request, Response
import os
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Курсы программирования Python с нуля</title>

<meta name="google-site-verification" content="v1PzejX5ey60Z5Y_8JEWPIzwRmTXIfcLQPmj0MLYKgs" />

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
font-family:'Segoe UI',sans-serif;
}

body{
background:#0f172a;
color:white;
}

header{
display:flex;
justify-content:space-between;
align-items:center;
padding:25px 10%;
background:#111827;
position:sticky;
top:0;
}

.logo{
font-size:32px;
font-weight:bold;
color:#38bdf8;
}

nav a{
color:white;
text-decoration:none;
margin-left:25px;
font-size:18px;
}

.hero{
height:100vh;
display:flex;
align-items:center;
justify-content:center;
flex-direction:column;
text-align:center;
background:linear-gradient(135deg,#0f172a,#1e3a8a);
}

.hero h1{
font-size:72px;
margin-bottom:20px;
}

.hero p{
font-size:24px;
max-width:700px;
margin-bottom:30px;
}

.btn{
background:#f59e0b;
padding:18px 40px;
border-radius:10px;
text-decoration:none;
color:white;
font-size:22px;
font-weight:bold;
}

.section{
padding:100px 10%;
}

.title{
text-align:center;
font-size:48px;
margin-bottom:50px;
}

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
gap:30px;
}

.card{
background:#1e293b;
padding:30px;
border-radius:20px;
}

.price{
font-size:32px;
font-weight:bold;
color:#22c55e;
margin-top:15px;
}

.pay-box{
margin-top:40px;
background:#111827;
padding:30px;
border-radius:20px;
text-align:center;
}

.pay-btn{
display:inline-block;
margin:10px;
padding:15px 25px;
background:#22c55e;
color:white;
border-radius:10px;
text-decoration:none;
font-weight:bold;
}

footer{
padding:30px;
text-align:center;
background:#020617;
}

@media (max-width: 768px) {

header{
padding:15px;
flex-direction:column;
align-items:flex-start;
gap:10px;
}

nav a{
margin:5px 10px 0 0;
font-size:14px;
display:inline-block;
}

.section{
padding:50px 15px;
}

.hero h1{
font-size:34px;
}

.hero p{
font-size:16px;
}

.cards{
grid-template-columns:1fr;
}

.card{
padding:20px;
}

.title{
font-size:26px;
}

.price{
font-size:24px;
}

.btn{
font-size:16px;
padding:12px 20px;
}

.pay-box{
padding:20px;
}
}
</style>
</head>

<body>

<header>
<div class="logo">Python Academy</div>
<nav>
<a href="#">Главная</a>
<a href="#">Курсы</a>
<a href="#">Отзывы</a>
<a href="#">Контакты</a>
</nav>
</header>

<section class="hero">
<h1>Стань Python Разработчиком</h1>
<p>Освой программирование с нуля и начни карьеру в IT.</p>

<a class="btn" href="https://wa.me/992109919197?text=Хочу записаться на курс Python">
🔥 Записаться
</a>
</section>

<section class="section">
<h2 class="title">Наши курсы</h2>

<div class="cards">

<div class="card">
<h3>Python с нуля</h3>
<p>Переменные, функции, циклы, ООП и проекты.</p>
<div class="price">499 сомони</div>
</div>

<div class="card">
<h3>Web-разработка</h3>
<p>Flask, Django, базы данных.</p>
<div class="price">999 сомони</div>
</div>

<div class="card">
<h3>AI и Machine Learning</h3>
<p>Нейросети и анализ данных.</p>
<div class="price">1499 сомони</div>
</div>

</div>
</section>

<section class="section">
<h2 class="title">Почему выбирают нас</h2>

<div class="cards">
<div class="card"><h3>100% Практика</h3><p>Работа над реальными проектами.</p></div>
<div class="card"><h3>Сертификат</h3><p>Подтверждение навыков.</p></div>
<div class="card"><h3>Трудоустройство</h3><p>Помощь с работой.</p></div>
</div>
</section>

<section class="section">
<h2 class="title">Отзывы студентов</h2>

<div class="cards">
<div class="card"><h3>Ахмад</h3><p>Начал брать заказы после курса.</p>⭐⭐⭐⭐⭐</div>
<div class="card"><h3>Мухаммад</h3><p>Очень понятное обучение.</p>⭐⭐⭐⭐⭐</div>
<div class="card"><h3>Фаррух</h3><p>Устроился Junior разработчиком.</p>⭐⭐⭐⭐⭐</div>
</div>
</section>

<section class="section">
<h2 class="title">Что вы изучите</h2>

<div class="cards">
<div class="card"><h3>Python Basics</h3><p>Основы языка</p></div>
<div class="card"><h3>ООП</h3><p>Классы и объекты</p></div>
<div class="card"><h3>Django</h3><p>Веб разработка</p></div>
<div class="card"><h3>Telegram Bots</h3><p>Боты</p></div>
<div class="card"><h3>Data Science</h3><p>Анализ данных</p></div>
<div class="card"><h3>AI</h3><p>Нейросети</p></div>
</div>
</section>

<section class="section">
<h2 class="title">Наши преимущества</h2>

<div class="cards">
<div class="card"><h3>1500+</h3><p>Выпускников</p></div>
<div class="card"><h3>50+</h3><p>Проектов</p></div>
<div class="card"><h3>95%</h3><p>Довольных</p></div>
<div class="card"><h3>24/7</h3><p>Поддержка</p></div>
</div>
</section>

<section class="section">
<h2 class="title">Оплата и запись</h2>

<div class="pay-box">
<p>Выберите способ связи:</p>

<a class="pay-btn" href="https://wa.me/992109919197" target="_blank">WhatsApp</a>

</div>

<div class="section">
<h2 class="title">Дополнительно</h2>
<div class="card">
Делаем сайты на заказ. Этот сайт тоже продаётся и может быть адаптирован под любой бизнес.
</div>
</div>

</section>

<footer>
© 2026 Python Academy
</footer>

</body>
</html>
"""

LOG_FILE = "visitors.txt"

@app.route("/")
def home():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    agent = request.headers.get("User-Agent")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{time} | {ip} | {agent}\n")

    return render_template_string(HTML)


@app.route("/admin")
def admin():
    password = request.args.get("password")

    if password != "Mustafosait":
        return "<h2>Неверный пароль</h2>"

    if not os.path.exists(LOG_FILE):
        return "<h2>Пока нет посетителей</h2>"

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    html = "<h1>Посетители</h1><table border=1><tr><th>Время</th><th>IP</th><th>Браузер</th></tr>"

    for line in lines[::-1]:
        parts = line.strip().split(" | ")
        if len(parts) == 3:
            html += f"<tr><td>{parts[0]}</td><td>{parts[1]}</td><td>{parts[2]}</td></tr>"

    html += "</table>"
    return html


@app.route("/robots.txt")
def robots():
    return Response(
        "User-agent: *\nAllow: /\nSitemap: https://python-academy.onrender.com/sitemap.xml",
        mimetype="text/plain"
    )


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
