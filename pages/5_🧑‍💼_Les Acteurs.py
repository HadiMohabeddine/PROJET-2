import streamlit as st
import pandas as pd
#doc : https://docs.streamlit.io/develop/api-reference/widgets
st.set_page_config(
    page_title="Wild Prime Video",
    page_icon="🎥",
    layout="wide")
df  = pd.read_csv(r"datasets\actors_final_version(2).csv", sep = ",")
ultimate = pd.read_csv(r"datasets\df_ultimate_2.csv", sep = ",")


ultimate[['biography', 'place_of_birth']] = ultimate[['biography', 'place_of_birth']].fillna("unknown")
ultimate = ultimate.dropna(subset = ['birthday'])
#print(df.isna().sum()/ len(df))
#st.dataframe(df.head())
names = ultimate.primaryName


#recuperer la chaine dans known for (ca devrait etre un str) 
akas = pd.read_csv(r'datasets\akas_clean(1).csv', sep=',')
movie = pd.read_csv('datasets\movie_final.csv')
 


st.image("images\wildprimevideo.png", width = 200)

     #st.title("Movie Recommendation System")
st.markdown(' ##  Ici retrouvez vos acteurs préférés et les films dans lesquels ils ont joué !')


with st.container():
     option = st.selectbox(
    "SAISISSEZ UN NOM D'ACTEUR 🎥",
      names)
     

     
ultimate_filter = ultimate[ultimate.primaryName == option].reset_index(drop = True)
          
col1, col2 = st.columns([0.2,0.8])
with col1 : 
               st.image(  ultimate_filter['profile_path'][0])
with col2 :
               known = ultimate_filter['knownForTitles'][0]
               place = ultimate_filter['place_of_birth'][0]
               date = ultimate_filter['birthday'][0]
               bio = ultimate_filter['biography'][0]
               profession = ultimate_filter['primaryProfession'][0]
               st.markdown(f"""
                           - Lieu de Naissance :
                           :grey[{place}]

                           - Date de Naissance : 
                           :blue[{date}]

                           - Profession
                           :blue[{profession}]

                           - Biography : 
                       
                           
                           """, unsafe_allow_html=True) ##f6112c :
               with st.container():
                    st.markdown(f"{bio}")
               
                    
st.write ("## Connu pour : 🔥🔥🔥")
nbr_film = len(ultimate_filter.knownForTitles)
  
result = st.columns(nbr_film)     
#st.dataframe(ultimate)
     
for i in range(len(result)):
          with result[i]:
               title = ultimate_filter['title_y'][i]
               st.write(f"{title}")
               url = ultimate_filter['poster_path'][i]
               st.image(f"{url}",width = 200)
               synopsis = ultimate_filter['overview'][i]
               with st.expander("## Synopsis") :
                    st.write(f"{synopsis}")
               





               

     
