"""
Geovana Candido Lash - página interativa em Python (Flask)

Como rodar:
    pip install flask
    python app.py
    abra http://127.0.0.1:5000

Foto dela (opcional): salve em  static/foto.jpg  (a página detecta sozinha).
Edite tudo que é texto no dicionário CONFIG logo abaixo.
"""
import os
from urllib.parse import quote
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    "nome": "Geovana Candido",
    "marca": "Geovana Candido Lash",
    "instagram": "geovanacandidolash",
    "whatsapp": "https://api.whatsapp.com/message/MHJYGC5F67KLJ1?autoload=1&app_absent=0&utm_source=ig",
    "anos": 8,
    "seguidores": "2,9 mil",
    # Ajuste os nomes/descrições das técnicas conforme o que ela realmente oferece
    "estilos": [
        {"slug": "fio-a-fio-classico", "nome": "Fio a Fio Clássico", "tag": "Natural e elegante",
         "desc": "Uma extensão aplicada em cada cílio natural. O resultado é um olhar definido e delicado, sem exageros.",
         "m": [95, 30, 80], "ideal": ["Primeira vez", "Dia a dia", "Efeito natural"]},
        {"slug": "volume-brasileiro", "nome": "Volume Brasileiro", "tag": "Leve e preenchido",
         "desc": "Fios em formato de “Y” aplicados em cada cílio natural: mais preenchimento, com leveza e um olhar marcante.",
         "m": [70, 65, 70], "ideal": ["Mais volume", "Efeito leve", "Olhar marcante"]},
        {"slug": "volume-egipcio", "nome": "Volume Egípcio", "tag": "Texturizado e cheio",
         "desc": "Leques de fios aplicados de forma cruzada, que criam um efeito texturizado e cheio, com muita presença no olhar.",
         "m": [55, 75, 60], "ideal": ["Texturizado", "Muito volume", "Olhar intenso"]},
        {"slug": "volume-hibrido", "nome": "Volume Híbrido", "tag": "O equilíbrio perfeito",
         "desc": "A mistura do fio a fio com leques de volume, para um acabamento com textura natural e mais densidade.",
         "m": [65, 70, 70], "ideal": ["Equilíbrio", "Textura natural", "Versátil"]},
        {"slug": "volume-russo", "nome": "Volume Russo", "tag": "Máxima densidade",
         "desc": "Leques finíssimos feitos à mão, com vários fios por cílio natural, para um olhar bem cheio, sedoso e dramático.",
         "m": [35, 95, 75], "ideal": ["Muito cheio", "Dramático", "Ocasiões especiais"]},
    ],
    "servicos": [
        "Extensão de cílios",
        "Manutenção",
        "Curso de extensão de cílios",
    ],
}


@app.route("/")
def home():
    has_photo = os.path.exists(os.path.join(BASE, "static", "foto.jpg"))
    return render_template_string(PAGE, cfg=CONFIG, has_photo=has_photo)


@app.post("/api/mensagem")
def mensagem():
    """Monta a mensagem de pré-agendamento e devolve o link do WhatsApp."""
    d = request.get_json(silent=True) or {}
    nome = (d.get("nome") or "").strip()[:60] or "Cliente"
    servico = (d.get("servico") or CONFIG["servicos"][0]).strip()[:80]
    periodo = (d.get("periodo") or "a combinar").strip()[:30]
    estilo = (d.get("estilo") or "").strip()[:40]
    linhas = [
        f"Olá, Geovana! Me chamo {nome}.",
        f"Quero agendar: {servico}.",
        f"Melhor período: {periodo}.",
    ]
    if estilo:
        linhas.append(f"Efeito que me interessou: {estilo}.")
    linhas.append("Pode me passar os horários disponíveis?")
    texto = "\n".join(linhas)
    return jsonify(texto=texto, link=CONFIG["whatsapp"], texto_url=quote(texto))


PAGE = r"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ cfg.marca }} | Extensão de cílios e cursos</title>
<meta name="description" content="Extensão de cílios com qualidade e excelência em menos de 1 hora. {{ cfg.anos }} anos de experiência. Agendamentos e cursos.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0f0a0b;--bg2:#1a1214;--card:#211819;--gold:#e3c08a;--gold2:#b98a4e;--rose:#e9a8b4;--txt:#f6eee8;--mut:#b9a99f;--r:26px}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--txt);font-family:'DM Sans',sans-serif;line-height:1.6;overflow-x:hidden}
h1,h2,h3{font-family:'Playfair Display',serif;line-height:1.1}
a{color:inherit;text-decoration:none}
.wrap{max-width:1120px;margin:auto;padding:0 24px}
section{padding:96px 0;position:relative}
.glow{position:fixed;width:520px;height:520px;border-radius:50%;pointer-events:none;z-index:0;
 background:radial-gradient(circle,rgba(227,192,138,.16),transparent 65%);transform:translate(-50%,-50%);left:50%;top:30%}
