import streamlit as st
import os
import pandas as pd
import random

# ============================================
# 1. CONFIGURAZIONE FORZATA (DARK MODE)
# ============================================
config_path = os.path.expanduser("~/.streamlit/config.toml")
os.makedirs(os.path.dirname(config_path), exist_ok=True)

with open(config_path, "w") as f:
    f.write("[theme]\nbase='dark'\nprimaryColor='#8e2de2'\nbackgroundColor='#0f0c29'\nsecondaryBackgroundColor='#302b63'\ntextColor='#ffffff'\nfont='sans serif'\n")

st.set_page_config(page_title="Sdrogo Games 2025", page_icon="🔥", layout="wide", initial_sidebar_state="expanded")

# ============================================
# 2. FUNZIONI DI STILE (PER COLORARE TUTTO)
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
# 3. CSS ESTREMO (Override Totale)
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

/* Rimuovere padding fastidiosi */
.block-container { padding-top: 2rem; }

/* Input Fields Style */
div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid #8e2de2;
    color: white;
}

/* Grafici */
rect { fill: #8e2de2 !important; }

</style>
""", unsafe_allow_html=True)

# ============================================
# DATI
# ============================================
people = ["Girla", "Paci", "Marti", "Paga", "Yara", "Gaia", "Chiara", "Ele", "Ceci", "Ari", "Bax", 
          "Enry", "Bomber", "Marghe", "Eugi", "Camilla", "Lulli", "Tommaso", "Stefano", "Elisa"]

if 'votes' not in st.session_state:
    st.session_state.votes = []

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown(title_html("SDROGO HUB", "#f09819", "2rem", "900"), unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("NAVIGAZIONE", ["Main Dashboard", "Online Games Links", "Event Betting", "Lupus in Fabula"], label_visibility="collapsed")
    st.markdown("---")
    st.markdown(f"<div style='text-align:center; color:#8e2de2;'>Logged in as: <b>Guest</b></div>", unsafe_allow_html=True)

# ============================================
# SEZIONE 1: MAIN DASHBOARD
# ============================================
if menu == "Main Dashboard":
    st.markdown(gradient_text("THE MEZZENILE TAKEOVER"), unsafe_allow_html=True)
    st.markdown(f"<h2 style='color:#8e2de2; letter-spacing:5px; margin-top:-20px;'>SDROGO NEW YEAR 2025</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
    st.markdown(title_html("MEZZENILE INSIGHTS", "#f09819", "2rem"), unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(neon_text("ORIGINS"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('The Name:')} Mezzenile derives from the Latin <i>"Mesenile"</i>, indicating a central settlement. It has always been the strategic heart of the lower Val di Lanzo.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("NOBLE HISTORY"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('The Castle:')} The Francesetti Castle is the town's crown jewel. It once hosted the high aristocracy of Turin seeking mountain refuge.
        </p>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(neon_text("CRAFTSMANSHIP"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('Nail Makers:')} Mezzenile was the European capital of handmade nails. The <i>"Chiodaioli"</i> were famous for their indestructible steel creations.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("THE LEGEND"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('The Sdrogo Code:')} What happens in the mountains stays in the mountains. This is the first and only rule of the 2025 takeover.
        </p>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(neon_text("ENVIRONMENT"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('Thin Air:')} At 600m+ elevation, oxygen is lower and spirits are higher. Science says one shot here counts as two in the valley.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(neon_text("SURVIVAL"), unsafe_allow_html=True)
        st.markdown(f"""
        <p style='color:#ddd;'>
            {gold_text('The Cold:')} Don't let the fire go out. Mezzenile winters are unforgiving for those who don't keep their "hydration" levels up.
        </p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

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

# ============================================
# SEZIONE 3: EVENT BETTING
# ============================================
elif menu == "Event Betting":
    st.markdown(gradient_text("PROP BETS"), unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🗳️ VOTE NOW", "🏆 LIVE PODIUMS"])
    
    single_bets = ["The Drunkest", "First to Throw Up", "First to Fall Asleep", "First to Take a Massive Shit", "First to Mess in Kitchen", "First to Break Something"]
    pair_bets = ["First Two to Argue", "First Couple to Kiss"]

    with tab1:
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        
        # TRUCCO: Etichetta HTML personalizzata sopra, label standard nascosta
        st.markdown(title_html("WHO ARE YOU?", "#f09819", "1.2rem"), unsafe_allow_html=True)
        voter_name = st.selectbox("", ["Select your name"] + people, label_visibility="collapsed")
        
        if voter_name != "Select your name":
            current_votes = {}
            st.markdown("---")
            st.markdown(neon_text("INDIVIDUAL BETS", "1.5rem"), unsafe_allow_html=True)
            
            for bet in single_bets:
                st.markdown(f"<br>{gold_text(bet)}", unsafe_allow_html=True)
                current_votes[bet] = st.selectbox("", people, key=f"{voter_name}_{bet}", label_visibility="collapsed")
            
            st.markdown("---")
            st.markdown(neon_text("PAIR BETS (Pick 2)", "1.5rem"), unsafe_allow_html=True)
            
            for bet in pair_bets:
                st.markdown(f"<br>{gold_text(bet)}", unsafe_allow_html=True)
                # Multiselect senza etichetta nativa per evitare il bianco
                pair = st.multiselect("", people, key=f"{voter_name}_{bet}_pair", label_visibility="collapsed")
                current_votes[bet] = tuple(sorted(pair))

            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🔒 LOCK IN PREDICTIONS", use_container_width=True):
                # Validazione
                valid = True
                for bet in pair_bets:
                    if current_votes[bet] is None or len(current_votes[bet]) != 2:
                        st.error(f"⚠️ For '{bet}', you must select EXACTLY 2 people!")
                        valid = False
                
                if valid:
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
            
            st.markdown(title_html("INDIVIDUAL RANKINGS", "#f09819"), unsafe_allow_html=True)
            for bet in single_bets:
                if bet in df.columns:
                    st.markdown(f"**{bet}**")
                    counts = df[bet].value_counts().head(3).reset_index()
                    counts.columns = ['Name', 'Votes']
                    st.bar_chart(counts, x='Name', y='Votes', color="#f09819")
            
            st.markdown(title_html("PAIR RANKINGS", "#8e2de2"), unsafe_allow_html=True)
            for bet in pair_bets:
                if bet in df.columns:
                    st.markdown(f"**{bet}**")
                    valid_pairs = df[bet].dropna()
                    if not valid_pairs.empty:
                        # Converti tuple in stringhe solo se sono tuple valide
                        pair_series = valid_pairs.apply(lambda x: f"{x[0]} & {x[1]}" if isinstance(x, tuple) and len(x)==2 else None).dropna()
                        if not pair_series.empty:
                            counts = pair_series.value_counts().head(3).reset_index()
                            counts.columns = ['Couple', 'Votes']
                            st.bar_chart(counts, x='Couple', y='Votes', color="#8e2de2")

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

    if not st.session_state.game_started:
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        st.markdown(title_html("THE RULES OF MEZZENILE", "#f09819"), unsafe_allow_html=True)
        st.markdown("""
        <div style='color:white;'>
        <b>1. Setup:</b> Wolves hidden among Villagers.<br>
        <b>2. Night:</b> Special roles act in secret.<br>
        <b>3. Day:</b> Debate and execute.<br>
        <b>4. Win:</b> Villagers kill Wolves OR Wolves outnumber Villagers.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🔥 START GAME", use_container_width=True):
            roles = (["Werewolf"]*4 + ["Seer", "Doctor", "Hunter", "Witch", "Cupid"] + ["Villager"]*10)
            random.shuffle(roles)
            temp_p = people.copy()
            narrator = temp_p.pop(random.randint(0, len(temp_p)-1))
            st.session_state.narrator_name = narrator
            st.session_state.game_roles = dict(zip(temp_p, roles))
            st.session_state.players_to_reveal = temp_p
            st.session_state.game_started = True
            st.rerun()

    elif st.session_state.current_player_index < len(st.session_state.players_to_reveal):
        st.markdown(f"### Narrator: {gold_text(st.session_state.narrator_name)}", unsafe_allow_html=True)
        player = st.session_state.players_to_reveal[st.session_state.current_player_index]
        
        st.markdown(f"<div class='glass-box' style='text-align:center;'>PASS PHONE TO:<br>{gradient_text(player, '2.5rem')}</div>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        if c1.button("👁️ REVEAL"): st.session_state.show_role = True
        if c2.button("NEXT ➡️"): 
            st.session_state.current_player_index += 1
            st.session_state.show_role = False
            st.rerun()
            
        if st.session_state.show_role:
            role = st.session_state.game_roles[player]
            st.markdown(f"<div style='background:#8e2de2; padding:20px; border-radius:10px; text-align:center; color:white;'><h1>{role}</h1></div>", unsafe_allow_html=True)

    else:
        st.markdown(f"### Narrator: {gold_text(st.session_state.narrator_name)}", unsafe_allow_html=True)
        with st.expander("📜 NARRATOR SCRIPT"):
            st.markdown("""
            <b style='color:#f09819'>NIGHT:</b><br>
            1. Cupid (1st night only)<br>2. Lovers (1st night only)<br>3. Wolves<br>4. Seer<br>5. Doctor<br>6. Witch<br>
            <b style='color:#f09819'>DAY:</b><br>Reveal dead, discuss, vote.
            """, unsafe_allow_html=True)
        
        # Gestione Morti
        if 'dead_p' not in st.session_state: st.session_state.dead_p = []
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(title_html("VILLAGERS", "#00ff88"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r != "Werewolf":
                    if st.checkbox(f"{n} ({r})", key=f"d_{n}"): 
                        if n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        with c2:
            st.markdown(title_html("WOLVES", "#ff4b4b"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r == "Werewolf":
                    if st.checkbox(f"{n}", key=f"d_{n}"):
                        if n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        
        wolves_alive = sum(1 for n,r in st.session_state.game_roles.items() if r=="Werewolf" and n not in st.session_state.dead_p)
        villagers_alive = sum(1 for n,r in st.session_state.game_roles.items() if r!="Werewolf" and n not in st.session_state.dead_p)
        
        if wolves_alive == 0: 
            st.markdown("<div style='background:#00ff88; color:black; padding:20px; text-align:center;'><h1>VILLAGERS WIN</h1></div>", unsafe_allow_html=True)
        elif wolves_alive >= villagers_alive:
             st.markdown("<div style='background:#ff4b4b; color:white; padding:20px; text-align:center;'><h1>WEREWOLVES WIN</h1></div>", unsafe_allow_html=True)
             
        if st.button("RESET GAME"):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()
