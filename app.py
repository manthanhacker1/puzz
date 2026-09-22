import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="For Vanshika",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width,
    initial-scale=1.0,
    maximum-scale=1.0,
    user-scalable=no"
>

<title>For Vanshika</title>

<style>

@import url(
'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600&family=DM+Sans:wght@300;400;500&display=swap'
);

* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html,
body {

    margin: 0;
    padding: 0;

    width: 100%;
    height: 100%;

    background: #090808;

    overflow: hidden;
}

body {

    font-family:
        "DM Sans",
        sans-serif;

    color: #f7f1e9;
}

#app {

    position: relative;

    width: 100%;
    height: 100svh;

    overflow: hidden;

    background:
        radial-gradient(
            circle at 50% 35%,
            rgba(132, 82, 48, .14),
            transparent 35%
        ),
        #090808;
}

/* =========================================================
   GRAIN
   ========================================================= */

.grain {

    position: absolute;

    inset: -50%;

    width: 200%;
    height: 200%;

    pointer-events: none;

    opacity: .055;

    background-image:
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");

    animation:
        grain .35s steps(2) infinite;
}

@keyframes grain {

    0% {
        transform: translate(0,0);
    }

    25% {
        transform: translate(-2%,-1%);
    }

    50% {
        transform: translate(1%,2%);
    }

    75% {
        transform: translate(2%,-2%);
    }

    100% {
        transform: translate(-1%,1%);
    }
}

/* =========================================================
   SCREENS
   ========================================================= */

.screen {

    position: absolute;

    inset: 0;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    padding:
        30px
        24px
        calc(30px + env(safe-area-inset-bottom));

    opacity: 0;

    pointer-events: none;

    transform:
        translateY(18px);

    transition:
        opacity 1s ease,
        transform 1s cubic-bezier(.2,.8,.2,1);
}

.screen.active {

    opacity: 1;

    pointer-events: auto;

    transform:
        translateY(0);
}

/* =========================================================
   TOP LABEL
   ========================================================= */

.label {

    position: absolute;

    top:
        calc(24px + env(safe-area-inset-top));

    left: 0;
    right: 0;

    text-align: center;

    color: #8f8883;

    font-size: 9px;

    letter-spacing: 4px;

    text-transform: uppercase;
}

/* =========================================================
   OPENING
   ========================================================= */

.opening {

    text-align: center;
}

.opening .micro {

    color: #8f8883;

    font-size: 10px;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 24px;
}

.opening h1 {

    margin: 0;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(68px, 20vw, 105px);

    line-height: .76;

    font-weight: 300;

    letter-spacing: -4px;

    color: #eee6db;
}

.opening .line {

    width: 45px;

    height: 1px;

    background: #a98a62;

    margin:
        32px auto 25px;
}

.opening p {

    margin: 0 auto 35px;

    max-width: 290px;

    color: #9f9791;

    font-size: 13px;

    line-height: 1.8;
}

.open {

    background: none;

    border: 1px solid rgba(221,190,145,.38);

    color: #d8c3a3;

    padding:
        14px 28px;

    border-radius: 999px;

    font-size: 10px;

    letter-spacing: 2px;

    text-transform: uppercase;

    cursor: pointer;

    transition: .4s ease;
}

.open:hover {

    background:
        rgba(218,184,133,.08);

    border-color:
        rgba(221,190,145,.7);
}

/* =========================================================
   LETTER
   ========================================================= */

.letter {

    width:
        min(350px, 88vw);

    height:
        min(520px, 72vh);

    background:

        linear-gradient(
            145deg,
            #eee4d5,
            #dfd0bc
        );

    color: #29221d;

    position: relative;

    padding:
        45px 32px;

    box-shadow:

        0 35px 90px
        rgba(0,0,0,.55),

        0 0 0 1px
        rgba(255,255,255,.08);

    transform:
        rotate(-1deg);

    display: flex;

    flex-direction: column;

    justify-content: space-between;
}

.letter:before {

    content: "";

    position: absolute;

    inset: 10px;

    border:
        1px solid
        rgba(86,66,43,.20);

    pointer-events: none;
}

.letterTop {

    font-size: 9px;

    letter-spacing: 3px;

    text-transform: uppercase;

    color: #87745d;
}

.letter h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-weight: 400;

    font-size: 48px;

    line-height: .9;

    margin:
        55px 0 25px;
}

.letter p {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 21px;

    line-height: 1.35;

    color: #43382f;
}

.letterBottom {

    font-size: 10px;

    letter-spacing: 2px;

    color: #89755e;
}

.next {

    margin-top: 22px;

    background: none;

    border: none;

    color: #b89a6b;

    font-size: 10px;

    letter-spacing: 2px;

    text-transform: uppercase;

    cursor: pointer;
}

/* =========================================================
   JEWELRY EDITORIAL
   ========================================================= */

