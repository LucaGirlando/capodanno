import streamlit as st
import os
import pandas as pd
import random

# ============================================
# CONFIGURAZIONE INIZIALE
# ============================================
config_path = os.path.expanduser("~/.streamlit/config.toml")
os.makedirs(os.path.dirname(config_path), exist_ok=True)

with open(config_path, "w") as f:
    f.write("[theme]\nbase='dark'\n")

st.set_page_config(
    page_title="Sdrogo Games 2025", 
    page_icon="🔥", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS COMPLETO E DEFINITIVO (SENZA TAGLI)
# ============================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Montserrat:wght@300;400;700;900&display=swap');

/* Variabili Globali */
:root {
    --primary-bg: #0f0c29;
    --accent-gold: #f09819;
    --accent-purple: #8e2de2;
    --text-white: #ffffff;
    --glass: rgba(255, 255, 255, 0.08);
}

/* 1. RESET SFONDO E TESTO GENERALE */
html, body, .stApp, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
    color: var(--text-white) !important;
    font-family: 'Montserrat', sans-serif;
}

/* Forziamo il bianco su tutti i testi e label nativi */
.stApp label, .stApp p, .stApp span, .stApp li, .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
    color: var(--text-white) !important;
}

/* 2. SIDEBAR */
[data-testid="stSidebar"] {
    background-color: rgba(15, 12, 41, 0.98) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
}
[data-testid="stSidebar"] * {
    color: var(--text-white) !important;
}

