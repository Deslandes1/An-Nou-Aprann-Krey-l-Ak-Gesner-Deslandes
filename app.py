import streamlit as st
import os

# ================== Page Config ==================
st.set_page_config(
    page_title="An Nou Aprann Kreyòl Ak Gesner Deslandes",
    page_icon="🇭🇹",
    layout="wide"
)

# ================== Custom CSS (Light Purple Theme & Layout) ==================
st.markdown("""
<style>
    /* Entire app background set to a beautiful light purple */
    .stApp, [data-testid="stSidebar"] {
        background-color: #E6E6FA !important; /* Lavender / Light Purple */
    }
    
    /* Sidebar specific styling adjusting elements over light purple */
    [data-testid="stSidebar"] {
        border-right: 3px solid #8A2BE2;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] label, [data-testid="stSidebar"] h2 {
        color: #333333 !important;
    }
    
    /* Clean Dark Typography for high readability over light background */
    h1, h2, h3, h4 { color: #4B0082 !important; } /* Indigo accents */
    p, li, span, .stMarkdown { color: #111111 !important; }
    
    /* Clean White-Glass Lesson Cards */
    .lesson-card {
        background: rgba(255, 255, 255, 0.75);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #8A2BE2; /* Deep purple indicator bar */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 25px;
    }
    
    /* Custom alignment wrapper for Title & Profile Image */
    .title-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-bottom: 5px;
    }
    .title-container h1 {
        margin: 0 !important;
        padding: 0 !important;
    }
    .title-avatar {
        border-radius: 50%;
        width: 75px;
        height: 75px;
        border: 3px solid #8A2BE2;
        object-fit: cover;
    }
    
    /* Footer styling */
    .main-footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem;
        border-top: 2px solid #8A2BE2;
        color: #4B0082 !important;
        font-weight: bold;
        font-size: 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# ================== GitHub Profile Picture Link ==================
GITHUB_AVATAR_URL = "https://github.com/Deslandes1.png"

# ================== Interactive Book Content Data ==================
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
    },
    "Lesson 2: Alfabè Kreyòl la (The 32 Letters)": {
        "video_url": "https://dl.dropboxusercontent.com/scl/fi/7l45fvh05k2v5006b5mff/Alfabe.mp4?rlkey=vqy884w582npt3bypm5068lq8&st=alfb1&dl=1",
        "captions": {
            "Haitian Creole (Original)": """
**Alfabè Kreyòl Ayisyen an genyen 32 lèt ladan li. Chak lèt gen yon sèl son inik. Ann aprann yo ansanm:**

### Vwayèl ak Konsòn Prensipal yo
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* Gen vwayèl nan nen tou: **AN, EN, ON, OUN**.

### Egzanp teknik:
* **Klavye** — Timoun yo ap manyen klavye a pou aprann lèt yo.
* **Lojisyèl** — Nou devlope lojisyèl sa a pou edike pwochen jenerasyon an.

_Konpayi Teknoloji ak Edikasyon: GlobalInternet.py_
""",
            "English": """
**The Haitian Creole Alphabet contains 32 letters. Each letter has a single unique sound. Let's learn them together:**

### Main Vowels and Consonants
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* There are also nasal vowels: **AN, EN, ON, OUN**.

### Technical Examples:
* **Klavye (Keyboard)** — The children are handling the keyboard to learn the letters.
* **Lojisyèl (Software)** — We developed this software to educate the next generation.

_Technology and Education Company: GlobalInternet.py_
""",
            "Spanish": """
**El alfabeto criollo haitiano contiene 32 letras. Cada letra tiene un único sonido. Aprendámoslas juntos:**

### Vocales y Consonantes Principales
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* También hay vocales nasales: **AN, EN, ON, OUN**.

### Ejemplos Técnicos:
* **Klavye (Teclado)** — Los niños están manejando el teclado para aprender las letras.
* **Lojisyèl (Software)** — Desarrollamos este software para educar a la próxima generación.

_Compañía de Tecnología y Educación: GlobalInternet.py_
""",
            "French": """
**L'alphabet créole haïtien contient 32 lettres. Chaque lettre a un son unique. Apprenons-les ensemble :**

### Voyelles et Consonnes Principales
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* Il y a aussi des voyelles nasales : **AN, EN, ON, OUN**.

### Exemples Techniques :
* **Klavye (Clavier)** — Les enfants manipulent le clavier pour apprendre les lettres.
* **Lojisyèl (Logiciel)** — Nous avons développé ce logiciel pour éduquer la prochaine génération.

_Entreprise de Technologie et d'Éducation : GlobalInternet.py_
"""
        }
    },
    "Lesson 3: Vwayèl nan Nen yo (Nasal Vowels)": {
        "video_url": "https://dl.dropboxusercontent.com/scl/fi/9u50h0k2vqm8104b5fnn/VwayelNen.mp4?rlkey=nx98124b89qpmc601b5nnrt&st=nasal1&dl=1",
        "captions": {
            "Haitian Creole (Original)": """
**Vwayèl nan nen yo enpòtan anpil pou chanje sans mo yo nan lang kreyòl la. Ann pratik:**

### 4 Vwayèl nan Nen yo:
1. **AN** — Chanje, Manman, Tan.
2. **EN** — Enjenyè, Pwogramasyon, Chyen.
3. **ON** — Bon, Kompanyi, Timoun.
4. **OUN** — Kouzen, Pwofon.

### Diferans Enpòtan:
* **"Sa a se yon bon chyen."** vs **"Kòd lojisyèl an byen ekri."** 

_Bati pa Enjenyè Gesner Deslandes_
""",
            "English": """
**Nasal vowels are crucial for changing word meanings in the Haitian Creole language. Let's practice:**

### The 4 Nasal Vowels:
1. **AN** — Change (Chanje), Mother (Manman), Time (Tan).
2. **EN** — Engineer (Enjenyè), Programming (Pwogramasyon), Dog (Chyen).
3. **ON** — Good (Bon), Company (Kompanyi), Children (Timoun).
4. **OUN** — Cousin (Kouzen), Deep (Pwofon).

### Crucial Difference:
* **"Sa a se yon bon chyen."** *(This is a good dog.)* vs **"Kòd lojisyèl an byen ekri."** *(The software code is well written.)*

_Built by Engineer Gesner Deslandes_
""",
            "Spanish": """
**Las vocales nasales son cruciales para cambiar el significado de las palabras en el idioma criollo haitiano. Practiquemos:**

### Las 4 Vocales Nasales:
1. **AN** — Cambiar (Chanje), Madre (Manman), Tiempo (Tan).
2. **EN** — Ingeniero (Enjenyè), Programación (Pwogramasyon), Perro (Chyen).
3. **ON** — Bueno (Bon), Compañía (Kompanyi), Niños (Timoun).
4. **OUN** — Primo (Kouzen), Profundo (Pwofon).

### Diferencia Crucial:
* **"Sa a se yon bon chyen."** *(Este es un buen perro.)* vs **"Kòd lojisyèl an byen ekri."** *(El código del software está bien escrito.)*

_Construido por el Ingeniero Gesner Deslandes_
""",
            "French": """
**Les voyelles nasales sont cruciales pour changer le sens des mots en créole haïtien. Pratiquons :**

### Les 4 Voyelles Nasales :
1. **AN** — Changer (Chanje), Mère (Manman), Temps (Tan).
2. **EN** — Ingénieur (Enjenyè), Programmation (Pwogramasyon), Chien (Chyen).
3. **ON** — Bon (Bon), Entreprise (Kompanyi), Enfants (Timoun).
4. **OUN** — Cousin (Kouzen), Profond (Pwofon).

### Différence Cruciale :
* **"Sa a se yon bon chyen."** *(C'est un bon chien.)* vs **"Kòd lojisyèl an byen ekri."** *(Le code du logiciel est bien écrit.)*

_Bâti par l'Ingénieur Gesner Deslandes_
"""
        }
    }
}

# ================== Sidebar Navigation & Controls ==================
with st.sidebar:
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="{GITHUB_AVATAR_URL}" style="border-radius: 50%; width: 110px; border: 3px solid #8A2BE2;">
        <h2 style="margin-top: 10px; font-size: 1.4rem; font-weight: bold;">GlobalInternet.py</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    st.header("📖 Lessons Menu")
    # All three lessons are now selectable right here
    selected_lesson = st.selectbox("Choose a lesson to study:", list(LESSONS_DATA.keys()))
    
    st.markdown("---")
    st.header("🌐 Book Translation")
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
# Flexbox title wrapper with your GitHub Profile Image
st.markdown(f"""
<div class="title-container">
    <h1>An Nou Aprann Kreyòl Ak Gesner Deslandes</h1>
    <img class="title-avatar" src="{GITHUB_AVATAR_URL}">
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 1.2rem; font-style: italic; color: #333333;'>An Interactive Audio-Visual Software Book for Mastering Haitian Creole and Modern Tech Terms</p>", unsafe_allow_html=True)

# Required structural ownership marking
st.markdown(
    "<h4 style='text-align: center; color: #8A2BE2 !important; letter-spacing: 1px; font-weight: bold;'>BUILT BY GESNER DESLANDES</h4>", 
    unsafe_allow_html=True
)
st.markdown("---")

# Layout Split: Video vs Script Card
col_video, col_text = st.columns([1.3, 1])
lesson_content = LESSONS_DATA[selected_lesson]

with col_video:
    st.markdown(f"### 🎬 Playing: {selected_lesson}")
    st.video(lesson_content["video_url"])
    st.caption("Media sound streams entirely in native Haitian Creole matching your explicit vocal recordings.")

with col_text:
    st.markdown(f"### 📄 Text Script ({selected_language})")
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    
    current_translation = lesson_content["captions"][selected_language]
    st.markdown(current_translation)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Persistent Footer branding
st.markdown('<div class="main-footer">© GlobalInternet.py – Built by GESNER DESLANDES.</div>', unsafe_allow_html=True)
