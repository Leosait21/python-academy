from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Курсы программирования Python с нуля</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',sans-serif;}

body{background:#0f172a;color:white;}

header{
display:flex;justify-content:space-between;align-items:center;
padding:25px 10%;background:#111827;position:sticky;top:0;
}

.logo{font-size:32px;font-weight:bold;color:#38bdf8;}

nav a{color:white;text-decoration:none;margin-left:25px;font-size:18px;}

.hero{
height:100vh;display:flex;align-items:center;justify-content:center;
flex-direction:column;text-align:center;
background:linear-gradient(135deg,#0f172a,#1e3a8a);
}

.hero h1{font-size:72px;margin-bottom:20px;}
.hero p{font-size:24px;max-width:700px;margin-bottom:30px;}

.btn{
background:#f59e0b;padding:18px 40px;border-radius:10px;
text-decoration:none;color:white;font-size:22px;font-weight:bold;
}

.section{padding:100px 10%;}
.title{text-align:center;font-size:48px;margin-bottom:50px;}

.cards{
display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));
gap:30px;
}

.card{
background:#1e293b;padding:30px;border-radius:20px;
}

.price{font-size:32px;font-weight:bold;color:#22c55e;margin-top:15px;}

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
</style>
</head>

<body>

<header>
<div class="logo">Python Academy</div>
<nav>
<a href="#">Главная</a>
<a href="#">Курсы</a>
<a href="#">Оплата</a>
</nav>
</header>

<section class="hero">
<h1>Стань Python Разработчиком</h1>
<p>Освой программирование с нуля и начни карьеру в IT.</p>

<a class="btn" href="tel:+992109919197">
📞 Позвонить
</a>
</section>

<section class="section">
<h2 class="title">Курсы</h2>

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
<h3>AI</h3>
<p>Нейросети и анализ данных.</p>
<div class="price">1499 сомони</div>
</div>
</div>
</section>

<section class="section">
<h2 class="title">Оплата</h2>

<div class="pay-box">

<p>Выбери способ оплаты:</p>

<a class="pay-btn" href="https://www.paypal.com" target="_blank">PayPal</a>

<a class="pay-btn" href="https://checkout.stripe.com" target="_blank">
Visa / Mastercard
</a>

<a class="pay-btn" href="https://wa.me/992109919197" target="_blank">
Оплата через WhatsApp
</a>

</div>
</section>

<footer>
© 2026 Python Academy
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
