cou = 1
import pandas as pd

print(cou)
print("Salut ça marche ! It's working !!")
#How to run strimlit app in Anaconda prompt
import streamlit as st
st.write("Hello, world! This is a Streamlit app.")

st.title("My Streamlit App")
st. subheader("Try out the app!")
st.text("This is a simple text element.")
# Choix dans une liste deroulante (dans la sidebar)
graph_type = st.sidebar.selectbox("lil Choisissez un type de graphique :", ["Ligne", "Barres", "Aucun"])

st.write(f"Vous avez choisi le type de graphique : {graph_type}")
#3 UPLOAD CSV FILE
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    import pandas as po
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())


#4 Affichage du graphique en fonction du type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres":
        st.bar_chart(df)
    else:
        st.write("Aucun graphique selectionné.")

st.write("Merci d'avoir utilise notre application Streamlit !")