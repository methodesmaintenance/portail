import streamlit as st
import base64

# 1. Configuration de la page
st.set_page_config(
    page_title="Portail d'Applications | Eiffage Énergie Systèmes", 
    page_icon="🏢", 
    layout="wide"
)

# 2. Définition de la charte graphique (Clévia / Eiffage)
EIFFAGE_BLUE = "#003B5C"     # Bleu profond Eiffage/Clévia
EIFFAGE_RED = "#E63312"      # Rouge/Orange dynamique Eiffage
BG_COLOR = "#F4F7F9"         # Gris-bleu très clair pour le fond
TEXT_COLOR = "#2C3E50"       # Gris anthracite pour une lecture douce
CARD_BG = "#FFFFFF"          # Fond des cartes

# 3. Injection du CSS personnalisé
st.markdown(f"""
    <style>
    /* Configuration globale */
    .stApp {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
        font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}

    /* En-tête principal */
    .main-header {{
        color: {EIFFAGE_BLUE};
        text-align: center;
        font-size: 2.8em;
        font-weight: 800;
        margin-top: 10px;
        margin-bottom: 40px;
        letter-spacing: -0.5px;
    }}

    /* Séparateur stylisé */
    hr {{
        border: 0;
        height: 1px;
        background-image: linear-gradient(to right, rgba(0, 59, 92, 0), rgba(0, 59, 92, 0.2), rgba(0, 59, 92, 0));
        margin: 40px 0;
    }}

    /* Design des Cartes d'application */
    .app-card {{
        background-color: {CARD_BG}; 
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); 
        padding: 30px;
        margin-bottom: 25px; 
        transition: all 0.3s ease; 
        height: 100%; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid rgba(0,0,0,0.03);
    }}
    .app-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0, 59, 92, 0.1); 
        border-bottom: 4px solid {EIFFAGE_RED};
    }}

    /* En-tête de la carte */
    .app-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 15px; 
    }}

    .app-card-header h2 {{
        color: {EIFFAGE_BLUE}; 
        font-size: 1.5em;
        font-weight: 700;
        margin: 0; 
        line-height: 1.3;
        padding-right: 15px;
    }}

    /* Icône d'information et Tooltip */
    .info-container {{
        position: relative;
        display: inline-block;
    }}

    .info-icon {{
        cursor: pointer;
        color: {EIFFAGE_BLUE};
        background-color: {BG_COLOR};
        border-radius: 50%;
        min-width: 28px; 
        height: 28px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        font-size: 0.9em;
        transition: all 0.2s ease;
        border: 1px solid rgba(0, 59, 92, 0.1);
    }}

    .info-icon:hover {{
        background-color: {EIFFAGE_BLUE};
        color: white;
    }}

    .tooltip-text {{
        visibility: hidden;
        width: 340px;
        background-color: {EIFFAGE_BLUE};
        color: #ffffff;
        text-align: left;
        border-radius: 10px;
        padding: 15px 20px;
        position: absolute;
        z-index: 1000;
        top: 130%; 
        right: 0; /* Aligné sur la droite pour ne pas sortir de l'écran */
        opacity: 0;
        transition: opacity 0.2s, top 0.2s;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        font-size: 0.9em;
        line-height: 1.5;
        font-weight: 400;
    }}

    .info-container:hover .tooltip-text {{
        visibility: visible;
        opacity: 1;
        top: 110%;
    }}

    .tooltip-text ul, .tooltip-text ol {{
        margin-top: 5px;
        margin-bottom: 10px;
        padding-left: 20px;
    }}

    .tooltip-text a {{
        color: #82C0E7; /* Bleu clair pour les liens sur fond foncé */
        text-decoration: none;
        font-weight: 600;
    }}
    .tooltip-text a:hover {{ text-decoration: underline; }}

    /* Texte de description de la carte */
    .app-card p.description {{
        flex-grow: 1; 
        font-size: 1.05em;
        color: {TEXT_COLOR};
        line-height: 1.6;
        margin-bottom: 25px;
    }}

    /* Boutons d'action */
    .app-button {{
        display: block; 
        padding: 14px 20px;
        background-color: {EIFFAGE_RED}; 
        color: #ffffff !important;
        text-align: center;
        text-decoration: none;
        font-size: 1em;
        font-weight: 600;
        border-radius: 6px;
        transition: background-color 0.3s, transform 0.1s; 
        width: 100%; 
    }}
    .app-button:hover {{
        background-color: {EIFFAGE_BLUE};
        transform: scale(1.02);
    }}

    /* Pied de page */
    .footer-container {{
        text-align: center;
        margin-top: 60px;
        padding-top: 30px;
        border-top: 1px solid rgba(0,0,0,0.05);
        font-size: 0.95em;
        color: #5C6F82;
    }}
    .footer-container a {{
        color: {EIFFAGE_BLUE};
        text-decoration: none;
        font-weight: bold;
    }}
    .footer-container a:hover {{ text-decoration: underline; }}
    
    .logo-container {{
        text-align: center;
        margin-bottom: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. En-tête avec Logo et Titre
# Fonction pour lire l'image locale et l'intégrer proprement dans le HTML
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Nom de votre fichier image (doit être dans le même dossier que ce script Python)
image_filename = "Eiffage_Énergie_Systèmes.svg (2).png"

try:
    img_base64 = get_base64_image(image_filename)
    img_tag = f'<img src="data:image/png;base64,{img_base64}" width="250" alt="Logo Eiffage">'
except FileNotFoundError:
    # Message d'erreur discret si le fichier n'est pas trouvé
    img_tag = f'<p style="color:#E63312;">⚠️ Image "{image_filename}" introuvable.</p>'

# Affichage avec le CSS pré-configuré
st.markdown(f"""
    <div class="logo-container">
        {img_tag}
    </div>
    <div class="main-header">Portail d'Applications Clévia</div>
""", unsafe_allow_html=True)

# 5. Cartes d'applications (Ligne 1)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>OptiRout'EES <br><span style="font-size: 0.8em; color: {EIFFAGE_RED};">La Poste Immobilier</span></h2>
            <div class="info-container">
                <div class="info-icon">i</div>
                <div class="tooltip-text">
                    <strong>Contrat LPI - Optimisation des tournées</strong><br><br>
                    Application connectée directement au fichier de suivi PEC. Elle intègre automatiquement les horaires mis à jour pour plus de 500 sites afin de générer les itinéraires de maintenance les plus efficaces.<br><br>
                    <em>⚠️ Nécessite un accès au réseau interne Eiffage (lien local).</em><br><br>
                    Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                </div>
            </div>
        </div>
        <p class="description">Générez et optimisez les tournées de vos techniciens spécifiquement pour le contrat La Poste Immobilier, avec synchronisation dynamique des données PEC.</p>
        <a href="http://172.17.38.0:8501/" target="_blank" class="app-button">Accéder à OptiRout'EES (LPI)</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>Générateur de Cartes & Sectorisation</h2>
            <div class="info-container">
                <div class="info-icon">i</div>
                <div class="tooltip-text">
                    <strong>Cartographie HTML interactive</strong><br><br>
                    Module permettant de visualiser et d'exporter vos données selon 3 logiques :
                    <ul>
                        <li><strong>K-means :</strong> Sectorisation automatique "intelligente" par zone.</li>
                        <li><strong>Réseau :</strong> Basée sur les agences Clévia Centre-Est.</li>
                        <li><strong>Sur-mesure :</strong> Basée sur vos propres colonnes (Technicien, Chargé d'affaires...).</li>
                    </ul>
                    Permet l'export CSV des coordonnées GPS.<br><br>
                    Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                </div>
            </div>
        </div>
        <p class="description">Transformez vos données en cartes interactives. Idéal pour visualiser vos secteurs d'intervention, répartir la charge et exporter vos coordonnées GPS.</p>
        <a href="https://creation-carte.streamlit.app/" target="_blank" class="app-button">Accéder à la Cartographie</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Cartes d'applications (Ligne 2)
col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>Matrice des Temps de Trajet (OSRM)</h2>
            <div class="info-container">
                <div class="info-icon">i</div>
                <div class="tooltip-text">
                    <strong>Moteur de calcul logistique</strong><br><br>
                    Cette interface s'appuie sur notre serveur OSRM local. Elle permet de croiser massivement des coordonnées GPS pour générer des matrices de temps de route et de distances sur tout le territoire français.<br><br>
                    <em>⚠️ Nécessite un accès au réseau interne Eiffage (lien local).</em><br><br>
                    Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                </div>
            </div>
        </div>
        <p class="description">Outil fondamental de planification : calculez instantanément les temps de parcours réels entre plusieurs centaines de points d'intervention en France.</p>
        <a href="http://172.17.38.0:8503/" target="_blank" class="app-button">Accéder au Calculateur de Temps</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <h2>OptiRout'EES <br><span style="font-size: 0.8em; color: {EIFFAGE_RED};">Outil Général</span></h2>
            <div class="info-container">
                <div class="info-icon">i</div>
                <div class="tooltip-text">
                    <strong>L'optimisation sur-mesure pour tous contrats</strong><br><br>
                    Démarche d'utilisation :
                    <ol>
                        <li>Remplissez le gabarit Excel type fourni.</li>
                        <li>Obtenez vos coordonnées GPS et calculez votre matrice (via l'outil OSRM).</li>
                        <li>Importez votre dossier complet pour générer vos tournées optimisées.</li>
                    </ol>
                    <em>⚠️ Nécessite un accès au réseau interne Eiffage (lien local).</em><br><br>
                    Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                </div>
            </div>
        </div>
        <p class="description">La solution universelle pour optimiser les itinéraires de vos équipes, quel que soit le contrat, l'agence ou le secteur d'activité visé.</p>
        <a href="http://172.17.38.0:8502/" target="_blank" class="app-button">Accéder à OptiRout'EES (Général)</a>
    </div>
    """, unsafe_allow_html=True)

# 7. Pied de page
st.markdown("""
    <div class="footer-container">
        Développé pour <strong>Eiffage Énergie Systèmes - Clévia</strong><br>
        Pour toute assistance technique, méthode ou évolution, contactez le service : <br>
        <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
    </div>
""", unsafe_allow_html=True)
