import streamlit as st
st.markdown('## Bienvenue sur notre système de recommandation de films en partenariat avec le Cinéma Guerét ')

st.markdown('')
st.markdown('')
st.markdown('')
col1, col2, col3= st.columns([0.3,0.25,0.35])

with col2:
     
     st.markdown('##      Qui sommes nous ? ')
     st.markdown('')
     st.markdown('')
     st.markdown('')
     
col1, col2, col3= st.columns([0.25,0.3,0.35])
with col2:
     st.image("images\Capture_d_écran_2024-05-15_150838-removebg-preview.png")
# Style CSS pour augmenter la taille du texte
st.markdown("""
    <style>
        .large-font {
            font-size:18px;
        }
    </style>
    """, unsafe_allow_html=True)

# Contenu avec la classe CSS appliquée
st.markdown('')

st.markdown('')

st.markdown("""
## Data Wave Innovations

<div class="large-font">
    Data Wave Innovations est une entreprise de pointe spécialisée dans l'analyse de données et les solutions innovantes qui en découlent. Notre mission est d'exploiter le pouvoir des données pour apporter des insights précieux et des solutions stratégiques à nos clients, les aidant ainsi à prendre des décisions éclairées et à rester compétitifs sur leur marché.
</div>
""", unsafe_allow_html=True)
col1, col2, col3= st.columns([0.3,0.45,0.25])

with col2:
     
     st.markdown('## Notre équipe se compose des meilleurs :  ')


col1, col2, col3, col4= st.columns(4)
with col1 :
    st.markdown("<h1 style='text-align: center;'>Dylan</h1>", unsafe_allow_html=True)
    st.image("images\dylan.jpg",use_column_width=True)
    st.write('## Expert Power BI')
with col2 :
    st.markdown("<h1 style='text-align: center;'>Hadi</h1>", unsafe_allow_html=True)
    st.image("images\hadi.jpg", use_column_width=True)
    st.write('')
    st.write('## Expert Streamlit')
with col3 :
    st.markdown("<h1 style='text-align: center;'>Henri</h1>", unsafe_allow_html=True)
    st.image("images\henri.jpg", width = 380, use_column_width=True)
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.write('## Expert Machine Learning')
    
with col4 :
    st.markdown("<h1 style='text-align: center;'>Idrissa</h1>", unsafe_allow_html=True)
    st.image("images\idrissa.jpg", use_column_width=True)
    st.write('## Expert Power BI')