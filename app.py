from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

<title>For You ✨</title>

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');

* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html, body {
    margin: 0;
    width: 100%;
    min-height: 100%;
    overflow-x: hidden;
}

body {
    background:
        radial-gradient(circle at 20% 10%, rgba(255, 182, 193, .18), transparent 30%),
        radial-gradient(circle at 80% 80%, rgba(255, 215, 150, .13), transparent 30%),
        #100b13;
    color: #fff;
    font-family: "DM Sans", sans-serif;
}

.page {
    min-height: 100svh;
    display: flex;
    justify-content: center;
    position: relative;
    overflow: hidden;
}

.glow {
    position: fixed;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    filter: blur(80px);
    opacity: .18;
    pointer-events: none;
}

.glow.one {
    background: #ff5f91;
    top: -100px;
    left: -100px;
}

.glow.two {
    background: #d8a04a;
    bottom: -100px;
    right: -100px;
}

.container {
    width: min(100%, 480px);
    min-height: 100svh;
    padding: 28px 20px 40px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    z-index: 2;
}

/* ---------- INTRO ---------- */

#intro {
    width: 100%;
    min-height: calc(100svh - 68px);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.small {
    color: #d9bfc9;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 16px;
}

h1 {
    font-family: "Cormorant Garamond", serif;
    font-size: clamp(48px, 15vw, 76px);
    line-height: .9;
    font-weight: 500;
    margin: 0;
    letter-spacing: -2px;
}

.subtitle {
    max-width: 330px;
    color: #d8ccd2;
    font-size: 15px;
    line-height: 1.7;
    margin: 22px 0 34px;
}

.start-btn {
    border: 1px solid rgba(255,255,255,.2);
    background: linear-gradient(135deg, #e99aaf, #b76b84);
    color: white;
    padding: 16px 27px;
    border-radius: 100px;
    font-size: 15px;
    font-weight: 600;
    box-shadow: 0 15px 45px rgba(201, 96, 129, .3);
    cursor: pointer;
    transition: .25s;
}

.start-btn:active {
    transform: scale(.95);
}

.heart {
    margin-top: 28px;
    font-size: 25px;
    animation: float 2.5s ease-in-out infinite;
}

@keyframes float {
    50% { transform: translateY(-8px); }
}

/* ---------- EXPERIENCE ---------- */

#experience {
    display: none;
    width: 100%;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.top {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.brand {
    font-family: "Cormorant Garamond", serif;
    font-size: 25px;
}

.counter {
    font-size: 12px;
    color: #c8b8c0;
}

.instruction {
    color: #d9cbd1;
    font-size: 14px;
    line-height: 1.6;
    max-width: 310px;
}

/* ---------- WRIST ---------- */

.wrist-area {
    width: 100%;
    height: 390px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 10px 0 12px;
}

.wrist {
    width: 105px;
    height: 300px;
    border-radius: 55px;
    background:
        linear-gradient(
            90deg,
            #9d5c43,
            #d89472 25%,
            #f0b28d 50%,
            #c7795c 75%,
            #92533f
        );
    box-shadow:
        inset 0 0 20px rgba(70,25,15,.25),
        0 20px 50px rgba(0,0,0,.35);
    position: relative;
    transform: rotate(2deg);
}

.wrist::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(255,255,255,.15),
        transparent
    );
}

.bangles {
    position: absolute;
    width: 155px;
    height: 330px;
    pointer-events: none;
}

.bangle {
    position: absolute;
    width: 155px;
    height: 34px;
    border-radius: 50%;
    left: 0;
    opacity: 0;
    transform: translateY(-160px) rotate(2deg) scale(.7);
    transition:
        transform .75s cubic-bezier(.18,.89,.32,1.28),
        opacity .35s;
}

.bangle.show {
    opacity: 1;
    transform: translateY(0) rotate(2deg) scale(1);
}

.bangle:nth-child(1) {
    top: 58px;
    border: 8px solid #e7b85a;
    box-shadow:
        0 0 0 2px #7b4b13,
        inset 0 0 5px #fff4bc,
        0 0 15px rgba(231,184,90,.35);
}

.bangle:nth-child(2) {
    top: 101px;
    border: 8px solid #cf7190;
    box-shadow:
        0 0 0 2px #7b304b,
        inset 0 0 5px #ffd7e4,
        0 0 15px rgba(207,113,144,.35);
}

.bangle:nth-child(3) {
    top: 144px;
    border: 7px solid #e6b955;
    box-shadow:
        0 0 0 2px #71480e,
        inset 0 0 5px #fff6c7,
        0 0 15px rgba(230,185,85,.35);
}

.bangle:nth-child(4) {
    top: 187px;
    border: 8px solid #a9466d;
    box-shadow:
        0 0 0 2px #5f1839,
        inset 0 0 5px #ffd1e0,
        0 0 15px rgba(169,70,109,.35);
}

.bangle:nth-child(5) {
    top: 230px;
    border: 7px solid #d8a447;
    box-shadow:
        0 0 0 2px #70420c,
        inset 0 0 5px #fff0ae,
        0 0 15px rgba(216,164,71,.35);
}

.tap-btn {
    width: 100%;
    max-width: 320px;
    padding: 17px;
    border: 1px solid rgba(255,255,255,.16);
    border-radius: 18px;
    background: rgba(255,255,255,.075);
    backdrop-filter: blur(15px);
    color: white;
    font-size: 15px;
    font-weight: 600;
    cursor: pointer;
}

