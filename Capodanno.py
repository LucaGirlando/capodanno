import streamlit as st
import pandas as pd
import random
import math
import time  
import io
import matplotlib.pyplot as plt
import os

# ============================================
# 1. CONFIGURAZIONE FORZATA 
# ============================================
config_path = os.path.expanduser("~/.streamlit/config.toml")
os.makedirs(os.path.dirname(config_path), exist_ok=True)

with open(config_path, "w") as f:
    f.write("[theme]\nbase='dark'\nprimaryColor='#8e2de2'\nbackgroundColor='#0f0c29'\nsecondaryBackgroundColor='#302b63'\ntextColor='#ffffff'\nfont='sans serif'\n")

st.set_page_config(page_title="Sdrogo Games 2025", page_icon="🔥", layout="wide", initial_sidebar_state="expanded")

# ============================================
# 2. FUNZIONI DI STILE
# ============================================
def title_html(text, color="#f09819", size="1.5rem", weight="bold"):
    return f"<div style='color:{color}; font-size:{size}; font-weight:{weight}; margin-bottom:5px; font-family:Montserrat, sans-serif;'>{text}</div>"

def gradient_text(text, size="3.5rem"):
    return f"""
    <div style='font-family: "Syncopate", sans-serif; font-weight: 700; font-size: {size}; 
    background: linear-gradient(90deg, #f09819, #edde5d); -webkit-background-clip: text; 
    -webkit-text-fill-color: transparent; text-transform: uppercase; margin-bottom: 10px;'>
    {text}
    </div>
    """

def neon_text(text, size="1.2rem"):
    return f"<span style='color:#8e2de2; font-weight:900; font-size:{size}; text-shadow: 0 0 10px rgba(142, 45, 226, 0.5);'>{text}</span>"

def gold_text(text, size="1rem"):
    return f"<span style='color:#f09819; font-weight:bold; font-size:{size};'>{text}</span>"

# ============================================
# 3. CSS 
# ============================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Montserrat:wght@300;400;700;900&display=swap');

/* Sfondo Animato */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #1a1a2e);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    font-family: 'Montserrat', sans-serif;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: rgba(15, 12, 41, 0.95);
    border-right: 2px solid #8e2de2;
}

/* Glass Cards */
.glass-box {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 16px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 25px;
    margin-bottom: 20px;
}

/* Pulsanti */
.stButton > button {
    background: linear-gradient(90deg, #8e2de2 0%, #4a00e0 100%);
    color: white;
    border: none;
    font-weight: bold;
    letter-spacing: 1px;
    padding: 0.5rem 1rem;
    transition: transform 0.2s;
}
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px rgba(142, 45, 226, 0.6);
}

/* Input Fields Style */
div[data-baseweb="select"] > div, div[data-baseweb="base-input"], div[data-baseweb="tag"], span[data-baseweb="tag"] {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid #8e2de2;
    color: white;
}

