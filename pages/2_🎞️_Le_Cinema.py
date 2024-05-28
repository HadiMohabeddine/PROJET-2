import streamlit as st
import pandas as pd
col1, col2, col3 = st.columns(3)
with col2:
    st.image('images\gueret.png', use_column_width=True)

st.markdown(' ## Le cinéma pas à pas : ')
col1, col2, col3  = st.columns([0.25,0.5,0.25])
with col2 : 
    st.image('images\image_2.png')



import streamlit as st

# Style CSS pour augmenter la taille du texte
st.markdown("""
    <style>
        .large-font {
            font-size:18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Contenu avec la classe CSS appliquée
st.markdown("""
## Le Cinéma Gueret

<div class="large-font">
    Le Cinéma Gueret, un équipement municipal guérétois, géré par l'association CRPI Le Sénéchal (loi 1901) depuis 1992.
</div>

## Un Lieu de Vie

<div class="large-font">
    Le Cinéma Gueret, bien plus qu'un cinéma, est avant tout un lieu de vie où se retrouvent tous les publics creusois. Situé au coeur de la ville de Guéret, il propose tout au long de l'année un grand nombre de films de tous genres pour satisfaire au mieux les goûts de chacun.
</div>

## Un Lieu de Culture Dynamique

<div class="large-font">
    Le Cinéma Gueret est un lieu de culture dynamique qui propose tout au long de l'année, en plus de sa programmation, un agenda d'évènements mêlant le cinéma à bien d'autres domaines artistiques.
</div>

## En Lien avec la Communauté

<div class="large-font">
    Intégré au coeur de la cité, le cinéma est en lien permanent avec le tissu associatif culturel, institutionnel, d'éducation populaire, permettant d'ouvrir le public, au delà de l'image, à l'échange et à la réflexion.
</div>
""", unsafe_allow_html=True)
col1, col2, col3  = st.columns([0.25,0.5,0.25])
with col2 : 
    st.image("images/entrée.jpg", use_column_width=True)

st.markdown("""
## Nos Chiffres Clés

<div class="large-font">
    - Nous sommes ouverts tous les jours de l'année, proposons plus de 2300 titres & plus de 6500 séances par an. Nous projetons principalement des Drames, des Thrillers et des films d'Animation pour petits et grands !<br>
    - En 2019 notre cinéma a réalisé 115 000 entrées.<br>
    - Nous sommes impliqués activement dans les dispositifs d'éducation à l'image : maternelle, école, collèges et lycéens au cinéma.<br>
    - Le Cinéma Gueret est un cinéma associatif (non subventionné) géré par le CRPI - Centre Régional de Promotion de l'Image - association Limousine loi 1901. La gestion est en affermage avec la Mairie de Guéret depuis 1991.
</div>
""", unsafe_allow_html=True)


