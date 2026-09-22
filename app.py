import streamlit as st
import time

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="For Vanshika",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');

/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 10% 5%,
            rgba(255, 105, 150, 0.20),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(226, 177, 80, 0.14),
            transparent 30%
        ),
        #100a12;

    color: white;
}

.block-container {
    max-width: 480px !important;
    padding: 25px 18px 45px !important;
}

header {
    background: transparent !important;
}

footer {
    visibility: hidden;
}

* {
    -webkit-tap-highlight-color: transparent;
}

/* ============================================================
   INTRO
   ============================================================ */

.hero {
    min-height: 70vh;

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    text-align: center;
}

.small {
    color: #d9b8c5;

    font-family: "DM Sans", sans-serif;

    font-size: 11px;

    letter-spacing: 3px;

    text-transform: uppercase;

    margin-bottom: 18px;
}

.hero h1 {
    font-family: "Cormorant Garamond", serif !important;

    font-size: 56px !important;

    line-height: .92 !important;

    font-weight: 500 !important;

    letter-spacing: -2px;

    margin: 0;
}

.hero p {
    max-width: 340px;

    color: #d9cbd2;

    font-family: "DM Sans", sans-serif;

    font-size: 14px;

    line-height: 1.85;

    margin: 28px 0 32px;
}

.sparkle {
    color: #e5adbf;

    font-size: 18px;

    margin-left: 5px;
}

/* ============================================================
   BUTTON
   ============================================================ */

div.stButton > button {

    width: 100%;

    min-height: 55px;

    border-radius: 18px !important;

    border: 1px solid rgba(255,255,255,.16);

    background:
        linear-gradient(
            135deg,
            #e99aae,
            #aa5f7b
        );

    color: white;

    font-family: "DM Sans", sans-serif;

    font-size: 15px;

    font-weight: 600;

    box-shadow:
        0 15px 45px rgba(190,80,120,.25);

    transition: all .2s ease;
}

div.stButton > button:hover {

    border-color:
        rgba(255,255,255,.30);

    color: white;

    transform:
        translateY(-1px);
}

div.stButton > button:active {

    transform:
        scale(.97);
}

/* ============================================================
   HEART DECORATION
   ============================================================ */

.heart {
    margin-top: 25px;

    text-align: center;
}

.heart span::before {

    content: "♥";

    color: #e7a8bc;

    font-size: 25px;

    animation:
        heartbeat 2s ease-in-out infinite;
}

@keyframes heartbeat {

    0%,100% {
        transform: scale(1);
    }

    50% {
        transform: scale(1.15);
    }
}

/* ============================================================
   BANGLE PAGE
   ============================================================ */

.title {

    text-align: center;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 31px;

    margin-bottom: 3px;
}

.counter {

    text-align: center;

    color: #cdbbc4;

    font-family:
        "DM Sans",
        sans-serif;

    font-size: 12px;

    margin-bottom: 8px;
}

.instruction {

    text-align: center;

    color: #d9cbd1;

    font-family:
        "DM Sans",
        sans-serif;

    font-size: 14px;

    line-height: 1.7;
}

/* ============================================================
   WRIST
   ============================================================ */

.wrist-box {

    width: 100%;

    height: 400px;

    position: relative;

    display: flex;

    justify-content: center;

    align-items: center;
}

.wrist {

    position: absolute;

    width: 105px;

    height: 295px;

    border-radius: 55px;

    background:
        linear-gradient(
            90deg,
            #92503c,
            #cf8466 25%,
            #efb08b 50%,
            #c47558 75%,
            #884837
        );

    box-shadow:

        inset 0 0 22px
        rgba(50,15,8,.30),

        0 25px 60px
        rgba(0,0,0,.42);
}

.wrist::after {

    content: "";

    position: absolute;

    inset: 0;

    border-radius: inherit;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,.12),
            transparent
        );
}

/* ============================================================
   BANGLES
   ============================================================ */

.bangle {

    position: absolute;

    width: 158px;

    height: 36px;

    border-radius: 50%;

    opacity: 0;

    transform:
        translateY(-150px)
        scale(.65);

    transition:
        opacity .25s ease,

        transform
        .75s
        cubic-bezier(.18,.89,.32,1.28);
}

.bangle.show {

    opacity: 1;

    transform:
        translateY(0)
        scale(1);
}

/* GOLD */

.b1 {

    top: 78px;

    border:
        8px solid #e4b34f;

    box-shadow:

        0 0 0 2px #74480f,

        inset 0 0 6px
        #fff1a8,

        0 0 18px
        rgba(228,179,79,.45);
}

/* PINK */

.b2 {

    top: 121px;

    border:
        8px solid #c95f84;

    box-shadow:

        0 0 0 2px #68283f,

        inset 0 0 6px
        #ffd5e2,

        0 0 18px
        rgba(201,95,132,.45);
}

/* GOLD */

.b3 {

    top: 164px;

    border:
        7px solid #e7b650;

    box-shadow:

        0 0 0 2px #71470e,

        inset 0 0 6px
        #fff4b6,

        0 0 18px
        rgba(231,182,80,.45);
}

/* DARK PINK */

.b4 {

    top: 207px;

    border:
        8px solid #a9436d;

    box-shadow:

        0 0 0 2px #5c1938,

        inset 0 0 6px
        #ffd1df,

        0 0 18px
        rgba(169,67,109,.45);
}

