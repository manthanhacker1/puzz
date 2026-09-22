import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Vanshika ✦", page_icon="✦", layout="wide")

APP = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#080709;color:#f8efe7}
body{font-family:"DM Sans",sans-serif}
button{font:inherit}
#app{height:100svh;min-height:650px;position:relative;overflow:hidden;background:#080709}
.bg{position:absolute;inset:-20%;background:
radial-gradient(circle at 50% 20%,rgba(220,161,91,.13),transparent 22%),
radial-gradient(circle at 10% 80%,rgba(177,77,120,.15),transparent 28%),
radial-gradient(circle at 90% 70%,rgba(103,78,140,.13),transparent 25%);
transition:transform .25s ease}
.grain{position:absolute;inset:0;opacity:.035;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='x'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23x)'/%3E%3C/svg%3E")}
.screen{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px 20px env(safe-area-inset-bottom);opacity:0;pointer-events:none;transform:scale(.985);transition:opacity .65s,transform .65s}
.screen.on{opacity:1;pointer-events:auto;transform:scale(1)}
.serif{font-family:"Cormorant Garamond",serif}
.eyebrow{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#9c9097}
h1,h2,h3,p{margin:0}
.gold{color:#dfb56b}
.muted{color:#a79aa0}
.cta{border:1px solid rgba(222,181,107,.48);background:rgba(222,181,107,.08);color:#e6c27e;border-radius:999px;padding:14px 24px;font-size:10px;letter-spacing:2px;text-transform:uppercase}
.cta:active{transform:scale(.95)}

#s0{text-align:center}
#s0 h1{font-size:clamp(70px,20vw,105px);font-weight:400;line-height:.75;letter-spacing:-4px;margin:20px 0 25px}
#s0 p{font-size:13px;line-height:1.8;max-width:300px;margin:auto;color:#a79aa0}
.cursor{display:inline-block;width:1px;height:18px;background:#dfb56b;vertical-align:-3px;margin-left:4px;animation:blink 1s infinite}
@keyframes blink{50%{opacity:0}}

.top{position:absolute;top:22px;left:20px;right:20px;display:flex;justify-content:space-between;align-items:center;z-index:20}
.top .step{font-size:9px;letter-spacing:2px;color:#766b72}
.progress{display:flex;gap:4px}.dot{width:20px;height:2px;background:#272127}.dot.done{background:#dcb26a}

#s1{justify-content:flex-start;padding-top:105px}
.letterArea{width:min(360px,94vw);height:410px;position:relative;touch-action:none}
.letterHint{text-align:center;margin-bottom:22px}
.letterHint h2{font-size:37px;font-weight:400}.letterHint p{font-size:12px;color:#94888e;margin-top:8px}
.envelope{position:absolute;left:50%;top:100px;transform:translateX(-50%);width:270px;height:190px;background:#d8c5ae;border-radius:5px;box-shadow:0 30px 80px #000;touch-action:none}
.envelope .flap{position:absolute;z-index:4;left:0;top:0;border-left:135px solid transparent;border-right:135px solid transparent;border-top:105px solid #bfa88f;transform-origin:top;transition:transform .8s cubic-bezier(.2,.8,.2,1)}
.envelope .paper{position:absolute;background:#f5eadc;color:#382b2b;left:15px;right:15px;top:20px;height:155px;padding:24px 18px;text-align:center;transition:transform .9s;z-index:2}
.paper h3{font-family:"Cormorant Garamond";font-size:28px;font-weight:600}.paper p{font-size:10px;line-height:1.7;margin-top:12px}
.seal{position:absolute;z-index:8;left:50%;top:82px;transform:translate(-50%,-50%);width:42px;height:42px;border-radius:50%;background:#a95873;display:grid;place-items:center;box-shadow:0 5px 20px #0008}
.opened .flap{transform:rotateX(175deg)}.opened .paper{transform:translateY(-95px)}

#s2{justify-content:flex-start;padding-top:85px}
.s2title{text-align:center;margin-bottom:12px}.s2title h2{font-size:38px;font-weight:400}.s2title p{font-size:11px;color:#92868d;margin-top:7px}
.tray{width:min(390px,95vw);height:470px;border-radius:32px;position:relative;overflow:hidden;background:
radial-gradient(ellipse at center,rgba(222,180,105,.08),transparent 55%),rgba(255,255,255,.018);
border:1px solid #2b242b;touch-action:none}
.tray:after{content:"";position:absolute;left:18%;right:18%;bottom:18px;height:55px;border-radius:50%;border:1px solid #3c3037;box-shadow:0 0 35px rgba(210,165,90,.07)}
.jewel{position:absolute;width:64px;height:64px;border-radius:50%;display:grid;place-items:center;z-index:5;touch-action:none;user-select:none;cursor:grab;transition:box-shadow .2s}
.jewel:active{cursor:grabbing}
.j1{border:8px solid #d7a954;box-shadow:0 0 25px #d7a95455,inset 0 2px 3px #fff4bf}
.j2{border:7px solid #c96f91;box-shadow:0 0 25px #c96f9155,inset 0 2px 3px #ffe2ea}
.j3{border:7px solid #b8b8bd;box-shadow:0 0 25px #bbb6;inset 0 2px 3px #fff}
.j4{border:7px solid #b77d4d;box-shadow:0 0 25px #b77d4d55,inset 0 2px 3px #ffe0b0}
.j5{border:7px solid #c4a1d8;box-shadow:0 0 25px #c4a1d855,inset 0 2px 3px #fff}
.jewel small{position:absolute;bottom:-22px;font-size:8px;color:#73686f;white-space:nowrap}
.trayCenter{position:absolute;left:50%;bottom:30px;transform:translateX(-50%);width:120px;height:38px;border-radius:50%;border:1px dashed #584b52;color:#796d73;display:grid;place-items:center;font-size:9px;letter-spacing:1px;text-transform:uppercase}
.pop{position:absolute;z-index:30;font-size:11px;color:#e4bd78;pointer-events:none;animation:pop 1s forwards}
@keyframes pop{0%{opacity:0;transform:translateY(5px)}20%{opacity:1}100%{opacity:0;transform:translateY(-45px)}}

#s3{text-align:center}
.question{max-width:350px}.question h2{font-size:53px;font-weight:400;line-height:.84;margin:17px 0}.question p{font-size:12px;line-height:1.8;color:#a4999e}
.meter{width:220px;height:2px;background:#29232a;margin:30px auto}.meter i{display:block;height:100%;width:0;background:#dcb06a;transition:width .7s}
.swipeCard{width:min(310px,85vw);height:190px;margin:0 auto 25px;position:relative;touch-action:none;transform-origin:center bottom}
.card{position:absolute;inset:0;border:1px solid #332a31;border-radius:25px;background:linear-gradient(145deg,#171217,#0e0b0f);display:flex;align-items:center;justify-content:center;flex-direction:column;box-shadow:0 25px 70px #0009}
.card .symbol{font-size:40px;margin-bottom:10px}.card span{font-size:9px;letter-spacing:3px;color:#84787f;text-transform:uppercase}
.swipeHint{font-size:10px;letter-spacing:2px;color:#6f646b;text-transform:uppercase}

#s4{text-align:center}
.boxScene{width:260px;height:230px;position:relative;margin-bottom:28px}
.box{position:absolute;left:30px;right:30px;bottom:35px;height:120px;background:linear-gradient(135deg,#8d4e63,#5c2e42);border-radius:8px;box-shadow:0 35px 70px #0009}
.lid{position:absolute;z-index:5;left:20px;right:20px;top:55px;height:35px;background:#a76376;border-radius:5px;transform-origin:15% 100%;transition:transform 1s cubic-bezier(.2,.9,.2,1)}
.boxLine{position:absolute;left:50%;top:0;bottom:0;width:22px;transform:translateX(-50%);background:#d7a85888}
.ribbon{position:absolute;z-index:6;left:50%;top:72px;transform:translateX(-50%);font-size:24px;color:#e5bb6e}
.mystery{position:absolute;left:50%;top:55px;transform:translate(-50%,-50%) scale(.2);opacity:0;font-size:58px;transition:1s;z-index:3}
.boxOpen .lid{transform:rotate(-27deg) translate(-5px,-35px)}.boxOpen .mystery{opacity:1;transform:translate(-50%,-50%) scale(1)}

#s5{text-align:center}
.final h2{font-size:67px;font-weight:400;line-height:.78;letter-spacing:-2px;margin:15px 0 22px}
.final p{max-width:310px;color:#a79ba0;font-size:13px;line-height:1.9;margin:auto}
.signature{font-family:"Cormorant Garamond";font-size:31px;color:#dfb56b;margin-top:25px}
.burst{position:absolute;left:50%;top:42%;width:5px;height:5px;border-radius:50%;background:#dfb56b;animation:burst 1.3s ease-out forwards;pointer-events:none}
@keyframes burst{to{transform:translate(var(--x),var(--y)) scale(.2);opacity:0}}

@media(max-height:720px){
  #s1{padding-top:80px}.letterArea{height:350px}.envelope{top:70px}
  #s2{padding-top:70px}.tray{height:390px}
}
</style>
</head>
<body>
<div id="app">
<div class="bg" id="bg"></div><div class="grain"></div>

<section id="s0" class="screen on">
  <div class="eyebrow">a tiny thing for one person</div>
  <h1 class="serif">Vanshika<span class="cursor"></span></h1>
  <p>Don't just read this.<br>There is a little surprise hidden inside it.</p>
  <button class="cta" id="begin" style="margin-top:30px">Enter ✦</button>
</section>

<section id="s1" class="screen">
  <div class="top"><span class="step">01 / 05</span><div class="progress"><i class="dot done"></i><i class="dot"></i><i class="dot"></i><i class="dot"></i><i class="dot"></i></div></div>
  <div class="letterArea">
    <div class="letterHint"><h2 class="serif">Something arrived.</h2><p>Don't press it. <b>Swipe the envelope open.</b></p></div>
    <div class="envelope" id="env">
      <div class="paper"><h3>Hi, Vanshika.</h3><p>I wanted to give you something small.<br>But small things can still be special.</p></div>
      <div class="flap"></div><div class="seal">✦</div>
    </div>
  </div>
</section>

<section id="s2" class="screen">
  <div class="top"><span class="step">02 / 05</span><div class="progress"><i class="dot done"></i><i class="dot done"></i><i class="dot"></i><i class="dot"></i><i class="dot"></i></div></div>
  <div class="s2title"><h2 class="serif">Make your own stack.</h2><p>Drag every bangle onto the little tray.</p></div>
  <div class="tray" id="tray">
    <div class="trayCenter">your stack</div>
    <div class="jewel j1" data-id="1" style="left:12%;top:8%;"><small>gold</small></div>
    <div class="jewel j2" data-id="2" style="left:68%;top:17%;"><small>rose</small></div>
    <div class="jewel j3" data-id="3" style="left:20%;top:42%;"><small>silver</small></div>
    <div class="jewel j4" data-id="4" style="left:65%;top:50%;"><small>sunset</small></div>
    <div class="jewel j5" data-id="5" style="left:43%;top:30%;"><small>lavender</small></div>
  </div>
</section>

<section id="s3" class="screen">
  <div class="top"><span class="step">03 / 05</span><div class="progress"><i class="dot done"></i><i class="dot done"></i><i class="dot done"></i><i class="dot"></i><i class="dot"></i></div></div>
  <div class="question">
    <div class="eyebrow">now, your turn</div>
    <h2 class="serif">Which one<br>would you wear?</h2>
    <div class="swipeCard" id="swipeCard">
      <div class="card"><div class="symbol" id="symbol">✦</div><span id="cardText">gold feels like you</span></div>
    </div>
    <div class="swipeHint">swipe left or right</div>
    <div class="meter"><i id="meter"></i></div>
  </div>
</section>

<section id="s4" class="screen">
  <div class="top"><span class="step">04 / 05</span><div class="progress"><i class="dot done"></i><i class="dot done"></i><i class="dot done"></i><i class="dot done"></i><i class="dot"></i></div></div>
  <div class="eyebrow">last little thing</div>
  <div class="boxScene" id="boxScene">
    <div class="box"><div class="boxLine"></div></div>
    <div class="lid"></div>
    <div class="ribbon">✦</div>
    <div class="mystery">💫</div>
  </div>
  <h2 class="serif" style="font-size:39px;font-weight:400">You found it.</h2>
  <p style="font-size:12px;color:#978b91;margin-top:8px">Hold the box for a second.</p>
</section>

<section id="s5" class="screen">
  <div class="final">
    <div class="eyebrow">05 / 05 · unlocked</div>
    <h2 class="serif">For<br><span class="gold">Vanshika.</span></h2>
    <p>I know this isn't a real box of bangles.</p>
    <p style="margin-top:10px">But you were far away, and I still wanted to give you a little something that took more than two seconds to send.</p>
    <div class="signature">So... did I make you smile?</div>
    <button class="cta" id="replay" style="margin-top:28px">Run it again</button>
  </div>
</section>
</div>

<script>
const $=s=>document.querySelector(s);
const screens=[...document.querySelectorAll(".screen")];
let audioCtx=null;

function sound(freq=720,dur=.13){
  try{
    audioCtx ||= new (window.AudioContext||window.webkitAudioContext)();
    const o=audioCtx.createOscillator(), g=audioCtx.createGain();
    o.frequency.value=freq;o.type="sine";g.gain.setValueAtTime(.0001,audioCtx.currentTime);
    g.gain.exponentialRampToValueAtTime(.07,audioCtx.currentTime+.015);
    g.gain.exponentialRampToValueAtTime(.0001,audioCtx.currentTime+dur);
    o.connect(g);g.connect(audioCtx.destination);o.start();o.stop(audioCtx.currentTime+dur+.02);
  }catch(e){}
}
function go(id){
  screens.forEach(s=>s.classList.remove("on"));
  $("#"+id).classList.add("on");
  sound(520,.08);
}
function burst(x,y,n=18){
  for(let i=0;i<n;i++){
    const p=document.createElement("i");p.className="burst";
    p.style.left=x+"px";p.style.top=y+"px";
    const a=Math.random()*Math.PI*2,d=50+Math.random()*170;
    p.style.setProperty("--x",Math.cos(a)*d+"px");
    p.style.setProperty("--y",Math.sin(a)*d+"px");
    document.body.appendChild(p);setTimeout(()=>p.remove(),1400);
  }
}
function pop(txt,x,y){
  const p=document.createElement("div");p.className="pop";p.textContent=txt;
  p.style.left=x+"px";p.style.top=y+"px";document.body.appendChild(p);
  setTimeout(()=>p.remove(),1000);
}
document.addEventListener("pointermove",e=>{
  $("#bg").style.transform=`translate(${(e.clientX-innerWidth/2)*-.012}px,${(e.clientY-innerHeight/2)*-.012}px)`;
},{passive:true});

$("#begin").onclick=()=>{
  sound(680,.2);go("s1");
};

/* Envelope swipe */
let sx=0,sy=0,opened=false;
$("#env").addEventListener("pointerdown",e=>{sx=e.clientX;sy=e.clientY;$("#env").setPointerCapture(e.pointerId)});
$("#env").addEventListener("pointerup",e=>{
  if(opened)return;
  const dx=e.clientX-sx,dy=e.clientY-sy;
  if(dx>35 || Math.abs(dy)>45){
    opened=true;$("#env").classList.add("opened");sound(900,.22);burst(e.clientX,e.clientY,12);
    setTimeout(()=>go("s2"),1100);
  }
});

/* Drag bangles */
let collected=0,drag=null,offset={x:0,y:0};
document.querySelectorAll(".jewel").forEach(j=>{
  j.addEventListener("pointerdown",e=>{
    drag=j;j.setPointerCapture(e.pointerId);
    const r=j.getBoundingClientRect();offset.x=e.clientX-r.left;offset.y=e.clientY-r.top;
    j.style.zIndex=20;j.style.transition="none";sound(650,.08);
  });
  j.addEventListener("pointermove",e=>{
    if(!drag)return;
    const tr=$("#tray").getBoundingClientRect();
    j.style.left=(e.clientX-tr.left-offset.x)+"px";
    j.style.top=(e.clientY-tr.top-offset.y)+"px";
  });
  j.addEventListener("pointerup",e=>{
    if(!drag)return;
    const tr=$("#tray").getBoundingClientRect();
    const cx=e.clientX-tr.left,cy=e.clientY-tr.top;
    const targetX=tr.width/2,targetY=tr.height-48;
    const dist=Math.hypot(cx-targetX,cy-targetY);
    if(dist<105){
      collected++;j.style.left=(targetX-32+collected*3)+"px";j.style.top=(targetY-32-collected*4)+"px";
      j.style.transform=`scale(${1-collected*.035})`;j.style.zIndex=10;
      sound(700+collected*100,.16);pop(["nice ✦","pretty","that one","almost","perfect"][collected-1],targetX-20,targetY-75);
      if(collected===5){burst(innerWidth/2,innerHeight*.65,25);setTimeout(()=>go("s3"),900)}
    }else{
      j.style.transition="left .35s,top .35s";j.style.left=j.dataset.origx||j.style.left;j.style.top=j.dataset.origy||j.style.top;
      sound(280,.07);
    }
    drag=null;
  });
  j.dataset.origx=j.style.left;j.dataset.origy=j.style.top;
});

/* Swipe choice */
let cardX=0, cardStart=0, swiped=0;
const cards=[
 ["✦","gold feels like you"],
 ["🌸","pink has your energy"],
 ["◌","simple is actually beautiful"],
 ["∞","okay... all of them wins"]
];
function nextCard(dir){
  if(swiped>=4)return;
  swiped++;
  $("#meter").style.width=(swiped*25)+"%";
  $("#swipeCard").animate([{transform:`translateX(${dir*260}px) rotate(${dir*18}deg)`,opacity:0},{transform:"translateX(0) rotate(0)",opacity:1}],{duration:420,easing:"ease-out"});
  const c=cards[swiped%cards.length];
  setTimeout(()=>{$("#symbol").textContent=c[0];$("#cardText").textContent=c[1]},170);
  sound(550+swiped*120,.12);
  if(swiped===4){burst(innerWidth/2,innerHeight*.48,18);setTimeout(()=>go("s4"),850)}
}
$("#swipeCard").addEventListener("pointerdown",e=>{cardStart=e.clientX;$("#swipeCard").setPointerCapture(e.pointerId)});
$("#swipeCard").addEventListener("pointerup",e=>{
  const dx=e.clientX-cardStart;
  if(Math.abs(dx)>45)nextCard(dx>0?1:-1);
});

/* Hold box */
let holdTimer=null, holding=false;
const box=$("#boxScene");
box.addEventListener("pointerdown",()=>{
  holding=true;sound(360,.08);
  holdTimer=setTimeout(()=>{
    if(!holding)return;
    box.classList.add("boxOpen");sound(980,.3);burst(innerWidth/2,innerHeight*.47,35);
    setTimeout(()=>go("s5"),1150);
  },1200);
});
["pointerup","pointercancel","pointerleave"].forEach(ev=>box.addEventListener(ev,()=>{
  holding=false;if(holdTimer)clearTimeout(holdTimer);
}));

$("#replay").onclick=()=>location.reload();
</script>
</body>
</html>
"""

components.html(APP, height=900, scrolling=False)