/* Grafici */
rect { fill: #8e2de2 !important; }

/* Messaggi */
.stAlert { background-color: rgba(0, 0, 0, 0.5) !important; color: white !important; }

/* Separatore */
hr { border-color: #8e2de2 !important; opacity: 0.3; }

</style>
""", unsafe_allow_html=True)

# ============================================
# DATI & COSTANTI
# ============================================
people = ["Girla", "Paci", "Marti", "Paga", "Yara", "Gaia", "Chiara", "Ele", "Ceci", "Ari", "Bax", "Camilla Consonni",
          "Enry", "Bomber", "Marghe", "Eugi", "Camilla De Ambrogio", "Lulli", "Tommaso", "Stefano", "Elisa"]

if 'votes' not in st.session_state:
    st.session_state.votes = []

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown(title_html("SDROGO HUB", "#f09819", "2rem", "900"), unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGAZIONE", ["Main Dashboard", "Online Games Links", "Event Betting", "Lupus in Fabula", "UwuFUFU Dojo", "Ludopazzia"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown(f"<div style='text-align:center; color:#8e2de2;'>Logged in as: <b>Guest</b></div>", unsafe_allow_html=True)

# ============================================
# SEZIONE 1: MAIN DASHBOARD
# ============================================
if menu == "Main Dashboard":
    st.markdown(gradient_text("THE MEZZENILE TAKEOVER"), unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#8e2de2; letter-spacing:5px; margin-top:-20px;'>SDROGO NEW YEAR 2025</h2>", unsafe_allow_html=True)
    
    # --- CARD 1: INSIGHTS ---
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    st.markdown(title_html("MEZZENILE INSIGHTS", "#f09819", "2rem"), unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(neon_text("ORIGINS"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('The Name:')} Mezzenile derives from the Latin <i>"Mesenile"</i>, indicating a central settlement. It has always been the strategic heart of the lower Val di Lanzo.
        </p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("NOBLE HISTORY"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('The Castle:')} The Francesetti Castle is the town's crown jewel. It once hosted the high aristocracy of Turin seeking mountain refuge.
        </p>""", unsafe_allow_html=True)

    with c2:
        st.markdown(neon_text("CRAFTSMANSHIP"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('Nail Makers:')} Mezzenile was the European capital of handmade nails. The <i>"Chiodaioli"</i> were famous for their indestructible steel creations.
        </p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("THE LEGEND"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('The Sdrogo Code:')} What happens in the mountains stays in the mountains. This is the first and only rule of the 2025 takeover.
        </p>""", unsafe_allow_html=True)

    with c3:
        st.markdown(neon_text("ENVIRONMENT"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('Thin Air:')} At 600m+ elevation, oxygen is lower and spirits are higher. Science says one shot here counts as two in the valley.
        </p>""", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("SURVIVAL"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd; font-size:0.95rem;'>
            {gold_text('The Cold:')} Don't let the fire go out. Mezzenile winters are unforgiving for those who don't keep their "hydration" levels up.
        </p>""", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- CARD 2: GRAN CENONE MENU (NATIVE STREAMLIT DESIGN) ---
    st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
    
    # Titolo Menu
    st.markdown(gradient_text("GRAND DINNER MENU", "2.8rem"), unsafe_allow_html=True)
    
    # Contenitore menu "simulato" usando colonne per centrare
    col_spacer_L, col_menu, col_spacer_R = st.columns([1, 6, 1])

    with col_menu:
        # Bordo dorato superiore
        st.markdown("<hr style='border: 2px solid #f09819; margin-bottom: 30px; opacity: 0.8;'>", unsafe_allow_html=True)

        # 1. STARTERS
        st.markdown("<div style='text-align: center; color: #8e2de2; font-size: 1.5rem; font-weight: 900; letter-spacing: 2px; margin-bottom: 10px;'>STARTERS</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Torte Salate Rustiche</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Panettone Gastronomico Salato</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Alpine Charcuterie Board</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: #aaa; font-size: 0.9rem; font-style: italic; margin-bottom: 30px;'>Selection of local cured meats & cheeses</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='text-align: center; color: #f09819; opacity: 0.5;'>♦</div>", unsafe_allow_html=True)

        # 2. FIRST COURSES
        st.markdown("<div style='text-align: center; color: #8e2de2; font-size: 1.5rem; font-weight: 900; letter-spacing: 2px; margin-top: 30px; margin-bottom: 10px;'>FIRST COURSES</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Risotto della Valle</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Lasagne al Pesto Genovese</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 30px;'>Lasagne al Ragù della Tradizione</div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; color: #f09819; opacity: 0.5;'>♦</div>", unsafe_allow_html=True)

        # 3. MAINS
        st.markdown("<div style='text-align: center; color: #8e2de2; font-size: 1.5rem; font-weight: 900; letter-spacing: 2px; margin-top: 30px; margin-bottom: 10px;'>MAIN COURSES & SIDES</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Polpo in Pignata e Purè</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Arrosto di Vitello alle Erbe</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 30px;'>Crispy Roasted Potatoes</div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center; color: #f09819; opacity: 0.5;'>♦</div>", unsafe_allow_html=True)

        # 4. DESSERTS
        st.markdown("<div style='text-align: center; color: #8e2de2; font-size: 1.5rem; font-weight: 900; letter-spacing: 2px; margin-top: 30px; margin-bottom: 10px;'>DESSERTS</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Salame di Cioccolato</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 5px;'>Classic Tiramisù</div>", unsafe_allow_html=True)
        st.markdown("<div style='text-align: center; color: white; font-size: 1.2rem; margin-bottom: 40px;'>Panettone con Crema Mascarpone</div>", unsafe_allow_html=True)

        # MIDNIGHT SPECIAL
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(142, 45, 226, 0.2) 0%, rgba(74, 0, 224, 0.2) 100%); 
                    border: 1px solid #8e2de2; border-radius: 10px; padding: 20px; text-align: center;'>
            <div style='color: #f09819; font-size: 1.3rem; letter-spacing: 2px; font-weight: bold; margin-bottom: 10px;'>MIDNIGHT SPECIAL</div>
            <div style='color: white; font-size: 1.5rem; font-weight: bold; margin-bottom: 5px;'>Cotechino con Lenticchie</div>
            <div style='color: #ffd700; font-size: 1rem; font-style: italic;'>✨ A tradition for good fortune in 2025 ✨</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Bordo dorato inferiore
        st.markdown("<hr style='border: 2px solid #f09819; margin-top: 30px; opacity: 0.8;'>", unsafe_allow_html=True)
    
# ============================================
# SEZIONE 2: ONLINE GAMES
# ============================================
elif menu == "Online Games Links":
    st.markdown(gradient_text("GAMING HQ"), unsafe_allow_html=True)
    
    st.markdown("<div class='glass-box' style='border-left: 5px solid #8e2de2;'>", unsafe_allow_html=True)
    st.markdown(title_html("TOURNAMENT RULES", "#8e2de2", "1.8rem"), unsafe_allow_html=True)
    st.markdown(f"""
    <div style='color:#eee; font-size:1.1rem; line-height:1.6;'>
        ► {gold_text('The Setup:')} Form <b>5 TEAMS of 4 players</b> each.<br>
        ► {gold_text('The Flow:')} Each team will play the 5 games in order. While one team competes, the others witness the performance.<br>
        ► {gold_text('The Penalty:')} At the end of every game round, the <b>4 LOSING TEAMS</b> must take a shot or a full glass of wine/beer.<br>
        ► {gold_text('The Grand Finale:')} After the final game, the <b>OVERALL WINNING TEAM</b> earns the right to choose <b>ONE PLAYER</b> from each of the other teams to take an extra penalty drink.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(title_html("THE 5 CHALLENGES", "#f09819", "1.5rem"), unsafe_allow_html=True)

    games = [
        {"name": "TimeGuessr", "url": "https://timeguessr.com/", "desc": "Identify year and location."},
        {"name": "FoodGuessr", "url": "https://www.foodguessr.com/", "desc": "Worldwide culinary hunt."},
        {"name": "The Auction Game", "url": "https://neal.fun/auction-game/", "desc": "Guess the price of absurd items."},
        {"name": "OpenGuessr", "url": "https://www.openguessr.com/maps", "desc": "Geography battle. Drop the pin."},
        {"name": "Higher or Lower", "url": "https://www.higherorlowergame.com/google/", "desc": "Which topic is searched more?"}
    ]

    for g in games:
        c1, c2 = st.columns([1, 4])
        with c1:
            st.markdown(f"<a href='{g['url']}' target='_blank'><button style='width:100%; padding:15px; background:#8e2de2; color:white; border:none; border-radius:10px; font-weight:bold; cursor:pointer;'>PLAY</button></a>", unsafe_allow_html=True)
        with c2:
            st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:10px; border-radius:10px;'>{gold_text(g['name'])}<br><span style='color:#ccc'>{g['desc']}</span></div>", unsafe_allow_html=True)
        st.write("")

    # --- SEZIONE BONUS ---
    st.markdown("<hr style='border-color:#f09819 !important; opacity:0.5; margin:30px 0;'>", unsafe_allow_html=True)
    st.markdown(title_html("EXTRA GAMES", "#f09819", "1.5rem"), unsafe_allow_html=True)
    
    # Make It Meme
    bc1, bc2 = st.columns([1, 4])
    with bc1:
        st.markdown(f"<a href='https://makeitmeme.com/it/' target='_blank'><button style='width:100%; padding:15px; background:linear-gradient(45deg, #f09819, #edde5d); color:black; border:none; border-radius:10px; font-weight:bold; cursor:pointer;'>OPEN</button></a>", unsafe_allow_html=True)
    with bc2:
        st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:10px; border-radius:10px;'>{gold_text('Make It Meme')}<br><span style='color:#ccc'>Not part of the tournament. Use this for chill moments!</span></div>", unsafe_allow_html=True)

    st.write("") # Spaziatore

    # Among Us Button
    au1, au2 = st.columns([1, 4])
    with au1:
        # Hack CSS per rendere ROSSO solo questo pulsante (target specifico per i pulsanti secondari in questa colonna se possibile, o uso di st.markdown per iniettare lo stile locale)
        st.markdown("""
        <style>
        /* Forza il colore rosso sui bottoni 'primary' solo in questa sezione se possibile, altrimenti sovrascrive */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(45deg, #ff0000, #cc0000) !important;
            border: 2px solid #ff0000 !important;
            color: white !important;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
        }
        div.stButton > button[kind="primary"]:hover {
            box-shadow: 0 0 25px rgba(255, 0, 0, 0.8);
            transform: scale(1.05);
        }
        </style>
        """, unsafe_allow_html=True)
        
        if st.button("AMONGUSSATAAAAAA!?", use_container_width=True, type="primary"):
            st.balloons()
            # SCRITTA GIGANTE OVERLAY
            st.markdown("""
            <div style='
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 90vw;
                padding: 60px;
                background-color: rgba(0, 0, 0, 0.95);
                border: 10px solid #ff0000;
                border-radius: 30px;
                text-align: center;
                z-index: 999999;
                box-shadow: 0 0 100px rgba(255, 0, 0, 0.9);
                backdrop-filter: blur(10px);
            '>
                <h1 style='
                    color: #ff0000; 
                    font-family: "Syncopate", sans-serif; 
                    font-size: 5vw; 
                    font-weight: 900; 
                    margin: 0; 
                    text-transform: uppercase;
                    text-shadow: 0 0 20px red;
                    line-height: 1.2;
                '>
                    ඞ<br>Let's play<br>Among Us!<br>ඞ
                </h1>
                <h2 style='
                    color: white; 
                    font-family: "Montserrat", sans-serif; 
                    font-size: 3vw; 
                    margin-top: 40px; 
                    font-weight: 800;
                    letter-spacing: 3px;
                '>
                    🚨 EMERGENCY MEETING CALLED! 🚨
                </h2>
            </div>
            """, unsafe_allow_html=True)
            
    with au2:
        st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:10px; border-radius:10px;'>{gold_text('Sus Button')}<br><span style='color:#ccc'>Warning: Pressing this button calls an Emergency Meeting.</span></div>", unsafe_allow_html=True)
# ============================================
# SEZIONE 3: EVENT BETTING
# ============================================
elif menu == "Event Betting":
    st.markdown(gradient_text("PROP BETS & ROULETTE"), unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🗳️ VOTE NOW", "🏆 LIVE RESULTS"])
    
    # 1. LISTA SCOMMESSE AGGIORNATA
    single_bets = [
        "The Ghost (Disappears without explanation)",
        "The Bladder (Most bathroom trips)",
        "The Zombie (Unconscious by midnight)",
        "The DJ Dictator (Monopolizes music)",
        "The Philosopher (First unrequested serious toast)",
        "The Clumsy One (First to spill something)",
        "The Confused (First to get a name wrong)",
        "The Drunkest", 
        "First to Throw Up", 
        "First to Break Something"
    ]
    pair_bets = ["First Two to Argue", "First Couple to Kiss HARD in Public"]

    # 2. HELPER PER COLORI ROULETTE
    def get_roulette_color(n):
        if n == 0: return "#00ff00" # Green
        red_nums = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        return "#ff0000" if n in red_nums else "#000000" # Red or Black

    with tab1:
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        
        st.markdown(title_html("WHO ARE YOU?", "#f09819", "1.2rem"), unsafe_allow_html=True)
        voter_name = st.selectbox("", ["Select your name"] + people, label_visibility="collapsed")
        
        if voter_name != "Select your name":
            current_votes = {}
            
            # --- SEZIONE 1: LE SCOMMESSE ---
            st.markdown("---")
            st.markdown(neon_text("INDIVIDUAL BETS", "1.5rem"), unsafe_allow_html=True)
            for bet in single_bets:
                st.markdown(f"<br>{gold_text(bet)}", unsafe_allow_html=True)
                current_votes[bet] = st.selectbox("", people, key=f"{voter_name}_{bet}", label_visibility="collapsed")
            
            st.markdown("---")
            st.markdown(neon_text("PAIR BETS (Pick 2)", "1.5rem"), unsafe_allow_html=True)
            for bet in pair_bets:
                st.markdown(f"<br>{gold_text(bet)}", unsafe_allow_html=True)
                pair = st.multiselect("", people, key=f"{voter_name}_{bet}_pair", label_visibility="collapsed")
                current_votes[bet] = tuple(sorted(pair))

            # --- SEZIONE 2: BUONI PROPOSITI ---
            st.markdown("---")
            st.markdown(neon_text("SECRET RESOLUTION", "1.5rem"), unsafe_allow_html=True)
            st.info("🔒 **Totally Anonymous.** Write a SERIOUS New Year's resolution. It will be shown shuffled with others.")
            current_votes['resolution'] = st.text_area("Your Resolution:", key=f"{voter_name}_res", placeholder="I promise to...")

            # --- SEZIONE 3: ROULETTE ---
            st.markdown("---")
            st.markdown(neon_text("THE SDROGO ROULETTE", "1.5rem"), unsafe_allow_html=True)
            st.warning("🎰 **THE PRIZE:** If your number is extracted, you win the **CHILL PASS**. You are authorized to do absolutely nothing and help no one.")
            
            # Genera opzioni roulette con colori
            roulette_options = list(range(37))
            
            # Visualizzazione personalizzata della scelta
            roulette_choice = st.selectbox(
                "Pick your Lucky Number (0-36)", 
                roulette_options, 
                key=f"{voter_name}_roulette"
            )
            
            # Mostra visivamente il colore scelto
            chosen_color = get_roulette_color(roulette_choice)
            st.markdown(f"""
            <div style='text-align:center; margin-top:10px;'>
                You picked: <span style='background-color:{chosen_color}; color:white; padding: 5px 15px; border-radius:5px; font-weight:bold; font-size:1.2rem; border:1px solid white;'>{roulette_choice}</span>
            </div>
            """, unsafe_allow_html=True)
            current_votes['roulette_num'] = roulette_choice

            st.markdown("<br>", unsafe_allow_html=True)
            
            # --- SALVATAGGIO ---
            if st.button("🔒 LOCK IN PREDICTIONS", use_container_width=True):
                valid = True
                for bet in pair_bets:
                    if current_votes[bet] is None or len(current_votes[bet]) != 2:
                        st.error(f"⚠️ For '{bet}', you must select EXACTLY 2 people!")
                        valid = False
                
                if valid:
                    # Rimuovi voti precedenti dello stesso utente
                    st.session_state.votes = [v for v in st.session_state.votes if v.get('_voter') != voter_name]
                    current_votes['_voter'] = voter_name
                    st.session_state.votes.append(current_votes)
                    st.balloons()
                    st.success(f"VOTES SAVED FOR {voter_name}!")

        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.votes:
            st.info("No votes yet. Be the first!")
        else:
            df = pd.DataFrame(st.session_state.votes)
            
            # 1. ROULETTE EXTRACTION (PRIMA DI TUTTO PER HYPE)
            st.markdown(title_html("🎰 ROULETTE EXTRACTION 🎰", "#ff0000"), unsafe_allow_html=True)
            
            if 'roulette_winner_num' not in st.session_state:
                st.session_state.roulette_winner_num = None

            spin_col1, spin_col2 = st.columns([1,3])
            with spin_col1:
                if st.button("🎲 SPIN THE WHEEL"):
                    placeholder = st.empty()
                    # Animazione
                    for _ in range(30):
                        temp_num = random.randint(0, 36)
                        temp_col = get_roulette_color(temp_num)
                        placeholder.markdown(f"""
                        <div style='text-align:center; font-size:4rem; font-weight:900; color:{temp_col}; text-shadow: 0 0 10px white;'>
                            {temp_num}
                        </div>
                        """, unsafe_allow_html=True)
                        time.sleep(0.05 + (_ * 0.005)) # Rallenta progressivamente
                    
                    # Numero Finale
                    final_num = random.randint(0, 36)
                    st.session_state.roulette_winner_num = final_num
                    placeholder.empty()

            # Mostra Risultato Roulette
            if st.session_state.roulette_winner_num is not None:
                win_n = st.session_state.roulette_winner_num
                win_c = get_roulette_color(win_n)
                st.markdown(f"""
                <div style='background: #111; border: 4px solid {win_c}; border-radius: 20px; padding: 20px; text-align: center; animation: pulse 1s infinite;'>
                    <div style='font-size: 1.5rem; color: #aaa;'>THE WINNING NUMBER IS</div>
                    <div style='font-size: 6rem; font-weight: 900; color: {win_c}; text-shadow: 0 0 20px {win_c};'>
                        {win_n}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Cerca i vincitori
                if 'roulette_num' in df.columns:
                    winners = df[df['roulette_num'] == win_n]['_voter'].tolist()
                    if winners:
                        st.markdown(f"""
                        <div style='margin-top:20px; text-align:center;'>
                            <h2 style='color:#ffd700;'>👑 CHILL PASS GRANTED TO: 👑</h2>
                            <h1 style='color:white;'>{", ".join(winners)}</h1>
                            <p style='color:#ccc;'>You are legally allowed to do nothing.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.markdown("<h3 style='text-align:center; color:#ff4b4b; margin-top:20px;'>🚫 NO WINNERS! EVERYONE GET BACK TO WORK! 🚫</h3>", unsafe_allow_html=True)

            st.markdown("---")

            # 2. RESOLUTIONS WALL
            st.markdown(title_html("📜 WALL OF RESOLUTIONS", "#f09819"), unsafe_allow_html=True)
            st.caption("Anonymous & Shuffled")
            
            if 'resolution' in df.columns:
                resolutions = df['resolution'].dropna().tolist()
                # Filtra stringhe vuote
                resolutions = [r for r in resolutions if len(str(r)) > 2]
                
                if resolutions:
                    random.shuffle(resolutions) # Mescola per anonimato
                    
                    # Visualizza come carte
                    res_cols = st.columns(2)
                    for i, res in enumerate(resolutions):
                        with res_cols[i % 2]:
                            st.markdown(f"""
                            <div style='background:rgba(255,255,255,0.05); padding:15px; border-radius:10px; margin-bottom:10px; border-left: 3px solid #f09819;'>
                                <span style='font-size:1.1rem; color:#eee; font-style:italic;'>"{res}"</span>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.write("No resolutions submitted yet.")

            st.markdown("---")

            # 3. CLASSIFICHE SCOMMESSE (Classico)
            st.markdown(title_html("BET RANKINGS", "#8e2de2"), unsafe_allow_html=True)
            
            for bet in single_bets:
                if bet in df.columns:
                    st.markdown(f"**{bet}**")
                    counts = df[bet].value_counts().head(3).reset_index()
                    counts.columns = ['Name', 'Votes']
                    st.bar_chart(counts, x='Name', y='Votes', color="#f09819")
            
            for bet in pair_bets:
                if bet in df.columns:
                    st.markdown(f"**{bet}**")
                    valid_pairs = df[bet].dropna()
                    if not valid_pairs.empty:
                        pair_series = valid_pairs.apply(lambda x: f"{x[0]} & {x[1]}" if isinstance(x, tuple) and len(x)==2 else None).dropna()
                        if not pair_series.empty:
                            counts = pair_series.value_counts().head(3).reset_index()
                            counts.columns = ['Couple', 'Votes']
                            st.bar_chart(counts, x='Couple', y='Votes', color="#8e2de2")
            
            # MVP
            st.markdown(gradient_text("OVERALL MVP"), unsafe_allow_html=True)
            all_names = []
            for col in single_bets: 
                if col in df.columns: all_names.extend(df[col].dropna().tolist())
            for col in pair_bets:
                if col in df.columns:
                    for p in df[col].dropna():
                        if isinstance(p, tuple): all_names.extend(list(p))
            
            if all_names:
                total = pd.Series(all_names).value_counts().reset_index()
                total.columns = ['Name', 'Total Votes']
                st.bar_chart(total, x='Name', y='Total Votes', color="#8e2de2")
                

# ============================================
# SEZIONE 4: LUPUS IN FABULA
# ============================================
elif menu == "Lupus in Fabula":
    st.markdown(gradient_text("LUPUS IN FABULA"), unsafe_allow_html=True)
    
    if 'game_started' not in st.session_state: st.session_state.game_started = False
    if 'current_player_index' not in st.session_state: st.session_state.current_player_index = 0
    if 'show_role' not in st.session_state: st.session_state.show_role = False

    # --- DATI RUOLI (NO HUNTER) ---
    role_data = {
        "Werewolf": {
            "desc": "🐺 <b>THE SOLDIER.</b> You are a normal Wolf. Wake up, agree on a victim, kill. Act innocent.",
            "tip": "Wake up with wolves. Point to kill. Don't make noise."
        },
        "Mascot Wolf": {
            "desc": "🐺👶 <b>THE MASCOT.</b> You are the pack's favorite. If you die, the NEXT night the Wolves kill <b>TWO</b> people out of rage.",
            "tip": "You are a Wolf. If you die, tell the Narrator secretly so he knows to grant the Double Kill."
        },
        "White Spirit": {
            "desc": "👻✨ <b>THE WHITE SPIRIT.</b> You are Good, but the Seer sees you as a WOLF. From Night 2, you can REVIVE a dead player. Max 2 resurrections. After the 2nd one, you die.",
            "tip": "NIGHT 1: Sleep. FROM NIGHT 2: Wake up and point to a dead player to revive. Remember: Seer sees you as 👎 (BAD)!"
        },
        "The Misunderstood": {
            "desc": "🤷‍♂️ <b>THE MISUNDERSTOOD.</b> You are a 100% Good Villager. However, the Seer sees you as a WOLF.",
            "tip": "You have no active powers. Just survive. Remember: If the Seer checks you, the Narrator will say you are 👎 (BAD)."
        },
        "Seer": {
            "desc": "🔮 <b>THE INVESTIGATOR.</b> Check one player every night to see if they are Good or Bad.",
            "tip": "Wake up. Point to a person. Narrator signals: 👍 = GOOD (Villager/Doc/Witch), 👎 = BAD (Wolf / Mascot / White Spirit / Misunderstood)."
        },
        "Doctor": {
            "desc": "💉 <b>THE SAVIOR.</b> Protect one person from Wolf attacks each night. You CAN protect yourself.",
            "tip": "Wake up. Point to someone to save from the bite. You cannot save from Witch's potion."
        },
        "Witch": {
            "desc": "🧪 <b>THE ALCHEMIST.</b> You have 2 one-use potions: 💚 LIFE (save a victim) and ☠️ DEATH (kill anyone).",
            "tip": "Narrator points to the victim. Thumbs UP = Save them. Thumbs DOWN = Kill someone else. You can do both."
        },
        "Cupid": {
            "desc": "💘 <b>THE MATCHMAKER.</b> Night 1 only: Link two Lovers. They live and die together.",
            "tip": "Wake up Night 1. Point to two people. They are now linked."
        },
        "Villager": {
            "desc": "🧑‍🌾 <b>THE MOB.</b> Sleep, Wake up, Vote. Trust no one.",
            "tip": "Sleep at night. Listen to sounds. Vote the wolves out during the day."
        }
    }

    if not st.session_state.game_started:
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        st.markdown(title_html("THE RULES OF MEZZENILE", "#f09819"), unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style='color:white; line-height:1.6;'>
            <p><b>THE BASICS:</b> Villagers vs Wolves. Wolves kill at night. Villagers vote to hang someone at day.</p>
            <hr style='border-color:#8e2de2'>
            <h3 style='color:#8e2de2'>🛑 SPECIAL ROLES EXPLAINED</h3>
            <ul>
                <li>🐺👶 <b>MASCOT WOLF (Evil):</b> A normal wolf, but beloved. If he dies, the Wolves get a <b>DOUBLE KILL</b> the next night out of rage.</li>
                <li>👻✨ <b>WHITE SPIRIT (Good):</b> Can revive dead players starting from Night 2. 
                    <br>⚠️ <b>CURSE:</b> He appears as a <b style='color:red'>WOLF</b> to the Seer.
                    <br>⚠️ <b>LIMIT:</b> Dies instantly after his 2nd resurrection.</li>
                <li>🤷‍♂️ <b>THE MISUNDERSTOOD (Good):</b> A normal villager with bad luck. He appears as a <b style='color:red'>WOLF</b> to the Seer.</li>
                <li>🔮 <b>SEER (Good):</b> Checks identities. <br>👍 = Good. <br>👎 = Bad (Wolf, Mascot, White Spirit, Misunderstood).</li>
                <li>💉 <b>DOCTOR (Good):</b> Protects from Wolf Bite (not from Witch). Can protect self.</li>
                <li>🧪 <b>WITCH (Good):</b> Has 1 Revive Potion and 1 Kill Potion. Can use anytime.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # GESTIONE GIOCATORI
        st.markdown(neon_text("WHO IS PLAYING?", "1.2rem"), unsafe_allow_html=True)
        active_players = st.multiselect("", people, default=people, key="active_p_sel", label_visibility="collapsed")
        st.markdown(f"<div style='margin:10px 0; color:#ddd;'>Active Players: <b>{len(active_players)}</b></div>", unsafe_allow_html=True)
        
        if len(active_players) < 5:
             st.error("Need at least 5 players to start!")
        else:
            st.markdown("---")
            st.markdown(gold_text("NARRATOR SELECTION MODE:"), unsafe_allow_html=True)
            narrator_mode = st.radio("", ["🎲 Random", "👤 Manual Selection"], label_visibility="collapsed", horizontal=True)
            
            manual_narrator = None
            if narrator_mode == "👤 Manual Selection":
                manual_narrator = st.selectbox("Select the Narrator:", active_players)

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button("🔥 START THE GAME (ASSIGN ROLES)", use_container_width=True):
                # 1. Narratore
                if narrator_mode == "👤 Manual Selection" and manual_narrator:
                    narrator = manual_narrator
                else:
                    narrator = random.choice(active_players)

                players_without_narrator = [p for p in active_players if p != narrator]
                n_actual_players = len(players_without_narrator)
                
                # 2. Setup Lupi (1 Mascot + Resto Normali)
                n_total_wolves = max(1, math.floor(n_actual_players / 4))
                wolves_list = ["Mascot Wolf"] + (["Werewolf"] * (n_total_wolves - 1))
                
                # 3. Setup Speciali (Senza Hunter)
                priority_specials = ["Seer", "Doctor", "Witch", "The Misunderstood", "White Spirit", "Cupid"]
                
                max_specials_count = max(0, n_actual_players - n_total_wolves - 1)
                active_specials = priority_specials[:min(len(priority_specials), max_specials_count)]
                
                # 4. Setup Villici
                n_villagers = n_actual_players - n_total_wolves - len(active_specials)
                
                # Mix
                roles_pool = wolves_list + active_specials + (["Villager"] * n_villagers)
                random.shuffle(roles_pool)
                
                st.session_state.narrator_name = narrator
                st.session_state.game_roles = dict(zip(players_without_narrator, roles_pool))
                st.session_state.players_to_reveal = players_without_narrator
                st.session_state.game_started = True
                st.rerun()

    elif st.session_state.current_player_index < len(st.session_state.players_to_reveal):
        st.markdown(f"""
        <div style='text-align:center; margin-bottom:20px;'>
            <div style='color:#8e2de2; font-size:1.2rem; font-weight:bold;'>THE NARRATOR IS</div>
            <div style='color:#f09819; font-size:4rem; font-weight:900; text-transform:uppercase; font-family:"Syncopate"; text-shadow:0 0 15px rgba(240, 152, 25, 0.5);'>
                {st.session_state.narrator_name}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        idx = st.session_state.current_player_index
        player = st.session_state.players_to_reveal[idx]
        
        st.markdown(f"<div class='glass-box' style='text-align:center;'>PASS PHONE TO:<br>{gradient_text(player, '2.5rem')}</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        if c1.button("👁️ REVEAL ROLE", use_container_width=True): st.session_state.show_role = True
        if c2.button("NEXT PLAYER ➡️", use_container_width=True): 
            st.session_state.current_player_index += 1
            st.session_state.show_role = False
            st.rerun()
            
        if st.session_state.show_role:
            role_name = st.session_state.game_roles[player]
            info = role_data.get(role_name, {"desc": "Role unknown", "tip": "No tip."})
            
            st.markdown(f"""
            <div style='background:rgba(142, 45, 226, 0.2); padding:20px; border-radius:10px; border:2px solid #8e2de2; text-align:center; margin-top:10px;'>
                <h1 style='color:#f09819; margin:0;'>{role_name.upper()}</h1>
                <p style='color:white; font-size:1.1rem; margin-top:10px;'>{info['desc']}</p>
                <div style='background: rgba(0,0,0,0.3); padding:10px; border-radius:5px; margin-top:15px; border-left: 3px solid #f09819;'>
                    <span style='color:#f09819; font-weight:bold;'>💡 PLAYER TIP:</span> <span style='color:#ddd; font-style:italic;'>{info['tip']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    else:
        # --- DASHBOARD NARRATORE ---
        st.markdown(f"""
        <div style='text-align:center; margin-bottom:30px;'>
            <span style='color:white; font-size:1.5rem;'>Narrator Dashboard:</span><br>
            <span style='color:#f09819; font-size:3rem; font-weight:900;'>{st.session_state.narrator_name}</span>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📜 OPEN NARRATOR SCRIPT (SUPER DETAILED)", expanded=True):
            st.markdown("### 🌚 THE NIGHT PHASE")
            st.write("🛑 **'Everyone, close your eyes! Deep sleep falls on Mezzenile.'**")
            
            st.markdown("---")
            st.info("""
            **💘 (NIGHT 1 ONLY) CUPID**
            * "Cupid, wake up. Point to the two Lovers."
            * "Cupid, sleep."
            * (Tap Lovers' shoulders).
            * "Lovers, wake up. Look at each other."
            * "Lovers, sleep."
            """)
            st.markdown("---")
            
            st.markdown("#### 👻 WHITE SPIRIT (Start from NIGHT 2)")
            st.warning("""
            1. "White Spirit, wake up."
            2. "Point to a DEAD player to revive."
            3. (If he points: That player wakes up tomorrow).
            4. **NOTE:** If this is his 2nd resurrection, White Spirit dies tomorrow morning.
            """)
            st.write("**'Spirit, sleep.'**")
            st.write("")

            st.markdown("#### 🐺 WEREWOLVES")
            st.warning("""
            **CHECK:** Did **Mascot Wolf** die yesterday?
            * **NO:** "Wolves, choose **ONE** victim."
            * **YES:** "Wolves, blinded by rage, choose **TWO** victims tonight!"
            """)
            st.write("**'Wolves, wake up... Choose your victim(s).'**")
            st.write("(Nod to confirm).")
            st.write("**'Wolves, sleep.'**")
            st.write("") 
            
            st.markdown("#### 🔮 THE SEER")
            st.warning("""
            **CRITICAL CHECK:**
            * If pointing at **Werewolf** -> 👎 (BAD)
            * If pointing at **Villager / Doc / Witch / Cupid** -> 👍 (GOOD)
            * If pointing at **THE MISUNDERSTOOD** -> 👎 (BAD - Lie to Seer)
            * If pointing at **WHITE SPIRIT** -> 👎 (BAD - Lie to Seer)
            """)
            st.write("**'Seer, wake up. Point to someone.'**")
            st.write("(Show sign: 👍 or 👎).")
            st.write("**'Seer, sleep.'**")
            st.write("")

            st.markdown("#### 💉 THE DOCTOR")
            st.write("**'Doctor, wake up. Who do you want to save from the bite?'**")
            st.write("(Remember: He saves from Wolves, NOT from Witch).")
            st.write("**'Doctor, sleep.'**")
            st.write("")

            st.markdown("#### 🧪 THE WITCH")
            st.warning("""
            **ACTION:**
            1. Point to the Wolf's victim. "This person is dying."
            2. Show **Life Potion** (Thumbs up). "Do you use it?"
            3. Show **Death Potion** (Thumbs down). "Do you want to kill someone else?"
            """)
            st.write("**'Witch, wake up...'** (Perform actions).")
            st.write("**'Witch, sleep.'**")

            st.markdown("### ☀️ THE DAY PHASE")
            st.write("🌅 **'Everybody wake up! The sun rises over Mezzenile.'**")
            
            st.markdown("#### 📢 MORNING ANNOUNCEMENTS (Choose the scenario)")
            
            # SCENARIO 1: NESSUNO MORTO
            st.success("""
            **CASE 1: NO ONE DIED (Doctor/Witch saved)**
            * 🗣️ "It is a miracle! The night was silent. **NOBODY DIED!**"
            """)
            
            # SCENARIO 2: QUALCUNO E' MORTO
            st.error("""
            **CASE 2: DEATHS OCCURRED**
            * 🗣️ "I have bad news... Last night, we found the body of **[PLAYER NAME]**."
            * *(If Witch killed too)*: "...and we also found a second body. **[PLAYER NAME]** is also dead."
            """)
            
            # SCENARIO 3: RESURREZIONE SPIRITO BIANCO
            st.info("""
            **CASE 3: WHITE SPIRIT RESURRECTION**
            * 🗣️ "BUT WAIT! A light shines upon the graveyard... **[PLAYER NAME]** comes back to life!"
            * *(If Spirit used 2nd revive)*: "...However, the magic required a life for a life. The White Spirit exhausted their power. **[SPIRIT NAME]** drops dead. Thank you for your sacrifice."
            """)
            
            st.markdown("#### ⚡ CHAIN REACTIONS (Check immediately!)")
            
            st.warning("""
            💔 **DID A LOVER DIE?**
            * 🗣️ "**[PARTNER NAME]**, you see your lover dead. Your heart cannot take it. You die of a broken heart immediately."
            
            🐺👶 **DID THE MASCOT WOLF DIE?**
            * 🗣️ "You fools! You killed the Mascot Wolf! The pack is howling in rage... **TOMORROW NIGHT THEY WILL KILL TWO PEOPLE!**"
            """)
            
            st.markdown("---")
            st.write("🗣️ **'Townspeople, discuss! Who is lying? Who is a Wolf? You have 5 minutes!'**")

        st.markdown("### 💀 GRAVEYARD & ALIVE PLAYERS")
        
        # Checkbox Logic
        if 'dead_p' not in st.session_state: st.session_state.dead_p = []
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(title_html("VILLAGERS TEAM", "#00ff88"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r not in ["Werewolf", "Mascot Wolf"]:
                    is_dead = st.checkbox(f"{n} ({r})", key=f"d_{n}")
                    if is_dead and n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif not is_dead and n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        with c2:
            st.markdown(title_html("WOLVES TEAM", "#ff4b4b"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r in ["Werewolf", "Mascot Wolf"]:
                    is_dead = st.checkbox(f"{n} ({r})", key=f"d_{n}")
                    if is_dead and n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif not is_dead and n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        
        wolves_alive = sum(1 for n,r in st.session_state.game_roles.items() if (r=="Werewolf" or r=="Mascot Wolf") and n not in st.session_state.dead_p)
        villagers_alive = sum(1 for n,r in st.session_state.game_roles.items() if (r!="Werewolf" and r!="Mascot Wolf") and n not in st.session_state.dead_p)
        
        st.markdown("---")
        if wolves_alive == 0: 
            st.markdown("<div style='background:#00ff88; color:black; padding:20px; text-align:center; border-radius:15px;'><h1>🎉 VILLAGERS WIN! 🎉</h1></div>", unsafe_allow_html=True)
        elif wolves_alive >= villagers_alive:
             st.markdown("<div style='background:#ff4b4b; color:white; padding:20px; text-align:center; border-radius:15px;'><h1>🐺 WEREWOLVES WIN! 🐺</h1></div>", unsafe_allow_html=True)
             
        if st.button("🔄 RESET GAME"):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()
# ============================================
# SEZIONE 5: UWUFUFU DOJO (CHILL & DEBATE)
# ============================================
elif menu == "UwuFUFU Dojo":
    st.markdown(gradient_text("UWUFUFU DOJO"), unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.05); border-left: 5px solid #f09819; padding: 20px; border-radius: 5px; margin-bottom: 30px;'>
        <h3 style='color: #f09819; margin: 0; font-family: "Syncopate", sans-serif;'>CHILL, JUDGE & DEBATE</h3>
        <p style='color: #ddd; font-size: 1.1rem; margin-top: 10px;'>
            Pick a tournament. Share your screen. Fight for your opinion.<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Lista dei tornei
    tournaments = [
        {"name": "BEST SONG OF ALL TIME", "url": "https://www.uwufufu.com/worldcup/best-songs-of-all-time-fouda", "icon": "🎵"},
        {"name": "BEST MOVIE EVER", "url": "https://www.uwufufu.com/worldcup/best-movie-of-all-time-nymphz", "icon": "🎬"},
        {"name": "ITALIAN RAP HITS", "url": "https://www.uwufufu.com/worldcup/canzoni-rap-italiane-alexwrite", "icon": "🎤"},
        {"name": "ANIMAL FIGHT CLUB (1v1)", "url": "https://www.uwufufu.com/worldcup/1v1-animal-tournament-dozed", "icon": "🦁"},
        {"name": "BEST SUPERPOWER", "url": "https://www.uwufufu.com/worldcup/top-98-superpowers-professor-tigs", "icon": "⚡"},
        {"name": "BEST FOOD WORLDWIDE", "url": "https://www.uwufufu.com/worldcup/best-food-worldwide-twitchtvzrvkk", "icon": "🍕"},
        {"name": "BEST ANIMATED MOVIE", "url": "https://www.uwufufu.com/worldcup/top-film-animazione-giulio-cavatorta", "icon": "👾"},
        {"name": "ULTIMATE DEATHMATCH", "url": "https://www.uwufufu.com/worldcup/chi-vincerebbe-in-uno-scontro-allultimo-sangue-gvc9", "icon": "⚔️"},
        {"name": "BETTER CHARACTER", "url": "https://www.uwufufu.com/worldcup/better-character-homelander2000", "icon": "🎭"},
        {"name": "BEST FRUITS TIER LIST", "url": "https://www.uwufufu.com/worldcup/best-fruits-charles", "icon": "🍎"},
        {"name": "BIGGEST CHAD EVER", "url": "https://www.uwufufu.com/worldcup/the-biggest-chad-of-all-time-compysage", "icon": "🗿"},
        {"name": "MOST BEAUTIFUL GIRL", "url": "https://www.uwufufu.com/worldcup/most-beautiful-girl-on-earth-jaqenoneal", "icon": "💃"}
    ]

    # Creazione Griglia 3 colonne
    cols = st.columns(3)
    
    for i, t in enumerate(tournaments):
        with cols[i % 3]:
            st.markdown(f"""
            <a href='{t['url']}' target='_blank' style='text-decoration: none;'>
                <div style='
                    background: linear-gradient(135deg, rgba(142, 45, 226, 0.1) 0%, rgba(15, 12, 41, 0.8) 100%);
                    border: 1px solid #8e2de2;
                    border-radius: 15px;
                    padding: 25px;
                    margin-bottom: 20px;
                    text-align: center;
                    transition: transform 0.2s;
                    min-height: 150px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                ' onmouseover="this.style.transform='scale(1.05)'; this.style.borderColor='#f09819';" onmouseout="this.style.transform='scale(1)'; this.style.borderColor='#8e2de2';">
                    <div style='font-size: 2.5rem; margin-bottom: 10px;'>{t['icon']}</div>
                    <div style='
                        color: white;
                        font-family: "Montserrat", sans-serif;
                        font-weight: 800;
                        font-size: 1.1rem;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                    '>{t['name']}</div>
                    <div style='color: #f09819; font-size: 0.8rem; margin-top: 5px;'>CLICK TO PLAY</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

# ===============================================================
# SEZIONE 6: CRAZY TIME SIMULATOR 
# ===============================================================
elif menu == "Ludopazzia":
    # --- CSS E STILI ---
    st.markdown("""
    <style>
    .bet-btn { border-radius: 10px; padding: 10px; text-align: center; color: black; font-weight: bold; margin: 5px; border: 2px solid white; transition: all 0.3s; cursor: pointer; }
    .bet-btn:hover { transform: scale(1.05); }
    .num-1 { background-color: #6fa8dc; }
    .num-2 { background-color: #ffd966; }
    .num-5 { background-color: #ea9999; }
    .num-10 { background-color: #8e7cc3; }
    .bonus-coin { background-color: #0b5394; color: white; border: 2px solid #3d85c6; }
    .bonus-cash { background-color: #38761d; color: white; border: 2px solid #6aa84f; }
    .bonus-pachinko { background-color: #a64d79; color: white; border: 2px solid #d5a6bd; }
    .bonus-crazy { background-color: #cc0000; color: white; border: 2px solid #ff0000; box-shadow: 0 0 15px red; animation: pulse 2s infinite; }
    
    .history-ball { display: inline-block; width: 35px; height: 35px; border-radius: 50%; text-align: center; line-height: 35px; margin-right: 5px; font-weight: bold; color: black; font-size: 0.8rem; border: 1px solid white; }
    
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(255, 0, 0, 0); } 100% { box-shadow: 0 0 0 0 rgba(255, 0, 0, 0); } }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(gradient_text("CRAZY TIME: SDROGO EDITION"), unsafe_allow_html=True)

    # --- STATE MANAGEMENT ---
    # Gestiamo le fasi del gioco: 'DEPOSIT', 'BETTING', 'SPINNING', 'BONUS_CHOICE', 'PAYOUT'
    if 'game_phase' not in st.session_state: st.session_state.game_phase = 'DEPOSIT'
    if 'balance' not in st.session_state: st.session_state.balance = 0.0
    if 'history' not in st.session_state: st.session_state.history = []
    if 'current_bets' not in st.session_state: st.session_state.current_bets = {}
    if 'spin_result' not in st.session_state: st.session_state.spin_result = None
    if 'top_slot_mult' not in st.session_state: st.session_state.top_slot_mult = 1
    if 'active_bonus' not in st.session_state: st.session_state.active_bonus = None

    # DEFINIZIONE SEGMENTI E COLORI
    wheel_segments = ([1]*21 + [2]*13 + [5]*7 + [10]*4 + ["Coin Flip"]*4 + ["Pachinko"]*2 + ["Cash Hunt"]*2 + ["CRAZY TIME"]*1)
    seg_colors = {1: "#6fa8dc", 2: "#ffd966", 5: "#ea9999", 10: "#8e7cc3", "Coin Flip": "#0b5394", "Pachinko": "#a64d79", "Cash Hunt": "#38761d", "CRAZY TIME": "#ff0000"}

    # ==========================================
    # FASE 1: DEPOSITO (SCAM CREDIT CARD)
    # ==========================================
    if st.session_state.game_phase == 'DEPOSIT' or st.session_state.balance < 1:
        st.markdown("<div class='glass-box' style='max-width: 500px; margin: auto;'>", unsafe_allow_html=True)
        st.markdown(title_html("💸 DEPOSIT FUNDS", "#f09819", "1.5rem"), unsafe_allow_html=True)
        st.caption("Please enter your credit card details to play. Trusted by 0 banks.")
        
        col_cc1, col_cc2 = st.columns(2)
        with col_cc1: st.text_input("Card Number", placeholder="XXXX-XXXX-XXXX-XXXX")
        with col_cc2: st.text_input("CVV", type="password", placeholder="123")
        
        st.text_input("Cardholder Name", placeholder="MR. LUDOPATIC")
        
        deposit_amount = st.number_input("Amount to Deposit (€)", min_value=10, step=50, value=100)
        
        if st.button("💳 AUTHORIZE TRANSACTION", use_container_width=True, type="primary"):
            with st.spinner("Contacting bank... Verifying funds... Stealing data..."):
                time.sleep(2) # Fake delay
                if deposit_amount > 20000:
                    st.error("🚫 TRANSACTION DECLINED: Insufficient Funds. Max limit is € 20,000. Stop dreaming.")
                else:
                    st.session_state.balance = float(deposit_amount)
                    st.session_state.game_phase = 'BETTING'
                    st.success("✅ DEPOSIT SUCCESSFUL! Good luck.")
                    time.sleep(1)
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ==========================================
    # FASE 2: GIOCO ATTIVO
    # ==========================================
    else:
        # --- HEADER: INFO E STORICO ---
        c1, c2 = st.columns([1, 2])
        with c1:
            st.markdown(f"""
            <div style='background: #111; border: 2px solid #f09819; border-radius: 10px; padding: 10px; text-align: center;'>
                <div style='color: #aaa; font-size: 0.8rem;'>BALANCE</div>
                <div style='color: #f09819; font-size: 1.8rem; font-weight: 900;'>€ {st.session_state.balance:.0f}</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("<div style='color:#aaa; font-size:0.8rem; margin-bottom:5px; text-align:right;'>LAST WINNERS:</div>", unsafe_allow_html=True)
            hist_html = "<div style='text-align:right;'>"
            for h in st.session_state.history[-10:]: 
                bg = seg_colors.get(h, "#333")
                txt = str(h)[0] if isinstance(h, str) else str(h)
                hist_html += f"<div class='history-ball' style='background:{bg};'>{txt}</div>"
            hist_html += "</div>"
            st.markdown(hist_html, unsafe_allow_html=True)

        st.markdown("---")

        # ==========================================
        # SOTTO-FASE: PIAZZARE SCOMMESSE
        # ==========================================
        if st.session_state.game_phase == 'BETTING':
            st.info("👇 PLACE YOUR BETS ON THE GRID 👇")
            
            # Helper input
            bets = {}
            cols = st.columns(4)
            labels = [(1, "num-1"), (2, "num-2"), (5, "num-5"), (10, "num-10")]
            for i, (l, c) in enumerate(labels):
                with cols[i]:
                    bets[l] = st.number_input(f"Bet {l}", min_value=0, step=10, key=f"bet_{l}", label_visibility="collapsed")
                    st.markdown(f"<div class='bet-btn {c}'>{l}</div>", unsafe_allow_html=True)

            cols_b = st.columns(4)
            labels_b = [("Coin Flip", "bonus-coin"), ("Cash Hunt", "bonus-cash"), ("Pachinko", "bonus-pachinko"), ("CRAZY TIME", "bonus-crazy")]
            for i, (l, c) in enumerate(labels_b):
                with cols_b[i]:
                    bets[l] = st.number_input(f"Bet {l}", min_value=0, step=10, key=f"bet_{l}", label_visibility="collapsed")
                    st.markdown(f"<div class='bet-btn {c}' style='font-size:0.8rem;'>{l}</div>", unsafe_allow_html=True)

            total_bet = sum(bets.values())
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🎰 BET & SPIN", use_container_width=True, type="primary"):
                if total_bet == 0:
                    st.warning("You must bet something to play!")
                elif total_bet > st.session_state.balance:
                    st.error("Insufficient funds! Sell your house or lower the bet.")
                else:
                    st.session_state.balance -= total_bet
                    st.session_state.current_bets = bets
                    st.session_state.game_phase = 'SPINNING'
                    st.rerun()
            
            # Tasto Cash Out
            if st.button("🚪 CASH OUT (Exit Game)"):
                st.session_state.game_phase = 'DEPOSIT'
                st.rerun()

        # ==========================================
        # SOTTO-FASE: SPINNING & TOP SLOT
        # ==========================================
        elif st.session_state.game_phase == 'SPINNING':
            # 1. TOP SLOT ANIMATION
            slot_ph = st.empty()
            with slot_ph.container():
                st.info("🎰 TOP SLOT SPINNING...")
                # Generazione Top Slot
                ts_seg = random.choice([1, 2, 5, 10, "Coin Flip", "Pachinko", "Cash Hunt", "CRAZY TIME"])
                ts_mult = random.choice([2, 3, 4, 5, 10, 20, 25, 50])
                
                # Suspense animation
                time.sleep(1.5) 
                st.markdown(f"""
                <div style='text-align:center; padding:15px; background:#222; border: 3px solid #ffd700; border-radius:15px; margin-bottom:20px; box-shadow: 0 0 20px #ffd700;'>
                    <div style='color:#aaa; font-size:0.9rem;'>TOP SLOT RESULT</div>
                    <span style='color:{seg_colors.get(ts_seg)}; font-weight:bold; font-size:1.5rem;'>{ts_seg}</span>
                    <span style='color:white; font-size:1.5rem;'> + </span>
                    <span style='color:#ffd700; font-weight:bold; font-size:1.5rem;'>{ts_mult}x</span>
                </div>
                """, unsafe_allow_html=True)
            
            # 2. WHEEL ANIMATION
            wheel_ph = st.empty()
            wheel_ph.markdown("<div style='text-align:center; font-size:2rem; margin-top:20px;'>The wheel is spinning...</div>", unsafe_allow_html=True)
            
            # Suspense loop
            for _ in range(10):
                temp = random.choice(wheel_segments)
                c = seg_colors.get(temp, "#fff")
                wheel_ph.markdown(f"<div style='text-align:center; font-size:4rem; font-weight:bold; color:{c}; opacity:0.5;'>{temp}</div>", unsafe_allow_html=True)
                time.sleep(0.2) # Rallenta un po'

            wheel_ph.markdown("<div style='text-align:center; font-size:2rem; margin-top:20px;'>Slowing down...</div>", unsafe_allow_html=True)
            time.sleep(1)

            # 3. RISULTATO FINALE
            final_res = random.choice(wheel_segments)
            st.session_state.spin_result = final_res
            st.session_state.history.append(final_res)
            
            # Check Top Slot Match
            st.session_state.top_slot_mult = 1
            if ts_seg == final_res:
                st.session_state.top_slot_mult = ts_mult
                st.success(f"🔥 TOP SLOT MATCH! Multiplier upgraded to {ts_mult}x!")
                time.sleep(1.5)

            # Aggiorna UI Ruota
            c_res = seg_colors.get(final_res, "#fff")
            wheel_ph.markdown(f"""
            <div style='text-align:center; transform: scale(1.1); padding: 20px; border: 4px solid {c_res}; border-radius: 20px;'>
                <div style='font-size:1.5rem; color:#aaa;'>RESULT</div>
                <div style='font-size:4rem; font-weight:900; color:{c_res}; text-shadow:0 0 20px {c_res};'>{final_res}</div>
            </div>
            """, unsafe_allow_html=True)
            time.sleep(2)

            # 4. DECISIONE PERCORSO (Bonus o Payout Diretto)
            if isinstance(final_res, str): # È UN BONUS
                # Controllo se l'utente ha puntato sul bonus
                if st.session_state.current_bets.get(final_res, 0) > 0:
                    st.session_state.active_bonus = final_res
                    st.session_state.game_phase = 'BONUS_CHOICE'
                    st.rerun()
                else:
                    st.error(f"😭 You didn't bet on {final_res}. You watch in silence.")
                    time.sleep(3)
                    st.session_state.game_phase = 'BETTING'
                    st.rerun()
            else:
                # È UN NUMERO
                st.session_state.game_phase = 'PAYOUT'
                st.rerun()

        # ==========================================
        # SOTTO-FASE: INTERAZIONE BONUS (LA PARTE DIVERTENTE)
        # ==========================================
        elif st.session_state.game_phase == 'BONUS_CHOICE':
            bonus = st.session_state.active_bonus
            mult = st.session_state.top_slot_mult
            
            st.markdown(f"<div style='background:#111; padding:20px; border-radius:15px; border: 2px solid #fff; text-align:center;'>", unsafe_allow_html=True)
            st.markdown(title_html(f"{bonus} ROUND", seg_colors[bonus]), unsafe_allow_html=True)
            if mult > 1: st.markdown(f"<h3 style='color:#ffd700;'>ACTIVE MULTIPLIER: {mult}x</h3>", unsafe_allow_html=True)

            # --- LOGICA SPECIFICA PER BONUS ---
            
            if bonus == "Coin Flip":
                st.write("🪙 **CHOOSE YOUR SIDE!**")
                # Generiamo i moltiplicatori nascosti
                m_red = random.choice([10, 15, 20, 25, 50, 100]) * mult
                m_blue = random.choice([2, 5, 10, 15, 20]) * mult
                
                c1, c2 = st.columns(2)
                choice = None
                with c1:
                    if st.button("🔴 RED", use_container_width=True): choice = "RED"
                with c2: 
                    if st.button("🔵 BLUE", use_container_width=True): choice = "BLUE"
                
                if choice:
                    st.write(f"You chose **{choice}**. Flipping...")
                    with st.spinner("Flipping coin..."):
                        time.sleep(2)
                    
                    flip_res = random.choice(["RED", "BLUE"])
                    win_mult = m_red if flip_res == "RED" else m_blue
                    
                    st.markdown(f"""
                    <div style='display:flex; justify-content:space-around; font-size:1.5rem; font-weight:bold; margin:20px 0;'>
                        <div style='color:#ff4b4b'>🔴 {m_red}x</div>
                        <div style='color:#4b4bff'>🔵 {m_blue}x</div>
                    </div>
                    <h2 style='color:white; text-align:center;'>RESULT: {flip_res}</h2>
                    """, unsafe_allow_html=True)
                    
                    final_win_mult = win_mult if choice == flip_res else 0 # Nel Coin Flip vero vinci il lato che esce, non quello che scegli. 
                    # MA ASPETTA: Nel gioco vero tu NON scegli, viene assegnato il colore alla moneta. 
                    # Rendiamolo "Interattivo": Tu scegli il colore, se esce il tuo colore prendi quel moltiplicatore.
                    # ANZI, facciamolo fedele al vero: La moneta ha due facce con due moltiplicatori. Viene lanciata. Tu vinci quello che esce.
                    # PERÒ l'utente voleva scegliere. Facciamo che l'utente "indovina" il lato per un boost? 
                    # NO, facciamo semplice: Mostriamo i due moltiplicatori assegnati ai colori. La moneta gira. Vince il lato che atterra.
                    
                    final_payout = win_mult # Vinci sempre il lato che esce nel vero gioco. Qui semplifichiamo: hai vinto il moltiplicatore uscito.
                    
                    time.sleep(2)
                    st.session_state.last_win_mult = final_payout
                    st.session_state.game_phase = 'PAYOUT'
                    st.rerun()

            elif bonus == "Cash Hunt":
                st.write("🦆 **AIM AND FIRE!** Choose a target symbol.")
                # Simuliamo la scelta con 3 opzioni cieche
                c1, c2, c3 = st.columns(3)
                target = None
                if c1.button("🌵 CACTUS"): target = "CACTUS"
                if c2.button("🐰 RABBIT"): target = "RABBIT"
                if c3.button("🐥 CHICKEN"): target = "CHICKEN"
                
                if target:
                    st.write(f"Aiming at {target}...")
                    with st.spinner("Sniper locking on..."):
                        time.sleep(2)
                    
                    found_mult = random.choice([10, 25, 50, 100, 500]) * mult
                    st.markdown(f"<h1 style='color:#00ff00; text-align:center;'>💥 BOOM! You found {found_mult}x!</h1>", unsafe_allow_html=True)
                    time.sleep(2)
                    st.session_state.last_win_mult = found_mult
                    st.session_state.game_phase = 'PAYOUT'
                    st.rerun()

            elif bonus == "Pachinko":
                st.write("🟣 **DROP THE PUCK!** Choose drop zone.")
                zones = st.columns(4)
                zone = None
                for i in range(1, 5):
                    if zones[i-1].button(f"Zone {i}"): zone = i
                
                if zone:
                    st.write(f"Dropping from Zone {zone}...")
                    placeholder = st.empty()
                    for i in range(3):
                        placeholder.write(f"Puck falling... bounces left... bounces right...")
                        time.sleep(1)
                    
                    landing = random.choice([10, 25, 50, 100, 200, "DOUBLE"])
                    if landing == "DOUBLE":
                        st.warning("✨ DOUBLE! Re-dropping with doubled values!")
                        time.sleep(1.5)
                        landing = random.choice([20, 50, 100, 200, 400]) * 2
                    
                    final_m = landing * mult
                    st.markdown(f"<h1 style='color:#e066ff; text-align:center;'>🕳️ Landed in {final_m}x!</h1>", unsafe_allow_html=True)
                    time.sleep(2)
                    st.session_state.last_win_mult = final_m
                    st.session_state.game_phase = 'PAYOUT'
                    st.rerun()

            elif bonus == "CRAZY TIME":
                st.error("🚨 **OPEN THE RED DOOR!** Choose your Flapper.")
                c1, c2, c3 = st.columns(3)
                flap = None
                if c1.button("🟢 GREEN"): flap = "GREEN"
                if c2.button("🔵 BLUE"): flap = "BLUE"
                if c3.button("🟡 YELLOW"): flap = "YELLOW"
                
                if flap:
                    st.markdown(f"You chose **{flap}**. The giant wheel spins...")
                    with st.spinner("SPINNING THE GIGANTIC WHEEL..."):
                        time.sleep(3) # Suspense massima
                    
                    # Logica Flapper: ognuno ha un risultato diverso potenzialmente
                    base_res = random.choice([50, 100, 200, 500, "DOUBLE", "TRIPLE"])
                    
                    # Simuliamo che il tuo flapper abbia preso un risultato specifico
                    if base_res in ["DOUBLE", "TRIPLE"]:
                        st.warning(f"✨ {base_res}! The wheel spins again for YOU!")
                        time.sleep(2)
                        base_res = random.choice([500, 1000, 2000])
                    
                    final_m = base_res * mult
                    st.markdown(f"<h1 style='color:red; font-size:4rem; text-align:center;'>{final_m}x</h1>", unsafe_allow_html=True)
                    time.sleep(3)
                    st.session_state.last_win_mult = final_m
                    st.session_state.game_phase = 'PAYOUT'
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)

        # ==========================================
        # SOTTO-FASE: PAYOUT & WIN
        # ==========================================
        elif st.session_state.game_phase == 'PAYOUT':
            res = st.session_state.spin_result
            bets = st.session_state.current_bets
            mult_active = st.session_state.top_slot_mult
            
            total_win = 0
            
            # Calcolo vincita Numero
            if isinstance(res, int):
                bet_amt = bets.get(res, 0)
                if bet_amt > 0:
                    # Payout = Bet + (Bet * Numero * TopSlot)
                    win = bet_amt + (bet_amt * res * mult_active)
                    total_win += win
            
            # Calcolo vincita Bonus
            elif isinstance(res, str) and 'last_win_mult' in st.session_state:
                bet_amt = bets.get(res, 0)
                if bet_amt > 0:
                    win_mult = st.session_state.last_win_mult
                    win = bet_amt + (bet_amt * win_mult)
                    total_win += win
                # Pulisci stato
                del st.session_state.last_win_mult

            # AGGIORNA SALDO
            if total_win > 0:
                st.session_state.balance += total_win
                st.balloons()
                st.markdown(f"""
                <div style='background: #004d00; padding: 30px; border-radius: 20px; text-align: center; border: 4px solid #00ff00; animation: pulse 2s infinite;'>
                    <h1 style='color: #fff; margin:0;'>YOU WON</h1>
                    <h1 style='color: #00ff00; font-size: 4rem; margin:0;'>€ {total_win:.0f}</h1>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("📉 YOU LOST. The house thanks you for your donation.")

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🔄 PLAY AGAIN", use_container_width=True, type="primary"):
                st.session_state.game_phase = 'BETTING'
                st.session_state.current_bets = {}
                st.rerun()