.tap-btn:active {
    transform: scale(.97);
}

/* ---------- FINAL ---------- */

#final {
    display: none;
    width: 100%;
    min-height: 85svh;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
}

.final-ring {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 12px solid #d9aa4f;
    box-shadow:
        0 0 0 3px #7b4b13,
        0 0 50px rgba(218,169,78,.35);
    margin-bottom: 35px;
    animation: pulse 2.2s infinite;
}

@keyframes pulse {
    50% {
        transform: scale(1.05);
        box-shadow:
            0 0 0 3px #7b4b13,
            0 0 70px rgba(218,169,78,.55);
    }
}

.final-title {
    font-family: "Cormorant Garamond", serif;
    font-size: 49px;
    line-height: 1;
    margin-bottom: 20px;
}

.final-text {
    color: #d9ccd2;
    line-height: 1.8;
    font-size: 15px;
    max-width: 330px;
}

.signature {
    margin-top: 28px;
    color: #e7b3c3;
    font-family: "Cormorant Garamond", serif;
    font-size: 24px;
}

/* ---------- PARTICLES ---------- */

.particle {
    position: fixed;
    pointer-events: none;
    z-index: 5;
    animation: particle 1.2s forwards ease-out;
}

@keyframes particle {
    0% {
        opacity: 1;
        transform: translate(0,0) scale(1);
    }
    100% {
        opacity: 0;
        transform: translate(
            var(--x),
            var(--y)
        ) scale(.2) rotate(180deg);
    }
}

@media (max-height: 680px) {
    .wrist-area {
        height: 330px;
    }

    .wrist {
        height: 260px;
    }

    .bangles {
        transform: scale(.85);
    }
}
</style>
</head>

<body>

<div class="page">

    <div class="glow one"></div>
    <div class="glow two"></div>

    <main class="container">

        <!-- INTRO -->
        <section id="intro">

            <div class="small">a tiny surprise</div>

            <h1>For the girl<br>who loves bangles.</h1>

            <p class="subtitle">
                Distance made one thing difficult...
                giving you something in person.
                So I made you something instead.
            </p>

            <button class="start-btn" onclick="startExperience()">
                Open your surprise ✨
            </button>

            <div class="heart">♡</div>

        </section>


        <!-- EXPERIENCE -->
        <section id="experience">

            <div class="top">
                <div class="brand">For You ♡</div>
                <div class="counter">
                    <span id="count">0</span> / 5
                </div>
            </div>

            <p class="instruction">
                Tap below and let me put these on your wrist...
            </p>

            <div class="wrist-area">

                <div class="wrist"></div>

                <div class="bangles">
                    <div class="bangle"></div>
                    <div class="bangle"></div>
                    <div class="bangle"></div>
                    <div class="bangle"></div>
                    <div class="bangle"></div>
                </div>

            </div>

            <button class="tap-btn" id="tapButton" onclick="addBangle()">
                Add the first one ✨
            </button>

        </section>


        <!-- FINAL -->
        <section id="final">

            <div class="final-ring"></div>

            <div class="final-title">
                If distance<br>had a sound...
            </div>

            <p class="final-text">
                I think it would sound like bangles
                softly going <i>chhan chhan</i> on your wrist.

                <br><br>

                Until I can give you the real ones,
                consider these a little reminder that
                someone somewhere is thinking about you. ♡
            </p>

            <div class="signature">
                — from someone who likes you a little too much ✨
            </div>

        </section>

    </main>
</div>


<script>

let current = 0;

const messages = [
    "Add the first one ✨",
    "One more... 🌸",
    "It's getting prettier ✨",
    "Almost there ♡",
    "One last one...",
    "Your little surprise is ready ♡"
];

function startExperience() {

    document.getElementById("intro").style.display = "none";
    document.getElementById("experience").style.display = "flex";

    if (navigator.vibrate) {
        navigator.vibrate(30);
    }
}

function addBangle() {

    if (current >= 5) return;

    current++;

    const bangle =
        document.querySelectorAll(".bangle")[current - 1];

    bangle.classList.add("show");

    document.getElementById("count").innerText = current;

    document.getElementById("tapButton").innerText =
        messages[current];

    createParticles();

    if (navigator.vibrate) {
        navigator.vibrate([20, 30, 20]);
    }

    if (current === 5) {

        setTimeout(() => {

            document.getElementById("experience").style.display = "none";
            document.getElementById("final").style.display = "flex";

            createParticles(35);

        }, 1100);
    }
}

function createParticles(amount = 10) {

    const symbols = ["✦", "✧", "♡", "·", "✶"];

    for (let i = 0; i < amount; i++) {

        const p = document.createElement("div");

        p.className = "particle";

        p.innerText =
            symbols[Math.floor(Math.random() * symbols.length)];

        p.style.left =
            (35 + Math.random() * 30) + "%";

        p.style.top =
            (45 + Math.random() * 15) + "%";

        p.style.fontSize =
            (10 + Math.random() * 14) + "px";

        p.style.setProperty(
            "--x",
            ((Math.random() - .5) * 220) + "px"
        );

        p.style.setProperty(
            "--y",
            (-80 - Math.random() * 180) + "px"
        );

        document.body.appendChild(p);

        setTimeout(() => p.remove(), 1400);
    }
}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
