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
# CSS "BLINDATO"
# ============================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Montserrat:wght@300;400;700;900&display=swap');

/* 1. SFONDO SCURO */
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%) !important;
    color: white !important;
    font-family: 'Montserrat', sans-serif;
}

/* 2. TESTI GENERICI BIANCHI (Default) */
p, label, span, li, div {
    color: white;
}

/* 3. SIDEBAR */
[data-testid="stSidebar"] {
    background-color: rgba(15, 12, 41, 0.98) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* 4. TITOLI PRINCIPALI */
.main-title {
    font-family: 'Syncopate', sans-serif;
    font-weight: 700;
    font-size: 3.5rem;
    background: linear-gradient(90deg, #f09819, #edde5d);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    display: block;
}

/* 5. GLASS CARDS */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 2.5rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(15px);
    margin-bottom: 2rem;
}

/* 6. PULSANTI */
.stButton > button {
    background: linear-gradient(45deg, #8e2de2, #4a00e0) !important;
    color: white !important;
    border: none !important;
    padding: 0.6rem 2rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    border-radius: 10px !important;
}
.stButton > button:hover {
    box-shadow: 0 0 15px rgba(142, 45, 226, 0.8) !important;
    transform: scale(1.02);
}

/* 7. LINK AI GIOCHI */
.game-link-btn {
    display: block;
    padding: 1rem;
    background: linear-gradient(45deg, #8e2de2, #4a00e0) !important;
    color: white !important;
    text-align: center;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
    text-transform: uppercase;
}

/* 8. WIDGET INPUT */
div[data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.1) !important;
    color: white !important;
}
div[role="listbox"] { background-color: #1a1a1a !important; }

/* 9. GRAFICI VIOLA */
rect { fill: #8e2de2 !important; }

/* Messaggi errore/successo */
.stAlert { background-color: rgba(0, 0, 0, 0.5) !important; color: white !important; }
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
    # Colori forzati inline
    st.markdown("<h2 style='color:#f09819 !important; font-weight:900;'>SDROGO HUB</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#8e2de2 !important; font-size:0.9rem;'>NAVIGATION</h4>", unsafe_allow_html=True)
    menu = st.radio("", ["Main Dashboard", "Online Games Links", "Event Betting", "Lupus in Fabula"], label_visibility="collapsed")

# ============================================
# MAIN DASHBOARD
# ============================================
if menu == "Main Dashboard":
    st.markdown("<div class='main-title'>THE MEZZENILE TAKEOVER</div>", unsafe_allow_html=True)
    # COLORE FORZATO: VIOLA
    st.markdown("<h3 style='color:#8e2de2 !important; font-weight:900; letter-spacing:6px; margin-top:0;'>SDROGO NEW YEAR 2025</h3><br>", unsafe_allow_html=True)
    
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    # COLORE FORZATO: ORO
    st.markdown("<h2 style='color:#f09819 !important; border:none; margin-bottom:30px; font-family: \"Syncopate\", sans-serif;'>MEZZENILE INSIGHTS</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # In ogni blocco qui sotto, i colori sono scritti direttamente nel tag HTML
    with col1:
        st.markdown("<h4 style='color:#8e2de2 !important; font-weight:bold;'>Origins</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#f09819 !important;'>The Name:</b> Mezzenile derives from the Latin <i>"Mesenile"</i>, indicating a central settlement. It has always been the strategic heart of the lower Val di Lanzo.
            </p>""", unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
        
        st.markdown("<h4 style='color:#f09819 !important; font-weight:bold;'>Noble History</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#8e2de2 !important;'>The Castle:</b> The Francesetti Castle is the town's crown jewel. It once hosted the high aristocracy of Turin seeking mountain refuge.
            </p>""", unsafe_allow_html=True)

    with col2:
        st.markdown("<h4 style='color:#f09819 !important; font-weight:bold;'>Craftsmanship</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#8e2de2 !important;'>Nail Makers:</b> Mezzenile was the European capital of handmade nails. The <i>"Chiodaioli"</i> were famous for their indestructible steel creations.
            </p>""", unsafe_allow_html=True)
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

        st.markdown("<h4 style='color:#8e2de2 !important; font-weight:bold;'>The Legend</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#f09819 !important;'>The Sdrogo Code:</b> What happens in the mountains stays in the mountains. This is the first and only rule of the 2025 takeover.
            </p>""", unsafe_allow_html=True)

    with col3:
        st.markdown("<h4 style='color:#8e2de2 !important; font-weight:bold;'>Environment</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#f09819 !important;'>Thin Air:</b> At 600m+ elevation, oxygen is lower and spirits are higher. Science says one shot here counts as two in the valley.
            </p>""", unsafe_allow_html=True)
            
        st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

        st.markdown("<h4 style='color:#f09819 !important; font-weight:bold;'>Survival</h4>", unsafe_allow_html=True)
        st.markdown("""
            <p style='font-size: 0.95rem; line-height: 1.6; color:white !important;'>
                <b style='color:#8e2de2 !important;'>The Cold:</b> Don't let the fire go out. Mezzenile winters are unforgiving for those who don't keep their "hydration" levels up.
            </p>""", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='text-align: center; margin-top: 50px; opacity: 0.7;'>
            <p style='letter-spacing: 3px; color:#cccccc !important;'>USE THE SIDEBAR TO ACCESS THE GAMING MODULES</p>
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
        <h2 style='color:#8e2de2 !important; border:none; margin-bottom:15px; font-family: "Syncopate", sans-serif;'>TOURNAMENT RULES</h2>
        <div style='font-size: 1.05rem; line-height: 1.7; color:white !important;'>
            <p><b style='color:#f09819 !important;'>The Setup:</b> Form <b>5 TEAMS of 4 players</b> each.</p>
            <p><b style='color:#f09819 !important;'>The Flow:</b> Each team will play the 5 games in order. While one team competes, the others witness the performance.</p>
            <p><b style='color:#f09819 !important;'>The Penalty:</b> At the end of every game round, the <b>4 LOSING TEAMS</b> must take a shot or a full glass of wine/beer.</p>
            <p><b style='color:#f09819 !important;'>The Grand Finale:</b> After the final game, the <b>OVERALL WINNING TEAM</b> earns the right to choose <b>ONE PLAYER</b> from each of the other teams to take an extra penalty drink.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 style='color:#f09819 !important; margin-top:40px; letter-spacing: 2px;'>THE 5 CHALLENGES</h3>", unsafe_allow_html=True)

    games = [
        {"name": "TimeGuessr", "url": "https://timeguessr.com/", "desc": "Identify the exact year and location of historical photos."},
        {"name": "FoodGuessr", "url": "https://www.foodguessr.com/", "desc": "A worldwide culinary hunt. Guess the country of origin."},
        {"name": "The Auction Game", "url": "https://neal.fun/auction-game/", "desc": "Guess the sale price of absurd auction items."},
        {"name": "OpenGuessr", "url": "https://www.openguessr.com/maps", "desc": "The ultimate geography battle. Drop the pin."},
        {"name": "Higher or Lower", "url": "https://www.higherorlowergame.com/google/", "desc": "Guess which topic has more Google searches."}
    ]

    for g in games:
        col_btn, col_txt = st.columns([1, 3])
        with col_btn:
            st.markdown(f"""
                <a href='{g['url']}' target='_blank' style='text-decoration: none;'>
                    <div class='game-link-btn'>PLAY {g['name']}</div>
                </a>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown(f"""
                <div style='padding: 0.5rem 1rem;'>
                    <b style='color:#f09819 !important; font-size: 1.1rem;'>{g['name']}</b><br>
                    <span style='color:#cccccc !important;'>{g['desc']}</span>
                </div>
            """, unsafe_allow_html=True)
        st.markdown("<hr style='opacity: 0.1; margin: 10px 0;'>", unsafe_allow_html=True)

# ============================================
# EVENT BETTING
# ============================================
elif menu == "Event Betting":
    st.markdown("<div class='main-title'>Prop Bets</div>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["VOTE NOW", "LIVE PODIUMS"])
    
    single_bets = [
        "The Drunkest of the Night", "First to Throw Up", "First to Fall Asleep", 
        "First to Take a Massive Shit", "First to Mess Up in the Kitchen", "First to Break Something"
    ]
    pair_bets = [
        "First Two to Start an Argument", "First Couple to Kiss in Public"
    ]

    with tab1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        voter_name = st.selectbox("Who is voting?", ["Select your name"] + people)
        
        if voter_name != "Select your name":
            current_votes = {}
            st.markdown("<h3 style='color:#f09819 !important;'>Individual Predictions</h3>", unsafe_allow_html=True)
            for bet in single_bets:
                current_votes[bet] = st.selectbox(f"**{bet}:**", people, key=f"{voter_name}_{bet}")
            
            st.markdown("---")
            st.markdown("<h3 style='color:#8e2de2 !important;'>Pair Predictions (Pick Two)</h3>", unsafe_allow_html=True)
            
            for bet in pair_bets:
                # FIX: Rimosso 'max_selections' e i controlli immediati. Nessun errore mentre selezioni.
                pair = st.multiselect(f"**{bet}:**", people, key=f"{voter_name}_{bet}_pair")
                
                # Salviamo sempre, controlliamo il numero solo al submit
                current_votes[bet] = tuple(sorted(pair))

            if st.button("SUBMIT MY PREDICTIONS", use_container_width=True):
                # Validazione
                errors = []
                for bet in pair_bets:
                    if len(current_votes[bet]) != 2:
                        errors.append(bet)
                
                if errors:
                    st.error(f"⚠️ Error: You must pick exactly 2 people for: {', '.join(errors)}")
                else:
                    # Se tutto ok
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
            
            # Rankings Singoli
            st.markdown("<h2 style='color:#f09819 !important;'>Individual Rankings</h2>", unsafe_allow_html=True)
            for bet in single_bets:
                st.markdown(f"#### {bet}")
                if bet in df.columns:
                    counts = df[bet].value_counts().head(3).reset_index()
                    counts.columns = ['Candidate', 'Votes']
                    st.bar_chart(data=counts, x='Candidate', y='Votes', color="#f09819")
                st.markdown("---")
            
            # Rankings Coppie
            st.markdown("<h2 style='color:#8e2de2 !important;'>Pair Rankings</h2>", unsafe_allow_html=True)
            for bet in pair_bets:
                st.markdown(f"#### {bet}")
                if bet in df.columns:
                    # Controllo che sia una tupla valida di 2 elementi prima di formattare
                    valid_pairs = df[bet].dropna()
                    if not valid_pairs.empty:
                        pair_series = valid_pairs.apply(lambda x: f"{x[0]} & {x[1]}" if isinstance(x, tuple) and len(x)==2 else None).dropna()
                        pair_counts = pair_series.value_counts().head(3).reset_index()
                        pair_counts.columns = ['Pair', 'Votes']
                        st.bar_chart(data=pair_counts, x='Pair', y='Votes', color="#8e2de2")
                st.markdown("---")
            
            # Overall Ranking
            st.markdown("<h2 style='color:#ffffff !important;'>Overall 'Sdrogo' Ranking</h2>", unsafe_allow_html=True)
            
            if not df.empty:
                all_names = []
                # Raccogli nomi dai singoli
                for col in single_bets:
                    if col in df.columns:
                        all_names.extend(df[col].dropna().tolist())
                # Raccogli nomi dalle coppie
                for col in pair_bets:
                    if col in df.columns:
                        for pair in df[col].dropna():
                            if isinstance(pair, tuple):
                                all_names.extend(list(pair))

                if all_names:
                    total_counts = pd.Series(all_names).value_counts().reset_index()
                    total_counts.columns = ['Name', 'Total Votes']
                    # Grafico finale (forzato viola dal CSS rect { fill: #8e2de2 })
                    st.bar_chart(data=total_counts, x='Name', y='Total Votes', color="#8e2de2")

# ============================================
# LUPUS IN FABULA
# ============================================
elif menu == "Lupus in Fabula":
    st.markdown("<div class='main-title'>Lupus in Fabula</div>", unsafe_allow_html=True)
    
    if 'game_started' not in st.session_state:
        st.session_state.game_started = False
    if 'current_player_index' not in st.session_state:
        st.session_state.current_player_index = 0
    if 'show_role' not in st.session_state:
        st.session_state.show_role = False

    if not st.session_state.game_started:
        st.markdown("""
        <div class='glass-card'>
            <h2 style='color:#f09819 !important; border:none;'>The Rules of Mezzenile</h2>
            <p style='color:white !important;'><b>1. The Setup:</b> There are Werewolves hidden among the Villagers.</p>
            <p style='color:white !important;'><b>2. The Night:</b> The Narrator wakes up special roles to perform their actions in secret.</p>
            <p style='color:white !important;'><b>3. The Day:</b> The town wakes up, finds out who died, and debates who to execute.</p>
            <p style='color:white !important;'><b>4. Goal:</b> Villagers must kill all Wolves. Wolves must outnumber Villagers.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔥 START THE GAME", use_container_width=True):
            roles_pool = (["Werewolf"] * 4 + ["Seer", "Doctor", "Hunter", "Witch", "Cupid"] + ["Villager"] * 10)
            random.shuffle(roles_pool)
            
            narrator_idx = random.randint(0, len(people)-1)
            temp_people = people.copy()
            narrator_name = temp_people.pop(narrator_idx)
            
            st.session_state.narrator_name = narrator_name
            st.session_state.game_roles = dict(zip(temp_people, roles_pool))
            st.session_state.players_to_reveal = temp_people
            st.session_state.game_started = True
            st.rerun()

    elif st.session_state.current_player_index < len(st.session_state.players_to_reveal):
        st.markdown(f"### The Narrator is: <span style='color:#f09819 !important;'>{st.session_state.narrator_name}</span>", unsafe_allow_html=True)
        
        idx = st.session_state.current_player_index
        player = st.session_state.players_to_reveal[idx]
        
        st.markdown(f"""
        <div class='glass-card' style='text-align: center;'>
            <p style='letter-spacing:2px; color:white !important;'>HAND THE PHONE TO:</p>
            <h1 style='color:white !important; border:none;'>{player.upper()}</h1>
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
                <h2 style='color:#8e2de2 !important; border:none;'>{role.upper()}</h2>
                <p style='color:white !important;'>{descriptions[role]}</p>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown(f"<h1>Narrator Dashboard: {st.session_state.narrator_name}</h1>", unsafe_allow_html=True)
        
        with st.expander("📜 FULL NARRATOR SCRIPT (Read Step-by-Step)"):
            st.markdown(f"""
            <div style='color:#f09819 !important; font-weight:bold;'>--- START OF THE NIGHT ---</div>
            <p style='color:white !important;'>1. <b>"Everyone, close your eyes. Night falls in Mezzenile."</b></p>
            <p style='color:white !important;'>2. <b>"Cupid, wake up (FIRST NIGHT ONLY)."</b> If it's the first night: <b>"Choose two souls to link forever."</b> (Touch their shoulders). If not: <b>"Cupid, go back to sleep."</b></p>
            <p style='color:white !important;'>3. <b>"The Lovers, wake up and look at each other (FIRST NIGHT ONLY). Now sleep."</b></p>
            <p style='color:white !important;'>4. <b>"Werewolves, wake up. Point at your victim."</b> (Take note, then: <b>"Wolves, sleep."</b>)</p>
            <p style='color:white !important;'>5. <b>"The Seer, wake up. Point at someone to inspect."</b> (Give thumbs down for Wolf, up for Villager. Then: <b>"Seer, sleep."</b>)</p>
            <p style='color:white !important;'>6. <b>"The Doctor, wake up. Point at the person you want to save tonight. Doctor, sleep."</b></p>
            <p style='color:white !important;'>7. <b>"The Witch, wake up. The victim is [Point]. Do you want to use your healing potion? (ONLY ONCE PER GAME). Do you want to use your poison? (ONLY ONCE PER GAME). Point at your target. Witch, sleep."</b></p>
            <div style='color:#f09819 !important; font-weight:bold;'>--- DAWN ---</div>
            <p style='color:white !important;'>8. <b>"Sun rises! Everyone open your eyes."</b></p>
            <p style='color:white !important;'>9. <b>"Last night, the person who died is... [Name/No one]."</b></p>
            <p style='color:white !important;'>10. <b>"Villagers, you have 5 minutes to discuss and vote someone to be executed."</b></p>
            """, unsafe_allow_html=True)

        st.markdown("### 💀 Graveyard & Live Roster")
        
        if 'dead_players' not in st.session_state:
            st.session_state.dead_players = []

        col_good, col_evil = st.columns(2)
        
        with col_good:
            st.markdown("<h4 style='color:#00ff88 !important;'>THE INNOCENTS</h4>", unsafe_allow_html=True)
            for name, role in st.session_state.game_roles.items():
                if role != "Werewolf":
                    is_dead = st.checkbox(f"Eliminate {name} ({role})", key=f"dead_{name}")
                    if is_dead and name not in st.session_state.dead_players:
                        st.session_state.dead_players.append(name)
                    elif not is_dead and name in st.session_state.dead_players:
                        st.session_state.dead_players.remove(name)

        with col_evil:
            st.markdown("<h4 style='color:#ff4b4b !important;'>THE WEREWOLVES</h4>", unsafe_allow_html=True)
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
                <h1 style='color:black !important; border:none;'>VILLAGERS WIN!</h1>
            </div>
            """, unsafe_allow_html=True)
            
        elif len(alive_wolves) >= len(alive_villagers):
            st.markdown("""
            <div style='background-color:#ff4b4b; padding:30px; border-radius:15px; text-align:center;'>
                <h1 style='color:white !important; border:none;'>WEREWOLVES WIN!</h1>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔄 RESET ENTIRE GAME"):
            for key in list(st.session_state.keys()):
                if key.startswith("dead_") or key in ['game_started', 'current_player_index', 'dead_players', 'game_roles', 'narrator_name', 'players_to_reveal', 'show_role']:
                    del st.session_state[key]
            st.rerun()