.editorial {

    width: 100%;

    max-width: 430px;

    height: 100%;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;
}

.editorial .tiny {

    color: #887e78;

    font-size: 9px;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 15px;
}

.editorial h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-weight: 300;

    font-size: 48px;

    line-height: .9;

    margin:
        0 0 28px;

    letter-spacing: -1px;
}

/* =========================================================
   ABSTRACT JEWELRY DISPLAY
   ========================================================= */

.jewelry {

    width:
        min(300px, 82vw);

    height:
        300px;

    position: relative;

    margin-bottom: 22px;
}

/* large shadow */

.jewelryShadow {

    position: absolute;

    left: 50%;

    bottom: 25px;

    width: 220px;

    height: 35px;

    transform:
        translateX(-50%);

    border-radius: 50%;

    background:
        rgba(0,0,0,.6);

    filter:
        blur(20px);
}

/* main bangle */

.bangle {

    position: absolute;

    left: 50%;

    top: 50%;

    width: 235px;

    height: 235px;

    transform:
        translate(-50%,-50%)
        rotateX(64deg)
        rotateZ(-13deg);

    border-radius: 50%;

    border:
        15px solid #b88332;

    background: transparent;

    box-shadow:

        inset 0 5px 4px
        rgba(255,244,189,.95),

        inset 0 -9px 10px
        rgba(76,40,7,.8),

        0 8px 12px
        rgba(0,0,0,.5),

        0 0 40px
        rgba(202,151,60,.14);
}

/* highlight */

.bangle:before {

    content: "";

    position: absolute;

    width: 110px;

    height: 5px;

    top: 4px;

    left: 40px;

    border-radius: 50%;

    background:
        rgba(255,247,208,.75);

    filter:
        blur(2px);

    transform:
        rotate(-8deg);
}

/* inner decorative ring */

.bangle2 {

    position: absolute;

    left: 50%;

    top: 50%;

    width: 180px;

    height: 180px;

    transform:
        translate(-50%,-50%)
        rotateX(64deg)
        rotateZ(-13deg);

    border-radius: 50%;

    border:
        4px solid #f0c96c;

    opacity: .9;

    box-shadow:
        0 0 9px
        rgba(246,211,123,.5);
}

/* stones */

.stones {

    position: absolute;

    left: 50%;

    top: 50%;

    width: 235px;

    height: 235px;

    transform:
        translate(-50%,-50%)
        rotateX(64deg)
        rotateZ(-13deg);
}

.stone {

    position: absolute;

    width: 12px;

    height: 12px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 30% 25%,
            #fff,
            #f7dca0 25%,
            #bc8330 70%
        );

    box-shadow:
        0 0 8px
        rgba(255,223,150,.8);
}

.s1 {
    top: 14px;
    left: 50%;
}

.s2 {
    top: 50%;
    right: 5px;
}

.s3 {
    bottom: 15px;
    left: 50%;
}

.s4 {
    top: 50%;
    left: 5px;
}

/* caption */

.caption {

    color: #918983;

    font-size: 12px;

    line-height: 1.7;

    max-width: 285px;

    margin-bottom: 25px;
}

.caption strong {

    color: #d4b783;

    font-weight: 400;
}

/* =========================================================
   MESSAGE
   ========================================================= */

.message {

    text-align: center;

    max-width: 340px;
}

.message .quote {

    color: #8e827a;

    font-size: 9px;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 25px;
}

.message h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(44px, 13vw, 65px);

    line-height: .92;

    font-weight: 300;

    letter-spacing: -2px;

    margin: 0 0 30px;
}

.message p {

    color: #aaa19b;

    font-size: 13px;

    line-height: 1.9;

    margin: 8px auto;

    max-width: 300px;
}

/* =========================================================
   FINAL
   ========================================================= */

.final {

    text-align: center;
}

.final .name {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(65px, 20vw, 100px);

    font-weight: 300;

    letter-spacing: -4px;

    line-height: .8;

    margin-bottom: 35px;
}

.final .rule {

    width: 38px;

    height: 1px;

    background: #a78961;

    margin:
        0 auto 28px;
}

.final p {

    color: #9f9690;

    font-size: 13px;

    line-height: 1.9;

    max-width: 300px;

    margin: auto;
}

.final .signature {

    margin-top: 35px;

    color: #c6a879;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 24px;
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    position: absolute;

    bottom:
        calc(17px + env(safe-area-inset-bottom));

    left: 0;
    right: 0;

    text-align: center;

    color: #514b48;

    font-size: 8px;

    letter-spacing: 2px;

    text-transform: uppercase;
}

/* =========================================================
   RESPONSIVE
   ========================================================= */

@media(max-height:680px){

    .letter{
        height:470px;
    }

    .jewelry{
        height:250px;
    }

    .bangle{
        width:200px;
        height:200px;
    }

    .bangle2{
        width:155px;
        height:155px;
    }

    .stones{
        width:200px;
        height:200px;
    }

}

