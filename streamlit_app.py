import streamlit as st
import time

# 1. Configuration de la page
st.set_page_config(page_title="Time Bonus", page_icon="🎮")

# 2. Style CSS : Noir & Blanc Strict, Texte en blanc pur
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }
    
    h1, h2, h3, p, label, .stMarkdown, .stSubheader {
        color: #FFFFFF !important;
    }
    
    h1 {
        text-align: center;
        font-family: sans-serif;
        font-weight: bold;
    }

    .stCheckbox {
        background-color: #000000;
        padding: 12px;
        border-radius: 5px;
        border: 1px solid #FFFFFF;
        margin-bottom: 8px;
    }

    .stCheckbox input:checked + div {
        animation: pulse-white 1s infinite;
    }

    @keyframes pulse-white {
        0% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    .timer-display {
        font-size: 70px;
        text-align: center;
        color: #FFFFFF;
        font-family: monospace;
        padding: 20px;
        border: 1px solid #FFFFFF;
        margin: 20px 0;
    }

    .stButton > button {
        background-color: #000000;
        color: #FFFFFF;
        border: 1px solid #FFFFFF;
        width: 100%;
        border-radius: 0;
    }
    .stButton > button:hover {
        background-color: #FFFFFF;
        color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialisation de la session
if 'chrono_bonus' not in st.session_state:
    st.session_state.chrono_bonus = 0

# 3. Titre
st.markdown("<h1>TIME BONUS</h1>", unsafe_allow_html=True)

# 4. Chronomètre de Mission (À la minute près)
st.subheader("Chronometre de Mission")
st.write("Activite : Coreen")

choix_minutes = st.number_input("Choisis tes minutes :", min_value=1, max_value=30, value=10)

# Calcul du gain du chrono
if choix_minutes == 30:
    gain_potentiel = 60
else:
    gain_potentiel = choix_minutes * 2

st.write(f"Gain : {gain_potentiel} minutes de bonus")

col1, col2 = st.columns(2)
with col1:
    if st.button("DEMARRER"):
        placeholder = st.empty()
        total_seconds = choix_minutes * 60
        while total_seconds > 0:
            m, s = divmod(total_seconds, 60)
            time_str = f'{m:02d}:{s:02d}'
            placeholder.markdown(f'<div class="timer-display">{time_str}</div>', unsafe_allow_html=True)
            time.sleep(1)
            total_seconds -= 1
        st.session_state.chrono_bonus = gain_potentiel
        placeholder.markdown(f'<div class="timer-display">+{gain_potentiel} MIN</div>', unsafe_allow_html=True)
        st.balloons()

with col2:
    if st.button("RESET CHRONO"):
        st.session_state.chrono_bonus = 0
        st.rerun()

st.divider()

# 5. Daily Quests (2 min par case)
st.subheader("Daily Quests")
st.write("Chaque quete terminee = 2 minutes de bonus")

q1 = st.checkbox("Faire mon lit")
q2 = st.checkbox("Preparer mon sac et mes habits")
q3 = st.checkbox("Ranger 5 objets")
q4 = st.checkbox("Bonus-Aide Maman")

quest_bonus = (q1 + q2 + q3 + q4) * 2

# SCORE TOTAL
total_bonus = st.session_state.chrono_bonus + quest_bonus

st.markdown(f"### Ton Time Bonus total : {total_bonus} minutes")

# 6. Rapport
st.divider()
tel = "33749472959"
msg_wa = f"Maman ! J'ai fini mes missions ! J'ai gagne {total_bonus} minutes de Time Bonus."
url_wa = f"https://wa.me/{tel}?text={msg_wa.replace(' ', '%20')}"

if st.button("Envoyer mon rapport"):
    st.markdown(f"### [CLIQUE ICI POUR ENVOYER]({url_wa})")
