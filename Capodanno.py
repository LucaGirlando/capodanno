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
div[data-baseweb="select"] > div, div[data-baseweb="base-input"] {
    background-color: rgba(255, 255, 255, 0.1);
    border: 1px solid #8e2de2;
    color: white;
}

/* Grafici */
rect { fill: #8e2de2 !important; }

/* Messaggi */
.stAlert { background-color: rgba(0, 0, 0, 0.5) !important; color: white !important; }

</style>
""", unsafe_allow_html=True)

# ============================================
# DATI & COSTANTI
# ============================================
people = ["Girla", "Paci", "Marti", "Paga", "Yara", "Gaia", "Chiara", "Ele", "Ceci", "Ari", "Bax", 
          "Enry", "Bomber", "Marghe", "Eugi", "Camilla", "Lulli", "Tommaso", "Stefano", "Elisa"]

role_descriptions = {
    "Werewolf": "🐺 <b>THE BAD GUY.</b> Every night, wake up with the other wolves and choose a victim to kill. Try to act like a villager during the day.",
    "Seer": "🔮 <b>THE INVESTIGATOR.</b> Every night, point at one player to reveal their true identity (Wolf or Villager). Keep this info secret or use it wisely.",
    "Doctor": "💉 <b>THE SAVIOR.</b> Every night, choose one player to protect. If the wolves attack them, they survive.",
    "Hunter": "🔫 <b>THE AVENGER.</b> If you are killed (by wolves or vote), you have 3 seconds to shoot (eliminate) another player immediately.",
    "Witch": "🧪 <b>THE ALCHEMIST.</b> You have TWO potions for the whole game. One to HEAL a victim, one to KILL anyone. Use them anytime at night.",
    "Cupid": "💘 <b>THE MATCHMAKER.</b> ONLY on the first night, choose two players to be Lovers. If one dies, the other dies of heartbreak.",
    "Villager": "🧑‍🌾 <b>THE MOB.</b> You have no powers. Sleep at night, wake up, and try to figure out who is lying. Vote to kill the wolves."
}

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
                pair = st.multiselect("", people, key=f"{voter_name}_{bet}_pair", label_visibility="collapsed")
                current_votes[bet] = tuple(sorted(pair))

            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("🔒 LOCK IN PREDICTIONS", use_container_width=True):
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
        
        st.markdown(f"""
        <div style='color:white; line-height:1.6;'>
            <p><b>1. THE GOAL:</b> Villagers must kill all Wolves. Wolves must kill enough Villagers to outnumber them.</p>
            <p><b>2. THE FLOW:</b>
                <ul>
                    <li><b>Night:</b> Everyone closes eyes. Narrator wakes up special roles one by one. Wolves kill.</li>
                    <li><b>Day:</b> Everyone wakes up. Deaths are announced. Debate ensues. One person is voted to be executed.</li>
                </ul>
            </p>
            <hr style='border-color:#8e2de2'>
            <h3 style='color:#8e2de2'>THE ROLES</h3>
            <ul>
                <li>🐺 <b>Werewolf:</b> Kills at night. Deceives by day.</li>
                <li>🔮 <b>Seer:</b> Checks one player's card every night.</li>
                <li>💉 <b>Doctor:</b> Saves one player from death every night.</li>
                <li>🔫 <b>Hunter:</b> If killed, shoots someone else instantly.</li>
                <li>🧪 <b>Witch:</b> Has 1 Heal Potion and 1 Kill Potion.</li>
                <li>💘 <b>Cupid:</b> Links two lovers on Night 1.</li>
                <li>🧑‍🌾 <b>Villager:</b> Just votes. No powers.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        if st.button("🔥 START THE GAME (ASSIGN ROLES)", use_container_width=True):
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
            role = st.session_state.game_roles[player]
            desc = role_descriptions.get(role, "")
            st.markdown(f"""
            <div style='background:rgba(142, 45, 226, 0.2); padding:20px; border-radius:10px; border:2px solid #8e2de2; text-align:center; margin-top:10px;'>
                <h1 style='color:#f09819; margin:0;'>{role.upper()}</h1>
                <p style='color:white; font-size:1.1rem; margin-top:10px;'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.markdown(f"""
        <div style='text-align:center; margin-bottom:30px;'>
            <span style='color:white; font-size:1.5rem;'>Narrator Dashboard:</span><br>
            <span style='color:#f09819; font-size:3rem; font-weight:900;'>{st.session_state.narrator_name}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # SCRIPT CORRETTO: STRUTTURA HTML SEMPLICE PER EVITARE BUG
        with st.expander("📜 OPEN FULL NARRATOR SCRIPT (STEP-BY-STEP)", expanded=True):
            st.markdown("""
            <h3 style='color:#8e2de2; margin-top:0;'>🌙 THE NIGHT PHASE</h3>
            <ol style='color:white; font-size:1rem; line-height:1.6;'>
                <li><b>"Everyone, close your eyes! Night falls on Mezzenile."</b></li>
                <li><b>"Cupid, wake up."</b> (Night 1 Only). Choose lovers. <b>"Cupid, sleep."</b></li>
                <li><b>"Lovers, wake up."</b> (Night 1 Only). Look at each other. <b>"Sleep."</b></li>
                <li><b>"Werewolves, wake up."</b> Choose victim. <b>"Wolves, sleep."</b></li>
                <li><b>"Seer, wake up."</b> Inspect one person. <b>"Seer, sleep."</b></li>
                <li><b>"Doctor, wake up."</b> Protect one person. <b>"Doctor, sleep."</b></li>
                <li><b>"Witch, wake up."</b> Show victim. Heal? Kill? <b>"Witch, sleep."</b></li>
            </ol>
            <h3 style='color:#f09819;'>☀️ THE DAY PHASE</h3>
            <ol start='8' style='color:white; font-size:1rem; line-height:1.6;'>
                <li><b>"Everybody wake up!"</b></li>
                <li>Announce the dead (or "Nobody died").</li>
                <li>If Hunter died: <b>"Hunter, shoot someone immediately."</b></li>
                <li><b>"Town, debate! Find the wolves!"</b> (5 mins).</li>
                <li><b>"3... 2... 1... VOTE!"</b> Execute the majority.</li>
            </ol>
            """, unsafe_allow_html=True)
        
        st.markdown("### 💀 GRAVEYARD & ALIVE PLAYERS")
        
        if 'dead_p' not in st.session_state: st.session_state.dead_p = []
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(title_html("VILLAGERS (GOOD)", "#00ff88"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r != "Werewolf":
                    is_dead = st.checkbox(f"{n} ({r})", key=f"d_{n}")
                    if is_dead and n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif not is_dead and n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        with c2:
            st.markdown(title_html("WOLVES (EVIL)", "#ff4b4b"), unsafe_allow_html=True)
            for n, r in st.session_state.game_roles.items():
                if r == "Werewolf":
                    is_dead = st.checkbox(f"{n}", key=f"d_{n}")
                    if is_dead and n not in st.session_state.dead_p: st.session_state.dead_p.append(n)
                    elif not is_dead and n in st.session_state.dead_p: st.session_state.dead_p.remove(n)
        
        wolves_alive = sum(1 for n,r in st.session_state.game_roles.items() if r=="Werewolf" and n not in st.session_state.dead_p)
        villagers_alive = sum(1 for n,r in st.session_state.game_roles.items() if r!="Werewolf" and n not in st.session_state.dead_p)
        
        st.markdown("---")
        if wolves_alive == 0: 
            st.markdown("<div style='background:#00ff88; color:black; padding:20px; text-align:center; border-radius:15px;'><h1>🎉 VILLAGERS WIN! 🎉</h1></div>", unsafe_allow_html=True)
        elif wolves_alive >= villagers_alive:
             st.markdown("<div style='background:#ff4b4b; color:white; padding:20px; text-align:center; border-radius:15px;'><h1>🐺 WEREWOLVES WIN! 🐺</h1></div>", unsafe_allow_html=True)
             
        if st.button("🔄 RESET GAME"):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()