</style>
</head>

<body>

<div id="app">

<div class="grain"></div>

<!-- =====================================================
     SCREEN 1
====================================================== -->

<section id="s1" class="screen active">

    <div class="label">
        PRIVATE · FOR VANSHIKA
    </div>

    <div class="opening">

        <div class="micro">
            I made something for you
        </div>

        <h1>
            Vanshika
        </h1>

        <div class="line"></div>

        <p>
            It's small.<br>
            It's a little unnecessary.<br>
            And I hope you like it.
        </p>

        <button class="open" onclick="go('s2')">
            Open
        </button>

    </div>

    <div class="footer">
        made somewhere far away
    </div>

</section>


<!-- =====================================================
     SCREEN 2 — LETTER
====================================================== -->

<section id="s2" class="screen">

    <div class="label">
        A NOTE
    </div>

    <div class="letter">

        <div class="letterTop">
            For Vanshika
        </div>

        <div>

            <h2>
                Some things<br>
                don't need<br>
                a reason.
            </h2>

            <p>
                I remembered that
                you like bangles.

                <br><br>

                And somehow that tiny
                detail stayed in my head.
            </p>

        </div>

        <div class="letterBottom">
            KEEP READING
        </div>

    </div>

    <button class="next" onclick="go('s3')">
        Turn the page →
    </button>

</section>


<!-- =====================================================
     SCREEN 3 — JEWEL
====================================================== -->

<section id="s3" class="screen">

    <div class="label">
        ONE LITTLE THING
    </div>

    <div class="editorial">

        <div class="tiny">
            I remembered
        </div>

        <h2>
            The bangles.
        </h2>

        <div class="jewelry">

            <div class="jewelryShadow"></div>

            <div class="bangle"></div>

            <div class="bangle2"></div>

            <div class="stones">

                <div class="stone s1"></div>
                <div class="stone s2"></div>
                <div class="stone s3"></div>
                <div class="stone s4"></div>

            </div>

        </div>

        <div class="caption">

            <strong>
                Not the real ones.
            </strong>

            <br>

            Just a little reminder that
            I was thinking about you.

        </div>

        <button class="open" onclick="go('s4')">
            There's more
        </button>

    </div>

</section>


<!-- =====================================================
     SCREEN 4 — MESSAGE
====================================================== -->

<section id="s4" class="screen">

    <div class="label">
        HONESTLY
    </div>

    <div class="message">

        <div class="quote">
            one thing I wanted to say
        </div>

        <h2>
            Distance<br>
            is annoying.
        </h2>

        <p>
            Because sometimes you just want
            to give someone something
            instead of sending another text.
        </p>

        <p>
            So this is my slightly
            ridiculous way of doing that.
        </p>

        <br>

        <button class="open" onclick="go('s5')">
            One last thing
        </button>

    </div>

</section>


<!-- =====================================================
     SCREEN 5 — FINAL
====================================================== -->

<section id="s5" class="screen">

    <div class="label">
        FOR YOU
    </div>

    <div class="final">

        <div class="name">
            Vanshika
        </div>

        <div class="rule"></div>

        <p>
            One day, these won't be
            on a screen.
        </p>

        <p>
            Until then,
            I hope this made you smile.
        </p>

        <div class="signature">
            — from me, to you.
        </div>

        <div style="
            margin-top:32px;
            color:#b9965d;
            font-size:14px;
            letter-spacing:8px;
        ">
            · · ·
        </div>

    </div>

</section>


<script>

/* =========================================================
   NAVIGATION
========================================================= */

function go(id){

    const current =
        document.querySelector(".screen.active");

    const next =
        document.getElementById(id);

    if(!next) return;

    if(current){
        current.classList.remove("active");
    }

    setTimeout(() => {

        next.classList.add("active");

    }, 120);
}


/* =========================================================
   SUBTLE PARALLAX ON JEWEL
========================================================= */

const jewel =
    document.querySelector(".jewelry");

document.addEventListener(
    "touchmove",
    function(e){

        if(!jewel) return;

        const touch =
            e.touches[0];

        const x =
            (touch.clientX /
            window.innerWidth - .5);

        const y =
            (touch.clientY /
            window.innerHeight - .5);

        jewel.style.transform =
            `translate(${x*8}px,${y*6}px)`;

    },
    {passive:true}
);


/* =========================================================
   DESKTOP MOUSE PARALLAX
========================================================= */

document.addEventListener(
    "mousemove",
    function(e){

        if(!jewel) return;

        const x =
            (e.clientX /
            window.innerWidth - .5);

        const y =
            (e.clientY /
            window.innerHeight - .5);

        jewel.style.transform =
            `translate(${x*8}px,${y*6}px)`;
    }
);

</script>

</div>

</body>
</html>
"""

components.html(
    HTML,
    height=900,
    scrolling=False
)