/* 3. TITOLI PRINCIPALI */
.main-title {
    font-family: 'Syncopate', sans-serif;
    font-weight: 700;
    font-size: 3.5rem;
    background: linear-gradient(90deg, var(--accent-gold), #edde5d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    display: block;
}

/* Classi per colori specifici Dashboard */
.text-gold { color: var(--accent-gold) !important; font-weight: 900 !important; }
.text-purple { color: var(--accent-purple) !important; font-weight: 900 !important; }

/* 4. GLASS CARDS */
.glass-card {
    background: var(--glass);
    padding: 2.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(15px);
    margin-bottom: 2rem;
}

/* 5. PULSANTI STREAMLIT (Submit, Start, Reset) */
.stButton > button {
    background: linear-gradient(45deg, var(--accent-purple), #4a00e0) !important;
    color: white !important;
    border: none !important;
    padding: 0.6rem 2rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    border-radius: 10px !important;
    transition: 0.3s ease !important;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 20px rgba(142, 45, 226, 0.5) !important;
}

/* 6. LINK AI GIOCHI */
.game-link-btn {
    display: block;
    padding: 1rem;
    background: linear-gradient(45deg, var(--accent-purple), #4a00e0) !important;
    color: white !important;
    text-align: center;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
    text-transform: uppercase;
}
.game-link-btn:hover {
    box-shadow: 0 0 20px rgba(142, 45, 226, 0.6);
    transform: scale(1.02);
}

/* 7. WIDGET INPUT (Selectbox, Tabs) */
div[data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.07) !important;
    color: white !important;
}
div[role="listbox"] { background-color: #1a1a1a !important; }

button[data-baseweb="tab"] p { color: rgba(255, 255, 255, 0.6) !important; }
button[aria-selected="true"] p { color: var(--accent-gold) !important; font-weight: bold !important; }

/* 8. FIX TOTALE PER I RETTANGOLI DEI GRAFICI */
/* Questa regola forza il colore Viola Neon a ogni elemento rettangolare dei grafici SVG */
rect {
    fill: #8e2de2 !important; 
}

/* Se i grafici usano percorsi invece di rettangoli */
path.mark-rect.role-mark {
    fill: #8e2de2 !important;
}

.stAlert { background-color: rgba(0, 255, 136, 0.1) !important; color: white !important; }

</style>
""", unsafe_allow_html=True)

# ============================================
# DATA & SESSION STATE
# ============================================
people = ["Girla", "Paci", "Marti", "Paga", "Yara", "Gaia", "Chiara", "Ele", "Ceci", "Ari", "Bax", 
          "Enry", "Bomber", "Marghe", "Eugi", "Camilla", "Lulli", "Tommaso", "Stefano", "Elisa"]

if 'votes' not in st.session_state:
    st.session_state.votes = []

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("<h2 style='color:#f09819;'>SDROGO HUB</h2>", unsafe_allow_html=True)
    menu = st.radio("NAVIGATION", ["Main Dashboard", "Online Games Links", "Event Betting", "Lupus in Fabula"])

# ============================================
# MAIN DASHBOARD
# ============================================
if menu == "Main Dashboard":
    st.markdown("<div class='main-title'>THE MEZZENILE TAKEOVER</div>", unsafe_allow_html=True)
    st.markdown("<h3 class='text-purple' style='letter-spacing:6px;'>SDROGO NEW YEAR 2025</h3><br>", unsafe_allow_html=True)
    
    # Layout a tre colonne per le curiosità
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='text-gold' style='border:none; margin-bottom:30px; font-family: \"Syncopate\", sans-serif;'>MEZZENILE INSIGHTS</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<h4 class='text-purple'>Origins</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>The Name:</b> Mezzenile derives from the Latin <i>"Mesenile"</i>, indicating a central settlement. It has always been the strategic heart of the lower Val di Lanzo.
            </p>""", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        
        st.markdown("<h4 class='text-gold'>Noble History</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>The Castle:</b> The Francesetti Castle is the town's crown jewel. It once hosted the high aristocracy of Turin seeking mountain refuge.
            </p>""", unsafe_allow_html=True)

    with col2:
        st.markdown("<h4 class='text-gold'>Craftsmanship</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>Nail Makers:</b> Mezzenile was the European capital of handmade nails. The <i>"Chiodaioli"</i> were famous for their indestructible steel creations.
            </p>""", unsafe_allow_html=True)
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

        st.markdown("<h4 class='text-purple'>The Legend</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>The Sdrogo Code:</b> What happens in the mountains stays in the mountains. This is the first and only rule of the 2025 takeover.
            </p>""", unsafe_allow_html=True)

    with col3:
        st.markdown("<h4 class='text-purple'>Environment</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>Thin Air:</b> At 600m+ elevation, oxygen is lower and spirits are higher. Science says one shot here counts as two in the valley.
            </p>""", unsafe_allow_html=True)
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

        st.markdown("<h4 class='text-gold'>Survival</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6;'>
                <b>The Cold:</b> Don't let the fire go out. Mezzenile winters are unforgiving for those who don't keep their "hydration" levels up.
            </p>""", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Call to action finale in basso
    st.markdown("""
        <div style='text-align: center; margin-top: 50px; opacity: 0.7;'>
            <p style='letter-spacing: 3px;'>USE THE SIDEBAR TO ACCESS THE GAMING MODULES</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================
# ONLINE GAMES LINKS
# ============================================
elif menu == "Online Games Links":
    st.markdown("<div class='main-title'>Gaming HQ</div>", unsafe_allow_html=True)
    
    # Tournament Rules
    st.markdown("""
    <div class='glass-card' style='border-left: 5px solid #8e2de2;'>
        <h2 style='color:#8e2de2; border:none; margin-bottom:15px; font-family: "Syncopate", sans-serif;'>TOURNAMENT RULES</h2>
        <div style='font-size: 1.05rem; line-height: 1.7;'>
            <p><b>The Setup:</b> Form <b>5 TEAMS of 4 players</b> each.</p>
            <p><b>The Flow:</b> Each team will play the 5 games in order. While one team competes, the others witness the performance.</p>
            <p><b>The Penalty:</b> At the end of every game round, the <b>4 LOSING TEAMS</b> must take a shot or a full glass of wine/beer.</p>
            <p><b>The Grand Finale:</b> After the final game, the <b>OVERALL WINNING TEAM</b> earns the right to choose <b>ONE PLAYER</b> from each of the other teams to take an extra penalty drink.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='text-gold' style='margin-top:40px; letter-spacing: 2px;'>THE 5 CHALLENGES</h3>", unsafe_allow_html=True)

    # Updated Games List
    games = [
        {
            "name": "TimeGuessr", 
            "url": "https://timeguessr.com/", 
            "desc": "Identify the exact year and location of historical photos. Precision is everything."
        },
        {
            "name": "FoodGuessr", 
            "url": "https://www.foodguessr.com/", 
            "desc": "A worldwide culinary hunt. Guess the country of origin based on traditional dish images."
        },
        {
            "name": "The Auction Game", 
            "url": "https://neal.fun/auction-game/", 
            "desc": "Test your luxury knowledge. Guess the actual sale price of the world's most absurd auction items."
        },
        {
            "name": "OpenGuessr", 
            "url": "https://www.openguessr.com/maps", 
            "desc": "The ultimate geography battle. Drop the pin on the map to find your location in the world."
        },
        {
            "name": "Higher or Lower", 
            "url": "https://www.higherorlowergame.com/google/", 
            "desc": "Analyze global trends. Guess which topic has the highest search volume on Google."
        }
    ]

    # Render Game Buttons
    for g in games:
        col_btn, col_txt = st.columns([1, 3])
        with col_btn:
            st.markdown(f"""
                <a href='{g['url']}' target='_blank' style='text-decoration: none;'>
                    <div class='game-link-btn' style='width: 100%; text-align: center;'>PLAY {g['name']}</div>
                </a>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown(f"""
                <div style='padding: 0.5rem 1rem;'>
                    <b style='color:#f09819; font-size: 1.1rem;'>{g['name']}</b><br>
                    <span style='color:#a0a0a0;'>{g['desc']}</span>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("<hr style='opacity: 0.1; margin: 10px 0;'>", unsafe_allow_html=True)

# ============================================
# EVENT BETTING (STATISTICS & PODIUMS)
# ============================================
elif menu == "Event Betting":
    st.markdown("<div class='main-title'>Prop Bets</div>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["VOTE NOW", "LIVE PODIUMS"])
    
    # Definiamo le domande
    single_bets = [
        "The Drunkest of the Night", 
        "First to Throw Up", 
        "First to Fall Asleep", 
        "First to Take a Massive Shit", 
        "First to Mess Up in the Kitchen", 
        "First to Break Something"
    ]
    pair_bets = [
        "First Two to Start an Argument", 
        "First Couple to Kiss in Public"
    ]

    with tab1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        voter_name = st.selectbox("Who is voting?", ["Select your name"] + people)
        
        if voter_name != "Select your name":
            current_votes = {}
            st.markdown("### Individual Predictions")
            for bet in single_bets:
                current_votes[bet] = st.selectbox(f"**{bet}:**", people, key=f"{voter_name}_{bet}")
            
            st.markdown("---")
            st.markdown("### Pair Predictions (Pick Two)")
            for bet in pair_bets:
                # Per le coppie usiamo un multiselect limitato a 2
                pair = st.multiselect(f"**{bet}:**", people, max_selections=2, key=f"{voter_name}_{bet}_pair")
                if len(pair) == 2:
                    # Ordiniamo i nomi alfabeticamente per far sì che (A,B) e (B,A) siano la stessa coppia
                    current_votes[bet] = tuple(sorted(pair))
                else:
                    current_votes[bet] = None

            if st.button("SUBMIT MY PREDICTIONS", use_container_width=True):
                if any(v is None for v in current_votes.values()):
                    st.error("Please complete all predictions (including pairs) before submitting.")
                else:
                    # Rimuoviamo voti precedenti dello stesso utente se esistono
                    st.session_state.votes = [v for v in st.session_state.votes if v.get('_voter') != voter_name]
                    current_votes['_voter'] = voter_name
                    st.session_state.votes.append(current_votes)
                    st.success(f"Predictions successfully locked in for {voter_name}!")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        if not st.session_state.votes:
            st.info("No data available. Start voting to see the podiums.")
        else:
            df = pd.DataFrame(st.session_state.votes)
            
            # --- SINGOLI ---
            st.markdown("## Individual Rankings")
            for bet in single_bets:
                st.markdown(f"#### {bet}")
                counts = df[bet].value_counts().head(3).reset_index()
                counts.columns = ['Candidate', 'Votes']
                st.bar_chart(data=counts, x='Candidate', y='Votes', color="#f09819")
                st.markdown("---")
            
            # --- COPPIE ---
            st.markdown("## Pair Rankings")
            for bet in pair_bets:
                st.markdown(f"#### {bet}")
                # Trasformiamo la tupla in stringa leggibile per il grafico
                pair_series = df[bet].dropna().apply(lambda x: f"{x[0]} & {x[1]}")
                pair_counts = pair_series.value_counts().head(3).reset_index()
                pair_counts.columns = ['Pair', 'Votes']
                st.bar_chart(data=pair_counts, x='Pair', y='Votes', color="#8e2de2")
                st.markdown("---")
            
            # --- TOTAL MVP (Most Voted Person) ---
            st.markdown("## Overall 'Sdrogo' Ranking")
            st.caption("Total number of times each person was voted across all categories")

            # Sicurezza: controlliamo che ci siano dati
            if not df.empty:
                all_names = []
                # Raccogliamo nomi dalle scommesse singole
                for col in single_bets:
                    if col in df.columns:
                        all_names.extend(df[col].dropna().tolist())
                # Raccogliamo nomi dalle scommesse di coppia
                for col in pair_bets:
                    if col in df.columns:
                        for pair in df[col].dropna():
                            all_names.extend(list(pair))

                if all_names:
                    total_counts = pd.Series(all_names).value_counts().reset_index()
                    total_counts.columns = ['Name', 'Total Votes']
                    
                    # Il CSS sopra (rect { fill: ... }) forzerà questo grafico a essere viola
                    st.bar_chart(data=total_counts, x='Name', y='Total Votes', color="#8e2de2")

# ============================================
# LUPUS IN FABULA
# ============================================
elif menu == "Lupus in Fabula":
    st.markdown("<div class='main-title'>Lupus in Fabula</div>", unsafe_allow_html=True)
    
    # Inizializzazione del gioco
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'current_player_index' not in st.session_state:
        st.session_state.current_player_index = 0
    if 'show_role' not in st.session_state:
        st.session_state.show_role = False

    # SCHERMATA INIZIALE
    if not st.session_state.game_started:
        st.markdown("""
        <div class='glass-card'>
            <h2 style='color:#f09819; border:none;'>The Rules of Mezzenile</h2>
            <p><b>1. The Setup:</b> There are Werewolves hidden among the Villagers.</p>
            <p><b>2. The Night:</b> The Narrator wakes up special roles to perform their actions in secret.</p>
            <p><b>3. The Day:</b> The town wakes up, finds out who died, and debates who to execute.</p>
            <p><b>4. Goal:</b> Villagers must kill all Wolves. Wolves must outnumber Villagers.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔥 START THE GAME", use_container_width=True):
            roles_pool = (["Werewolf"] * 4 + ["Seer", "Doctor", "Hunter", "Witch", "Cupid"] + ["Villager"] * 10)
            random.shuffle(roles_pool)
            
            # Estrazione Narratore (uno dei 20)
            narrator_idx = random.randint(0, len(people)-1)
            temp_people = people.copy()
            narrator_name = temp_people.pop(narrator_idx)
            
            st.session_state.narrator_name = narrator_name
            st.session_state.game_roles = dict(zip(temp_people, roles_pool))
            st.session_state.players_to_reveal = temp_people
            st.session_state.game_started = True
            st.rerun()

    # SCHERMATA ASSEGNAZIONE RUOLI
    elif st.session_state.current_player_index < len(st.session_state.players_to_reveal):
        st.markdown(f"### The Narrator is: <span style='color:#f09819;'>{st.session_state.narrator_name}</span>", unsafe_allow_html=True)
        
        idx = st.session_state.current_player_index
        player = st.session_state.players_to_reveal[idx]
        
        st.markdown(f"""
        <div class='glass-card' style='text-align: center;'>
            <p style='letter-spacing:2px;'>HAND THE PHONE TO:</p>
            <h1 style='color:white; border:none;'>{player.upper()}</h1>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("👁️ REVEAL ROLE", use_container_width=True):
                st.session_state.show_role = True
        
        with col2:
            if st.button("NEXT PLAYER ➡️", use_container_width=True):
                st.session_state.current_player_index += 1
                st.session_state.show_role = False
                st.rerun()

        if st.session_state.show_role:
            role = st.session_state.game_roles[player]
            descriptions = {
                "Werewolf": "Kill one villager every night with your pack. Stay hidden.",
                "Seer": "Check one player's identity every night.",
                "Doctor": "Protect one player from being killed every night.",
                "Hunter": "If you die, you can immediately kill another player of your choice.",
                "Witch": "You have ONLY TWO potions for the whole game: one to heal a victim and one to poison a player. Use them wisely!",
                "Cupid": "ONLY ON THE FIRST NIGHT, link two players: if one dies, the other dies of a broken heart.",
                "Villager": "Find the wolves and vote them out. You have no special powers."
            }
            st.markdown(f"""
            <div style='background:rgba(142, 45, 226, 0.2); padding:20px; border-radius:10px; border:1px solid #8e2de2; text-align:center;'>
                <h2 style='color:#8e2de2; border:none;'>{role.upper()}</h2>
                <p>{descriptions[role]}</p>
            </div>
            """, unsafe_allow_html=True)

    # SCHERMATA NARRATORE FINALE
    else:
        st.markdown(f"<h1>Narrator Dashboard: {st.session_state.narrator_name}</h1>", unsafe_allow_html=True)
        
        with st.expander("📜 FULL NARRATOR SCRIPT (Read Step-by-Step)"):
            st.markdown(f"""
            <div style='color:#f09819; font-weight:bold;'>--- START OF THE NIGHT ---</div>
            <p>1. <b>"Everyone, close your eyes. Night falls in Mezzenile."</b></p>
            <p>2. <b>"Cupid, wake up (FIRST NIGHT ONLY)."</b> If it's the first night: <b>"Choose two souls to link forever."</b> (Touch their shoulders). If not: <b>"Cupid, go back to sleep."</b></p>
            <p>3. <b>"The Lovers, wake up and look at each other (FIRST NIGHT ONLY). Now sleep."</b></p>
            <p>4. <b>"Werewolves, wake up. Point at your victim."</b> (Take note, then: <b>"Wolves, sleep."</b>)</p>
            <p>5. <b>"The Seer, wake up. Point at someone to inspect."</b> (Give thumbs down for Wolf, up for Villager. Then: <b>"Seer, sleep."</b>)</p>
            <p>6. <b>"The Doctor, wake up. Point at the person you want to save tonight. Doctor, sleep."</b></p>
            <p>7. <b>"The Witch, wake up. The victim is [Point]. Do you want to use your healing potion? (ONLY ONCE PER GAME). Do you want to use your poison? (ONLY ONCE PER GAME). Point at your target. Witch, sleep."</b></p>
            <div style='color:#f09819; font-weight:bold;'>--- DAWN ---</div>
            <p>8. <b>"Sun rises! Everyone open your eyes."</b></p>
            <p>9. <b>"Last night, the person who died is... [Name/No one]."</b></p>
            <p>10. <b>"Villagers, you have 5 minutes to discuss and vote someone to be executed."</b></p>
            """, unsafe_allow_html=True)

        st.markdown("### 💀 Graveyard & Live Roster")
        
        if 'dead_players' not in st.session_state:
            st.session_state.dead_players = []

        col_good, col_evil = st.columns(2)
        
        with col_good:
            st.markdown("<h4 style='color:#00ff88;'>THE INNOCENTS</h4>", unsafe_allow_html=True)
            for name, role in st.session_state.game_roles.items():
                if role != "Werewolf":
                    is_dead = st.checkbox(f"Eliminate {name} ({role})", key=f"dead_{name}")
                    if is_dead and name not in st.session_state.dead_players:
                        st.session_state.dead_players.append(name)
                    elif not is_dead and name in st.session_state.dead_players:
                        st.session_state.dead_players.remove(name)

        with col_evil:
            st.markdown("<h4 style='color:#ff4b4b;'>THE WEREWOLVES</h4>", unsafe_allow_html=True)
            for name, role in st.session_state.game_roles.items():
                if role == "Werewolf":
                    is_dead = st.checkbox(f"Eliminate {name}", key=f"dead_{name}")
                    if is_dead and name not in st.session_state.dead_players:
                        st.session_state.dead_players.append(name)
                    elif not is_dead and name in st.session_state.dead_players:
                        st.session_state.dead_players.remove(name)

        alive_villagers = [n for n, r in st.session_state.game_roles.items() if r != "Werewolf" and n not in st.session_state.dead_players]
        alive_wolves = [n for n, r in st.session_state.game_roles.items() if r == "Werewolf" and n not in st.session_state.dead_players]

        st.markdown("---")
        
        if len(alive_wolves) == 0:
            st.balloons()
            st.markdown("""
            <div style='background-color:#00ff88; padding:30px; border-radius:15px; text-align:center;'>
                <h1 style='color:black; border:none;'>VILLAGERS WIN!</h1>
            </div>
            """, unsafe_allow_html=True)
            
        elif len(alive_wolves) >= len(alive_villagers):
            st.markdown("""
            <div style='background-color:#ff4b4b; padding:30px; border-radius:15px; text-align:center;'>
                <h1 style='color:white; border:none;'>WEREWOLVES WIN!</h1>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔄 RESET ENTIRE GAME"):
            for key in list(st.session_state.keys()):
                if key.startswith("dead_") or key in ['game_started', 'current_player_index', 'dead_players', 'game_roles', 'narrator_name', 'players_to_reveal', 'show_role']:
                    del st.session_state[key]
            st.rerun()
