import streamlit as st
import datetime
import time

# 1. Configuration de la page
st.set_page_config(page_title="Time Bonus", page_icon="🎮")

# 2. Style CSS : Minimalisme Noir & Blanc avec textes de quêtes en blanc
st.markdown("""
    <style>
    /* Fond noir total et cadre blanc tout autour */
    .stApp {
        background-color: #000000;
        color: #FFFFFF; /* Texte blanc par défaut */
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }
    
    /* Titre en Blanc simple */
    h1 {
        color: #FFFFFF;
        text-align: center;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: bold;
    }
    
    .stSubheader {
        color: #FFFFFF;
    }

    /* --- Style des quêtes journalières --- */
    
    /* Style de base des cases à cocher */
    .stCheckbox {
        background-color: #1A1A1A; /* Fond légèrement plus clair pour le contraste */
        padding: 15px; /* Plus d'espace pour le texte */
        border-radius: 8px;
        border: 1px solid #FFFFFF; /* Bordure blanche pour chaque quête */
        margin-bottom: 10px;
        transition: all 0.3s ease;
    }

    /* Texte des quêtes en blanc éclatant */
    .stCheckbox > label {
        color: #FFFFFF !important; /* Force le texte en blanc pur */
        font-size: 1.2rem; /* Texte légèrement plus grand */
        font-weight: 500;
    }

    /* Icône de la case à cocher en blanc */
    .stCheckbox div[data-testid="stMarkdownContainer"] > p {
        color: #FFFFFF !important;
    }

    /* Animation quand la case est cochée */
    .stCheckbox input:checked + div {
        animation: pulse-border 1s infinite;
        border-color: #FFFFFF !important;
        box-shadow: 0 0 15px #FFFFFF;
    }

    /* Définition de l'animation de pulsation */
    @keyframes pulse-border {
        0% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(255, 255, 255, 0); }
        100% { box-shadow: 0 0 0 0 rgba(255, 255, 255, 0); }
    }

    /* --- Style du Timer --- */
    .timer-display {
        font-size: 60px;
        text-align: center;
        color: #FFFFFF;
        font-family: 'Courier New', Courier, monospace;
        padding: 20px;
        border: 2px solid #FFFFFF;
        border-radius: 10px;
        margin: 20px 0;
    }

    /* --- Style des Boutons --- */
    .stButton > button {
        background-color: #000000;
        color: #FFFFFF;
        border: 1px solid #FFFFFF;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FFFFFF;
        color: #000000;
    }
    
    /* Style spécifique pour le bouton d'envoi du rapport */
    div[data-testid="stVerticalBlock"] > div:last-child .stButton > button {
        background-color: #FFFFFF;
        color: #000000;
        border: none;
    }
    div[data-testid="stVerticalBlock"] > div:last-child .stButton > button:hover {
        background-color: #F0F0F0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Titre
st.markdown("<h1>TIME BONUS</h1>", unsafe_allow_html=True)

# 4. Le Chronomètre ajustable
st.subheader("⏱️ Chronomètre de Mission")
st.write("Choisis ton temps de mission (minutes) :")
choix_temps = st.select_slider(
    label="Temps de mission",
    options=[5, 10, 15],
    value=10,
    label_visibility="collapsed"
)

col1, col2 = st.columns(2)
with col1:
    start_button = st.button("▶️ DÉMARRER")
with col2:
    stop_button = st.button("⏹️ RESET")

if start_button:
    placeholder = st.empty()
    seconds = choix_temps * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02d}:{secs:02d}'
        placeholder.markdown(f'<div class="timer-display">{time_format}</div>', unsafe_allow_html=True)
        time.sleep(1)
        seconds -= 1
    placeholder.markdown('<div class="timer-display">MISSION ACCOMPLIE ! 🏆</div>', unsafe_allow_html=True)
    st.balloons()

st.divider()

# 5. Daily Quests (Missions du jour)
st.subheader("🎯 Daily Quests")

c1, c2 = st.columns(2)
with c1:
    q1 = st.checkbox("📚 10 min Coréen")
    q2 = st.checkbox("🦷 Brosser les dents")
    q3 = st.checkbox("🧸 Ranger ma chambre")
with c2:
    q4 = st.checkbox("🛏️ Faire mon lit")
    q5 = st.checkbox("👟 Préparer mon sac")
    q6 = st.checkbox("🎁 Bonus - Aide Maman")

# Calcul des points (Total 30)
points = (q1*10) + (q2*4) + (q3*4) + (q4*4) + (q5*4) + (q6*4)

st.write(f"### ⚡ Score Actuel : {points} / 30")

if points >= 24:
    st.success(f"GÉNIAL ! Tu as gagné {points} minutes de bonus !")

# 6. Envoi du rapport
st.divider()
mon_tel = "33749472959"
msg = f"Maman ! J'ai fini mes Daily Quests ! Score : {points} pts."
whatsapp_url = f"https://wa.me/{mon_tel}?text={msg.replace(' ', '%20')}"

if st.button("📤 Envoyer mon rapport à Maman"):
    st.markdown(f"### [CLIQUE ICI POUR ENVOYER L'ÉCRAN À MAMAN 💌]({whatsapp_url})")
