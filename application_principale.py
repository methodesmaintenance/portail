import streamlit as st
import base64

# 1. Configuration de la page
st.set_page_config(
    page_title="Portail d'Applications | Eiffage Énergie Systèmes",
    page_icon="🏢",
    layout="wide"
)

# 2. Charte graphique EIFFAGE — Version lumineuse
EIFFAGE_BLACK = "#111111"
EIFFAGE_RED = "#E63312"
BG_COLOR = "#FFFFFF"
TEXT_COLOR = "#2A2A2A"
CARD_BG = "#FFFFFF"
SUBTLE_GRAY = "#6B7280"
LIGHT_SURFACE = "#F7F8FA"

# 3. CSS personnalisé — Version Lumineuse Moderne
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ═══════════════════════════════════════
       CONFIGURATION GLOBALE
       ═══════════════════════════════════════ */
    .stApp {{
        background: {BG_COLOR};
        color: {TEXT_COLOR};
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }}

    #MainMenu, footer, header {{visibility: hidden;}}
    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }}

    /* ═══════════════════════════════════════
       ANIMATIONS
       ═══════════════════════════════════════ */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(25px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    /* ═══════════════════════════════════════
       EN-TÊTE (HERO) — VERSION LUMINEUSE
       ═══════════════════════════════════════ */
    .hero-section {{
        background: {LIGHT_SURFACE};
        border-radius: 20px;
        padding: 48px 40px 44px 40px;
        text-align: center;
        margin-bottom: 45px;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.6s ease-out;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }}

    /* Ligne d'accent rouge en haut */
    .hero-section::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 60px;
        height: 4px;
        background: {EIFFAGE_RED};
        border-radius: 0 0 4px 4px;
    }}

    /* Cercle décoratif subtil */
    .hero-section::after {{
        content: '';
        position: absolute;
        top: -60px;
        right: -60px;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, rgba(230, 51, 18, 0.04) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }}

    .hero-logo {{
        margin-bottom: 22px;
        position: relative;
        z-index: 1;
    }}

    .hero-title {{
        color: {EIFFAGE_BLACK};
        font-size: 2.5em;
        font-weight: 800;
        margin: 0 0 8px 0;
        letter-spacing: -1px;
        position: relative;
        z-index: 1;
    }}

    .hero-subtitle {{
        color: {SUBTLE_GRAY};
        font-size: 1.05em;
        font-weight: 400;
        letter-spacing: 0.3px;
        position: relative;
        z-index: 1;
    }}

    .hero-badge {{
        display: inline-block;
        background: rgba(230, 51, 18, 0.08);
        border: 1px solid rgba(230, 51, 18, 0.15);
        color: {EIFFAGE_RED};
        padding: 6px 18px;
        border-radius: 50px;
        font-size: 0.82em;
        font-weight: 600;
        margin-top: 18px;
        position: relative;
        z-index: 1;
        letter-spacing: 0.3px;
    }}

    /* ═══════════════════════════════════════
       TITRES DE SECTION
       ═══════════════════════════════════════ */
    .section-header {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 25px;
        animation: fadeInUp 0.6s ease-out 0.15s both;
    }}

    .section-header h3 {{
        color: {EIFFAGE_BLACK};
        font-size: 1.25em;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.3px;
    }}

    .section-header .section-icon {{
        background: {EIFFAGE_RED};
        color: white;
        width: 34px;
        height: 34px;
        border-radius: 9px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1em;
    }}

    .section-header::after {{
        content: '';
        flex: 1;
        height: 1px;
        background: linear-gradient(to right, rgba(0,0,0,0.06), transparent);
        margin-left: 10px;
    }}

    /* ═══════════════════════════════════════
       CARTES D'APPLICATION
       ═══════════════════════════════════════ */
    .app-card {{
        background: {CARD_BG};
        border-radius: 16px;
        border: 1px solid rgba(0, 0, 0, 0.06);
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
        padding: 32px;
        margin-bottom: 25px;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        animation: fadeInUp 0.6s ease-out 0.25s both;
        position: relative;
        overflow: hidden;
    }}

    .app-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: {EIFFAGE_RED};
        opacity: 0;
        transition: opacity 0.3s ease;
    }}

    .app-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.07);
        border-color: rgba(230, 51, 18, 0.12);
    }}

    .app-card:hover::before {{
        opacity: 1;
    }}

    /* En-tête de la carte */
    .app-card-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 16px;
    }}

    .app-card-title-group {{
        display: flex;
        align-items: flex-start;
        gap: 14px;
        flex: 1;
    }}

    .app-card-emoji {{
        font-size: 2em;
        line-height: 1;
        margin-top: 2px;
    }}

    .app-card-header h2 {{
        color: {EIFFAGE_BLACK};
        font-size: 1.3em;
        font-weight: 700;
        margin: 0;
        line-height: 1.3;
        letter-spacing: -0.3px;
    }}

    .app-card-header h2 .card-subtitle {{
        font-size: 0.78em;
        color: {EIFFAGE_RED};
        font-weight: 600;
        display: block;
        margin-top: 3px;
    }}

    /* Badge de statut */
    .status-badge {{
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 4px 10px;
        border-radius: 50px;
        font-size: 0.72em;
        font-weight: 600;
        white-space: nowrap;
        margin-top: 8px;
    }}

    .status-badge.internal {{
        background: rgba(16, 185, 129, 0.08);
        color: #059669;
        border: 1px solid rgba(16, 185, 129, 0.15);
    }}

    .status-badge.external {{
        background: rgba(59, 130, 246, 0.08);
        color: #2563EB;
        border: 1px solid rgba(59, 130, 246, 0.15);
    }}

    /* Icône info et Tooltip */
    .info-container {{
        position: relative;
        display: inline-block;
        flex-shrink: 0;
    }}

    .info-icon {{
        cursor: pointer;
        color: {SUBTLE_GRAY};
        background-color: {LIGHT_SURFACE};
        border-radius: 50%;
        min-width: 30px;
        height: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 700;
        font-size: 0.85em;
        transition: all 0.25s ease;
        border: 1px solid rgba(0, 0, 0, 0.06);
    }}

    .info-icon:hover {{
        background-color: {EIFFAGE_BLACK};
        color: white;
        transform: scale(1.1);
    }}

    .tooltip-text {{
        visibility: hidden;
        width: 350px;
        background: {EIFFAGE_BLACK};
        color: #ffffff;
        text-align: left;
        border-radius: 14px;
        padding: 20px 24px;
        position: absolute;
        z-index: 9999;
        bottom: 140%;
        right: 0;
        opacity: 0;
        transition: opacity 0.25s ease, transform 0.25s ease;
        transform: translateY(5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
        font-size: 0.88em;
        line-height: 1.6;
        font-weight: 400;
    }}

    .info-container:hover .tooltip-text {{
        visibility: visible;
        opacity: 1;
        transform: translateY(0);
    }}

    .tooltip-text::after {{
        content: "";
        position: absolute;
        top: 100%;
        right: 12px;
        border-width: 7px;
        border-style: solid;
        border-color: {EIFFAGE_BLACK} transparent transparent transparent;
    }}

    .tooltip-text strong {{
        color: #FF6B57;
        font-size: 1.05em;
    }}

    .tooltip-text ul, .tooltip-text ol {{
        margin-top: 8px;
        margin-bottom: 10px;
        padding-left: 18px;
    }}

    .tooltip-text li {{
        margin-bottom: 4px;
    }}

    .tooltip-text em {{
        color: rgba(255, 255, 255, 0.55);
        font-size: 0.92em;
    }}

    .tooltip-text a {{
        color: #FF6B57;
        text-decoration: none;
        font-weight: 600;
    }}
    .tooltip-text a:hover {{
        color: #FFB4A8;
        text-decoration: underline;
    }}

    /* Description */
    .app-card p.description {{
        flex-grow: 1;
        font-size: 0.96em;
        color: {SUBTLE_GRAY};
        line-height: 1.7;
        margin-bottom: 24px;
    }}

    /* ═══════════════════════════════════════
       BOUTONS D'ACTION
       ═══════════════════════════════════════ */
    .app-button {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        padding: 14px 24px;
        background: {EIFFAGE_RED};
        color: #ffffff !important;
        text-align: center;
        text-decoration: none;
        font-size: 0.93em;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        width: 100%;
        letter-spacing: 0.2px;
        position: relative;
        overflow: hidden;
    }}

    .app-button::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.12), transparent);
        transition: left 0.5s ease;
    }}

    .app-button:hover {{
        background: {EIFFAGE_BLACK};
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
    }}

    .app-button:hover::before {{
        left: 100%;
    }}

    .app-button .btn-arrow {{
        transition: transform 0.3s ease;
        font-size: 1.1em;
    }}

    .app-button:hover .btn-arrow {{
        transform: translateX(4px);
    }}

    /* ═══════════════════════════════════════
       SÉPARATEUR
       ═══════════════════════════════════════ */
    hr {{
        border: 0;
        height: 1px;
        background: linear-gradient(to right, transparent, rgba(0, 0, 0, 0.05), transparent);
        margin: 10px 0 35px 0;
    }}

    /* ═══════════════════════════════════════
       PIED DE PAGE
       ═══════════════════════════════════════ */
    .footer-container {{
        text-align: center;
        margin-top: 60px;
        padding: 32px 30px;
        background: {LIGHT_SURFACE};
        border-radius: 16px;
        border: 1px solid rgba(0, 0, 0, 0.04);
        animation: fadeInUp 0.6s ease-out 0.4s both;
    }}

    .footer-brand {{
        font-size: 1em;
        font-weight: 700;
        color: {EIFFAGE_BLACK};
        margin-bottom: 6px;
    }}

    .footer-contact {{
        font-size: 0.9em;
        color: {SUBTLE_GRAY};
        margin-bottom: 10px;
    }}

    .footer-container a {{
        color: {EIFFAGE_RED};
        text-decoration: none;
        font-weight: 600;
        transition: color 0.2s;
    }}
    .footer-container a:hover {{
        color: {EIFFAGE_BLACK};
        text-decoration: underline;
    }}

    .footer-divider {{
        width: 40px;
        height: 2px;
        background: {EIFFAGE_RED};
        margin: 14px auto;
        border-radius: 1px;
    }}

    .footer-copy {{
        font-size: 0.78em;
        color: rgba(0,0,0,0.25);
    }}
    </style>
