import streamlit as st
import base64

# 1. Configuration de la page
st.set_page_config(
    page_title="Portail d'Applications | Eiffage Énergie Systèmes", 
    page_icon="🏢", 
    layout="wide"
)

# 2. Définition de la charte graphique officielle EIFFAGE & Couleurs modernes
EIFFAGE_BLACK = "#111111"    # Noir pur / Anthracite principal Eiffage
EIFFAGE_RED = "#E63312"      # Rouge dynamique Eiffage
BG_COLOR = "#F4F7F6"         # Gris très clair et moderne pour le fond
TEXT_COLOR = "#333333"       # Gris sombre textuel
CARD_BG = "#FFFFFF"          # Blanc pur pour les cartes
CLOUD_COLOR = "#007BFF"      # Bleu pour indiquer le Cloud
LOCAL_COLOR = "#F39C12"      # Orange pour indiquer le Local

# 3. Injection du CSS personnalisé
st.markdown(f"""
    <style>
    /* Configuration globale */
    .stApp {{
        background-color: {BG_COLOR};
        font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }}

    /* Container de l'en-tête (Flexbox pour aligner à gauche et à droite) */
    .header-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        margin-bottom: 30px;
        padding-bottom: 20px;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        flex-wrap: wrap;
        gap: 20px;
    }}

    /* Section Gauche : Logo et Titre */
    .header-left {{
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }}

    .main-title {{
        color: {EIFFAGE_BLACK};
        font-size: 2.4em;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-top: 15px;
    }}

    /* Section Droite : Légende d'accès */
    .header-right {{
        background: #FFFFFF;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.03);
        border: 1px solid rgba(0,0,0,0.05);
        font-size: 0.9em;
        color: {TEXT_COLOR};
        max-width: 400px;
    }}
    
    .legend-title {{
        font-weight: 700;
        margin-bottom: 8px;
        color: {EIFFAGE_BLACK};
        border-bottom: 2px solid {BG_COLOR};
        padding-bottom: 5px;
    }}

    .legend-item {{
        margin-bottom: 6px;
        line-height: 1.4;
    }}

    /* Badges Local / Cloud */
    .badge {{
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: 700;
        color: white;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 10px;
    }}
    .badge-local {{ background-color: {LOCAL_COLOR}; }}
    .badge-cloud {{ background-color: {CLOUD_COLOR}; }}
    .badge-inline {{ margin-bottom: 0; margin-right: 8px; }}

    /* Design des Cartes d'application modernisées */
    .app-card {{
        background-color: {CARD_BG}; 
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04); 
        padding: 30px;
        margin-bottom: 25px; 
        transition: transform 0.3s ease, box-shadow 0.3s ease; 
        height: 100%; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid rgba(0,0,0,0.03);
        position: relative;
        z-index: 1;
    }}
    .app-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.08); 
        z-index: 50;
    }}
    
    /* Bordure supérieure de couleur au survol */
    .app-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; height: 4px;
        background: {EIFFAGE_RED};
        border-radius: 16px 16px 0 0;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    .app-card:hover::before {{ opacity: 1; }}

    /* En-tête de la carte */
    .app-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 15px; 
    }}

    .app-card-header h2 {{
        color: {EIFFAGE_BLACK}; 
        font-size: 1.4em;
        font-weight: 700;
        margin: 0; 
        line-height: 1.3;
        padding-right: 15px;
    }}
    
    .subtitle {{
        font-size: 0.85em; 
        color: {EIFFAGE_RED};
        font-weight: 600;
        text-transform: uppercase;
        display: block;
        margin-top: 5px;
    }}

    /* Icône d'information et Tooltip */
    .info-container {{
        position: relative;
        display: inline-block;
    }}

    .info-icon {{
        cursor: pointer;
        color: #A0A0A0;
        background-color: {BG_COLOR};
        border-radius: 50%;
        min-width: 32px; 
        height: 32px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        font-size: 1em;
        transition: all 0.2s ease;
    }}

    .info-icon:hover {{
        background-color: {EIFFAGE_BLACK};
        color: white;
    }}

    .tooltip-text {{
        visibility: hidden;
        width: 300px;
        background-color: {EIFFAGE_BLACK};
        color: #ffffff;
        text-align: left;
        border-radius: 12px;
        padding: 15px 20px;
        position: absolute;
        z-index: 9999; 
        top: 135%; 
        right: -10px; 
        opacity: 0;
        transition: opacity 0.2s, bottom 0.2s;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        font-size: 0.9em;
        line-height: 1.5;
        font-weight: 400;
    }}

    .info-container:hover .tooltip-text {{
        visibility: visible;
        opacity: 1;
        top: 125%; 
    }}

    .tooltip-text::after {{
        content: "";
        position: absolute;
        bottom : 100%;
        right: 20px;
        margin-left: -5px;
        border-width: 6px;
        border-style: solid;
        border-color: {EIFFAGE_BLACK} transparent transparent transparent;
    }}

    .tooltip-text ul, .tooltip-text ol {{
        margin-top: 8px;
        margin-bottom: 10px;
        padding-left: 20px;
    }}

    .tooltip-text a {{
        color: #FF8E7D;
        text-decoration: none;
        font-weight: 600;
    }}
    .tooltip-text a:hover {{ text-decoration: underline; }}

    /* Texte de description de la carte */
    .app-card p.description {{
        flex-grow: 1; 
        font-size: 1em;
        color: {TEXT_COLOR};
        line-height: 1.6;
        margin-bottom: 25px;
        opacity: 0.85;
    }}

    /* Boutons d'action modernisés */
    .app-button {{
        display: flex; 
        justify-content: center;
        align-items: center;
        padding: 14px 20px;
        background-color: {EIFFAGE_RED}; 
        color: #ffffff !important;
        text-decoration: none;
        font-size: 1em;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease; 
        width: 100%; 
        border: none;
    }}
    .app-button:hover {{
        background-color: {EIFFAGE_BLACK};
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}

    /* Pied de page */
    .footer-container {{
        text-align: center;
        margin-top: 60px;
        padding-top: 30px;
        border-top: 1px solid rgba(0,0,0,0.05);
        font-size: 0.9em;
        color: #777777;
    }}
    .footer-container a {{
        color: {EIFFAGE_RED};
        text-decoration: none;
        font-weight: bold;
    }}
    .footer-container a:hover {{ text-decoration: underline; }}
    </style>
""", unsafe_allow_html=True)

