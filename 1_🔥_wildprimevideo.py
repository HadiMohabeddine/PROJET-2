import streamlit as st
st.set_page_config(layout="wide")

# Style CSS pour augmenter la taille du texte
st.markdown("""
    <style>
        .large-font {
            font-size:18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Afficher l'image avec une largeur spécifiée
st.image('images/wildprimevideo.png', width=450)

# Contenu avec la classe CSS appliquée
st.markdown('## Bienvenue sur le système de recommandation de films du Cinéma Guerét')

st.markdown("""
<div class="large-font">
    Ici retrouvez notre Demo.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="large-font">
    Via nos différents onglets, retrouvez l'ensemble des films que le Cinéma Gueret met à la disposition de ses spectateurs.
</div>
""", unsafe_allow_html=True)