.blob{position:absolute;border-radius:50%;filter:blur(90px);opacity:.35;animation:float 14s ease-in-out infinite}
.b1{width:420px;height:420px;background:#7a3b4a;top:-80px;right:-120px}
.b2{width:360px;height:360px;background:#8a6a35;bottom:-100px;left:-100px;animation-delay:-6s}
@keyframes float{50%{transform:translate(30px,40px) scale(1.1)}}
nav{position:fixed;inset:0 0 auto 0;z-index:50;padding:16px 0;transition:.3s}
nav.sc{background:rgba(15,10,11,.82);backdrop-filter:blur(14px);padding:10px 0;border-bottom:1px solid #ffffff12}
nav .wrap{display:flex;justify-content:space-between;align-items:center}
.logo{font-family:'Playfair Display',serif;font-size:1.25rem;color:var(--gold)}
.logo small{display:block;font:500 .62rem 'DM Sans';letter-spacing:.3em;color:var(--mut);text-transform:uppercase}
nav ul{display:flex;gap:28px;list-style:none;font-size:.92rem;color:var(--mut)}
nav ul a:hover{color:var(--gold)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 30px;border-radius:99px;font-weight:700;border:0;cursor:pointer;font-size:1rem;
 background:linear-gradient(135deg,var(--gold),var(--gold2));color:#2a1a0c;transition:transform .25s,box-shadow .25s;box-shadow:0 10px 30px -10px #e3c08a88;position:relative;overflow:hidden}
.btn:hover{transform:translateY(-3px);box-shadow:0 18px 40px -10px #e3c08acc}
.btn.ghost{background:transparent;color:var(--txt);border:1px solid #ffffff30;box-shadow:none}
.btn.ghost:hover{border-color:var(--gold);color:var(--gold)}
.btn::after{content:"";position:absolute;top:0;left:-120%;width:60%;height:100%;background:linear-gradient(100deg,transparent,#fff7,transparent);transform:skewX(-20deg);transition:.6s}
.btn:hover::after{left:140%}
/* hero */
.hero{min-height:100vh;display:flex;align-items:center;padding-top:110px;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center;position:relative;z-index:2}
.tag{display:inline-block;padding:7px 16px;border:1px solid #e3c08a55;border-radius:99px;color:var(--gold);font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;margin-bottom:22px}
.hero h1{font-size:clamp(2.6rem,6vw,4.7rem);margin-bottom:22px}
.hero h1 em{color:var(--gold);font-style:italic;display:inline-block;min-width:3ch;transition:opacity .35s,transform .35s}
.hero h1 em.out{opacity:0;transform:translateY(14px)}
.hero p{color:var(--mut);font-size:1.12rem;max-width:520px;margin-bottom:34px}
.cta{display:flex;gap:14px;flex-wrap:wrap}
.visual{position:relative;aspect-ratio:1;max-width:460px;margin-left:auto;width:100%}
.ring{position:absolute;inset:0;border-radius:50%;padding:5px;background:conic-gradient(from 0deg,var(--gold),var(--rose),var(--gold2),var(--gold));animation:spin 10s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.photo{position:absolute;inset:14px;border-radius:50%;background:radial-gradient(circle at 30% 25%,#3a2528,#150e0f);overflow:hidden;display:grid;place-items:center}
.photo img{width:100%;height:100%;object-fit:cover}
.photo span{font:700 6rem 'Playfair Display';color:var(--gold)}
.chip{position:absolute;background:#1f1517e6;backdrop-filter:blur(10px);border:1px solid #ffffff1c;border-radius:18px;padding:12px 18px;font-size:.85rem;animation:bob 5s ease-in-out infinite;z-index:3}
.chip b{display:block;font:700 1.35rem 'Playfair Display';color:var(--gold)}
.c1{left:-26px;top:16%}.c2{right:-12px;bottom:22%;animation-delay:-2s}.c3{left:12%;bottom:-14px;animation-delay:-3.5s}
@keyframes bob{50%{transform:translateY(-12px)}}
/* stats */
.stats{padding:0}
.stats .wrap{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;border-block:1px solid #ffffff14;padding-block:44px}
.stat{text-align:center}
.stat b{font:700 3.2rem 'Playfair Display';color:var(--gold);display:block}
.stat span{color:var(--mut);font-size:.95rem}
/* section head */
.head{text-align:center;max-width:640px;margin:0 auto 54px}
.head small{color:var(--rose);letter-spacing:.25em;text-transform:uppercase;font-size:.78rem}
.head h2{font-size:clamp(2rem,4.5vw,3.2rem);margin:10px 0 14px}
.head p{color:var(--mut)}
/* simulator */
.sim{display:grid;grid-template-columns:1.2fr .8fr;gap:30px;background:var(--card);border:1px solid #ffffff12;border-radius:36px;padding:34px}
.eyebox{background:linear-gradient(160deg,#ecc9ad,#c9936f);border-radius:var(--r);display:grid;place-items:center;padding:0;aspect-ratio:400/267;align-self:center;background-size:cover;background-position:center;overflow:hidden}
.eyebox .art{display:none}#ph{display:block}.eyebox.drawn .art{display:inline}.eyebox.drawn #ph{display:none}.eyebox .eye{animation:none}
.eyebox svg{width:100%;height:100%;display:block}
.lh{fill:#0d0708;stroke:none}.lash{stroke:#0a0607;fill:none;stroke-linecap:round;animation:grow .7s cubic-bezier(.2,.9,.3,1.2) backwards}
@keyframes grow{from{opacity:0;stroke-dasharray:60;stroke-dashoffset:60}}
.eye{animation:blink 6s infinite;transform-origin:200px 115px}
@keyframes blink{0%,94%,100%{transform:scaleY(1)}97%{transform:scaleY(.1)}}
.ctrl h3{font-size:1.7rem;margin-bottom:6px}
.ctrl p{color:var(--mut);font-size:.95rem;margin-bottom:20px;min-height:48px}
.pills{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:24px}
.pill{padding:9px 16px;border-radius:99px;border:1px solid #ffffff26;background:transparent;color:var(--txt);cursor:pointer;font:500 .9rem 'DM Sans';transition:.25s}
.pill:hover{border-color:var(--gold)}
.pill.on{background:var(--gold);color:#2a1a0c;border-color:var(--gold)}
input[type=range]{width:100%;accent-color:var(--gold);margin:4px 0 14px}
.lbl{display:flex;justify-content:space-between;font-size:.8rem;color:var(--mut)}
/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.step{background:var(--card);border:1px solid #ffffff10;border-radius:var(--r);padding:34px 28px;transition:.35s;transform-style:preserve-3d}
.step:hover{border-color:#e3c08a66}
.step i{font:italic 600 3rem 'Playfair Display';color:var(--gold2)}
.step h3{font-size:1.4rem;margin:8px 0}
.step p{color:var(--mut);font-size:.96rem}
/* courses */
.course{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;background:linear-gradient(135deg,#2a1a1d,#1a1214);border:1px solid #e3c08a33;border-radius:40px;padding:56px}
.course h2{font-size:clamp(2rem,4vw,2.9rem);margin:12px 0 16px}
.course p{color:var(--mut);margin-bottom:26px}
.course ul{list-style:none;display:grid;gap:14px}
.course li{display:flex;gap:14px;align-items:center;background:#ffffff08;padding:16px 20px;border-radius:18px}
.course li::before{content:"✦";color:var(--gold)}
/* booking */
.book{max-width:720px;margin:auto;background:var(--card);border:1px solid #ffffff12;border-radius:36px;padding:40px}
.field{margin-bottom:24px}
.field>label{display:block;font-size:.85rem;color:var(--mut);margin-bottom:10px;letter-spacing:.06em;text-transform:uppercase}
.book input[type=text]{width:100%;padding:16px 18px;border-radius:16px;border:1px solid #ffffff22;background:#150e10;color:var(--txt);font:inherit}
.book input[type=text]:focus{outline:0;border-color:var(--gold)}
.preview{white-space:pre-line;background:#150e10;border-left:3px solid var(--gold);padding:16px 20px;border-radius:12px;color:var(--mut);font-size:.92rem;margin-bottom:24px}
.note{font-size:.8rem;color:var(--mut);margin-top:14px;text-align:center}
/* faq */
.faq{max-width:760px;margin:auto}
details{background:var(--card);border:1px solid #ffffff10;border-radius:20px;padding:20px 26px;margin-bottom:14px;transition:.3s}
details[open]{border-color:#e3c08a55}
summary{cursor:pointer;font-weight:700;list-style:none;display:flex;justify-content:space-between}
summary::after{content:"+";color:var(--gold);font-size:1.4rem;line-height:1;transition:.3s}
details[open] summary::after{transform:rotate(45deg)}
details p{color:var(--mut);margin-top:12px}
footer{border-top:1px solid #ffffff12;padding:48px 0 90px;text-align:center;color:var(--mut)}
footer .logo{font-size:1.6rem;margin-bottom:10px}
.soc{display:flex;gap:22px;justify-content:center;margin-top:16px}
.soc a:hover{color:var(--gold)}
.fab{position:fixed;right:22px;bottom:22px;z-index:60;width:62px;height:62px;border-radius:50%;background:#25d366;display:grid;place-items:center;box-shadow:0 10px 30px #25d36688;animation:pulse 2.4s infinite}
.fab svg{width:32px;fill:#fff}
@keyframes pulse{0%{box-shadow:0 0 0 0 #25d366aa}100%{box-shadow:0 0 0 22px #25d36600}}
.toast{position:fixed;left:50%;bottom:30px;transform:translate(-50%,120px);background:var(--gold);color:#2a1a0c;padding:14px 26px;border-radius:99px;font-weight:700;z-index:80;transition:.4s}
.toast.show{transform:translate(-50%,0)}
.rv{opacity:0;transform:translateY(34px);transition:opacity .8s,transform .8s}
.rv.in{opacity:1;transform:none}
@media(max-width:860px){
 nav ul{display:none}
 .hero .wrap,.sim,.course{grid-template-columns:1fr}
 .visual{margin:0 auto;max-width:340px}.steps{grid-template-columns:1fr}
 .course{padding:34px 26px}.stat b{font-size:2.3rem}.book{padding:28px 20px}.sim{padding:20px}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.rv{opacity:1;transform:none}}

.tabs{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:28px}
.sty{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:center}
.shot{position:relative;aspect-ratio:4/5;border-radius:34px;overflow:hidden;border:1px solid #e3c08a40;box-shadow:0 40px 80px -30px #000;transition:transform .2s;transform-style:preserve-3d;background:#160e10}
.ph{position:absolute;inset:0;background:radial-gradient(circle at 50% 28%,#4d2c33,#150d0f 75%)}
.ph .art{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.ph .pic{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .7s cubic-bezier(.4,0,.2,1);z-index:1}
.ph .pic.on{opacity:1}
.ph.has .art,.ph.has .soon{display:none}
.soon{position:absolute;left:0;right:0;bottom:26px;text-align:center;font-size:.78rem;letter-spacing:.2em;text-transform:uppercase;color:#e3c08a99;z-index:0}
.cnt{position:absolute;top:18px;left:20px;font:600 1rem 'Playfair Display',serif;color:var(--gold);background:#0f0a0bb3;backdrop-filter:blur(8px);padding:6px 14px;border-radius:99px;z-index:2}
.swap{display:none;position:absolute;right:14px;bottom:14px;z-index:3;background:#0f0a0bcc;padding:8px 14px;border-radius:99px;font-size:.8rem;cursor:pointer}
.fa{fill:none;stroke:url(#gg);stroke-width:2.6;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;animation:dr 1s ease forwards}
.fa.th{stroke-width:1.4}.fa.base{stroke:#ffffff30;stroke-width:5;animation:none;stroke-dasharray:none;stroke-dashoffset:0}
@keyframes dr{to{stroke-dashoffset:0}}
.info .tagx,.info h3,.info p,.info .meters,.info .ideal,.info .btn{transition:opacity .5s cubic-bezier(.4,0,.2,1),transform .5s cubic-bezier(.4,0,.2,1)}
.info.out .tagx,.info.out h3,.info.out p,.info.out .meters,.info.out .ideal,.info.out .btn{opacity:0;transform:translateY(12px)}
.tagx{color:var(--rose);letter-spacing:.2em;text-transform:uppercase;font-size:.78rem;display:block;margin-top:4px}
.info h3{font-size:clamp(2rem,4.4vw,3.2rem);margin:8px 0 14px}
.info p{color:var(--mut);font-size:1.05rem;margin-bottom:26px;max-width:520px}
.meters{display:grid;gap:14px;margin-bottom:24px;max-width:480px}
.mt{display:grid;grid-template-columns:110px 1fr 38px;align-items:center;gap:12px;font-size:.88rem;color:var(--mut)}
.mt i{display:block;height:8px;border-radius:9px;background:#ffffff14;overflow:hidden}
.mt i b{display:block;height:100%;width:0;border-radius:9px;background:linear-gradient(90deg,var(--gold2),var(--gold));transition:width 1s cubic-bezier(.2,.8,.2,1)}
.ideal{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:30px}
.ideal span{border:1px solid #e3c08a44;color:var(--gold);padding:6px 14px;border-radius:99px;font-size:.84rem}
@media(max-width:860px){.sty{grid-template-columns:1fr;gap:28px}.shot{max-width:380px;margin:auto;width:100%}.tabs{justify-content:flex-start;flex-wrap:nowrap;overflow-x:auto;padding-bottom:6px;margin-bottom:20px}.tabs .pill{white-space:nowrap}}
</style>
</head>
<body>
<div class="glow" id="glow"></div>

<nav id="nav"><div class="wrap">
  <a href="#top" class="logo">{{ cfg.nome }}<small>Lash Designer</small></a>
  <ul><li><a href="#estilos">Estilos</a></li><li><a href="#processo">Atendimento</a></li><li><a href="#cursos">Cursos</a></li><li><a href="#agendar">Agendar</a></li></ul>
  <a class="btn" href="#agendar" style="padding:11px 22px;font-size:.9rem">Agendar</a>
</div></nav>

<header class="hero" id="top">
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="wrap">
    <div>
      <span class="tag">Extensão de cílios &amp; cursos</span>
      <h1>Um olhar <em id="word">marcante</em> em menos de 1 hora.</h1>
      <p>Qualidade e excelência em cada fio. São {{ cfg.anos }} anos de experiência no mundo Lash para realçar o seu olhar com cuidado e precisão.</p>
      <div class="cta">
        <a class="btn" href="#agendar">Quero agendar ✦</a>
        <a class="btn ghost" href="#cursos">Conhecer os cursos</a>
      </div>
    </div>
    <div class="visual">
      <div class="ring"></div>
      <div class="photo">{% if has_photo %}<img src="/static/foto.jpg" alt="{{ cfg.nome }}">{% else %}<span>G</span>{% endif %}</div>
      <div class="chip c1"><b>{{ cfg.anos }} anos</b>no mundo Lash</div>
      <div class="chip c2"><b>&lt; 1h</b>de atendimento</div>
      <div class="chip c3"><b>{{ cfg.seguidores }}</b>no Instagram</div>
    </div>
  </div>
</header>

<section class="stats"><div class="wrap">
  <div class="stat rv"><b data-n="{{ cfg.anos }}" data-s="+">0</b><span>anos de experiência</span></div>
  <div class="stat rv"><b>1h</b><span>ou menos por atendimento</span></div>
  <div class="stat rv"><b>100%</b><span>foco em qualidade e excelência</span></div>
</div></section>

<section id="estilos"><div class="wrap">
  <div class="head rv"><small>Técnicas</small><h2>Qual estilo combina com você?</h2><p>Toque em cada técnica para ver o resultado, o efeito e para quem ela é indicada.</p></div>
  <div class="sty rv">
    <div class="shot" id="shot">
      <div class="ph" id="phWrap"></div>
      <span class="cnt" id="cnt"></span>
      <label class="swap" id="swap">📷 trocar foto<input type="file" id="sFile" accept="image/*" hidden></label>
    </div>
    <div class="info" id="info">
      <div class="tabs" id="tabs"></div>
      <span class="tagx" id="iTag"></span>
      <h3 id="iNome"></h3>
      <p id="iDesc"></p>
      <div class="meters" id="meters"></div>
      <div class="ideal" id="ideal"></div>
      <a class="btn" href="#agendar" id="wantBtn">Quero esse estilo</a>
    </div>
  </div>
</div></section>

<section id="processo" style="background:var(--bg2)"><div class="wrap">
  <div class="head rv"><small>Atendimento</small><h2>Do primeiro olhar ao resultado</h2><p>Um processo pensado para ser rápido, confortável e com acabamento impecável.</p></div>
  <div class="steps">
    <div class="step rv"><i>01</i><h3>Conversa</h3><p>Você conta o que imagina e juntas escolhem o efeito ideal para o seu olhar.</p></div>
    <div class="step rv"><i>02</i><h3>Aplicação</h3><p>Fio a fio, com técnica e cuidado, em menos de 1 hora.</p></div>
    <div class="step rv"><i>03</i><h3>Cuidados</h3><p>Orientações para o resultado durar mais e continuar lindo.</p></div>
  </div>
</div></section>

<section id="cursos"><div class="wrap">
  <div class="course rv">
    <div>
      <span class="tag">Cursos</span>
      <h2>Aprenda com quem vive Lash há {{ cfg.anos }} anos</h2>
      <p>Quer transformar a extensão de cílios em profissão? Chame no WhatsApp e conheça as turmas e formatos disponíveis.</p>
      <a class="btn" href="{{ cfg.whatsapp }}" target="_blank" rel="noopener">Falar sobre cursos</a>
    </div>
    <ul><li>Técnica na prática</li><li>Qualidade e excelência desde a base</li><li>Experiência real de mercado</li></ul>
  </div>
</div></section>

<section id="agendar" style="background:var(--bg2)"><div class="wrap">
  <div class="head rv"><small>Agendamento</small><h2>Monte seu pedido em 10 segundos</h2><p>Preencha abaixo e a mensagem vai pronta para o WhatsApp.</p></div>
  <div class="book rv">
    <div class="field"><label>Seu nome</label><input type="text" id="fNome" placeholder="Como posso te chamar?" maxlength="60"></div>
    <div class="field"><label>O que você procura?</label><div class="pills" id="fServ"></div></div>
    <div class="field"><label>Melhor período</label><div class="pills" id="fPer"></div></div>
    <div class="preview" id="prev"></div>
    <button class="btn" id="send" style="width:100%;justify-content:center">Enviar pelo WhatsApp</button>
    <p class="note">A mensagem é copiada automaticamente: é só colar na conversa que abrir.</p>
  </div>
</div></section>

<section><div class="wrap">
  <div class="head rv"><small>Dúvidas</small><h2>Perguntas frequentes</h2></div>
  <div class="faq rv">
    <details><summary>Quanto tempo dura o atendimento?</summary><p>O foco é entregar qualidade e excelência em menos de 1 hora.</p></details>
    <details><summary>Como faço para agendar?</summary><p>Use o formulário desta página ou chame direto no WhatsApp para ver os horários disponíveis.</p></details>
    <details><summary>Vocês oferecem cursos?</summary><p>Sim! Chame no WhatsApp para saber sobre turmas e formatos.</p></details>
  </div>
</div></section>

<footer><div class="wrap">
  <div class="logo">{{ cfg.marca }}</div>
  <p>Extensão de cílios &amp; cursos</p>
  <div class="soc">
    <a href="https://instagram.com/{{ cfg.instagram }}" target="_blank" rel="noopener">Instagram @{{ cfg.instagram }}</a>
    <a href="{{ cfg.whatsapp }}" target="_blank" rel="noopener">WhatsApp</a>
  </div>
</div></footer>

<a class="fab" href="{{ cfg.whatsapp }}" target="_blank" rel="noopener" aria-label="WhatsApp">
  <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.2-1.200l-.3-.2-3 .8.8-2.900-.2-.3A8.200 8.200 0 1 1 12 20.200zm4.500-6.100c-.2-.1-1.500-.7-1.700-.8s-.4-.1-.6.100-.6.800-.8 1-.3.100-.6 0a6.700 6.700 0 0 1-3.300-2.900c-.2-.4.200-.4.700-1.300.1-.1 0-.3 0-.4l-.8-1.800c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.300 3 3 0 0 0-.9 2.200c0 1.300.9 2.500 1 2.700s1.800 2.800 4.500 3.900c2.200.9 2.700.7 3.100.6.500-.1 1.600-.7 1.800-1.300s.2-1.100.2-1.200-.2-.2-.4-.3z"/></svg>
</a>
<div class="toast" id="toast"></div>

<script>
const CFG = {{ cfg|tojson }};
const $ = s => document.querySelector(s);
/* ---- estilos (galeria) ---- */
const IMG='/static/', EST=CFG.estilos, ML=['Naturalidade','Volume','Leveza'];
let cur=0, curStyle=null, auto=null; const localPics={};
const tabs=$('#tabs');
EST.forEach((e,i)=>{const b=document.createElement('button');b.className='pill';b.textContent=e.nome;b.onclick=()=>{stop();show(i);restartAuto()};tabs.append(b)});
function ln(x,y,ang,len,d,th,lean){const a=(-90+ang)*Math.PI/180,ex=x+Math.cos(a)*len+lean,ey=y+Math.sin(a)*len;
  return `<path pathLength="1" class="fa${th?' th':''}" style="animation-delay:${d}ms" d="M${x.toFixed(1)} ${y.toFixed(1)} Q${(x+Math.cos(a)*len*.45).toFixed(1)} ${(y+Math.sin(a)*len*.7).toFixed(1)} ${ex.toFixed(1)} ${ey.toFixed(1)}"/>`}
function lashArt(slug){
  const N=7; let p='',pts=[];
  for(let c=0;c<N;c++){
    const t=c/(N-1), bx=64+t*172, by=300-Math.sin(Math.PI*t)*30+t*12, lean=(t-.5)*30, d=c*90;
    pts.push([bx,by]);
    if(slug==='fio-a-fio-classico') p+=ln(bx,by,(t-.5)*10,170,d,0,lean);
    else if(slug==='volume-brasileiro'){const sy=by-62;p+=ln(bx,by,0,62,d,0,lean*.2)+ln(bx+lean*.2,sy,-20,100,d+250,0,lean*.5)+ln(bx+lean*.2,sy,20,100,d+250,0,lean*.5)}
    else if(slug==='volume-egipcio'){p+=ln(bx-7,by,15,150,d,0,lean)+ln(bx+7,by,-15,150,d,0,lean)+ln(bx,by,0,165,d+120,0,lean)}
    else if(slug==='volume-hibrido'){ if(c%2===0)p+=ln(bx,by,0,165,d,0,lean); else p+=[-13,0,13].map((a,k)=>ln(bx,by,a,150+k*6,d+k*60,1,lean)).join('')}
    else {p+=[-22,-13,-4,4,13,22].map((a,k)=>ln(bx,by,a,120+((k*17)%5)*9,d+k*45,1,lean)).join('')}
  }
  const base='M'+pts.map(q=>q[0].toFixed(1)+' '+(q[1]+3).toFixed(1)).join(' L');
  return `<defs><linearGradient id="gg" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#b98a4e"/><stop offset="1" stop-color="#f4dfb8"/></linearGradient></defs><path class="fa base" d="${base}"/>${p}`;
}
function show(i){
  cur=i; const e=EST[i], ph=$('#phWrap'), info=$('#info');
  document.querySelectorAll('#tabs .pill').forEach((p,k)=>p.classList.toggle('on',k===i));

  // começa o fade-out do texto junto
  info.classList.add('out');

  // crossfade da foto + texto sincronizados
  const src=localPics[e.slug]||IMG+e.slug+'.jpg';
  const im=new Image(); im.className='pic'; im.alt=e.nome;
  let done=false;
  const finish=(ok)=>{
    if(done)return; done=true;

    // atualiza o texto ainda invisível
    $('#cnt').textContent='0'+(i+1)+' / 0'+EST.length;
    $('#iTag').textContent=e.tag; $('#iNome').textContent=e.nome; $('#iDesc').textContent=e.desc;
    $('#ideal').innerHTML=e.ideal.map(t=>`<span>${t}</span>`).join('');
    $('#meters').innerHTML=e.m.map((v,k)=>`<div class="mt"><span>${ML[k]}</span><i><b data-w="${v}"></b></i><span>${v}%</span></div>`).join('');

    // foto
    if(!ph.querySelector('.art')){
      ph.insertAdjacentHTML('afterbegin',`<svg class="art" viewBox="0 0 300 375">${lashArt(e.slug)}</svg><span class="soon">Foto em breve</span>`);
    }
    if(ok){
      ph.querySelectorAll('.pic.on').forEach(p=>p.classList.remove('on'));
      ph.appendChild(im);
      void im.offsetWidth;
      im.classList.add('on');
      ph.classList.add('has');
      setTimeout(()=>{
        ph.querySelectorAll('.pic:not(.on)').forEach(p=>p.remove());
        const art=ph.querySelector('.art');
        if(art) art.outerHTML=`<svg class="art" viewBox="0 0 300 375">${lashArt(e.slug)}</svg>`;
      },750);
    }else{
      ph.classList.remove('has');
      const art=ph.querySelector('.art');
      if(art) art.outerHTML=`<svg class="art" viewBox="0 0 300 375">${lashArt(e.slug)}</svg>`;
      else ph.insertAdjacentHTML('afterbegin',`<svg class="art" viewBox="0 0 300 375">${lashArt(e.slug)}</svg><span class="soon">Foto em breve</span>`);
    }

    // fade-in do texto no mesmo momento da foto
    requestAnimationFrame(()=>{
      info.classList.remove('out');
      requestAnimationFrame(()=>requestAnimationFrame(()=>document.querySelectorAll('.mt b').forEach(b=>b.style.width=b.dataset.w+'%')));
    });
  };
  im.onload=()=>finish(true);
  im.onerror=()=>finish(false);
  im.src=src;
  if(im.complete && im.naturalWidth) finish(true);
}
function stop(){clearInterval(auto);auto=null}
function restartAuto(){stop();auto=setInterval(()=>show((cur+1)%EST.length),7500)}
$('#wantBtn').onclick=()=>{curStyle={n:EST[cur].nome};updatePrev()};
const shot=$('#shot');
shot.addEventListener('pointermove',e=>{const r=shot.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;shot.style.transform=`perspective(900px) rotateY(${x*9}deg) rotateX(${-y*9}deg)`});
shot.addEventListener('pointerleave',()=>shot.style.transform='');
if(location.search.includes('editar'))$('#swap').style.display='block';
$('#sFile').onchange=e=>{const f=e.target.files[0];if(f){localPics[EST[cur].slug]=URL.createObjectURL(f);show(cur)}};
show(0); restartAuto();

/* ---- booking ---- */
const state={servico:CFG.servicos[0],periodo:'Manhã'};
function pillGroup(el,items,key){
  items.forEach((t,i)=>{const b=document.createElement('button');b.type='button';b.className='pill'+(i==0?' on':'');b.textContent=t;
    b.onclick=()=>{el.querySelectorAll('.pill').forEach(p=>p.classList.remove('on'));b.classList.add('on');state[key]=t;updatePrev()};el.append(b)});
}
pillGroup($('#fServ'),CFG.servicos,'servico');
pillGroup($('#fPer'),['Manhã','Tarde','Noite','Sem preferência'],'periodo');
function texto(){
  const nome=$('#fNome').value.trim()||'Cliente';
  let t=`Olá, Geovana! Me chamo ${nome}.\nQuero agendar: ${state.servico}.\nMelhor período: ${state.periodo}.`;
  if(curStyle&&curStyle.n)t+=`\nEfeito que me interessou: ${curStyle.n}.`;
  return t+`\nPode me passar os horários disponíveis?`;
}
function updatePrev(){$('#prev').textContent=texto()}
$('#fNome').oninput=updatePrev; updatePrev();
function toast(m){const t=$('#toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),3600)}
$('#send').onclick=async()=>{
  let msg=texto(), link=CFG.whatsapp;
  try{
    const r=await fetch('/api/mensagem',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({nome:$('#fNome').value,servico:state.servico,periodo:state.periodo,estilo:curStyle&&curStyle.n})});
    const d=await r.json(); msg=d.texto; link=d.link;
  }catch(e){}
  try{await navigator.clipboard.writeText(msg);toast('Mensagem copiada! Cole na conversa ✦')}catch(e){toast('Abrindo o WhatsApp...')}
  setTimeout(()=>window.open(link,'_blank','noopener'),700);
};

/* ---- rotating word, glow, nav, reveal, counters, tilt ---- */
const words=['marcante','elegante','natural','inesquecível'];let wi=0;const w=$('#word');
setInterval(()=>{w.classList.add('out');setTimeout(()=>{wi=(wi+1)%words.length;w.textContent=words[wi];w.classList.remove('out')},350)},2600);
const g=$('#glow');addEventListener('pointermove',e=>{g.style.left=e.clientX+'px';g.style.top=e.clientY+'px'});
addEventListener('scroll',()=>$('#nav').classList.toggle('sc',scrollY>40));
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');
  const b=e.target.querySelector('[data-n]');if(b&&!b.done){b.done=1;const T=+b.dataset.n;let c=0;const id=setInterval(()=>{c++;b.textContent=c+(b.dataset.s||'');if(c>=T)clearInterval(id)},110)}
  io.unobserve(e.target)}}),{threshold:.2});
document.querySelectorAll('.rv').forEach((el,i)=>{el.style.transitionDelay=(i%3)*90+'ms';io.observe(el)});
document.querySelectorAll('.step').forEach(c=>{
  c.addEventListener('pointermove',e=>{const r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform=`perspective(700px) rotateY(${x*10}deg) rotateX(${-y*10}deg) translateY(-6px)`});
  c.addEventListener('pointerleave',()=>c.style.transform='')});
</script>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)
