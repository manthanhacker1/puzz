import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For Vanshika",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

APP = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
<meta name="theme-color" content="#120b10">
<title>For Vanshika</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');

:root{
  --bg:#10090e;
  --pink:#e8a1b8;
  --gold:#e4b04d;
  --cream:#fff7ee;
  --muted:#cdbcc4;
}

*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}

html,body{
  margin:0;
  padding:0;
  width:100%;
  min-height:100%;
  background:#10090e;
}

body{
  font-family:"DM Sans",sans-serif;
  color:white;
  overflow:hidden;
}

button{
  font-family:inherit;
  -webkit-appearance:none;
}

#app{
  position:relative;
  width:100%;
  min-height:100svh;
  overflow:hidden;
  background:
    radial-gradient(circle at 15% 8%,rgba(226,126,159,.18),transparent 31%),
    radial-gradient(circle at 92% 92%,rgba(225,171,73,.12),transparent 32%),
    linear-gradient(150deg,#170c13,#0d080c 70%);
}

.noise{
  position:absolute;
  inset:0;
  opacity:.055;
  pointer-events:none;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 160 160' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.55'/%3E%3C/svg%3E");
}

.screen{
  position:absolute;
  inset:0;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  padding:30px 20px calc(30px + env(safe-area-inset-bottom));
  opacity:0;
  pointer-events:none;
  transform:scale(1.025);
  transition:opacity .65s ease,transform .75s cubic-bezier(.2,.8,.2,1);
}

.screen.active{
  opacity:1;
  pointer-events:auto;
  transform:scale(1);
}

.eyebrow{
  font-size:10px;
  letter-spacing:3.4px;
  text-transform:uppercase;
  color:#d5b7c1;
  margin-bottom:17px;
}

.serif{
  font-family:"Cormorant Garamond",serif;
}

.introTitle{
  text-align:center;
  font-size:clamp(48px,14vw,72px);
  line-height:.88;
  font-weight:500;
  letter-spacing:-2.2px;
  margin:0;
}

.introText{
  max-width:330px;
  text-align:center;
  color:var(--muted);
  font-size:14px;
  line-height:1.8;
  margin:25px 0 30px;
}

