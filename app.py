import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vanshika — A Little Something", page_icon="♡", layout="wide")

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<title>For Vanshika</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500;600&display=swap');
:root{--bg:#070608;--fg:#f5eee8;--muted:#93898f;--gold:#dfb76e;--pink:#bd718c}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#070608;color:var(--fg)}
body{font-family:"DM Sans",sans-serif}
button{font:inherit}
#app{height:100svh;min-height:620px;position:relative;overflow:hidden;background:#070608}
#world{position:absolute;inset:0;transition:background 1.5s ease}
.grain{position:absolute;inset:0;opacity:.035;pointer-events:none;z-index:100;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='x'%3E%3CfeTurbulence baseFrequency='.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23x)'/%3E%3C/svg%3E")}
.serif{font-family:"Cormorant Garamond",serif}
.screen{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;padding:30px 20px env(safe-area-inset-bottom);opacity:0;visibility:hidden;transform:scale(1.025);transition:opacity .8s,transform .8s}
.screen.active{opacity:1;visibility:visible;transform:none}
.eyebrow{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#81767d}
.muted{color:var(--muted)}
.gold{color:var(--gold)}
.cta{border:1px solid #dfb76e77;color:#e6c27d;background:#dfb76e0d;border-radius:100px;padding:14px 25px;font-size:10px;letter-spacing:2px;text-transform:uppercase}
.cta:active{transform:scale(.96)}
.top{position:absolute;top:20px;left:20px;right:20px;display:flex;justify-content:space-between;z-index:40}
.top span{font-size:9px;letter-spacing:2px;color:#71676d}

/* OPENING */
#opening{text-align:center;background:radial-gradient(circle at 50% 48%,#25151d 0,#0b080a 35%,#070608 70%)}
#opening .tiny{font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#8d8188}
#opening h1{font-size:clamp(65px,19vw,100px);font-weight:400;line-height:.72;letter-spacing:-4px;margin:22px 0}
#opening .line{width:1px;height:0;background:var(--gold);margin:0 auto 20px;transition:height 1s}
#opening.ready .line{height:48px}
.type{font-size:13px;line-height:1.8;min-height:50px;color:#a69aa0}
.caret{display:inline-block;width:1px;height:15px;background:#dcb16a;margin-left:3px;vertical-align:-2px;animation:blink 1s infinite}
@keyframes blink{50%{opacity:0}}

/* NOTIFICATION */
#notif{background:#080709}
.phone{width:min(350px,91vw);height:560px;border:1px solid #30292f;border-radius:36px;background:linear-gradient(145deg,#121014,#09080a);box-shadow:0 30px 100px #000;position:relative;overflow:hidden;padding:18px}
.notch{width:92px;height:22px;background:#050505;border-radius:20px;margin:auto}
.status{display:flex;justify-content:space-between;margin-top:15px;font-size:9px;color:#8b8087}
.locktime{text-align:center;margin-top:55px;font-size:60px;font-weight:300}
.date{text-align:center;font-size:10px;color:#82777d;margin-top:3px}
.notification{position:absolute;left:17px;right:17px;top:225px;border:1px solid #3a3036;background:#201a20dd;backdrop-filter:blur(20px);border-radius:20px;padding:17px;box-shadow:0 20px 50px #000;transition:.45s;touch-action:none}
.notification b{font-size:11px}.notification p{font-size:11px;color:#b2a7ac;line-height:1.5;margin-top:7px}
.notification small{font-size:8px;color:#786d73;display:block;margin-bottom:7px}
.notification.swiped{transform:translateX(130%) rotate(8deg);opacity:0}
.swipeLabel{text-align:center;margin-top:25px;color:#655b61;font-size:9px;letter-spacing:2px;text-transform:uppercase}

/* DARK ROOM */
#room{background:radial-gradient(circle at 50% 52%,#191116 0,#09070a 35%,#050506 75%)}
.roomTitle{position:absolute;top:72px;text-align:center;opacity:0;transition:1s}
.roomTitle.show{opacity:1}
.roomTitle h2{font-size:35px;font-weight:400}.roomTitle p{font-size:11px;margin-top:7px}
.explore{position:absolute;inset:0;touch-action:none}
.lamp{position:absolute;left:50%;top:54%;transform:translate(-50%,-50%);width:210px;height:210px;border-radius:50%;background:radial-gradient(circle,#b8754650 0,#7b493d18 30%,transparent 68%);filter:blur(2px);opacity:.08;transition:opacity 1.5s}
.roomGlow{position:absolute;width:90px;height:90px;border-radius:50%;background:#e1a96b;box-shadow:0 0 80px 35px #dba26366;pointer-events:none;mix-blend-mode:screen;transform:translate(-50%,-50%);opacity:0;transition:opacity .4s}
.hiddenObj{position:absolute;width:34px;height:34px;border-radius:50%;opacity:.05;transform:scale(.6);transition:.3s;touch-action:none}
.hiddenObj.found{opacity:1;transform:scale(1)}
.hiddenObj:before{content:"✦";position:absolute;inset:0;display:grid;place-items:center;color:#dfb76e;font-size:25px;text-shadow:0 0 25px #dfb76e}
.obj1{left:22%;top:31%}.obj2{right:18%;top:42%}.obj3{left:48%;bottom:20%}
.roomMessage{position:absolute;bottom:70px;left:20px;right:20px;text-align:center;font-size:11px;color:#a3989e;opacity:0;transition:.6s}.roomMessage.show{opacity:1}
.tapHint{position:absolute;bottom:30px;font-size:8px;letter-spacing:2px;color:#5f565c;text-transform:uppercase}

/* DRAWER */
#drawerScene{background:linear-gradient(#0a080a,#110b0e)}
.drawerWrap{width:min(350px,92vw);height:430px;position:relative;perspective:900px}
.dresser{position:absolute;left:8%;right:8%;bottom:30px;height:250px;background:linear-gradient(110deg,#39232a,#1c1116);border-radius:10px;box-shadow:0 35px 80px #000}
.dresserTop{position:absolute;left:-3%;right:-3%;top:-18px;height:32px;border-radius:7px;background:#4a3030}
.drawer{position:absolute;left:10%;right:10%;top:55px;height:110px;background:linear-gradient(#3b252b,#24151a);border-radius:6px;transition:transform 1s cubic-bezier(.2,.9,.2,1);touch-action:none}
.drawer:after{content:"";position:absolute;left:50%;top:22px;width:42px;height:7px;border-radius:10px;background:#b58a55;transform:translateX(-50%);box-shadow:0 2px 4px #000}
.drawer.open{transform:translateY(125px)}
.drawerInside{position:absolute;left:12%;right:12%;top:70px;height:100px;border-radius:8px;background:#120c0f;border:1px solid #3b2930;opacity:0;transition:opacity .8s}
.drawer.open+.drawerInside{opacity:1}
.drawerObj{position:absolute;width:45px;height:45px;border-radius:50%;display:grid;place-items:center;color:#e3b86f;border:1px solid #7d6242;background:#241a19;font-size:19px}
.do1{left:14%;top:25px}.do2{left:43%;top:32px}.do3{right:12%;top:20px}
.drawerTitle{text-align:center;margin-bottom:15px}.drawerTitle h2{font-size:38px;font-weight:400}.drawerTitle p{font-size:11px;color:#90858b;margin-top:6px}
.drawerHint{position:absolute;bottom:35px;font-size:9px;letter-spacing:2px;color:#665b61;text-transform:uppercase}

/* BANGLES */
#bangles{background:radial-gradient(circle at 50% 45%,#1b1215,#080709 65%)}
.bangleTitle{text-align:center;position:absolute;top:65px}.bangleTitle h2{font-size:38px;font-weight:400}.bangleTitle p{font-size:11px;color:#90858b;margin-top:7px}
.bangleArena{position:relative;width:min(390px,96vw);height:450px;border-radius:30px;border:1px solid #2c242b;background:radial-gradient(circle at 50% 58%,#20181a,#0d0a0d);overflow:hidden;touch-action:none}
.bangle{position:absolute;width:72px;height:72px;border-radius:50%;touch-action:none;cursor:grab;user-select:none;transition:box-shadow .2s}
.bangle.g{border:9px solid #d5a54f;box-shadow:inset 0 2px 3px #fff0ae,0 0 24px #d5a54f44}
.bangle.p{border:8px solid #c66d8c;box-shadow:inset 0 2px 3px #ffdce7,0 0 24px #c66d8c44}
.bangle.s{border:8px solid #b9bdc2;box-shadow:inset 0 2px 3px white,0 0 24px #bbb4}
.bangle.l{border:8px solid #a786bf;box-shadow:inset 0 2px 3px #fff,0 0 24px #a786bf44}
.bangle.c{border:8px solid #c77a4f;box-shadow:inset 0 2px 3px #ffd5b5,0 0 24px #c77a4f44}
.stackZone{position:absolute;left:50%;bottom:22px;transform:translateX(-50%);width:150px;height:85px;border-radius:50%;border:1px dashed #6a5350;display:grid;place-items:center;color:#756970;font-size:8px;letter-spacing:2px;text-transform:uppercase}
.count{position:absolute;right:15px;top:15px;font-size:9px;letter-spacing:2px;color:#7d7177}
.bangleMsg{position:absolute;left:20px;right:20px;bottom:100px;text-align:center;color:#b2a6ab;font-size:11px;opacity:0;transition:.5s}.bangleMsg.on{opacity:1}

/* CHOICE */
#choice{background:radial-gradient(circle at 50% 45%,#21131a,#080709 70%);text-align:center}
#choice h2{font-size:55px;font-weight:400;line-height:.82;margin:18px 0}
.choiceSub{max-width:290px;font-size:12px;color:#a0969b;line-height:1.7}
.choiceRow{display:flex;gap:12px;margin-top:28px}
.choiceCard{width:94px;height:120px;border-radius:20px;border:1px solid #32272e;background:#151014;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;color:#d8cbd0}
.choiceCard i{font-style:normal;font-size:31px}.choiceCard span{font-size:8px;letter-spacing:1px;color:#776c72}
.choiceCard:active{transform:scale(.94)}
.choiceCard.selected{border-color:#dcb16c;box-shadow:0 0 30px #dcb16c22}

/* DISTANCE */
#distance{background:#060608}
.distanceTitle{text-align:center;position:absolute;top:75px}.distanceTitle h2{font-size:40px;font-weight:400}.distanceTitle p{font-size:11px;color:#8e8389;margin-top:8px}
.map{width:min(370px,94vw);height:390px;position:relative}
.mapLine{position:absolute;left:18%;right:18%;top:52%;height:1px;background:linear-gradient(90deg,#b06c86,#d6ad67);transform-origin:left;transition:.2s}
.person{position:absolute;top:calc(52% - 23px);width:46px;height:46px;border-radius:50%;display:grid;place-items:center;border:1px solid #5e4a51;background:#160f13;z-index:3;touch-action:none;box-shadow:0 0 25px #000}
.you{left:8%}.her{right:8%;border-color:#806143}.person b{font-size:8px;font-weight:400;letter-spacing:1px}
.distanceText{text-align:center;color:#8e8289;font-size:10px;letter-spacing:1px}
.distanceText strong{display:block;font-family:"Cormorant Garamond";font-size:29px;color:#dcb16c;font-weight:400;margin-bottom:3px}
.mapHint{font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#61575d;margin-top:17px}

/* FINAL */
#final{background:radial-gradient(circle at 50% 46%,#2a151e,#0a080a 48%,#050506 80%);text-align:center}
.ring{width:115px;height:115px;border:2px solid #d9ad62;border-radius:50%;box-shadow:0 0 45px #d9ad6240,inset 0 0 30px #d9ad6218;display:grid;place-items:center;margin-bottom:30px;animation:rotate 8s linear infinite}
.ring:before{content:"";width:12px;height:12px;background:#e2b76c;box-shadow:0 0 25px #e2b76c;border-radius:50%;transform:translateY(-58px)}
@keyframes rotate{to{transform:rotate(360deg)}}
#final h2{font-size:65px;font-weight:400;line-height:.77;letter-spacing:-2px;margin-bottom:22px}
#final p{max-width:305px;font-size:13px;line-height:1.9;color:#a69ba0}
.signature{font-family:"Cormorant Garamond";font-size:31px;color:#dfb76e;margin-top:25px}
#final .tinyFinal{font-size:9px;letter-spacing:2px;color:#665b61;margin-top:22px;text-transform:uppercase}

/* FX */
.particle{position:absolute;width:4px;height:4px;border-radius:50%;background:#dfb76e;pointer-events:none;z-index:90;animation:fly 1.5s ease-out forwards}
@keyframes fly{to{transform:translate(var(--x),var(--y)) scale(.1);opacity:0}}
.flash{position:absolute;inset:0;background:white;opacity:0;pointer-events:none;z-index:80}
@keyframes flash{0%{opacity:0}15%{opacity:.13}100%{opacity:0}}
</style>
</head>
<body>
<div id="app">
<div id="world"></div><div class="grain"></div><div class="flash" id="flash"></div>

<section class="screen active" id="opening">
  <div class="tiny">for one particular person</div>
  <h1 class="serif">Vanshika</h1>
  <div class="line"></div>
  <div class="type" id="type"></div>
  <button class="cta" id="enter" style="margin-top:27px;opacity:0;transition:1s">don't just watch</button>
</section>

<section class="screen" id="notif">
  <div class="phone">
    <div class="notch"></div>
    <div class="status"><span>9:41</span><span>♡　▰</span></div>
    <div class="locktime">9:41</div><div class="date">Tuesday · just for you</div>
    <div class="notification" id="notification">
      <small>ONE NEW MESSAGE</small><b>someone who remembered</b>
      <p>Vanshika, I made something instead of sending you another boring text.</p>
    </div>
    <div class="swipeLabel">swipe it away →</div>
  </div>
</section>

<section class="screen" id="room">
  <div class="roomTitle" id="roomTitle"><div class="eyebrow">01 · look closer</div><h2 class="serif">There are three things hidden here.</h2><p class="muted">Move the little light with your finger.</p></div>
  <div class="explore" id="explore">
    <div class="lamp" id="lamp"></div><div class="roomGlow" id="roomGlow"></div>
    <div class="hiddenObj obj1" data-msg="You notice little things."></div>
    <div class="hiddenObj obj2" data-msg="That's one thing I like about you."></div>
    <div class="hiddenObj obj3" data-msg="Okay... you're actually good at this."></div>
  </div>
  <div class="roomMessage" id="roomMessage"></div>
  <div class="tapHint">explore the dark</div>
</section>

<section class="screen" id="drawerScene">
  <div class="drawerTitle"><div class="eyebrow">02 · something left behind</div><h2 class="serif">Open the drawer.</h2><p>Drag the handle down.</p></div>
  <div class="drawerWrap" id="drawerWrap">
    <div class="dresser"><div class="dresserTop"></div></div>
    <div class="drawer" id="drawer"></div>
    <div class="drawerInside">
      <div class="drawerObj do1">✦</div><div class="drawerObj do2">♡</div><div class="drawerObj do3">◌</div>
    </div>
  </div>
  <div class="drawerHint">pull ↓</div>
</section>

<section class="screen" id="bangles">
  <div class="bangleTitle"><div class="eyebrow">03 · the part I remembered</div><h2 class="serif">Build the stack.</h2><p>Drag all five bangles into the circle.</p></div>
  <div class="bangleArena" id="bangleArena">
    <span class="count" id="bCount">0 / 5</span>
    <div class="bangle g" data-id="1" style="left:12%;top:14%"></div>
    <div class="bangle p" data-id="2" style="left:66%;top:17%"></div>
    <div class="bangle s" data-id="3" style="left:22%;top:43%"></div>
    <div class="bangle l" data-id="4" style="left:67%;top:48%"></div>
    <div class="bangle c" data-id="5" style="left:43%;top:31%"></div>
    <div class="stackZone">stack here</div>
    <div class="bangleMsg" id="bMsg"></div>
  </div>
</section>

<section class="screen" id="choice">
  <div class="eyebrow">04 · your choice</div>
  <h2 class="serif">Which feels<br>most like you?</h2>
  <p class="choiceSub">There isn't a correct answer. I just wanted to know.</p>
  <div class="choiceRow">
    <button class="choiceCard" data-choice="gold"><i>✦</i><span>gold</span></button>
    <button class="choiceCard" data-choice="pink"><i>♡</i><span>pink</span></button>
    <button class="choiceCard" data-choice="simple"><i>◌</i><span>simple</span></button>
  </div>
</section>

<section class="screen" id="distance">
  <div class="distanceTitle"><div class="eyebrow">05 · the annoying part</div><h2 class="serif">Close the distance.</h2><p>Drag us toward each other.</p></div>
  <div class="map" id="map">
    <div class="mapLine" id="mapLine"></div>
    <div class="person you" id="you"><b>YOU</b></div>
    <div class="person her" id="her"><b>HER</b></div>
  </div>
  <div class="distanceText"><strong id="distanceNumber">far</strong><span id="distanceCaption">still too much screen between us</span></div>
  <div class="mapHint">drag either circle</div>
</section>

<section class="screen" id="final">
  <div class="ring"></div>
  <div class="eyebrow">all five unlocked</div>
  <h2 class="serif">For<br><span class="gold">Vanshika.</span></h2>
  <p>I couldn't give you the real bangles from this far away.</p>
  <p style="margin-top:10px">So I made you something that took a little more effort than typing “good morning”.</p>
  <div class="signature">I hope you smiled.</div>
  <div class="tinyFinal">the real ones are still pending ♡</div>
  <button class="cta" id="again" style="margin-top:25px">experience it again</button>
</section>
</div>

<script>
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
let audio=null;
function tone(f=600,d=.12){
 try{
  audio ||= new (window.AudioContext||window.webkitAudioContext)();
  const o=audio.createOscillator(),g=audio.createGain();
  o.type="sine";o.frequency.value=f;g.gain.setValueAtTime(.0001,audio.currentTime);
  g.gain.exponentialRampToValueAtTime(.055,audio.currentTime+.015);
  g.gain.exponentialRampToValueAtTime(.0001,audio.currentTime+d);
  o.connect(g);g.connect(audio.destination);o.start();o.stop(audio.currentTime+d+.02);
 }catch(e){}
}
function go(id){
 $$("section.screen").forEach(s=>s.classList.remove("active"));
 $("#"+id).classList.add("active");
 tone(520,.08);
}
function particles(x,y,n=22){
 for(let i=0;i<n;i++){
  const p=document.createElement("i");p.className="particle";p.style.left=x+"px";p.style.top=y+"px";
  const a=Math.random()*Math.PI*2,d=60+Math.random()*210;
  p.style.setProperty("--x",Math.cos(a)*d+"px");p.style.setProperty("--y",Math.sin(a)*d+"px");
  document.body.appendChild(p);setTimeout(()=>p.remove(),1600);
 }
}
function flash(){const f=$("#flash");f.style.animation="none";void f.offsetWidth;f.style.animation="flash .65s"}
function typeText(el,text,cb){
 let i=0;const t=setInterval(()=>{el.innerHTML=text.slice(0,++i)+'<span class="caret"></span>';if(i>=text.length){clearInterval(t);setTimeout(cb,450)}},42)
}
setTimeout(()=>{
 $("#opening").classList.add("ready");
 typeText($("#type"),"I made you a little world to play with.",()=>{$("#enter").style.opacity=1});
},500);
$("#enter").onclick=()=>{tone(700,.2);go("notif")};

/* notification swipe */
let nstart=0;
$("#notification").addEventListener("pointerdown",e=>{nstart=e.clientX;$("#notification").setPointerCapture(e.pointerId)});
$("#notification").addEventListener("pointerup",e=>{
 if(e.clientX-nstart>45){$("#notification").classList.add("swiped");tone(850,.16);setTimeout(()=>{go("room");$("#roomTitle").classList.add("show")},550)}
});

/* room flashlight */
let found=0, lastMove=0;
const glow=$("#roomGlow"),lamp=$("#lamp"),explore=$("#explore");
explore.addEventListener("pointermove",e=>{
 const r=explore.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
 glow.style.left=x+"px";glow.style.top=y+"px";glow.style.opacity=.9;
 lamp.style.opacity=.18;
 if(Date.now()-lastMove>100){lastMove=Date.now();$$(".hiddenObj").forEach(o=>{
  const rr=o.getBoundingClientRect(),cx=rr.left+rr.width/2,cy=rr.top+rr.height/2;
  const d=Math.hypot(e.clientX-cx,e.clientY-cy);
  if(d<70&&!o.classList.contains("found")){
   o.classList.add("found");found++;tone(700+found*130,.18);
   $("#roomMessage").textContent=o.dataset.msg;$("#roomMessage").classList.add("show");
   particles(e.clientX,e.clientY,10);
   if(found===3)setTimeout(()=>go("drawerScene"),1000);
  }
 })}});
explore.addEventListener("pointerdown",e=>{glow.style.opacity=.95});
explore.addEventListener("pointerup",()=>{glow.style.opacity=.45});

/* drawer pull */
let ds=0,openedDrawer=false;
$("#drawer").addEventListener("pointerdown",e=>{ds=e.clientY;$("#drawer").setPointerCapture(e.pointerId)});
$("#drawer").addEventListener("pointermove",e=>{
 if(openedDrawer)return;
 const dy=Math.max(0,Math.min(130,e.clientY-ds));
 $("#drawer").style.transform=`translateY(${dy}px)`;
});
$("#drawer").addEventListener("pointerup",e=>{
 if(openedDrawer)return;
 if(e.clientY-ds>55){
  openedDrawer=true;$("#drawer").classList.add("open");tone(430,.22);particles(innerWidth/2,innerHeight*.55,15);
  setTimeout(()=>go("bangles"),900);
 }else $("#drawer").style.transform="";
});

/* bangles */
let bFound=0,drag=null,offX=0,offY=0;
$$(".bangle").forEach(b=>{
 const orig={l:b.style.left,t:b.style.top};b.dataset.ol=orig.l;b.dataset.ot=orig.t;
 b.addEventListener("pointerdown",e=>{
  drag=b;b.setPointerCapture(e.pointerId);const r=b.getBoundingClientRect();
  offX=e.clientX-r.left;offY=e.clientY-r.top;b.style.zIndex=20;b.style.transition="none";tone(620,.07);
 });
 b.addEventListener("pointermove",e=>{
  if(!drag)return;const r=$("#bangleArena").getBoundingClientRect();
  b.style.left=(e.clientX-r.left-offX)+"px";b.style.top=(e.clientY-r.top-offY)+"px";
 });
 b.addEventListener("pointerup",e=>{
  if(!drag)return;
  const ar=$("#bangleArena").getBoundingClientRect(),x=e.clientX-ar.left,y=e.clientY-ar.top;
  const tx=ar.width/2,ty=ar.height-65;
  if(Math.hypot(x-tx,y-ty)<110){
   bFound++;b.style.left=(tx-36+bFound*2)+"px";b.style.top=(ty-36-bFound*5)+"px";b.style.transform=`scale(${1-bFound*.035})`;
   tone(700+bFound*100,.15);$("#bCount").textContent=bFound+" / 5";
   $("#bMsg").textContent=["the gold one.","a little colour.","one more.","almost there.","that's the stack."][bFound-1];$("#bMsg").classList.add("on");
   particles(e.clientX,e.clientY,8);
   if(bFound===5){flash();particles(innerWidth/2,innerHeight*.65,30);setTimeout(()=>go("choice"),950)}
  }else{
   b.style.transition="left .35s,top .35s";b.style.left=b.dataset.ol;b.style.top=b.dataset.ot;
  }
  drag=null;
 });
});

/* choice branches visually */
$$(".choiceCard").forEach(c=>c.onclick=()=>{
 $$(".choiceCard").forEach(x=>x.classList.remove("selected"));c.classList.add("selected");
 const choice=c.dataset.choice;
 $("#world").style.background=choice==="pink"?"radial-gradient(circle at 70% 35%,#4a1d31,#080709 65%)":choice==="gold"?"radial-gradient(circle at 50% 35%,#44311a,#080709 65%)":"radial-gradient(circle at 50% 35%,#202026,#080709 65%)";
 tone(choice==="pink"?820:choice==="gold"?660:520,.22);particles(innerWidth/2,innerHeight*.55,16);
 setTimeout(()=>go("distance"),700);
});

/* distance drag */
let youX=.08,herX=.92,which=null,startX=0;
function renderDistance(){
 const w=$("#map").clientWidth;
 const yx=youX*w,hx=herX*w;
 $("#you").style.left=(yx-23)+"px";$("#her").style.left=(hx-23)+"px";$("#her").style.right="auto";
 const gap=Math.abs(hx-yx)/w;
 $("#mapLine").style.left=yx+"px";$("#mapLine").style.width=Math.max(1,hx-yx)+"px";
 $("#distanceNumber").textContent=gap<.16?"almost there":gap<.3?"closer":"far";
 $("#distanceCaption").textContent=gap<.16?"okay... that's better":"still too much screen between us";
}
["you","her"].forEach(id=>{
 const el=$("#"+id);
 el.addEventListener("pointerdown",e=>{which=id;startX=e.clientX;el.setPointerCapture(e.pointerId)});
 el.addEventListener("pointermove",e=>{
  if(!which)return;
  const r=$("#map").getBoundingClientRect(),p=Math.max(.06,Math.min(.94,(e.clientX-r.left)/r.width));
  if(which==="you")youX=Math.min(p,herX-.045);else herX=Math.max(p,youX+.045);
  renderDistance();
 });
 el.addEventListener("pointerup",()=>{
  if(Math.abs(herX-youX)<.16){
   which=null;tone(900,.3);particles(innerWidth/2,innerHeight*.5,40);flash();
   setTimeout(()=>go("final"),900);
  }
  which=null;
 });
});
renderDistance();

$("#again").onclick=()=>location.reload();
</script>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=False)
