import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A little game for Vanshika",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>For Vanshika</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500;600&display=swap');

:root{
  --bg:#0d090c;
  --panel:#171016;
  --cream:#f7eee5;
  --muted:#a99ca2;
  --gold:#d8aa58;
  --pink:#d886a4;
}

*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;background:#0d090c;color:#fff;overflow:hidden}
body{font-family:"DM Sans",sans-serif}
#game{
  min-height:100svh;
  position:relative;
  overflow:hidden;
  background:
    radial-gradient(circle at 20% 15%,rgba(210,125,158,.13),transparent 30%),
    radial-gradient(circle at 85% 85%,rgba(215,169,81,.10),transparent 28%),
    #0d090c;
}
.noise{position:absolute;inset:0;pointer-events:none;opacity:.045;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}

.screen{position:absolute;inset:0;padding:28px 20px calc(25px + env(safe-area-inset-bottom));display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;pointer-events:none;transform:translateY(12px);transition:.55s ease}
.screen.active{opacity:1;pointer-events:auto;transform:none}

.eyebrow{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#8e8288;margin-bottom:16px}
.serif{font-family:"Cormorant Garamond",serif}

h1,h2,p{margin:0}
.hero{text-align:center}
.hero h1{font-size:clamp(58px,17vw,84px);font-weight:400;line-height:.78;letter-spacing:-3px}
.hero .sub{max-width:310px;color:var(--muted);font-size:13px;line-height:1.8;margin:25px auto 30px}
button{font:inherit}
.primary{min-height:50px;padding:0 24px;border-radius:999px;border:1px solid rgba(216,170,88,.4);background:rgba(216,170,88,.08);color:#e8c889;font-size:11px;letter-spacing:2px;text-transform:uppercase}
.primary:active{transform:scale(.96)}

.hud{position:absolute;top:25px;left:20px;right:20px;display:flex;justify-content:space-between;align-items:center}
.hud span{font-size:10px;letter-spacing:2px;color:#8e8288;text-transform:uppercase}
.score{color:#e8c889!important}

.playTitle{text-align:center;margin-bottom:12px}
.playTitle h2{font-size:36px;font-weight:400}
.playTitle p{color:var(--muted);font-size:12px;margin-top:6px}

.arena{width:min(390px,94vw);height:430px;position:relative;border:1px solid rgba(255,255,255,.07);border-radius:28px;background:rgba(255,255,255,.018);overflow:hidden;box-shadow:inset 0 0 70px rgba(0,0,0,.35)}
.arena:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,rgba(214,165,81,.06),transparent 55%)}
.item{position:absolute;width:58px;height:58px;border-radius:50%;display:grid;place-items:center;cursor:pointer;user-select:none;touch-action:manipulation;animation:float 2.8s ease-in-out infinite}
.bangle{border:8px solid #d8aa58;box-shadow:inset 0 2px 3px #fff0b0,0 0 18px rgba(216,170,88,.28)}
.bangle.pink{border-color:#c87391;box-shadow:inset 0 2px 3px #ffdce8,0 0 18px rgba(200,115,145,.25)}
.star{font-size:27px;color:#e5bc6b;text-shadow:0 0 15px rgba(229,188,107,.55)}
.item.hit{animation:hit .32s ease forwards}
@keyframes float{50%{transform:translateY(-8px) rotate(5deg)}}
@keyframes hit{to{transform:scale(1.8);opacity:0}}

.instruction{text-align:center;color:#b8abb1;font-size:12px;margin:13px 0 10px}
.progress{width:min(260px,70vw);height:3px;background:#292026;border-radius:5px;overflow:hidden;margin:auto}
.progress div{height:100%;width:0;background:linear-gradient(90deg,var(--pink),var(--gold));transition:.35s}

.choiceWrap{text-align:center;width:min(360px,92vw)}
.choiceWrap h2{font-size:40px;font-weight:400;line-height:.9;margin-bottom:13px}
.choiceWrap p{color:var(--muted);font-size:13px;line-height:1.8;margin-bottom:24px}
.choices{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.choice{min-height:72px;border:1px solid rgba(255,255,255,.10);border-radius:18px;background:#171116;color:#eee0d3;font-size:13px}
.choice:active{transform:scale(.97)}
.choice.selected{border-color:#d8aa58;background:rgba(216,170,88,.09);color:#edc982}

.reveal{text-align:center;max-width:340px}
.envelope{width:210px;height:145px;margin:0 auto 28px;position:relative;background:#e5d6c3;box-shadow:0 25px 55px rgba(0,0,0,.45);border-radius:4px;overflow:hidden}
.envelope:before{content:"";position:absolute;left:0;right:0;top:0;border-left:105px solid transparent;border-right:105px solid transparent;border-top:72px solid #cbb9a4;z-index:2}
.envelope:after{content:"";position:absolute;left:0;bottom:0;border-left:105px solid #d7c5af;border-top:70px solid transparent;border-right:105px solid #d7c5af}
.seal{position:absolute;z-index:4;left:50%;top:65px;transform:translate(-50%,-50%);width:35px;height:35px;border-radius:50%;background:#b45f78;display:grid;place-items:center;font-size:12px;box-shadow:0 3px 9px rgba(0,0,0,.25)}

.reveal h2{font-size:47px;font-weight:400;line-height:.88;margin-bottom:18px}
.reveal p{color:#b9adb2;font-size:13px;line-height:1.9}
.finalName{color:#e4b96e;font-family:"Cormorant Garamond",serif;font-size:30px;margin-top:24px}

.confetti{position:absolute;pointer-events:none;font-size:15px;animation:confetti 1.1s ease forwards}
@keyframes confetti{to{transform:translate(var(--x),var(--y)) rotate(240deg);opacity:0}}

@media(max-height:700px){.arena{height:350px}.item{width:50px;height:50px}.playTitle h2{font-size:31px}}
</style>
</head>

<body>
<div id="game">
<div class="noise"></div>

<section id="intro" class="screen active">
  <div class="hero">
    <div class="eyebrow">A tiny game · made for Vanshika</div>
    <h1 class="serif">Vanshika</h1>
    <p class="sub">I couldn't send you a surprise through the screen...<br>so I made the screen the surprise.</p>
    <button class="primary" id="start">Let's play</button>
  </div>
</section>

<section id="hunt" class="screen">
  <div class="hud">
    <span>little mission</span>
    <span class="score" id="score">0 / 5</span>
  </div>
  <div class="playTitle">
    <h2 class="serif">Catch the bangles</h2>
    <p>They're shy. Tap them before they disappear.</p>
  </div>
  <div class="arena" id="arena"></div>
  <div class="instruction" id="instruction">Find all five.</div>
  <div class="progress"><div id="bar"></div></div>
</section>

<section id="choice" class="screen">
  <div class="choiceWrap">
    <div class="eyebrow">One important question</div>
    <h2 class="serif">Pick one for me.</h2>
    <p>No wrong answer. I'm just curious what Vanshika would choose.</p>
    <div class="choices">
      <button class="choice">Gold ✦</button>
      <button class="choice">Pink 🌸</button>
      <button class="choice">Simple ✨</button>
      <button class="choice">All of them</button>
    </div>
  </div>
</section>

<section id="reveal" class="screen">
  <div class="reveal">
    <div class="envelope"><div class="seal">✦</div></div>
    <h2 class="serif">Okay, you earned it.</h2>
    <p>I remembered that you like bangles.</p>
    <p>And somehow, that little detail stayed in my head.</p>
    <div class="finalName">For Vanshika</div>
    <button class="primary" id="openLetter" style="margin-top:28px">Open the last note</button>
  </div>
</section>

<section id="final" class="screen">
  <div class="reveal">
    <div class="eyebrow">The actual surprise</div>
    <h2 class="serif">Distance is annoying.</h2>
    <p>Because sometimes you want to give someone something instead of sending another text.</p>
    <p style="margin-top:12px">So until I can give you the real bangles...</p>
    <div class="finalName">I hope this made you smile.</div>
    <p style="margin-top:22px;color:#8f8389">— from someone who remembered.</p>
    <button class="primary" id="again" style="margin-top:28px">Play again</button>
  </div>
</section>

<script>
const screens = ["intro","hunt","choice","reveal","final"];
let found = 0;
let running = false;
let timers = [];

function show(id){
  screens.forEach(x => document.getElementById(x).classList.remove("active"));
  document.getElementById(id).classList.add("active");
}

function clearTimers(){
  timers.forEach(clearTimeout);
  timers = [];
}

function sparkle(x,y){
  const chars=["✦","✧","·","♥"];
  for(let i=0;i<8;i++){
    const p=document.createElement("div");
    p.className="confetti";
    p.textContent=chars[Math.floor(Math.random()*chars.length)];
    p.style.left=x+"px";
    p.style.top=y+"px";
    p.style.color=i%2 ? "#d8aa58" : "#d886a4";
    p.style.setProperty("--x",(Math.random()*150-75)+"px");
    p.style.setProperty("--y",(-30-Math.random()*110)+"px");
    document.body.appendChild(p);
    setTimeout(()=>p.remove(),1200);
  }
}

function spawn(){
  const arena=document.getElementById("arena");
  arena.innerHTML="";
  const types=["bangle","bangle pink","star","bangle","bangle pink"];
  for(let i=0;i<5;i++){
    const el=document.createElement("div");
    el.className="item "+types[i];
    const x=18+Math.random()*72;
    const y=10+Math.random()*78;
    el.style.left=x+"%";
    el.style.top=y+"%";
    el.style.animationDelay=(-Math.random()*2)+"s";
    el.setAttribute("aria-label","bangle");
    el.addEventListener("pointerdown",e=>{
      if(el.classList.contains("hit")) return;
      el.classList.add("hit");
      found++;
      document.getElementById("score").textContent=found+" / 5";
      document.getElementById("bar").style.width=(found*20)+"%";
      sparkle(e.clientX,e.clientY);
      if(found===5){
        document.getElementById("instruction").textContent="You found them all ✦";
        timers.push(setTimeout(()=>show("choice"),650));
      }
    });
    arena.appendChild(el);
  }
}

document.getElementById("start").addEventListener("click",()=>{
  show("hunt");
  found=0;
  document.getElementById("score").textContent="0 / 5";
  document.getElementById("bar").style.width="0%";
  spawn();
});

document.querySelectorAll(".choice").forEach(btn=>{
  btn.addEventListener("click",()=>{
    document.querySelectorAll(".choice").forEach(x=>x.classList.remove("selected"));
    btn.classList.add("selected");
    sparkle(window.innerWidth/2,window.innerHeight/2);
    timers.push(setTimeout(()=>show("reveal"),500));
  });
});

document.getElementById("openLetter").addEventListener("click",()=>{
  sparkle(window.innerWidth/2,window.innerHeight/2);
  timers.push(setTimeout(()=>show("final"),250));
});

document.getElementById("again").addEventListener("click",()=>{
  clearTimers();
  found=0;
  show("intro");
});
</script>
</div>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=False)