.primary{
  border:1px solid rgba(255,255,255,.18);
  background:linear-gradient(135deg,#e99bb1,#a95677);
  color:white;
  border-radius:18px;
  min-height:56px;
  padding:0 28px;
  font-size:15px;
  font-weight:600;
  box-shadow:0 18px 50px rgba(192,78,119,.26);
  cursor:pointer;
}

.primary:active{transform:scale(.97)}

.floatingHeart{
  margin-top:25px;
  color:#e7a3b9;
  font-size:24px;
  animation:heartbeat 2.2s infinite;
}

@keyframes heartbeat{
  0%,100%{transform:scale(1)}
  50%{transform:scale(1.14)}
}

/* gift */
.giftScene{
  width:min(330px,84vw);
  height:290px;
  position:relative;
  margin-bottom:12px;
}

.giftGlow{
  position:absolute;
  width:190px;
  height:190px;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  border-radius:50%;
  background:rgba(230,166,73,.14);
  filter:blur(35px);
}

.box{
  position:absolute;
  width:190px;
  height:125px;
  left:50%;
  top:105px;
  transform:translateX(-50%);
  transform-style:preserve-3d;
}

.boxBody{
  position:absolute;
  left:0;
  right:0;
  bottom:0;
  height:100px;
  border-radius:8px 8px 18px 18px;
  background:
    linear-gradient(135deg,#8d254a,#5d1831 62%,#3c1122);
  box-shadow:0 28px 45px rgba(0,0,0,.45);
  overflow:hidden;
}

.boxBody:after{
  content:"";
  position:absolute;
  left:50%;
  top:0;
  bottom:0;
  width:27px;
  transform:translateX(-50%);
  background:linear-gradient(90deg,#d7a23f,#ffe39a 48%,#b97c20);
  opacity:.95;
}

.lid{
  position:absolute;
  left:-7px;
  top:12px;
  width:204px;
  height:48px;
  border-radius:9px;
  background:linear-gradient(135deg,#a82f59,#651934 68%,#421021);
  box-shadow:0 14px 23px rgba(0,0,0,.38);
  transform-origin:12px 40px;
  transition:transform 1s cubic-bezier(.2,.9,.25,1);
  z-index:4;
}

.lid:after{
  content:"";
  position:absolute;
  left:50%;
  top:0;
  bottom:0;
  width:27px;
  transform:translateX(-50%);
  background:linear-gradient(90deg,#d7a23f,#ffe39a 48%,#b97c20);
}

.ribbon{
  position:absolute;
  left:50%;
  top:45px;
  width:24px;
  height:125px;
  transform:translateX(-50%);
  background:linear-gradient(90deg,#b17a20,#f6d67c,#b17a20);
  z-index:3;
}

.bow{
  position:absolute;
  z-index:5;
  top:16px;
  left:50%;
  width:90px;
  height:50px;
  transform:translateX(-50%);
}

.bow:before,.bow:after{
  content:"";
  position:absolute;
  top:0;
  width:47px;
  height:37px;
  border:7px solid #e1b34e;
  background:#8d254a;
  border-radius:50% 50% 45% 45%;
}
.bow:before{left:0;transform:rotate(-22deg)}
.bow:after{right:0;transform:rotate(22deg)}

.boxOpen .lid{
  transform:translateY(-55px) rotateX(62deg) rotateZ(-2deg);
}

.boxOpen .bow{
  opacity:0;
  transform:translate(-50%,-70px) scale(.7);
  transition:1s ease;
}

.boxOpen .giftGlow{
  opacity:.7;
}

.tapHint{
  color:#d5c4ca;
  font-size:12px;
  letter-spacing:.5px;
  margin-top:6px;
}

/* jewelry */
.jewelStage{
  width:min(380px,100%);
  height:470px;
  position:relative;
  margin-top:2px;
}

.ambient{
  position:absolute;
  width:270px;
  height:270px;
  border-radius:50%;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  background:radial-gradient(circle,rgba(220,158,62,.16),transparent 68%);
  filter:blur(15px);
}

.hand{
  position:absolute;
  left:50%;
  top:43px;
  width:168px;
  height:370px;
  transform:translateX(-50%) rotate(-8deg);
  border-radius:88px 88px 70px 70px;
  background:
    radial-gradient(ellipse at 30% 17%,rgba(255,229,201,.55),transparent 17%),
    linear-gradient(100deg,#8f4c3a 0%,#bc7055 22%,#e0a17f 50%,#c77a5c 78%,#8e4b3a 100%);
  box-shadow:
    inset 10px 0 17px rgba(65,25,18,.25),
    inset -9px 0 18px rgba(74,27,19,.25),
    0 30px 70px rgba(0,0,0,.45);
  overflow:visible;
}

.hand:before{
  content:"";
  position:absolute;
  left:19px;
  top:-38px;
  width:39px;
  height:110px;
  border-radius:25px 25px 16px 16px;
  background:linear-gradient(100deg,#9e5845,#d69272 58%,#b86850);
  transform:rotate(-4deg);
  box-shadow:inset 5px 0 7px rgba(66,26,18,.2);
}

.hand:after{
  content:"";
  position:absolute;
  right:9px;
  top:-28px;
  width:44px;
  height:104px;
  border-radius:25px 25px 17px 17px;
  background:linear-gradient(100deg,#9a5341,#d08a6b 58%,#a75b47);
  transform:rotate(13deg);
}

.wristShadow{
  position:absolute;
  width:190px;
  height:35px;
  left:50%;
  bottom:33px;
  transform:translateX(-50%);
  border-radius:50%;
  background:rgba(0,0,0,.42);
  filter:blur(14px);
}

.banglesReal{
  position:absolute;
  left:50%;
  top:105px;
  width:190px;
  height:180px;
  transform:translateX(-50%) rotate(-8deg);
  pointer-events:none;
}

.ring{
  position:absolute;
  left:50%;
  width:190px;
  height:54px;
  transform:translateX(-50%) scale(.2) rotateX(75deg);
  border-radius:50%;
  opacity:0;
  transition:
    transform .9s cubic-bezier(.16,.9,.24,1),
    opacity .35s;
}

.ring.on{
  opacity:1;
  transform:translateX(-50%) scale(1) rotateX(0deg);
}

.ring.gold{
  border:12px solid #d7a33d;
  box-shadow:
    inset 0 3px 3px rgba(255,250,201,.9),
    inset 0 -5px 7px rgba(88,48,7,.65),
    0 0 0 2px #76500f,
    0 8px 18px rgba(0,0,0,.22),
    0 0 18px rgba(226,172,71,.28);
}

.ring.pink{
  border:11px solid #b84d74;
  box-shadow:
    inset 0 3px 3px rgba(255,225,236,.8),
    inset 0 -5px 8px rgba(76,18,39,.6),
    0 0 0 2px #67213b,
    0 8px 18px rgba(0,0,0,.2);
}

.ring.gem{
  border:9px solid #d7a33d;
  background:
    repeating-linear-gradient(
      90deg,
      transparent 0 13px,
      rgba(255,245,187,.9) 14px 17px,
      transparent 18px 29px
    );
  box-shadow:
    inset 0 3px 3px #fff2ad,
    inset 0 -5px 7px #70420b,
    0 0 0 2px #76500f,
    0 0 16px rgba(230,180,75,.3);
}

.ring:nth-child(1){top:0}
.ring:nth-child(2){top:40px}
.ring:nth-child(3){top:80px}
.ring:nth-child(4){top:120px}

.progress{
  width:min(310px,88vw);
  height:3px;
  background:rgba(255,255,255,.09);
  border-radius:10px;
  overflow:hidden;
  margin:5px auto 16px;
}

.progress > div{
  height:100%;
  width:0%;
  background:linear-gradient(90deg,#d88aa4,#e6b14f);
  transition:width .65s ease;
}

.jewelTitle{
  text-align:center;
  margin-bottom:2px;
  font-size:29px;
  font-weight:500;
}

.jewelSub{
  text-align:center;
  color:#cdbcc4;
  font-size:13px;
  margin-bottom:2px;
}

.actionRow{
  width:min(330px,90vw);
  display:flex;
  flex-direction:column;
  gap:9px;
  margin-top:-3px;
}

/* final */
.finalIcon{
  width:120px;
  height:120px;
  border-radius:50%;
  border:11px solid #d9a94a;
  box-shadow:
    0 0 0 3px #714a12,
    0 0 65px rgba(219,169,71,.35);
  position:relative;
  margin-bottom:34px;
  animation:floatIcon 3s ease-in-out infinite;
}

.finalIcon:after{
  content:"";
  position:absolute;
  inset:24px;
  border-radius:50%;
  border:2px solid rgba(255,244,193,.75);
}

@keyframes floatIcon{
  0%,100%{transform:translateY(0)}
  50%{transform:translateY(-8px)}
}

.finalTitle{
  text-align:center;
  font-size:51px;
  line-height:.92;
  font-weight:500;
  letter-spacing:-1.6px;
  margin:0 0 23px;
}

.finalText{
  max-width:335px;
  text-align:center;
  color:#d8cbd1;
  font-size:14px;
  line-height:1.9;
  margin:6px 0;
}

.signature{
  margin-top:26px;
  color:#e5a7bc;
  font-family:"Cormorant Garamond",serif;
  font-size:26px;
  text-align:center;
}

.sparkleFinal{
  margin-top:19px;
  color:#e4ad4f;
  font-size:19px;
  letter-spacing:10px;
  animation:blink 1.8s infinite;
}

@keyframes blink{
  50%{opacity:.35}
}

#toast{
  position:fixed;
  left:50%;
  bottom:20px;
  transform:translate(-50%,20px);
  background:rgba(24,14,20,.9);
  border:1px solid rgba(255,255,255,.12);
  backdrop-filter:blur(14px);
  padding:11px 17px;
  border-radius:999px;
  font-size:12px;
  color:#f1e6ea;
  opacity:0;
  pointer-events:none;
  transition:.35s ease;
  z-index:20;
  white-space:nowrap;
}

#toast.show{
  opacity:1;
  transform:translate(-50%,0);
}

.particle{
  position:fixed;
  z-index:30;
  pointer-events:none;
  font-size:18px;
  animation:particle 1.35s ease-out forwards;
}

@keyframes particle{
  from{
    opacity:1;
    transform:translate(0,0) scale(1) rotate(0deg);
  }
  to{
    opacity:0;
    transform:translate(var(--x),var(--y)) scale(.2) rotate(220deg);
  }
}

@media(max-height:700px){
  .jewelStage{height:395px}
  .hand{transform:translateX(-50%) rotate(-8deg) scale(.86);top:18px}
  .banglesReal{transform:translateX(-50%) rotate(-8deg) scale(.86)}
}

@media(max-width:360px){
  .introTitle{font-size:45px}
  .finalTitle{font-size:44px}
}
</style>
</head>

<body>
<div id="app">
<div class="noise"></div>

<!-- INTRO -->
<section id="intro" class="screen active">
  <div class="eyebrow">A little surprise for Vanshika</div>

  <h1 class="serif introTitle">
    For the girl<br>
    who loves bangles.
  </h1>

  <p class="introText">
    I couldn't be there to give you something in person...
    so I made a little surprise that could travel the distance.
  </p>

  <button class="primary" onclick="openGift()">
    Open your gift
  </button>

  <div class="floatingHeart">♥</div>
</section>

<!-- GIFT -->
<section id="gift" class="screen">
  <div class="eyebrow">Something small, just for you</div>

  <div class="giftScene">
    <div class="giftGlow"></div>

    <div class="box" id="giftBox">
      <div class="boxBody"></div>
      <div class="ribbon"></div>
      <div class="lid"></div>
      <div class="bow"></div>
    </div>
  </div>

  <h2 class="serif" style="font-size:34px;font-weight:500;margin:0 0 8px">
    Made for Vanshika
  </h2>

  <p class="tapHint">Tap the box</p>
</section>

<!-- JEWELRY -->
<section id="jewelry" class="screen">

  <div class="eyebrow">For your wrist</div>

  <div class="jewelTitle serif">One at a time...</div>
  <div class="jewelSub">Tap the button and watch them come alive.</div>

  <div class="progress">
    <div id="progress"></div>
  </div>

  <div class="jewelStage">
    <div class="ambient"></div>

    <div class="wristShadow"></div>

    <div class="hand"></div>

    <div class="banglesReal">
      <div class="ring gold"></div>
      <div class="ring pink"></div>
      <div class="ring gem"></div>
      <div class="ring gold"></div>
    </div>
  </div>

  <div class="actionRow">
    <button class="primary" id="bangleBtn" onclick="addBangle()">
      Put on the first one
    </button>
  </div>
</section>

<!-- FINAL -->
<section id="final" class="screen">

  <div class="finalIcon"></div>

  <h1 class="serif finalTitle">
    Vanshika,<br>
    one day these<br>
    won't be on a screen.
  </h1>

  <p class="finalText">
    Until then, let this little gift remind you
    that someone is thinking about you from far away.
  </p>

  <p class="finalText">
    And yes... I still owe you the real bangles.
  </p>

  <div class="signature">
    — someone who likes you a little too much
  </div>

  <div class="sparkleFinal">✦ · ✦</div>

  <button class="primary" style="margin-top:28px" onclick="location.reload()">
    See it again
  </button>

</section>

<div id="toast"></div>

<script>
let bangleCount = 0;
let audioCtx = null;

function screen(name){
  document.querySelectorAll(".screen").forEach(s => s.classList.remove("active"));
  document.getElementById(name).classList.add("active");
}

function sound(freq=620, duration=.08){
  try{
    if(!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = "sine";
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(
      freq * 1.65,
      audioCtx.currentTime + duration
    );

    gain.gain.setValueAtTime(.0001, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(
      .075,
      audioCtx.currentTime + .012
    );
    gain.gain.exponentialRampToValueAtTime(
      .0001,
      audioCtx.currentTime + duration
    );

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + duration + .02);
  }catch(e){}
}

function openGift(){

  sound(420,.12);

  screen("gift");

  setTimeout(() => {

    const box = document.getElementById("giftBox");

    box.classList.add("boxOpen");

    sound(690,.16);

    setTimeout(() => {
      screen("jewelry");
      burst(18);
    }, 1050);

  }, 450);
}

function addBangle(){

  if(bangleCount >= 4) return;

  const rings = document.querySelectorAll(".ring");

  rings[bangleCount].classList.add("on");

  bangleCount++;

  document.getElementById("progress").style.width =
    ((bangleCount / 4) * 100) + "%";

  const button = document.getElementById("bangleBtn");

  const text = [
    "One more...",
    "It's getting prettier...",
    "Almost there...",
    "One last sparkle..."
  ];

  button.innerText = text[bangleCount - 1];

  sound(560 + bangleCount * 95,.11);

  burst(10);

  if(bangleCount === 4){

    setTimeout(() => {

      button.innerText = "One last thing...";

      button.onclick = () => {

        sound(780,.18);
        burst(30);

        setTimeout(() => {
          screen("final");
        }, 650);

      };

    }, 800);
  }
}

function burst(amount){

  const chars = ["✦","·","✧","♥"];

  for(let i=0;i<amount;i++){

    const p = document.createElement("div");

    p.className = "particle";

    p.innerText =
      chars[Math.floor(Math.random()*chars.length)];

    p.style.left =
      (35 + Math.random()*30) + "%";

    p.style.top =
      (35 + Math.random()*25) + "%";

    p.style.setProperty(
      "--x",
      ((Math.random()-.5)*240) + "px"
    );

    p.style.setProperty(
      "--y",
      (-80-Math.random()*210) + "px"
    );

    p.style.color =
      Math.random() > .5 ? "#e4b04d" : "#e5a5ba";

    document.body.appendChild(p);

    setTimeout(() => p.remove(),1450);
  }
}

/* tap anywhere on the gift box */
document.getElementById("gift").addEventListener("click", function(e){

  if(e.target.closest("button")) return;

  if(!document.getElementById("giftBox").classList.contains("boxOpen")){
    openGift();
  }
});

</script>

</div>
</body>
</html>
"""

components.html(APP, height=820, scrolling=False)
