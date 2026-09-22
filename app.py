import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Bangle & Co. — For Vanshika", page_icon="♡", layout="wide")

HTML = r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<title>Bangle & Co.</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@400;500&display=swap');
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{margin:0;background:#f7f3ee;color:#201b1d;font-family:"DM Sans",sans-serif}
body{overflow-x:hidden}
button{font:inherit;cursor:pointer}
.app{min-height:100svh;background:#f7f3ee}
.nav{height:64px;position:sticky;top:0;z-index:50;background:#f7f3eef0;backdrop-filter:blur(18px);border-bottom:1px solid #e8dfd7;display:flex;align-items:center;justify-content:space-between;padding:0 18px}
.logo{font-family:"Playfair Display",serif;font-size:20px;letter-spacing:-.5px}.logo span{color:#ad7a45}
.navRight{display:flex;gap:8px;align-items:center}
.iconBtn{width:40px;height:40px;border:1px solid #ded4cc;background:#fff;border-radius:50%;display:grid;place-items:center;color:#3a3033;position:relative}
.badge{position:absolute;right:-2px;top:-2px;background:#ad6d82;color:#fff;width:17px;height:17px;border-radius:50%;font-size:8px;display:none;place-items:center}
.badge.show{display:grid}
.hero{padding:28px 18px 22px;background:linear-gradient(145deg,#eee1d7,#f8f4ef)}
.hero small{font-size:9px;letter-spacing:3px;color:#907e78;text-transform:uppercase}
.hero h1{font-family:"Playfair Display",serif;font-weight:400;font-size:42px;line-height:.95;margin:12px 0 9px;letter-spacing:-1.8px}
.hero p{font-size:11px;color:#806f72;line-height:1.7;max-width:310px}
.tabs{display:flex;gap:7px;overflow:auto;padding:15px 18px 4px;scrollbar-width:none}.tabs::-webkit-scrollbar{display:none}
.tab{border:1px solid #ddd3cc;background:#fff;border-radius:100px;padding:9px 14px;font-size:9px;white-space:nowrap;color:#75686b}
.tab.active{background:#292123;color:#fff;border-color:#292123}
.grid{padding:15px 14px 110px;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.product{background:#fff;border-radius:17px;overflow:hidden;border:1px solid #e9e0d9;box-shadow:0 5px 18px #4b30200a;position:relative}
.pic{height:205px;position:relative;display:grid;place-items:center;overflow:hidden;background:#eee8e2}
.pic img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .45s ease}.product:hover .pic img{transform:scale(1.035)}
.save{position:absolute;right:10px;top:10px;width:30px;height:30px;border:0;background:#fffdfbd9;border-radius:50%;font-size:14px;z-index:2}
.productInfo{padding:12px 12px 13px}
.name{font-family:"Playfair Display",serif;font-size:16px}.desc{font-size:8px;color:#938487;margin:4px 0 10px;line-height:1.5}
.row{display:flex;justify-content:space-between;align-items:center}.price{font-size:11px;font-weight:600}
.add{border:0;background:#292123;color:#fff;border-radius:9px;padding:8px 10px;font-size:8px;letter-spacing:.6px;text-transform:uppercase}.add:active{transform:scale(.95)}
.toast{position:fixed;left:50%;bottom:22px;transform:translate(-50%,20px);background:#292123;color:#fff;padding:11px 16px;border-radius:100px;font-size:9px;z-index:100;opacity:0;transition:.3s;pointer-events:none;white-space:nowrap}.toast.show{opacity:1;transform:translate(-50%,0)}
.overlay{position:fixed;inset:0;background:#17111399;backdrop-filter:blur(5px);z-index:70;opacity:0;pointer-events:none;transition:.3s}.overlay.open{opacity:1;pointer-events:auto}
.cart{position:fixed;z-index:80;left:0;right:0;bottom:0;background:#faf7f3;border-radius:26px 26px 0 0;transform:translateY(105%);transition:.45s cubic-bezier(.2,.8,.2,1);max-height:82svh;overflow:auto;padding:20px 18px calc(25px + env(safe-area-inset-bottom));box-shadow:0 -20px 70px #0003}.cart.open{transform:none}
.handle{width:38px;height:4px;border-radius:10px;background:#d8cec7;margin:0 auto 18px}
.cartTitle{display:flex;justify-content:space-between;align-items:center;margin-bottom:15px}.cartTitle h2{font-family:"Playfair Display";font-weight:400;font-size:28px}.close{border:0;background:none;font-size:20px}
.cartItem{display:flex;gap:12px;padding:11px 0;border-bottom:1px solid #e7ded7}.mini{width:62px;height:62px;border-radius:12px;display:grid;place-items:center;overflow:hidden;background:#eee8e2}.mini img{width:100%;height:100%;object-fit:cover}
.ciInfo{flex:1}.ciName{font-family:"Playfair Display";font-size:14px}.ciPrice{font-size:9px;color:#8a7d80;margin-top:4px}.qty{display:flex;align-items:center;gap:8px;margin-top:8px}.qty button{width:22px;height:22px;border:1px solid #d9cec7;background:#fff;border-radius:50%;font-size:11px}
.total{display:flex;justify-content:space-between;padding:18px 0;font-size:12px}.checkout{width:100%;border:0;background:#292123;color:#fff;padding:15px;border-radius:12px;font-size:9px;letter-spacing:2px;text-transform:uppercase}
.empty{text-align:center;padding:30px;color:#96898c;font-size:11px}
.checkoutPanel{position:fixed;z-index:90;inset:0;background:#f7f3ee;transform:translateY(100%);transition:.6s;overflow:auto;padding:28px 20px}.checkoutPanel.open{transform:none}
.checkoutTop{display:flex;align-items:center;gap:12px;margin-bottom:35px}.back{border:1px solid #ddd2ca;background:#fff;width:38px;height:38px;border-radius:50%}.checkoutTop h2{font-family:"Playfair Display";font-weight:400;font-size:29px}
.field{background:#fff;border:1px solid #e5dcd5;border-radius:12px;padding:14px;margin-bottom:10px}.field label{display:block;font-size:8px;letter-spacing:1px;text-transform:uppercase;color:#938487;margin-bottom:5px}.field div{font-size:11px;color:#3c3335}
.note{margin:18px 0;background:#f0e3d9;border-radius:15px;padding:15px;font-size:10px;color:#745f62;line-height:1.7}
.place{width:100%;border:0;background:#ad7182;color:#fff;padding:16px;border-radius:12px;font-size:10px;letter-spacing:2px;text-transform:uppercase}
.success{position:fixed;inset:0;background:#181114;color:#fff;z-index:120;display:flex;align-items:center;justify-content:center;text-align:center;padding:30px;opacity:0;pointer-events:none;transition:.6s}.success.open{opacity:1;pointer-events:auto}
.successInner{max-width:340px}.check{width:80px;height:80px;border:1px solid #d5aa68;border-radius:50%;display:grid;place-items:center;margin:0 auto 28px;color:#e1b86e;font-size:27px}
.success h2{font-family:"Playfair Display";font-weight:400;font-size:48px;line-height:.9;margin-bottom:20px}.success p{font-size:12px;color:#b8aaaf;line-height:1.9}
.orderLine{margin:25px auto 0;width:220px;height:1px;background:#403237}.surprise{font-family:"Playfair Display";font-size:24px;color:#dfb46d;margin-top:23px}
.continue{margin-top:27px;border:1px solid #d9ac6870;background:transparent;color:#dfb46d;border-radius:100px;padding:12px 20px;font-size:9px;letter-spacing:2px}
@media(max-width:360px){.pic{height:180px}.hero h1{font-size:37px}}
</style>
</head>
<body>
<div class="app">
<nav class="nav">
  <div class="logo">Bangle <span>&</span> Co.</div>
  <div class="navRight">
    <button class="iconBtn">♡</button>
    <button class="iconBtn" id="cartBtn">🛍<i class="badge" id="badge">0</i></button>
  </div>
</nav>

<header class="hero">
  <small>Vanshika's private collection</small>
  <h1>Pick something<br>you'd actually wear.</h1>
  <p>Curated especially for someone who apparently has very good taste in bangles.</p>
</header>

<div class="tabs">
  <button class="tab active" data-filter="all">All pieces</button>
  <button class="tab" data-filter="gold">Gold</button>
  <button class="tab" data-filter="pink">Pink</button>
  <button class="tab" data-filter="silver">Silver</button>
  <button class="tab" data-filter="lavender">Lavender</button>
</div>

<main class="grid" id="grid"></main>
<div class="toast" id="toast"></div>
<div class="overlay" id="overlay"></div>

<aside class="cart" id="cart">
  <div class="handle"></div>
  <div class="cartTitle"><h2>Your picks</h2><button class="close" id="closeCart">×</button></div>
  <div id="cartItems"></div>
  <div class="total"><span>Little cart total</span><b id="total">₹0</b></div>
  <button class="checkout" id="checkout">Continue to checkout →</button>
</aside>

<section class="checkoutPanel" id="checkoutPanel">
  <div class="checkoutTop"><button class="back" id="back">←</button><h2>Almost ordered.</h2></div>
  <div class="field"><label>Delivery to</label><div>Vanshika</div></div>
  <div class="field"><label>Payment</label><div>Obviously not charging you.</div></div>
  <div class="field"><label>Delivery</label><div>When we meet in person.</div></div>
  <div class="note">Everything in your cart is a surprise order. The actual delivery address is currently classified as <b>“wherever we meet.”</b></div>
  <button class="place" id="place">Place the very real order</button>
</section>

<section class="success" id="success">
  <div class="successInner">
    <div class="check">✓</div>
    <div class="eyebrow">ORDER CONFIRMED · #VANSHIKA01</div>
    <h2>Your order is<br>officially placed.</h2>
    <p id="orderSummary"></p>
    <div class="orderLine"></div>
    <div class="surprise">Delivery: when we meet. ♡</div>
    <p style="margin-top:10px">No shipping fee.<br>No address required.<br>Just one future handover.</p>
    <button class="continue" id="done">Keep this little secret</button>
  </div>
</section>
</div>

<script>
const products=[
 {id:1,name:"Champagne Glow",cat:"gold",price:1299,desc:"Warm gold · intricate traditional detail",cls:"p1",img:"https://www.viranijewelers.com/cdn/shop/products/Virani11-27-2022_21.jpg?v=1671516721"},
 {id:2,name:"Rose Blush",cat:"pink",price:899,desc:"Pink kundan · gold detailing",cls:"p2",img:"https://img.tatacliq.com/images/i25/1348Wx2000H/MP000000027406913_1348Wx2000H_202507180159111.jpeg"},
 {id:3,name:"Moonlight",cat:"silver",price:1099,desc:"Silver · classic stone-studded stack",cls:"p3",img:"https://www.viranijewelers.com/cdn/shop/products/Virani11-27-2022_21.jpg?v=1671516721"},
 {id:4,name:"Lavender Dream",cat:"lavender",price:949,desc:"Soft pastel · pearl and gold finish",cls:"p4",img:"https://images.squarespace-cdn.com/content/v1/56015302e4b01fb31d19b1a8/1678742290068-J14YLXELN64C9E2LYV70/IMG_20220816_115206.jpg"},
 {id:5,name:"Sunset Glass",cat:"gold",price:1199,desc:"Pink & gold · sparkling glass set",cls:"p5",img:"https://www.shreeparshavnathcreations.com/uploads/category/colourful-glass-bangle-set.webp"},
 {id:6,name:"Royal Blue",cat:"silver",price:999,desc:"Blue silk · pearl & gold accents",cls:"p6",img:"https://choodiyan.com/cdn/shop/products/image_e2b598b4-2910-42c1-9f74-e9c96f52844c_5000x.jpg?v=1625667525"}
];
let cart=[];
const $=s=>document.querySelector(s);
function money(n){return "₹"+n.toLocaleString("en-IN")}
function renderProducts(filter="all"){
 $("#grid").innerHTML=products.filter(p=>filter==="all"||p.cat===filter).map(p=>`
 <article class="product">
  <div class="pic ${p.cls}">
   <button class="save">♡</button>
   <img src="${p.img}" alt="${p.name} bangle set" loading="lazy">
  </div>
  <div class="productInfo">
   <div class="name">${p.name}</div>
   <div class="desc">${p.desc}</div>
   <div class="row"><span class="price">${money(p.price)}</span><button class="add" data-id="${p.id}">Add to bag</button></div>
  </div>
 </article>`).join("");
 document.querySelectorAll(".add").forEach(b=>b.onclick=()=>add(+b.dataset.id));
 document.querySelectorAll(".save").forEach(b=>b.onclick=()=>{b.textContent=b.textContent==="♡"?"♥":"♡";toast(b.textContent==="♥"?"Saved for later":"Removed")});
}
function add(id){
 const p=products.find(x=>x.id===id),x=cart.find(x=>x.id===id);
 if(x)x.qty++;else cart.push({...p,qty:1});
 updateCart();toast(p.name+" added to your bag");if(navigator.vibrate)navigator.vibrate(12);
}
function updateCart(){
 const count=cart.reduce((a,b)=>a+b.qty,0);$("#badge").textContent=count;$("#badge").classList.toggle("show",count>0);
 $("#cartItems").innerHTML=cart.length?cart.map(p=>`
 <div class="cartItem">
  <div class="mini"><img src="${p.img}" alt="${p.name}"></div>
  <div class="ciInfo"><div class="ciName">${p.name}</div><div class="ciPrice">${money(p.price)}</div>
   <div class="qty"><button onclick="change(${p.id},-1)">−</button><span>${p.qty}</span><button onclick="change(${p.id},1)">+</button></div>
  </div>
 </div>`).join(""):`<div class="empty">Your bag is empty.<br>Go find something pretty.</div>`;
 const total=cart.reduce((a,b)=>a+b.price*b.qty,0);$("#total").textContent=money(total);
 $("#checkout").style.opacity=cart.length?1:.4;
}
window.change=(id,n)=>{const x=cart.find(p=>p.id===id);if(!x)return;x.qty+=n;if(x.qty<=0)cart=cart.filter(p=>p.id!==id);updateCart()};
function openCart(){$("#overlay").classList.add("open");$("#cart").classList.add("open")}
function closeCart(){$("#overlay").classList.remove("open");$("#cart").classList.remove("open")}
function toast(t){const x=$("#toast");x.textContent=t;x.classList.add("show");clearTimeout(window.tt);window.tt=setTimeout(()=>x.classList.remove("show"),1700)}
renderProducts();updateCart();
document.querySelectorAll(".tab").forEach(t=>t.onclick=()=>{document.querySelectorAll(".tab").forEach(x=>x.classList.remove("active"));t.classList.add("active");renderProducts(t.dataset.filter)});
$("#cartBtn").onclick=openCart;$("#closeCart").onclick=closeCart;$("#overlay").onclick=closeCart;
$("#checkout").onclick=()=>{if(!cart.length){toast("Add at least one bangle first");return}closeCart();$("#checkoutPanel").classList.add("open")};
$("#back").onclick=()=>$("#checkoutPanel").classList.remove("open");
$("#place").onclick=()=>{
 const names=cart.map(x=>x.name+(x.qty>1?" ×"+x.qty:"")).join(" · ");
 $("#orderSummary").innerHTML=`You picked <b>${names}</b>.<br><br>Your choices have been saved to the imaginary order system.`;
 $("#checkoutPanel").classList.remove("open");$("#success").classList.add("open");
 for(let i=0;i<35;i++){const p=document.createElement("i");p.style.position="fixed";p.style.left="50%";p.style.top="45%";p.style.width="4px";p.style.height="4px";p.style.borderRadius="50%";p.style.background=i%2?"#dfb46d":"#bd718c";p.style.zIndex=200;const a=Math.random()*Math.PI*2,d=50+Math.random()*220;p.animate([{transform:"translate(0,0)",opacity:1},{transform:`translate(${Math.cos(a)*d}px,${Math.sin(a)*d}px)`,opacity:0}],{duration:1000+Math.random()*700,easing:"ease-out"});document.body.appendChild(p);setTimeout(()=>p.remove(),1800)}
};
$("#done").onclick=()=>{$("#success").classList.remove("open");cart=[];updateCart();window.scrollTo({top:0,behavior:"smooth"});toast("Order saved. See you in person.")};
</script>
</body>
</html>
"""

components.html(HTML, height=900, scrolling=True)
