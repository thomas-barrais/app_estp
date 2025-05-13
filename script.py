import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Trail App", layout="wide")

# Header commun
st.markdown("""
    <style>
        .main-header {
            font-size: 36px;
            font-weight: bold;
            color: #2E8B57;
            text-align: center;
            margin-bottom: 30px;
        }
        .sub-header {
            font-size: 24px;
            font-weight: bold;
            color: #2E8B57;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Bienvenue sur Trail App</div>', unsafe_allow_html=True)

# Navigation entre les pages
page = st.sidebar.radio("Navigation", ["Présentation de l'athlète", "Présentation de la marque", "Contact"])

# Page : Présentation de l'athlète
if page == "Présentation de l'athlète":
    st.markdown('<div class="sub-header">Présentation de l\'athlète</div>', unsafe_allow_html=True)
    st.image("greg-rosenke-E9PdTVfEujI-unsplash.jpg", caption="Athlète de trail", use_container_width=True)
    st.write("""
    **Nom :** Alex Montagne  
    **Âge :** 29 ans  
    **Spécialité :** Trail long et ultra-trail  
    **Palmarès :**
    - 1er - Trail des Volcans 2022
    - 2e - Ultra du Jura 2023
    - 4e - UTMB 2024

    Passionné par les grands espaces, Alex s'entraîne en montagne toute l'année et partage ses aventures sur les réseaux sociaux.
    """)

# Page : Présentation de la marque
elif page == "Présentation de la marque":
    st.markdown('<div class="sub-header">Présentation de la marque</div>', unsafe_allow_html=True)
    st.image("mary-hammel-pjKPi8SpqiQ-unsplash.jpg", caption="Marque de trail", use_container_width=True)
    st.write("""
    **Nom :** SummitTrail Gear  
    **Fondée en :** 2017  
    **Spécialité :** Équipement de trail haute performance (chaussures, sacs, vêtements)

    SummitTrail Gear conçoit des produits testés par des athlètes de haut niveau dans des conditions extrêmes. Son objectif : repousser les limites du possible avec confort et performance.
    """)

# Page : Contact
elif page == "Contact":
    st.markdown('<div class="sub-header">Contact</div>', unsafe_allow_html=True)
    with st.form("contact_form"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")

        if submitted:
            st.success("Merci pour votre message ! Nous vous répondrons rapidement.")