# 4. En-tête avec Logo, Titre et Légende d'accès
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_filename = "Eiffage_Énergie_Systèmes.svg (2).png"

try:
    img_base64 = get_base64_image(image_filename)
    img_tag = f'<img src="data:image/png;base64,{img_base64}" width="220" alt="Logo Eiffage">'
except FileNotFoundError:
    img_tag = f'<p style="color:{EIFFAGE_RED}; font-weight:bold;">⚠️ Image introuvable</p>'

st.markdown(f"""
    <div class="header-container">
        <div class="header-left">
            {img_tag}
            <div class="main-title">Portail d'Applications</div>
        </div>
        <div class="header-right">
            <div class="legend-title">Informations d'accès</div>
            <div class="legend-item">
                <span class="badge badge-local badge-inline">🔒 Local</span> 
                Accessible uniquement sur le réseau Eiffage (bureau en Wi-Fi/câble ou VPN). Inaccessible en télétravail direct.
            </div>
            <div class="legend-item" style="margin-top: 10px;">
                <span class="badge badge-cloud badge-inline">☁️ Cloud</span> 
                Accessible de n'importe où, même depuis un ordinateur ou téléphone personnel.
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# 5. LIGNE 1 : Les deux applications OptiRout'EES
col1, col2 = st.columns(2)



with col1:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <div>
                <span class="badge badge-local">🔒 Local</span>
                <h2>OptiRout'EES <span class="subtitle">Outil Général</span></h2>
            </div>
            <div class="info-container">
                <div class="info-icon">?</div>
                <div class="tooltip-text">
                    <strong>Solution d'optimisation sur-mesure</strong><br><br>
                    Marche à suivre :
                    <ol>
                        <li>Renseignez le gabarit Excel type téléchargeable dans l'application.</li>
                        <li>Obtenez vos coordonnées GPS et calculez votre matrice via les outils cartographies et matrice de temps de route.</li>
                        <li>Importez votre dossier pour générer les tournées.</li>
                    </ol>
                    L'application génère l'itinéraire idéal et suggère des sites complémentaires si la journée du technicien n'est pas pleine.<br><br>
                </div>
            </div>
        </div>
        <p class="description">La solution polyvalente pour optimiser les itinéraires de vos techniciens en itinérance, applicable à n'importe quel contrat de maintenance.</p>
        <a href="http://172.17.38.0:8502/" target="_blank" class="app-button">Accéder à OptiRout'EES (Général)</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <div>
                <span class="badge badge-local">🔒 Local</span>
                <h2>OptiRout'EES <span class="subtitle">Contrat La Poste Immobilier</span></h2>
            </div>
            <div class="info-container">
                <div class="info-icon">?</div>
                <div class="tooltip-text">
                    <strong>Optimisation des tournées - LPI</strong><br><br>
                    Application connectée en temps réel au fichier de suivi Prise en Charge (PEC). Elle intègre automatiquement les mises à jour Excel et génère les itinéraires de maintenance les plus performants pour plus de 500 sites.<br><br>
                    <strong>⚠️ Accès restreint</strong><br>
                    Un mot de passe est nécessaire. Pour l'obtenir, <a href="mailto:methodesmaintenance.energie@eiffage.com">contactez le support </a>
                </div>
            </div>
        </div>
        <p class="description">Générez et optimisez les tournées des techniciens avec une synchronisation dynamique des données PEC, un outil sur-mesure pour le contrat LPI.</p>
        <a href="http://172.17.38.0:8501/" target="_blank" class="app-button">Accéder à OptiRout'EES (LPI)</a>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# 6. LIGNE 2 : Outils transverses (Cartes et OSRM)
col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <div>
                <span class="badge badge-cloud">☁️ Cloud</span>
                <h2>Cartographie & Sectorisation</h2>
            </div>
            <div class="info-container">
                <div class="info-icon">?</div>
                <div class="tooltip-text">
                    <strong>Visualisation de données géographiques</strong><br><br>
                    Exportez et visualisez vos données selon 3 logiques :
                    <ul>
                        <li><strong>Intelligente :</strong> Sectorisation automatique selon le nombre de zones souhaité.</li>
                        <li><strong>Réseau :</strong> Découpage basé sur les agences Clévia Centre-Est.</li>
                        <li><strong>Sur-mesure :</strong> Basé sur vos propres critères (Technicien, Chargé d'affaires, secteur d'activité...).</li>
                    </ul>
                    Permet également d'exporter les coordonnées GPS.<br><br>
                </div>
            </div>
        </div>
        <p class="description">Transformez vos données brutes en cartes interactives. Un outil puissant pour visualiser vos secteurs d'intervention et répartir la charge de travail.</p>
        <a href="https://creation-carte.streamlit.app/" target="_blank" class="app-button">Ouvrir l'outil de Cartographie</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="app-card">
        <div class="app-card-header">
            <div>
                <span class="badge badge-local">🔒 Local</span>
                <h2>Matrice des Temps (OSRM)</h2>
            </div>
            <div class="info-container">
                <div class="info-icon">?</div>
                <div class="tooltip-text">
                    <strong>Moteur de calcul logistique interne</strong><br><br>
                    Cette interface s'appuie sur notre serveur OSRM local (France métropolitaine). Elle permet de croiser massivement des coordonnées GPS pour générer des matrices (export CSV).<br><br>
                    <em>Prérequis indispensable avant d'ajouter de nouveaux contrats dans OptiRout'EES.</em><br><br>
                </div>
            </div>
        </div>
        <p class="description">Calculez instantanément les temps de route entre plusieurs centaines de points d'intervention. Indispensable pour paramétrer un nouveau contrat sur OptiRout'EES.</p>
        <a href="http://172.17.38.0:8503/" target="_blank" class="app-button">Lancer le Calculateur (OSRM)</a>
    </div>
    """, unsafe_allow_html=True)

# 7. Pied de page
st.markdown(f"""
    <div class="footer-container">
        Développé pour <strong>Eiffage Énergie Systèmes - Clévia</strong><br>
        Pour toute assistance, contactez le service : <br>
        <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
    </div>
""", unsafe_allow_html=True)