""", unsafe_allow_html=True)

# 4. Logo
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

image_filename = "Eiffage_Énergie_Systèmes.svg (2).png"

try:
    img_base64 = get_base64_image(image_filename)
    img_tag = f'<img src="data:image/png;base64,{img_base64}" width="220" alt="Logo Eiffage">'
except FileNotFoundError:
    img_tag = f'<p style="color:{EIFFAGE_RED};">⚠️ Image "{image_filename}" introuvable.</p>'

# 5. Section Hero — Lumineuse
st.markdown(f"""
    <div class="hero-section">
        <div class="hero-logo">
            {img_tag}
        </div>
        <div class="hero-title">Portail d'Applications</div>
        <div class="hero-subtitle">Eiffage Énergie Systèmes — Clévia Centre-Est</div>
        <div class="hero-badge">✦ Maintenance & Optimisation</div>
    </div>
""", unsafe_allow_html=True)

# 6. SECTION : Optimisation des tournées
st.markdown("""
    <div class="section-header">
        <div class="section-icon">🚀</div>
        <h3>Optimisation des Tournées</h3>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <div class="app-card-header">
                <div class="app-card-title-group">
                    <div class="app-card-emoji">📮</div>
                    <div>
                        <h2>OptiRout'EES <span class="card-subtitle">La Poste Immobilier</span></h2>
                        <div class="status-badge internal">🟢 Réseau interne</div>
                    </div>
                </div>
                <div class="info-container">
                    <div class="info-icon">?</div>
                    <div class="tooltip-text">
                        <strong>Contrat LPI — Optimisation des tournées</strong><br><br>
                        Application connectée directement au fichier de suivi PEC. Elle intègre automatiquement les horaires mis à jour pour plus de 500 sites afin de générer les itinéraires de maintenance les plus efficaces.<br><br>
                        <em>⚠️ Nécessite un accès au réseau interne Eiffage.</em><br><br>
                        Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                    </div>
                </div>
            </div>
            <p class="description">Générez et optimisez les tournées de vos techniciens pour le contrat La Poste Immobilier, avec synchronisation dynamique des données PEC.</p>
        </div>
        <a href="http://172.17.38.0:8501/" target="_blank" class="app-button">
            Accéder à OptiRout'EES (LPI) <span class="btn-arrow">→</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <div class="app-card-header">
                <div class="app-card-title-group">
                    <div class="app-card-emoji">🔧</div>
                    <div>
                        <h2>OptiRout'EES <span class="card-subtitle">Outil Général</span></h2>
                        <div class="status-badge internal">🟢 Réseau interne</div>
                    </div>
                </div>
                <div class="info-container">
                    <div class="info-icon">?</div>
                    <div class="tooltip-text">
                        <strong>L'optimisation sur-mesure pour tous contrats</strong><br><br>
                        Démarche d'utilisation :
                        <ol>
                            <li>Remplissez le gabarit Excel type fourni.</li>
                            <li>Obtenez vos coordonnées GPS et calculez votre matrice (via l'outil OSRM).</li>
                            <li>Importez votre dossier complet pour générer vos tournées optimisées.</li>
                        </ol>
                        <em>⚠️ Nécessite un accès au réseau interne Eiffage.</em><br><br>
                        Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                    </div>
                </div>
            </div>
            <p class="description">La solution universelle pour optimiser les itinéraires de vos équipes, quel que soit le contrat, l'agence ou le secteur d'activité visé.</p>
        </div>
        <a href="http://172.17.38.0:8502/" target="_blank" class="app-button">
            Accéder à OptiRout'EES (Général) <span class="btn-arrow">→</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. SECTION : Outils Transverses
st.markdown("""
    <div class="section-header">
        <div class="section-icon">🛠️</div>
        <h3>Outils Transverses</h3>
    </div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <div class="app-card-header">
                <div class="app-card-title-group">
                    <div class="app-card-emoji">🗺️</div>
                    <div>
                        <h2>Générateur de Cartes & Sectorisation</h2>
                        <div class="status-badge external">🌐 Accès cloud</div>
                    </div>
                </div>
                <div class="info-container">
                    <div class="info-icon">?</div>
                    <div class="tooltip-text">
                        <strong>Cartographie HTML interactive</strong><br><br>
                        Module permettant de visualiser et d'exporter vos données selon 3 logiques :
                        <ul>
                            <li><strong>K-means :</strong> Sectorisation automatique par zone.</li>
                            <li><strong>Réseau :</strong> Basée sur les agences Clévia Centre-Est.</li>
                            <li><strong>Sur-mesure :</strong> Basée sur vos propres colonnes.</li>
                        </ul>
                        Permet l'export CSV des coordonnées GPS.<br><br>
                        Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                    </div>
                </div>
            </div>
            <p class="description">Transformez vos données en cartes interactives. Idéal pour visualiser vos secteurs d'intervention, répartir la charge et exporter vos coordonnées GPS.</p>
        </div>
        <a href="https://creation-carte.streamlit.app/" target="_blank" class="app-button">
            Accéder à la Cartographie <span class="btn-arrow">→</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="app-card">
        <div>
            <div class="app-card-header">
                <div class="app-card-title-group">
                    <div class="app-card-emoji">⏱️</div>
                    <div>
                        <h2>Matrice des Temps de Trajet (OSRM)</h2>
                        <div class="status-badge internal">🟢 Réseau interne</div>
                    </div>
                </div>
                <div class="info-container">
                    <div class="info-icon">?</div>
                    <div class="tooltip-text">
                        <strong>Moteur de calcul logistique</strong><br><br>
                        Cette interface s'appuie sur le serveur OSRM local. Elle permet de croiser massivement des coordonnées GPS pour générer des matrices de temps de route et de distances sur tout le territoire français.<br><br>
                        <em>⚠️ Nécessite un accès au réseau interne Eiffage.</em><br><br>
                        Assistance : <a href="mailto:methodesmaintenance.energie@eiffage.com">Contactez le support</a>
                    </div>
                </div>
            </div>
            <p class="description">Outil fondamental de planification : calculez instantanément les temps de parcours réels entre plusieurs centaines de points d'intervention en France.</p>
        </div>
        <a href="http://172.17.38.0:8503/" target="_blank" class="app-button">
            Accéder au Calculateur de Temps <span class="btn-arrow">→</span>
        </a>
    </div>
    """, unsafe_allow_html=True)

# 8. Pied de page
st.markdown(f"""
    <div class="footer-container">
        <div class="footer-brand">Eiffage Énergie Systèmes — Clévia</div>
        <div class="footer-contact">
            Pour toute assistance technique, méthode ou évolution, contactez le service :
        </div>
        <a href="mailto:methodesmaintenance.energie@eiffage.com">methodesmaintenance.energie@eiffage.com</a>
        <div class="footer-divider"></div>
        <div class="footer-copy">© 2026 — Portail développé par le service Méthodes Maintenance</div>
    </div>
""", unsafe_allow_html=True)