/* GOLD */

.b5 {

    top: 250px;

    border:
        7px solid #d6a043;

    box-shadow:

        0 0 0 2px #70410c,

        inset 0 0 6px
        #fff0a9,

        0 0 18px
        rgba(214,160,67,.45);
}

/* ============================================================
   FINAL PAGE
   ============================================================ */

.final {

    min-height: 78vh;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    text-align: center;
}

.final-ring {

    width: 108px;

    height: 108px;

    border-radius: 50%;

    border:
        11px solid #d9aa4f;

    margin-bottom: 35px;

    box-shadow:

        0 0 0 3px #754a12,

        0 0 55px
        rgba(220,170,75,.42);

    animation:
        pulse 2.2s ease-in-out infinite;
}

@keyframes pulse {

    0%,100% {

        transform:
            scale(1);
    }

    50% {

        transform:
            scale(1.06);
    }
}

.final h1 {

    font-family:
        "Cormorant Garamond",
        serif !important;

    font-size:
        49px !important;

    line-height:
        1 !important;

    font-weight:
        500 !important;

    letter-spacing:
        -1px;

    margin:
        0 0 25px;
}

.final p {

    max-width: 340px;

    color: #d8cbd1;

    font-family:
        "DM Sans",
        sans-serif;

    font-size: 14px;

    line-height: 1.9;

    margin:
        8px auto;
}

.signature {

    margin-top: 28px;

    color: #e3a8ba;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 25px;
}

/* ============================================================
   FINAL HEART
   ============================================================ */

.final-heart {

    margin-top: 20px;

    color: #e7a8bc;

    font-size: 24px;
}

.final-heart::before {

    content: "♥";

    animation:
        heartbeat 2s ease-in-out infinite;
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 500px) {

    .hero {

        min-height:
            70vh;
    }

    .hero h1 {

        font-size:
            51px !important;
    }

    .wrist-box {

        height:
            370px;
    }
}

@media (max-height: 680px) {

    .hero {

        min-height:
            65vh;
    }

    .wrist-box {

        height:
            330px;
    }

    .wrist {

        height:
            260px;
    }

    .bangle {

        transform:
            translateY(-130px)
            scale(.85);
    }

    .bangle.show {

        transform:
            translateY(0)
            scale(.85);
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state.page = "intro"

if "count" not in st.session_state:
    st.session_state.count = 0


# ============================================================
# INTRO
# ============================================================

if st.session_state.page == "intro":

    st.markdown("""
    <div class="hero">

        <div class="small">
            a little surprise for Vanshika
        </div>

        <h1>
            For Vanshika,<br>
            the girl who loves bangles.
        </h1>

        <p>
            I couldn't be there to put bangles
            on your wrist myself...

            <br><br>

            So I made you a little something instead.
            <span class="sparkle">✦</span>
        </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Open your surprise",
        use_container_width=True
    ):

        st.session_state.page = "bangles"

        st.rerun()

    st.markdown("""
    <div class="heart">
        <span></span>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# BANGLES
# ============================================================

elif st.session_state.page == "bangles":

    st.markdown("""
    <div class="title">
        For You, Vanshika
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="counter">
            {st.session_state.count} / 5
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="instruction">
        Tap below and let me put these on your wrist...
    </div>
    """, unsafe_allow_html=True)

    # ----------------------------------------
    # Bangles
    # ----------------------------------------

    bangle_classes = [
        "b1",
        "b2",
        "b3",
        "b4",
        "b5"
    ]

    bangles = ""

    for index, class_name in enumerate(bangle_classes):

        if index < st.session_state.count:

            visible = "show"

        else:

            visible = ""

        bangles += f"""
        <div class="bangle {class_name} {visible}"></div>
        """

    # ----------------------------------------
    # Wrist
    # ----------------------------------------

    st.markdown(
        f"""
        <div class="wrist-box">

            <div class="wrist"></div>

            {bangles}

        </div>
        """,
        unsafe_allow_html=True
    )

    # ----------------------------------------
    # Button
    # ----------------------------------------

    button_text = [

        "Add the first one",

        "One more...",

        "It's getting prettier",

        "Almost there",

        "One last one..."

    ]

    current = st.session_state.count

    if current < 5:

        if st.button(
            button_text[current],
            use_container_width=True
        ):

            st.session_state.count += 1

            st.rerun()

    else:

        if st.button(
            "See what I wanted to tell you",
            use_container_width=True
        ):

            time.sleep(.5)

            st.session_state.page = "final"

            st.rerun()


# ============================================================
# FINAL
# ============================================================

elif st.session_state.page == "final":

    st.markdown("""
    <div class="final">

        <div class="final-ring"></div>

        <h1>
            Vanshika,<br>
            if distance had a sound...
        </h1>

        <p>
            I think it would sound like bangles
            softly going <i>chhan chhan</i>
            on your wrist.
        </p>

        <p>
            Until I can give you the real ones,
            let these be a tiny reminder
            that someone somewhere is thinking
            about you.
        </p>

        <div class="signature">
            — for Vanshika, with a little extra care
        </div>

        <div class="final-heart"></div>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "Replay the surprise",
        use_container_width=True
    ):

        st.session_state.page = "intro"

        st.session_state.count = 0

        st.rerun()
