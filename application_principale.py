import streamlit as st

# Configuration de la page Streamlit pour un affichage large
st.set_page_config(page_title="Mon Portail d'Applications Eiffage", layout="wide")

# --- Définition des couleurs inspirées d'Eiffage ---
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

    /* Nouvelle section pour l'en-tête de la carte avec l'icône d'info */
    .app-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px; /* Espace entre l'en-tête et le contenu */
        border-bottom: 2px solid {EIFFAGE_ORANGE}; /* Soulignement orange */
        padding-bottom: 10px;
    }}

    .app-card-header h2 {{
        color: {EIFFAGE_BLUE_DARK}; 
        font-size: 1.8em;
        margin: 0; /* Supprime la marge par défaut du h2 pour un meilleur alignement */
        border-bottom: none; /* Le h2 n'a pas son propre soulignement */
    }}

    /* Styles pour l'icône d'information (i) et l'info-bulle */
    .info-icon {{
        position: relative;
        display: inline-block;
        cursor: help;
        font-size: 0.9em; /* Taille de l'icône */
        color: {EIFFAGE_BLUE_DARK};
        font-weight: bold;
        background-color: {EIFFAGE_GREY_LIGHT};
        border-radius: 50%;
        width: 25px;
        height: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    .info-icon:hover {{
        background-color: {EIFFAGE_ORANGE};
        color: {EIFFAGE_WHITE};
    }}

    .info-icon .tooltip-text {{
        visibility: hidden;
        width: 300px; /* Largeur de l'info-bulle */
        background-color: {EIFFAGE_BLUE_DARK};
        color: {EIFFAGE_WHITE};
        text-align: left;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%; /* Affiche l'info-bulle au-dessus de l'icône */
        left: 50%;
        margin-left: -150px; /* Centre l'info-bulle */
        opacity: 0;
        transition: opacity 0.3s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        font-size: 0.9em;
        line-height: 1.4;
    }}

    .info-icon .tooltip-text::after {{
        content: "";
        position: absolute;
        top: 100%; /* Pointe en bas de l'info-bulle */
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: {EIFFAGE_BLUE_DARK} transparent transparent transparent;
    }}

    .info-icon:hover .tooltip-text {{
        visibility: visible;
        opacity: 1;
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

# Première ligne : OptiRout'EES La Poste et Création de Cartes
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>OptiRout'EES La Poste Immobilier</h2>
            <div class="info-icon">
                i
                <span class="tooltip-text">
                    Cette application est dédiée à l'optimisation des tournées des techniciens pour le contrat La Poste Immobilier. Elle s'actualise directement avec le fichier de suivi PEC, intégrant les horaires mis à jour pour plus de 500 sites afin de maximiser l'efficacité.
                    <br><br>
                    Note : Cette application utilise un lien local et peut nécessiter un accès au réseau interne.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com" style="color: {EIFFAGE_WHITE}; text-decoration: underline;">methodesmaintenance.energie@eiffage.com</a>
                </span>
            </div>
        </div>
        <p>Optimisez les tournées techniciens du contrat La Poste Immobilier, avec mise à jour directe via le suivi PEC.</p>
        <a href="http://172.17.38.0:8501/" target="_blank" class="app-button">Accéder à OptiRout'EES La Poste</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>Application de Création de Cartes</h2>
            <div class="info-icon">
                i
                <span class="tooltip-text">
                    Créez des cartes HTML interactives avec différentes options de sectorisation : intelligente (k-means pour des clusters géographiques), par agence Clévia Centre-Est, ou personnalisée via une colonne de données (par technicien, chargé d'affaires, secteur d'activité). Elle permet également de récupérer les données GPS de tous les points au format CSV.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com" style="color: {EIFFAGE_WHITE}; text-decoration: underline;">methodesmaintenance.energie@eiffage.com</a>
                </span>
            </div>
        </div>
        <p>Créez facilement des cartes interactives avec diverses options de sectorisation et exportez les données GPS.</p>
        <a href="https://creation-carte.streamlit.app/" target="_blank" class="app-button">Accéder à l'Application de Création de Cartes</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---") # Ligne de séparation visuelle

# Deuxième ligne : Matrice de Temps de Trajet et OptiRout'EES Générale
col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>Matrice des Temps de Trajet</h2>
            <div class="info-icon">
                i
                <span class="tooltip-text">
                    Cette application utilise un serveur OSRM local pour générer des matrices de temps de route en France, même pour un grand nombre de points. C'est un outil essentiel pour la planification et est notamment utilisée par OptiRout'EES Générale pour créer de nouveaux onglets ou contrats.
                    <br><br>
                    Note : Cette application utilise un lien local et peut nécessiter un accès au réseau interne.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com" style="color: {EIFFAGE_WHITE}; text-decoration: underline;">methodesmaintenance.energie@eiffage.com</a>
                </span>
            </div>
        </div>
        <p>Générez des matrices pour estimer les temps de déplacement entre de multiples points en France.</p>
        <a href="http://172.17.38.0:8503/" target="_blank" class="app-button">Accéder à la Matrice des Temps de Trajet</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>Application OptiRout'EES Générale</h2>
            <div class="info-icon">
                i
                <span class="tooltip-text">
                    Similaire à l'application La Poste Immobilier, cette version généralisée d'OptiRout'EES permet d'optimiser les itinéraires pour n'importe quel contrat ou secteur. Il suffit de remplir un template fourni, de récupérer les coordonnées GPS via l'application dédiée, puis la matrice de temps de trajet, et de tout uploader pour planifier votre journée. Cette application n'est pas connectée directement à un SharePoint.
                    <br><br>
                    Note : Cette application utilise un lien local et peut nécessiter un accès au réseau interne.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com" style="color: {EIFFAGE_WHITE}; text-decoration: underline;">methodesmaintenance.energie@eiffage.com</a>
                </span>
            </div>
        </div>
        <p>Optimisez vos itinéraires pour n'importe quel contrat ou secteur en personnalisant vos propres parcours.</p>
        <a href="http://172.17.38.0:8502/" target="_blank" class="app-button">Accéder à OptiRout'EES Générale</a>
    </div>
    """, unsafe_allow_html=True)

# Ajout du pied de page
st.markdown(f"""
    <div class="footer-text">
        Développé avec ❤️ pour Eiffage Énergie Systèmes<br>
        Pour toute assistance ou question technique, veuillez contacter : <a href="mailto:methodesmaintenance.energie@eiffage.com" style="color: {EIFFAGE_BLUE_DARK}; text-decoration: underline;">methodesmaintenance.energie@eiffage.com</a>
    </div>
    """, unsafe_allow_html=True)
