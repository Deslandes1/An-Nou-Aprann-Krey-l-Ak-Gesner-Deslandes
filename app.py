import streamlit as st
import os

# ================== Page Config ==================
st.set_page_config(
    page_title="An Nou Aprann Kreyòl Ak Gesner Deslandes",
    page_icon="🇭🇹",
    layout="wide"
)

# ================== Custom Custom CSS Branding ==================
st.markdown("""
<style>
    /* Dark professional tech theme */
    .stApp { background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%); }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f3460 0%, #1a1a2e 100%);
        border-right: 2px solid #e94560;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] h2 {
        color: #ffffff !important;
    }
    
    /* Typography color overrides */
    h1, h2, h3 { color: #ffd966 !important; }
    p, li, span, .stMarkdown { color: #ffffff !important; }
    
    /* Card design for lessons */
    .lesson-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #e94560;
        margin-bottom: 25px;
    }
    
    /* Footer styling */
    .main-footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        border-top: 2px solid #e94560;
        color: #ffd966 !important;
        font-weight: bold;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ================== Interactive Book Content Data ==================
# This structure stores the exact Haitian Creole script you speak, plus accurate translations.
LESSONS_DATA = {
    "Lesson 1: Lèt È ak Lèt Ò (Accents)": {
        "video_url": "https://dl.dropboxusercontent.com/scl/fi/2boi3k2p9hm666pa5vmui/E-ak-O.mp4?rlkey=csq569rorqh25ff0bupso8nbp&st=bgct5dv1&dl=1",
        "captions": {
            "Haitian Creole (Original)": """
**Genhen 2 lèt ki pran aksan fòs nan kreyòl Ayisyen, se È ak Ò. Men 5 egzanp senp klè pou lèt sa yo:**

### 1. Lèt È
* **Enjenyè** — Enjenyè a ap travay sou kòd la.
* **Pwofesè** — Pwofesè a byen esplike leson alfabè a.
* **Tèks** — Nou mete tout aksan yo nan tèks la.
* **Frè** — Frè m nan ap ede m deplwaye lojisyèl la.
* **Lèt** — Gen 32 lèt nan alfabè Kreyòl la.

### 2. Lèt Ò
* **Lojisyèl** — Lojisyèl la ap mache san okenn erè.
* **Kòd** — Kòd pwogram nan pwòp anpil.
* **Lekòl** — Timoun yo ap aprann enfòmatik nan lekòl la.
* **Pòt** — Teknoloji kantik la louvri pòt pou lavni.
* **Kòf** — Nou sere tout dokiman yo nan kòf la.

_Enjenye Gesner Deslandes at Globalinternet.py Kompanyi lojisyel_
""",
            "English": """
**There are 2 letters that take a strong accent in Haitian Creole, which are È and Ò. Here are 5 simple, clear examples for these letters:**

### 1. The Letter È
* **Enjenyè (Engineer)** — The engineer is working on the code.
* **Pwofesè (Teacher)** — The teacher explained the alphabet lesson well.
* **Tèks (Text)** — We put all the accents in the text.
* **Frè (Brother)** — My brother is helping me deploy the software.
* **Lèt (Letter)** — There are 32 letters in the Creole alphabet.

### 2. The Letter Ò
* **Lojisyèl (Software)** — The software is running without any errors.
* **Kòd (Code)** — The program code is very clean.
* **Lekòl (School)** — The children are learning computer science at school.
* **Pòt (Door)** — Quantum technology opens doors for the future.
* **Kòf (Trunk/Safe)** — We stored all the documents in the safe.

_Engineer Gesner Deslandes at Globalinternet.py Software Company_
""",
            "Spanish": """
**Hay 2 letras que llevan un acento fuerte en el criollo haitiano, que son È y Ò. Aquí hay 5 ejemplos simples y claros para estas letras:**

### 1. La Letra È
* **Enjenyè (Ingeniero)** — El ingeniero está trabajando en el código.
* **Pwofesè (Profesor)** — El profesor explicó bien la lección del alfabeto.
* **Tèks (Texto)** — Pusimos todos los acentos en el texto.
* **Frè (Hermano)** — Mi hermano me está ayudando a implementar el software.
* **Lèt (Letra)** — Hay 32 letras en el alfabeto criollo.

### 2. La Letra Ò
* **Lojisyèl (Software)** — El software funciona sin ningún error.
* **Kòd (Código)** — El código del programa está muy limpio.
* **Lekòl (Escuela)** — Los niños están aprendiendo informática en la escuela.
* **Pòt (Puerta)** — La tecnología cuántica abre puertas para el futuro.
* **Kòf (Caja fuerte)** — Guardamos todos los documentos en la caja fuerte.

_Ingeniero Gesner Deslandes en Globalinternet.py Compañía de Software_
""",
            "French": """
**Il y a 2 lettres qui prennent un accent grave en créole haïtien, ce sont È et Ò. Voici 5 exemples simples et clairs pour ces lettres :**

### 1. La Lettre È
* **Enjenyè (Ingénieur)** — L'ingénieur travaille sur le code.
* **Pwofesè (Professeur)** — Le professeur a bien expliqué la leçon sur l'alphabet.
* **Tèks (Texte)** — Nous avons mis tous les accents dans le texte.
* **Frè (Frère)** — Mon frère m'aide à déployer le logiciel.
* **Lèt (Lettre)** — Il y a 32 lettres dans l'alphabet créole.

### 2. La Lettre Ò
* **Lojisyèl (Logiciel)** — Le logiciel fonctionne sans aucune erreur.
* **Kòd (Code)** — Le code du programme est très propre.
* **Lekòl (École)** — Les enfants apprennent l'informatique à l'école.
* **Pòt (Porte)** — La technologie quantique ouvre des portes pour l'avenir.
* **Kòf (Coffre-fort)** — Nous avons rangé tous les documents dans le coffre-fort.

_Ingénieur Gesner Deslandes chez Globalinternet.py Entreprise de Logiciels_
"""
        }
    }
    # You can quickly paste new video lessons matching this exact layout right here!
}

# ================== Sidebar Navigation & Controls ==================
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="https://raw.githubusercontent.com/Deslandes1/Haitian-Creole-Background-Music-Sound/main/Gesner%20Deslandes.png" style="border-radius: 50%; width: 110px; border: 3px solid #ffd966;">
        <h2 style="margin-top: 10px; font-size: 1.3rem;">GlobalInternet.py</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    st.header("📖 Navigation")
    selected_lesson = st.selectbox("Choose a lesson to study:", list(LESSONS_DATA.keys()))
    
    st.markdown("---")
    st.header("🌐 Book Translation")
    # Language selector handles dynamic on-the-fly text changes
    selected_language = st.selectbox(
        "Translate Lesson Text Caption into:",
        ["Haitian Creole (Original)", "English", "Spanish", "French"]
    )
    
    st.markdown("---")
    st.markdown("### 📞 Contact Author")
    st.markdown("**Enjenyè-an-Chèf:** GESNER DESLANDES")
    st.markdown("📱 (509) 4738 5663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("[Visit Website](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")

# ================== Main Window Rendering ==================
# Header with the required title and GitHub avatar setup
st.markdown("<h1 style='text-align: center; font-size: 2.8rem;'>An Nou Aprann Kreyòl Ak Gesner Deslandes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2rem; font-style: italic;'>An Interactive Audio-Visual Software Book for Mastering Haitian Creole and Modern Tech Terms</p>", unsafe_allow_html=True)

# Required structural ownership marking on the main page canvas
st.markdown(
    "<h4 style='text-align: center; color: #e94560 !important; letter-spacing: 1px;'>BUILT BY GESNER DESLANDES</h4>", 
    unsafe_allow_html=True
)
st.markdown("---")

# Layout Split: Left side runs the Video Media Player, Right side shows the Dynamic Script Card
col_video, col_text = st.columns([1.3, 1])

lesson_content = LESSONS_DATA[selected_lesson]

with col_video:
    st.markdown("### 🎬 Video Lesson Layout")
    # Streamed audio-visual array synced perfectly with Dropbox streaming headers
    st.video(lesson_content["video_url"])
    st.caption(f"Playing source container for {selected_lesson}. Media voice tracks are narrated entirely in native Haitian Creole.")

with col_text:
    st.markdown(f"### 📄 Text Caption ({selected_language})")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    
    # Renders the localized map array selected from the sidebar dynamically
    current_translation = lesson_content["captions"][selected_language]
    st.markdown(current_translation)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Mandatory persistent branding signature line at the very bottom
st.markdown('<div class="main-footer">© GlobalInternet.py – Built by GESNER DESLANDES.</div>', unsafe_allow_html=True)
