import streamlit as st
import pandas as pd
import base64


st.title('Ici retrouvez vos films préférés, leur bande-annonce etc.')


couleur_fond ='#F7F2D6'
st.markdown(f"""
    <style>
        body {{
            background-color: {couleur_fond};
        }}
    </style>
""", unsafe_allow_html=True)


link = "datasets\df_ultimate_2.csv"
df_movies = pd.read_csv(link)

   
with st.container():
   col1, col2, col3, col4, col5, col6, col7 = st.columns([0.25, 0.05, 0.05, 0.3, 0.05,0.05,0.25], gap="small")

   with col1:
      st.write(" Recherchez un film ou un mot clé")
      prompt1 = st.chat_input("Veuillez entrer un titre ou un moto clé...")
      
   with col7:
      option = st.selectbox(
      " ## Recherchez par genre",
      ('Documentary', 'Adventure', 'Biography', 'Mystery', 'Sci-Fi', 'History', 'Crime', 'Drama', 'Family', 'Sport', 'Horror', 'Animation', 'Thriller', 'Musical', 'War', 'Comedy', 'Romance', 'Action', 'Fantasy', 'Music', 'Western'),
       index=None,
       placeholder="Selectionnez un genre...",)
col1, col2, col3 = st.columns(3)    
with col2:
    st.image("images\wildprimevideo.png")
      
st.write("--------------")    
         
if prompt1:
                    resultats = df_movies[df_movies['title_y'].str.contains(prompt1, case=False) ]
                    if len(resultats) == 0 :
                        resultats = df_movies[df_movies['name_x'].str.contains(prompt1, case=False)]
                    if not resultats.empty:
                            resultats = resultats.sort_values(by='averageRating_y', ascending=False).head(5)
                            for index, row in resultats.iterrows():
                                st.write("--------------")                                      
                                with st.container(): 
                                    col1, col2 = st.columns([0.2, 0.8])
                                    with col1:
                                         st.image(row['poster_path'], caption=row['title_y'], use_column_width=True)
                                         st.write("     ")
                                        
                                    with col2:
                                         st.subheader('Description')
                                         st.write("     ")
                                         st.markdown(row['overview'])
                                         st.write("--------------")
                                         st.write("Durée :  " + str(row['runtimeMinutes_y']) +" minutes" )
                                         st.write("Note :  " + str(row['averageRating_y']) + " / 10" )  
                                         st.write("--------------")
                                         st.subheader("Bande d'annonce") 

                                         col1, col2, col3 = st.columns([0.1,0.8, 0.1])    

                                         with col2:                                                                      
                                           st.video(row['lien']) 
                                         st.write("--------------") 
                                         with st.container(border=True):                              
                                            st.subheader('Vous aimerez aussi ces films...')
                                            st.write("     ")

                                            col1, col2, col3, col4= st.columns([0.15, 0.4, 0.15, 0.4])
                                            with col1:
                                                st.image(row['post_reco1'], use_column_width=True)   
                                                                            
                                            with col2:      
                                                st.subheader(f"{row['title_reco1']}")
                                                with st.expander("Plus de détail..."):                              
                                                    st.write("Note :  " + str(row['note_reco1']) + " / 10" )
                                                    st.write("--------------")
                                                    st.write(f" Synopssis : {row['descrip_reco1']}")
                                                    st.write("--------------")
                                                    st.write("Bande d'annonce")
                                                    st.video(row['lien_reco1'])
                                                    
                                                                                                                                                                            
                                            with col3:
                                                st.image(row['post_reco2'], use_column_width=True)

                                            with col4:
                                                    st.subheader(f"{row['title_reco2']}")
                                                    with st.expander("Plus de détail..."):                              
                                                        st.write("Note :  " + str(row['note_reco2']) + " / 10" )
                                                        st.write("--------------")
                                                        st.write(f" Synopssis : {row['descrip_reco2']}")
                                                        st.write("--------------")
                                                        st.write("Bande d'annonce")
                                                        st.video(row['lien_reco2'])
                                                                                         
                                            
                                                                    
                    else:
                       st.write("Désolé nous n'avons aucun résultat pour ces informations") 

      

if option:
                    resultats = df_movies[df_movies['genres_y'].str.contains(option, case=False)]
                    if not resultats.empty:
                            resultats = resultats.sort_values(by='averageRating_y', ascending=False).head(10)
                            for index, row in resultats.iterrows():
                                st.write("--------------")

                                with st.container(): 
                                    col1, col2 = st.columns([0.3, 0.7])

                                    with col1:
                                         st.image(row['poster_path'], caption=row['title_y'], use_column_width=True)
                                         st.write("     ")

                                    with col2:
                                         st.subheader('Description')
                                         st.write("     ")
                                         st.markdown(row['overview'])
                                         st.write("--------------")
                                         st.write("Durée :  " + str(row['runtimeMinutes_y']) +" minutes" )
                                         st.write("Note :  " + str(row['averageRating_y']) + " / 10" ) 
                                         with st.container(border=True): 
                                          st.subheader('Vous aimerez aussi ces films...')
                                          st.write("     ")
                                         
                                          col1, col2, col3, col4= st.columns([0.1, 0.4, 0.1, 0.4])
                                          with col1:
                                             st.image(row['post_reco1'], use_column_width=True)   
                                                                         
                                          with col2:
                                              st.subheader(f"{row['title_reco1']}")
                                              with st.expander("Plus de détail..."):                              
                                                st.write("Note :  " + str(row['note_reco1']) + " / 10" )
                                                st.write("--------------")
                                                st.write(f" Synopssis : {row['descrip_reco1']}")
                                                st.write("--------------")
                                                st.write("Bande d'annonce")
                                                st.video(row['lien_reco1'])
                                              
                                                                                                                                                                        
                                         with col3:
                                              st.image(row['post_reco2'], use_column_width=True)
                                         with col4:
                                                st.subheader(f"{row['title_reco2']}")
                                                with st.expander("Plus de détail..."):                              
                                                 st.write("Note :  " + str(row['note_reco2']) + " / 10" )
                                                 st.write("--------------")
                                                 st.write(f" Synopssis : {row['descrip_reco2']}")
                                                 st.write("--------------")
                                                 st.write("Bande d'annonce")
                                                 st.video(row['lien_reco2'])
                                                
                                                                    
                    else:
                        st.write("Désolé nous n'avons aucun résultat pour ces informations") 
        

   
