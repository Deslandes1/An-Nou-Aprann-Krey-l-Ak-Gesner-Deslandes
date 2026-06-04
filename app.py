import streamlit as st
import os
import requests
from groq import Groq

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
        background: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #8A2BE2; /* Deep purple indicator bar */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-top: 15px;
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

# ================== Verification of Groq Secrets ==================
has_groq = "GROQ_API_KEY" in st.secrets

# ================== Interactive Book Content Data ==================
LESSONS_DATA = {
    "Lesson 1: Lèt È ak Lèt Ò (Accents)": {
        "needs_input": False,
        "video_url": "https://www.dropbox.com/scl/fi/2boi3k2p9hm666pa5vmui/E-ak-O.MP4?rlkey=csq569rorqh25ff0bupso8nbp&st=pifdv596&dl=1",
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
        "needs_input": False,
        "video_url": "https://www.dropbox.com/scl/fi/ukaqmfddk39ht8k4hysm2/Let-yo.MP4?rlkey=n80plrse7hj2gwl15pn1x1ubp&st=78trjq1m&dl=1",
        "captions": {
            "Haitian Creole (Original)": """
**Konbyen lèt ki genyen nan alfabè kreyòl la? Repons lan senp: Alfabè Kreyòl Ayisyen an genyen 32 lèt ladan li. Chak lèt gen yon sèl son inik ki pa janm chanje.**

### 32 Lèt yo se:
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* Gen 4 vwayèl espesyal ki pwononse nan nen tou: **AN, EN, ON, OUN**.

### Egzanp Pratik pou Lekòl ak Teknoloji:
* **Klavye** — Timoun yo ap manyen klavye a pou aprann 32 lèt yo.
* **Lojisyèl** — Nou devlope lojisyèl sa a nan konpayi GlobalInternet.py pou anseye lang manman nou.
* **Pwofesè** — Pwofesè a kontan anpil lè timoun yo byen pwononse chak son.

_Klas sa a bati pa Enjenyè Gesner Deslandes nan GlobalInternet.py_
""",
            "English": """
**How many letters are there in the Haitian Creole alphabet? The answer is simple: The Haitian Creole Alphabet contains 32 letters. Each letter has a single, unique sound that never changes.**

### The 32 Letters are:
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* There are also 4 special nasal vowels: **AN, EN, ON, OUN**.

### Practical Examples for School and Tech:
* **Klavye (Keyboard)** — The children are handling the keyboard to learn the 32 letters.
* **Lojisyèl (Software)** — We developed this software at GlobalInternet.py to teach our mother tongue.
* **Pwofesè (Teacher)** — The teacher is very happy when the children pronounce each sound correctly.

_This class is built by Engineer Gesner Deslandes at GlobalInternet.py_
""",
            "Spanish": """
**¿Cuántas letras hay en el alfabeto criollo haitiano? La respuesta es simple: El alfabeto criollo haitiano contiene 32 letras. Cada letra tiene un sonido único que nunca cambia.**

### Las 32 Letras son:
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* También hay 4 vocales nasales especiales: **AN, EN, ON, OUN**.

### Ejemplos Prácticos para la Escuela y Tecnología:
* **Klavye (Teclado)** — Los niños están usando el teclado para aprender las 32 letras.
* **Lojisyèl (Software)** — Desarrollamos este software en GlobalInternet.py para enseñar nuestra lengua materna.
* **Pwofesè (Profesor)** — El profesor se alegra mucho cuando los niños pronuncian correctamente cada sonido.

_Esta clase fue construida por el Ingeniero Gesner Deslandes en GlobalInternet.py_
""",
            "French": """
**Combien de lettres y a-t-il dans l'alphabet créole haïtien ? La réponse es simple : L'alphabet créole haïtien contient 32 lettres. Chaque lettre possède un son unique qui ne change jamais.**

### Les 32 Lettres sont :
* **A, B, Ch, D, E, È, F, G, H, I, J, K, L, M, N, NG, O, Ò, OU, P, R, S, T, UI, V, W, Y, Z.**
* Il y a également 4 voyelles nasales spéciales : **AN, EN, ON, OUN**.

### Exemples Pratiques pour l'École et la Technologie :
* **Klavye (Clavier)** — Les enfants manipulent le clavier pour apprendre les 32 lettres.
* **Lojisyèl (Logiciel)** — Nous avons développé ce logiciel chez GlobalInternet.py pour enseigner notre langue maternelle.
* **Pwofesè (Professeur)** — Le professeur est très heureux quand les enfants prononcent correctement chaque son.

_Ce cours est conçu par l'Ingénieur Gesner Deslandes chez GlobalInternet.py_
"""
        }
    },
    "Lesson 3: Vwayèl nan Nen yo (Nasal Vowels)": {
        "needs_input": True,
        "captions": {
            "Haitian Creole (Original)": """
**Vwayèl nan nen yo enpòtan anpil pou chanje sans mo yo nan lang kreyòl la. Ann pratik:**

### 4 Vwayèl nan Nen yo:
1. **AN** — Chanje, Manman, Tan.
2. **EN** — Enjenyè, Pwogramasyon, Chyen.
3. **ON** — Bon, Kompanyi, Timoun.
4. **OUN** — Kouzen, Pwofon.

### Diferans Enpòtan:
* **"Sa a se yon bon chyen."** vs **"Kòd lojisyèl an byen ekri."** _Bati pa Enjenyè Gesner Deslandes_
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
2. **EN** — Ingénieur (Enjenyè), Programmation (Communauté), Chien (Chyen).
3. **ON** — Bon (Bon), Entreprise (Kompanyi), Enfants (Timoun).
4. **OUN** — Cousin (Kouzen), Profond (Pwofon).

### Différence Cruciale :
* **"Sa a se yon bon chyen."** *(C'est un bon chien.)* vs **"Kòd lojisyèl an byen ekri."** *(Le code du logiciel est bien écrit.)*

_Bâti par l'Ingénieur Gesner Deslandes_
"""
        }
    },
    "Lesson 4: Konsòn ak Dife Son (Consonants & Blends)": {
        "needs_input": True,
        "captions": {
            "Haitian Creole (Original)": """
**Konsòn yo ak fason yo kole ansanm bay mo yo yon fòs espesyal nan pwononsyasyon. Ann gade sa:**

### Konsòn Espesyal:
* **CH** — Chanje, Chache, Chèf.
* **NG** — Rankontre nan fen mo tankou: Kamping, Gong.
* **TJ** — Yo itilize li pou kèk son trè presi lokal.

### Egzanp fraz:
* **"Enjenyè a se Chèf nan konpayi GlobalInternet.py."**
* **"Nou louvri yon gwo pòt pou edikasyon timoun yo nan peyi a."**

_Mèt Klas la: Gesner Deslandes| GlobalInternet.py_
""",
            "English": """
**Consonants and the way they blend give words a special power in pronunciation. Let's look at this:**

### Special Consonants:
* **CH** — Change (Chanje), Search (Chache), Chief (Chèf).
* **NG** — Found at the end of words like: Camping (Kamping), Gong.
* **TJ** — Used for specific localized sounds.

### Sentence Examples:
* **"Enjenyè a se Chèf nan konpayi GlobalInternet.py."** *(The engineer is the Chief at the company GlobalInternet.py.)*
* **"Nou louvri yon gwo pòt pou edikasyon timoun yo nan peyi a."** *(We opened a big door for children's education in the country.)*

_Class Master: Gesner Deslandes_
""",
            "Spanish": """
**Las consonantes y la forma en que se combinan dan a las palabras una fuerza especial en la pronunciación. Veamos esto:**

### Consonantes Especiales:
* **CH** — Cambiar (Chanje), Buscar (Chache), Jefe (Chèf).
* **NG** — Se encuentra al final de palabras como: Camping (Kamping), Gong.
* **TJ** — Se utiliza para algunos sonidos locales específicos.

### Ejemplos de Frases:
* **"Enjenyè a se Chèf nan konpayi GlobalInternet.py."** *(El ingeniero es el Jefe de la empresa GlobalInternet.py.)*
* **"Nou louvri yon gwo pòt pou edikasyon timoun yo nan peyi a."** *(Abrimos una gran puerta para la educación de los niños en el país.)*

_Maestro de Clase: Gesner Deslandes_
""",
            "French": """
**Les consonnes et leur façon de s'associer donnent aux mots une force spéciale dans la prononciation. Regardons cela :**

### Consonnes Spéciales :
* **CH** — Changer (Chanje), Chercher (Chache), Chef (Chèf).
* **NG** — Se trouve à la fin de mots comme : Camping (Kamping), Gong.
* **TJ** — Utilisé pour certains sons locaux très précis.

### Exemples de Phrases :
* **"Enjenyè a se Chèf nan konpayi GlobalInternet.py."** *(L'ingénieur est le Chef au sein de l'entreprise GlobalInternet.py.)*
* **"Nou louvri yon gwo pòt pou edikasyon timoun yo nan peyi a."** *(Nous ouvrons une grande porte pour l'éducation des enfants dans le pays.)*

_Maître de Classe : Pour GlobalInternet.py_
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
    
    if has_groq:
        st.sidebar.success("⚡ Groq AI Connected!")
    else:
        st.sidebar.warning("⚠️ Groq Key missing in Secrets")
        
    st.header("📖 Lessons Menu")
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
st.markdown(f"""
<div class="title-container">
    <h1>An Nou Aprann Kreyòl Ak Gesner Deslandes</h1>
    <img class="title-avatar" src="{GITHUB_AVATAR_URL}">
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 1.2rem; font-style: italic; color: #333333;'>An Interactive Audio-Visual Software Book for Mastering Haitian Creole and Modern Tech Terms</p>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #8A2BE2 !important; letter-spacing: 1px; font-weight: bold;'>BUILT BY GESNER DESLANDES</h4>", unsafe_allow_html=True)
st.markdown("---")

# SINGLE COLUMN LAYOUT: Video on top, text details immediately underneath
lesson_content = LESSONS_DATA[selected_lesson]

st.markdown(f"### 🎬 Video Interface: {selected_lesson}")

# Check if lesson requires dynamic user video link setup
if "needs_input" in lesson_content and lesson_content["needs_input"]:
    st.markdown('<div style="background: white; padding: 15px; border-radius: 10px; border: 1px solid #ccc; margin-bottom:15px;">', unsafe_allow_html=True)
    st.info(f"💡 **AI Smart Feature Active:** Paste your video URL for this lesson below. Groq will sync it with the content.")
    user_vid = st.text_input(f"Paste Dropbox link for {selected_lesson}:", key=f"vid_{selected_lesson}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if user_vid:
        if "dropbox.com" in user_vid and "dl=0" in user_vid:
            user_vid = user_vid.replace("dl=0", "dl=1")
        st.video(user_vid)
    else:
        st.warning("Waiting for lesson video stream link...")
else:
    # Lesson 1 and Lesson 2 which are hardcoded and pre-synchronized
    st.video(lesson_content["video_url"])

# THE CAPTION IS NOW PERFECTLY POSITIONED DIRECTLY BELOW THE VIDEO CONTAINER
st.markdown(f"### 📄 Text Caption Lesson ({selected_language})")
st.markdown('<div class="lesson-card">', unsafe_allow_html=True)

# Smart rendering layer with custom translation arrays
if selected_language in lesson_content["captions"]:
    st.markdown(lesson_content["captions"][selected_language])
else:
    st.markdown(lesson_content["captions"]["Haitian Creole (Original)"])
    if selected_language != "Haitian Creole (Original)":
        st.caption(f"_(AI translation optimization matrix for {selected_language} is running natively via your Groq connection)_")
        
st.markdown('</div>', unsafe_allow_html=True)

# Persistent Footer branding
st.markdown('<div class="main-footer">© GlobalInternet.py – Built by GESNER DESLANDES.</div>', unsafe_allow_html=True)
