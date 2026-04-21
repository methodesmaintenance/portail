import streamlit as st

# Configuration de la page Streamlit pour un affichage large
st.set_page_config(page_title="Mon Portail d'Applications Eiffage", layout="wide")

# --- Définition des couleurs inspirées d'Eiffage ---
# Vous pouvez ajuster ces codes hexadécimaux si vous avez des couleurs spécifiques
EIFFAGE_BLUE_DARK = "#013970"  # Bleu foncé principal
EIFFAGE_ORANGE = "#DF1C02"     # Orange pour les accents et boutons
EIFFAGE_GREY_LIGHT = "#F0F2F6" # Gris très clair pour le fond de page
EIFFAGE_GREY_TEXT = "#01003D"  # Gris foncé pour le texte
EIFFAGE_WHITE = "#FFFFFF"      # Blanc pour les fonds de cartes

# --- Injection de CSS Personnalisé pour un look plus moderne ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {EIFFAGE_GREY_LIGHT}; /* Fond gris clair pour la page */
        color: {EIFFAGE_GREY_TEXT}; /* Couleur de texte par défaut */
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; /* Police plus moderne */
    }}

    h1 {{
        color: {EIFFAGE_BLUE_DARK}; /* Bleu foncé Eiffage */
        text-align: center;
        font-size: 3em;
        margin-bottom: 30px;
        font-weight: bold;
        padding-top: 20px;
    }}

    p {{
        font-size: 1.1em;
        line-height: 1.6;
        color: {EIFFAGE_GREY_TEXT};
    }}
    
    a {{
        text-decoration: none;
    }}

    .app-card {{
        background-color: {EIFFAGE_WHITE}; 
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); 
        padding: 25px;
        margin-bottom: 20px; 
        transition: transform 0.2s ease-in-out; 
        height: 100%; 
        display: flex;
        flex-direction: column;
        justify-content: space-between; 
    }}
    .app-card:hover {{
        transform: translateY(-5px); 
    }}


    .app-card h2 {{
        color: {EIFFAGE_BLUE_DARK}; 
        font-size: 1.8em;
        margin-top: 0;
        margin-bottom: 15px;
        border-bottom: 2px solid {EIFFAGE_ORANGE}; 
        padding-bottom: 10px;
    }}

    .app-card p {{
        flex-grow: 1; 
        margin-bottom: 20px;
    }}

    .app-button {{
        display: block; 
        padding: 12px 25px;
        background-color: {EIFFAGE_ORANGE}; 
        color: white !important;
        text-align: center;
        text-decoration: none;
        font-size: 17px;
        border-radius: 8px;
        margin-top: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease; 
        width: 100%; 
    }}
    .app-button:hover {{
        background-color: {EIFFAGE_BLUE_DARK};
        color: {EIFFAGE_WHITE} !important;
    }}

    .footer-text {{
        text-align: center;
        margin-top: 30px;
        font-size: 1.1em;
        color: {EIFFAGE_BLUE_DARK};
        font-style: italic;
    }}

    </style>
    """, unsafe_allow_html=True)


st.title("Portail d'Applications")


st.markdown("---") # Ligne de séparation visuelle

# Création de deux colonnes pour organiser les applications côte à côte
col1, col2 = st.columns(2)

with col1:
    # Contenu de la première application dans une "carte" stylisée
    st.markdown(f"""
    <div class="app-card">
        <h2>Application d'Optimisation de tournée</h2>
        <p>Cette application permet d'optimiser les tournées techniciens pour le contrat La Poste.</p>
        <a href="https://interfaceoptimisation.streamlit.app/" target="_blank" class="app-button">Accéder à l'Application d'Optimisation</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Contenu de la deuxième application dans une "carte" stylisée
    st.markdown(f"""
    <div class="app-card">
        <h2>Application de Création de Cartes</h2>
        <p>Créez facilement des cartes interactives.</p>
        <a href="https://creation-carte.streamlit.app/" target="_blank" class="app-button">Accéder à l'Application de Création de Cartes</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---") # Ligne de séparation visuelle

