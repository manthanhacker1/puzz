import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import random
from PIL import Image, ImageDraw
import io

# Set page config
st.set_page_config(
    page_title="💍 Special Surprise for Vanshika",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
    }
    
    body {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .title-box {
        text-align: center;
        padding: 40px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .card-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .bangle-item {
        background: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s;
    }
    
    .bangle-item:hover {
        transform: scale(1.05);
    }
    
    .message-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
    }
    
    .stats-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    
    h1, h2, h3 {
        color: #333;
    }
    
    .special-text {
        color: #f5576c;
        font-weight: bold;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'revealed' not in st.session_state:
    st.session_state.revealed = False
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0

# Title Section
st.markdown("""
<div class="title-box">
    <h1 style="color: white; font-size: 48px; margin-bottom: 10px;">💍 Vanshika 💍</h1>
    <p style="color: #f0f0f0; font-size: 18px;">Something Special Created Just For You</p>
</div>
""", unsafe_allow_html=True)

# Main Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🎯 Welcome", "💎 Bangle Gallery", "🎮 Quiz", "💌 Special Message", "✨ Surprise"])

# TAB 1: Welcome
with tab1:
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="card-box">
            <h2>Welcome, Vanshika! 👋</h2>
            <p style="font-size: 16px; color: #555;">
            Hey Vanshika! I created this special virtual experience just for you. 
            I know you absolutely love beautiful things, especially bangles, so I've curated 
            something magical here just for you. Take your time exploring all the tabs - 
            there's something special waiting at the end! 💫
            </p>
            <br>
            <p style="font-size: 14px; color: #888;">
            👉 Start by checking out the Bangle Gallery, then play the Quiz, 
            read the Special Message, and finally discover the Surprise!
            </p>
            <br>
            <p style="font-size: 15px; color: #f5576c; font-weight: bold;">
            This is my way of saying: You mean everything to me, Vanshika. 💕
            </p>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: Bangle Gallery
with tab2:
    st.markdown("<h2 style='text-align: center; color: white;'>✨ Vanshika's Exclusive Bangle Collection ✨</h2>", unsafe_allow_html=True)
    
    bangles = [
        {"name": "Golden Dream", "type": "Gold", "price": "Priceless", "emoji": "👑", "desc": "Classic elegance - just like your grace"},
        {"name": "Emerald Beauty", "type": "Green", "price": "Precious", "emoji": "💚", "desc": "Deep green like the spark in your eyes"},
        {"name": "Rose Quartz", "type": "Pink", "price": "Magical", "emoji": "💕", "desc": "Soft and delicate, just like your heart"},
        {"name": "Diamond Sparkle", "type": "Silver", "price": "Eternal", "emoji": "✨", "desc": "Shines bright like you, Vanshika"},
        {"name": "Peacock Glory", "type": "Blue", "price": "Royal", "emoji": "💙", "desc": "Bold and beautiful - that's you"},
        {"name": "Ruby Red", "type": "Red", "price": "Passionate", "emoji": "❤️", "desc": "The color of my love for you"},
    ]
    
    cols = st.columns(3)
    for idx, bangle in enumerate(bangles):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="bangle-item">
                <div style="font-size: 48px; margin-bottom: 10px;">{bangle['emoji']}</div>
                <h3 style="color: #333; margin: 10px 0;">{bangle['name']}</h3>
                <p style="color: #f5576c; font-weight: bold; font-size: 14px;">{bangle['type']}</p>
                <p style="color: #888; font-size: 12px; margin: 8px 0;">{bangle['desc']}</p>
                <p style="color: #667eea; font-weight: bold; margin-top: 10px;">Worth: {bangle['price']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")

# TAB 3: Quiz
with tab3:
    st.markdown("<h2 style='text-align: center; color: white;'>🎮 How Well Do I Know Vanshika? 🎮</h2>", unsafe_allow_html=True)
    
    quiz_questions = [
        {
            "q": "Vanshika's favorite bangle material is?",
            "options": ["Gold", "Silver", "Platinum", "Copper"],
            "answer": 0
        },
        {
            "q": "What emotion does Vanshika feel when wearing bangles?",
            "options": ["Confident", "Beautiful", "Complete", "All of the above"],
            "answer": 3
        },
        {
            "q": "Vanshika's ideal bangle has...",
            "options": ["Simplicity", "Intricate designs", "Both", "Neither"],
            "answer": 2
        },
    ]
    
    col1, col2, col3 = st.columns(3)
    
    for idx, question in enumerate(quiz_questions):
        st.write(f"**Question {idx+1}: {question['q']}**")
        selected = st.radio(
            "Choose your answer:",
            question['options'],
            key=f"q{idx}",
            horizontal=True
        )
        
        if selected == question['options'][question['answer']]:
            st.success("✅ Correct! I know you so well, Vanshika!")
            if 'quiz_answers' not in st.session_state:
                st.session_state.quiz_answers = []
            st.session_state.quiz_answers.append(True)
        else:
            st.info(f"The answer was: {question['options'][question['answer']]}")
            if 'quiz_answers' not in st.session_state:
                st.session_state.quiz_answers = []
            st.session_state.quiz_answers.append(False)
        st.write("---")
    
    if 'quiz_answers' in st.session_state and len(st.session_state.quiz_answers) == len(quiz_questions):
        score = sum(st.session_state.quiz_answers)
        percentage = (score / len(quiz_questions)) * 100
        
        st.markdown(f"""
        <div class="card-box">
            <h3 style="text-align: center;">Your Score: {score}/{len(quiz_questions)} ({percentage:.0f}%)</h3>
            <p style="text-align: center; color: #666;">
            {"Vanshika, you're perfect! 🎉" if percentage == 100 else "Amazing, Vanshika! 💪" if percentage >= 66 else "Come on, Vanshika! 💭"}
            </p>
        </div>
        """, unsafe_allow_html=True)

# TAB 4: Special Message
with tab4:
    st.markdown("<h2 style='text-align: center; color: white;'>💌 A Message For Vanshika 💌</h2>", unsafe_allow_html=True)
    
    if st.button("🎁 Click to Reveal the Message", use_container_width=True, key="reveal_btn"):
        st.session_state.revealed = True
    
    if st.session_state.revealed:
        st.markdown("""
        <div class="message-box">
            <p style="font-size: 24px; margin-bottom: 20px;">Dear Vanshika,</p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 You're like a bangle - beautiful, graceful, and perfect in every way.
            </p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 Just as bangles add beauty to the wrist, you add beauty to my life, Vanshika.
            </p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 Even though distance separates us right now, my thoughts are always with you.
            </p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 Every moment I spend thinking about you makes me smile.
            </p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 This site is just a tiny expression of what you mean to me.
            </p>
            <p style="margin: 20px 0; font-size: 18px;">
            💫 Vanshika, you make every moment special. You're my favorite person.
            </p>
            <p style="margin-top: 30px; font-size: 22px;">
            You're worth more than all the bangles in the world to me. 💕
            </p>
            <p style="margin-top: 30px; font-size: 18px;">
            Counting days until I see your beautiful smile again.
            </p>
            <p style="margin-top: 20px; font-size: 16px;">
            - Yours Always ✨
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.balloons()

# TAB 5: Surprise
with tab5:
    st.markdown("<h2 style='text-align: center; color: white;'>🎉 Final Surprise For Vanshika! 🎉</h2>", unsafe_allow_html=True)
    
    # Create a beautiful summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="stats-box">
            <h3 style="color: #f5576c;">😊</h3>
            <p style="color: #666; margin-top: 10px;">Pages For You</p>
            <h2 style="color: #f5576c;">5</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-box">
            <h3 style="color: #667eea;">💎</h3>
            <p style="color: #666; margin-top: 10px;">Bangles Selected</p>
            <h2 style="color: #667eea;">6</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stats-box">
            <h3 style="color: #764ba2;">💌</h3>
            <p style="color: #666; margin-top: 10px;">Love Messages</p>
            <h2 style="color: #764ba2;">∞</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    st.markdown("""
    <div class="card-box">
        <h3 style="text-align: center; color: #333;">🌟 Vanshika, You're My Sparkle 🌟</h3>
        <p style="text-align: center; color: #666; font-size: 16px; margin: 20px 0;">
        Here's how bright you make my world:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beautiful sparkle chart
    fig = go.Figure(data=[
        go.Bar(
            x=['Vanshika Sparkle Level'],
            y=[100],
            marker=dict(color=['#f5576c']),
            showlegend=False,
            text=['100% ✨'],
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        height=300,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False, range=[0, 120]),
        font=dict(color='white', size=14)
    )
    fig.update_yaxes(title_text="Sparkle Level ✨", title_font=dict(color='white'))
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="message-box" style="margin-top: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <p style="font-size: 20px; margin-bottom: 15px;">
        💞 Thank you for being YOU, Vanshika 💞
        </p>
        <p style="font-size: 16px;">
        This surprise is just the beginning. 
        The real gift is the moments we'll share together.
        </p>
        <p style="margin-top: 20px; font-size: 15px;">
        Distance is temporary, but what I feel for you is forever.
        </p>
        <p style="margin-top: 20px; font-size: 14px; font-style: italic;">
        Until we meet again, Vanshika... stay sparkly! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.write("")
    
    # Confetti on scroll
    if st.button("🎊 Celebrate Love! 🎊", use_container_width=True):
        st.balloons()

# Footer
st.markdown("""
<div style="text-align: center; color: #f0f0f0; margin-top: 50px; padding: 20px;">
    <p>Made with 💚 for Vanshika | Long distance but close at heart</p>
    <p style="font-size: 12px; color: #bbb;">Created with love: """ + datetime.now().strftime("%B %d, %Y") + """</p>
</div>
""", unsafe_allow_html=True)
