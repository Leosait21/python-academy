from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Разработка сайтов на заказ</title>

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
font-size:28px;
font-weight:bold;
color:#38bdf8;
}

nav a{
color:white;
text-decoration:none;
margin-left:20px;
font-size:16px;
}

.hero{
height:90vh;
display:flex;
align-items:center;
justify-content:center;
flex-direction:column;
text-align:center;
background:linear-gradient(135deg,#0f172a,#1e3a8a);
padding:20px;
}

.hero h1{
font-size:52px;
margin-bottom:20px;
}

.hero p{
font-size:20px;
max-width:700px;
margin-bottom:30px;
opacity:0.9;
}

.btn{
background:#f59e0b;
padding:15px 35px;
border-radius:10px;
text-decoration:none;
color:white;
font-size:18px;
font-weight:bold;
}

.section{
padding:80px 10%;
}

.title{
text-align:center;
font-size:40px;
margin-bottom:40px;
}

.cards{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
gap:20px;
}

.card{
background:#1e293b;
padding:25px;
border-radius:15px;
}

.contact-box{
margin-top:40px;
background:#111827;
padding:30px;
border-radius:15px;
text-align:center;
}

.contact-box a{
display:inline-block;
margin:10px;
padding:12px 20px;
border-radius:10px;
text-decoration:none;
color:white;
font-weight:bold;
}

.whatsapp{
background:#22c55e;
}

.insta{
background:#e1306c;
}

footer{
padding:25px;
text-align:center;
background:#020617;
}

/* MOBILE */
@media (max-width: 768px){

.hero h1{font-size:32px;}
.hero p{font-size:16px;}
.section{padding:50px 15px;}
.title{font-size:26px;}
}
</style>

</head>

<body>

<header>
<div class="logo">Web Studio</div>
<nav>
<a href="#services">Услуги</a>
<a href="#contact">Контакты</a>
</nav>
</header>

<section class="hero">
<h1>Делаем сайты на заказ</h1>
<p>Создаём современные сайты для бизнеса, которые привлекают клиентов и заявки.</p>

<a class="btn" href="#contact">Связаться</a>
</section>

<section class="section" id="services">
<h2 class="title">Что мы делаем</h2>

<div class="cards">
<div class="card">Сайты для бизнеса</div>
<div class="card">Лендинги</div>
<div class="card">Сайты под заявки</div>
<div class="card">Адаптивный дизайн</div>
</div>
</section>

<section class="section">
<h2 class="title">Этот сайт тоже продаётся</h2>
<div class="card">
Этот сайт является примером работы и может быть адаптирован под любой бизнес.
</div>
</section>

<section class="section" id="contact">
<h2 class="title">Связь со мной</h2>

<div class="contact-box">

<p>Напишите для заказа сайта:</p>

<a class="whatsapp" href="https://wa.me/992109919197" target="_blank">
WhatsApp
</a>

<a class="insta" href="https://instagram.com/darkness_leo_" target="_blank">
Instagram
</a>

</div>
</section>

<footer>
© 2026 Web Studio
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
