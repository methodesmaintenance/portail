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

    /* Styles pour le titre principal */
    h1 {{
        color: {EIFFAGE_BLUE_DARK}; /* Bleu foncé Eiffage */
        text-align: center;
        font-size: 3em;
        margin-top: 20px;
        margin-bottom: 30px;
        font-weight: bold;
        padding-top: 0; /* Supprimé le padding-top car il y a déjà un margin-top */
    }}

    p {{
        font-size: 1.1em;
        line-height: 1.6;
        color: {EIFFAGE_GREY_TEXT};
    }}
    
    a {{
        text-decoration: none;
    }}

    /* Styles pour les cartes d'application */
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

    /* En-tête de la carte avec titre et icône d'info */
    .app-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 15px; 
        border-bottom: 2px solid {EIFFAGE_ORANGE}; 
        padding-bottom: 10px;
    }}

    .app-card-header h2 {{
        color: {EIFFAGE_BLUE_DARK}; 
        font-size: 1.8em;
        margin: 0; 
        border-bottom: none; 
    }}

    /* Styles pour l'icône d'information (i) et l'info-bulle */
    .info-icon {{
        position: relative;
        display: inline-block;
        cursor: help;
        font-size: 1em; /* Taille de l'icône */
        color: {EIFFAGE_BLUE_DARK};
        font-weight: bold;
        background-color: {EIFFAGE_GREY_LIGHT};
        border-radius: 50%;
        width: 30px; /* Taille augmentée pour meilleure visibilité */
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        z-index: 10; /* Assure que l'icône est au-dessus pour le survol */
    }}

    .info-icon:hover {{
        background-color: {EIFFAGE_ORANGE};
        color: {EIFFAGE_WHITE};
    }}

    .info-icon .tooltip-text {{
        visibility: hidden;
        width: 320px; /* Largeur de l'info-bulle légèrement augmentée */
        background-color: {EIFFAGE_BLUE_DARK};
        color: {EIFFAGE_WHITE};
        text-align: left;
        border-radius: 8px; /* Bords plus arrondis */
        padding: 12px;
        position: absolute;
        z-index: 999; /* TRÈS IMPORTANT : Assure que l'info-bulle est au premier plan */
        bottom: 125%; 
        left: 50%;
        margin-left: -160px; /* Centre l'info-bulle (moitié de la largeur) */
        opacity: 0;
        transition: opacity 0.3s ease-in-out; /* Transition douce pour l'apparition */
        box-shadow: 0 6px 20px rgba(0,0,0,0.3); /* Ombre plus prononcée */
        font-size: 0.95em; /* Texte légèrement plus grand */
        line-height: 1.5;
    }}

    .info-icon .tooltip-text a {{ /* Style pour les liens dans l'info-bulle */
        color: {EIFFAGE_WHITE};
        text-decoration: underline;
    }}

    .info-icon .tooltip-text::after {{
        content: "";
        position: absolute;
        top: 100%; 
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

    /* Styles pour les boutons d'application */
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

    /* Styles pour le pied de page */
    .footer-text {{
        text-align: center;
        margin-top: 40px; /* Marge supérieure augmentée */
        padding-top: 20px;
        border-top: 1px solid rgba(0,0,0,0.1); /* Ligne subtile au-dessus du pied de page */
        font-size: 1em;
        color: {EIFFAGE_BLUE_DARK};
        font-style: italic;
    }}

    .footer-text a {{
        color: {EIFFAGE_BLUE_DARK};
        text-decoration: underline;
        font-weight: bold;
    }}

    .eiffage-logo {{
        display: block;
        max-width: 200px; /* Ajustez la taille du logo si nécessaire */
        margin: 20px auto 10px auto; /* Centre le logo et ajoute des marges */
    }}

    </style>
    """, unsafe_allow_html=True)

# --- Affichage du logo Eiffage ---
# REMPLACEZ '[CHEMIN_VERS_VOTRE_LOGO.png]' par le chemin d'accès local ou l'URL publique de votre logo.
# Par exemple: st.image("mon_dossier/logo_eiffage.png") ou st.image("https://example.com/logo_eiffage.png")
st.image("https://www.eiffage.com/themes/eiffage/images/logo.png", use_column_width=False, output_format="PNG", caption="Logo Eiffage", width=200)


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
                    **Note importante :** Cette application utilise un lien local et peut nécessiter un accès au réseau interne d'Eiffage pour fonctionner.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
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
                    Créez des cartes HTML interactives avec différentes options de sectorisation :
                    <ul>
                        <li>**Sectorisation intelligente (K-means)** : Choisissez le nombre de clusters pour des secteurs à vol d'oiseau.</li>
                        <li>**Sectorisation par agence** : Basée sur les agences Clévia Centre-Est.</li>
                        <li>**Sectorisation personnalisée** : Utilisez une colonne de données existante (par technicien, chargé d'affaires, secteur d'activité).</li>
                    </ul>
                    Elle permet également de récupérer les données GPS de tous les points au format CSV.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
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
                    Cette application appelle un serveur OSRM local pour générer des matrices de temps de route en France, supportant un grand nombre de points. C'est un outil fondamental pour la planification logistique et est notamment utilisée par OptiRout'EES Générale pour la création de nouveaux onglets, contrats ou secteurs.
                    <br><br>
                    **Note importante :** Cette application utilise un lien local et peut nécessiter un accès au réseau interne d'Eiffage pour fonctionner.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
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
                    Similaire à l'application La Poste Immobilier, cette version généralisée d'OptiRout'EES permet d'optimiser les itinéraires pour n'importe quel contrat ou secteur. Le processus inclut :
                    <ol>
                        <li>Remplir un template fourni dans l'appli.</li>
                        <li>Récupérer les coordonnées GPS via l'application "Coordonnées GPS" (non listée ici).</li>
                        <li>Générer la matrice de temps de trajet grâce à l'application "Matrice des Temps de Trajet".</li>
                        <li>Uploader ces données dans l'appli pour retrouver votre contrat et utiliser l'outil d'optimisation d'itinéraire sur la journée.</li>
                    </ol>
                    Cette application n'est pas directement connectée à un SharePoint.
                    <br><br>
                    **Note importante :** Cette application utilise un lien local et peut nécessiter un accès au réseau interne d'Eiffage pour fonctionner.
                    <br><br>
                    Pour toute question ou assistance, contactez : <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
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
        Pour toute assistance ou question technique, veuillez contacter : <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
    </div>
    """, unsafe_allow_html=True)
