import streamlit as st
from PIL import Image
import pandas as pd
import random
import pickle
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import requests
import json
import mlflow


# Suppression des warnings pour SHAP :
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
import shap
shap.initjs()

# Information de l'onglet application:
st.set_page_config(page_title = 'Scoring Nouveau Client')

# Chargement des données et mise en cache :
@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

OldData = load_data("C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\OldDataP7s.csv")
Variables = list(OldData.columns)

# Création d'onglets :
option = st.sidebar.selectbox(
    "Sommaire :",
    ("Page d'accueil", "Informations Clients"))

# Def ouverture des images :
def OpenPicture (url, size):
    image = Image.open(url)
    return st.image(image, width = size)

# Onglet N°1 : Page d'accueil :
if option == "Page d'accueil" :
    # En tête :
    st.markdown("<h1 style='text-align: center; color: red;'>Bonjour, bienvenue sur : </h1>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    st.markdown('')

    # Logo Entreprise :
    col1, col2, col3, col4 = st.columns(4) # Division en colonne pour centrer l'image.
    with col2 :
        OpenPicture('C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\LogoEntreprise.png', 300)

        
    st.markdown('')
    st.markdown('')
    
    st.markdown("<h2 style='text-align: center; color: grey;'>L'application qui vous donne le résultat en toute tranPRETrance.</h1>", unsafe_allow_html=True)
    st.markdown('')
    
    # But de l'application :
    st.markdown("<h3 style='font-weight:bold;'>But de l'application :</h1>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('#### Permettre aux clients et aux chargés de clientèles de comprendre les résultats.')




if option == "Informations Clients" :
    # Titre
    st.markdown("<h2 style='text-align: center; color: green;'>Informations Clients :</h1>", unsafe_allow_html=True)

    # N° de client :
        # Ouverture liste des clients :
    def ListeNewClient (listecsv):
        listNewClients = pd.read_csv(listecsv)
        listNewClients.reset_index(inplace = True)
        listeNC = list(listNewClients['SK_ID_CURR'])
        # Ajout d'un client 0 pour que rien ne s'affiche au départ :
        listeNC.insert(0, ' ')
        return listeNC, listNewClients
    
    listeNC = ListeNewClient('listNewClients.csv')[0]
    listNewClients = ListeNewClient('listNewClients.csv')[1]
    
        # Séléction d'un client par le chargé de clientel :
    def ChoixClient (listeNC) :
        Client = st.selectbox('Veuillez choisir le numéro de votre client : ', listeNC)
        return Client
    
    Client = ChoixClient(listeNC)
    
    # Si pas de client séléctionné :
    if Client == ' ' :
        st.write ('')
    
    else : 
        IndexClient = list(listNewClients[listNewClients['SK_ID_CURR'] == Client]['index'].values)
        for i in IndexClient:
            IndexClient = i
        IndexOther = list(listNewClients['index'])
        IndexOther.remove(IndexClient+1)
        IndexOther.remove(0)
        
            # Slice du client sur la DF NewClient (moins lourd à ouvrir)
        DataClient = pd.read_csv('NewDataP7.csv', skiprows = IndexOther, nrows = 1)
        DataClient = DataClient.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
        NumClient = DataClient['SK_ID_CURR'].values
        for i in NumClient:
            NumClient = i
        st.write('**N° Client :** ', NumClient)
        DataClient = DataClient[Variables]
        DataClient = DataClient.drop(columns = 'TARGET')
        
        # Personalisation du client :
        Prenoms = pd.read_csv('Prenoms.csv', sep =';', encoding='latin-1')
        Prenoms = list(Prenoms[Prenoms['03_langage'] == 'french']['01_prenom'])
        Prenoms = [i.capitalize() for i in Prenoms]
        Prenoms = random.choice(Prenoms)
        st.write('**Prenom :** ', Prenoms)
        
        Noms = pd.read_csv('patronymes.csv')
        Noms = Noms.dropna()
        Noms = list(Noms['patronyme'])
        Noms = random.choice(Noms)
        st.write('**Nom :** ', Noms)
        
        # Titre
        st.markdown("<h2 style='text-align: center; color: green;'>  Résultats du prêt :</h1>", unsafe_allow_html=True)
         
        # Résultats models avec l'API FLASK reliée à MLFLOW :
        url = 'https://prediction-app-p7-6a2e12152edf.herokuapp.com/api/'
        
        Variables.remove('TARGET')
        data = DataClient.values.tolist()
        j_data = json.dumps(data)
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=j_data, headers=headers)
        result2 = float(r.text.split(' ')[1].split(']]')[0])
        result2 = int(round(result2,2)*100)
        
        # Si on utilise directement le model de puis un fichier de sauvegarde :
        loaded_model = pickle.load(open('ModelGrid.sav', 'rb'))
        #result2 = loaded_model.predict_proba(DataClient)
        #result2 = int(result2[0][1]*100)
        
        # Graphique jauge :     
        def JaugeClient (result2) :
            plot_bgcolor = "#def"
            quadrant_colors = [plot_bgcolor, "#2bad4e", "#85e043", "#f2a529", "#f25829"] 
            quadrant_text = ["", "<b>Very High</b>", "<b>High</b>", "<b>Low</b>", "<b>Very Low</b>"]
            n_quadrants = len(quadrant_colors) - 1
            
            current_value = result2
            min_value = 0
            max_value = 100
            hand_length = np.sqrt(2) / 4
            hand_angle = np.pi * (1 - (max(min_value, min(max_value, current_value)) - min_value) / (max_value - min_value))
            
            fig = go.Figure(
                data=[
                    go.Pie(
                        values=[0.5] + (np.ones(n_quadrants) / 2 / n_quadrants).tolist(),
                        rotation=90,
                        hole=0.5,
                        marker_colors=quadrant_colors,
                        text=quadrant_text,
                        textinfo="text",
                        hoverinfo="skip",
                    ),
                ],
                layout=go.Layout(
                    showlegend=False,
                    margin=dict(b = 0,t= 50,l=5,r=5),
                    width=350,
                    height=350,
                    paper_bgcolor=plot_bgcolor,
                    annotations=[
                        go.layout.Annotation(
                            text=f"<b>Niveau de remboursement :</b><br>{current_value}%",
                            x=0.5, xanchor="center", xref="paper",
                            y=0.2, yanchor="bottom", yref="paper",
                            showarrow=False,
                        )
                    ],
                    shapes=[
                        go.layout.Shape(
                            type="circle",
                            x0=0.48, x1=0.52,
                            y0=0.48, y1=0.52,
                            fillcolor="#333",
                            line_color="#333",
                        ),
                        go.layout.Shape(
                            type="line",
                            x0=0.5, x1=0.5 + hand_length * np.cos(hand_angle),
                            y0=0.5, y1=0.5 + hand_length * np.sin(hand_angle),
                            line=dict(color="#333", width=4)
                        )
                    ]
                )
            )
            return st.plotly_chart(fig)
        
        col1, col2 = st.columns(2) # Division en colonne pour centrer l'image.
        with col2 :
            JaugeClient (result2)
            
        with col1 :
            if result2 >= 50:
                OpenPicture('PouceVert.png', 300)
            if result2 < 50:
                OpenPicture('PouceRouge.png', 300)
    
        # Feature importance globale :
        st.markdown("<h2 style='text-align: center; color: green;'>Feature Importance Globale :</h1>", unsafe_allow_html=True)
        OpenPicture('SHAPGlobale.png', 600)
    
        # Feature importance locale :
        st.markdown("<h2 style='text-align: center; color: green;'>Feature Importance Locale :</h1>", unsafe_allow_html=True)
            
        # Explainer + Visualisation :
        def ShapLocale(loaded_model, OldData) :
            explainer = shap.TreeExplainer(loaded_model, OldData)
            shap_values = explainer(DataClient, check_additivity=False)
            return shap_values[0]
        
        ShapValues = ShapLocale(loaded_model, OldData)
                     
        shap.waterfall_plot(ShapValues, max_display = 10)
        st.set_option('deprecation.showPyplotGlobalUse', False) # Option pour enlever l'erreur PyplotGlobalUseWarning
        st.pyplot(bbox_inches = 'tight')
        
        # Récupération des variables importantes du client :
        def GoodVariables(ShapValues, OldData):
            Columns = DataClient.columns
            BestVariables = pd.DataFrame(zip(ShapLocale(loaded_model, OldData).values, Columns))
            BestVariables[0] = abs(BestVariables[0]).round(2)
            BestVariables = BestVariables.sort_values(0, ascending = False)
            BestVariables = list(BestVariables.iloc[:15][1])
            BestVariables.insert(0, ' ')
            return BestVariables
        
        # Création de la colonnes predict_proba pour toute la DF :
        Target = OldData['TARGET']
        OldData = OldData.drop(columns = 'TARGET')
        result = loaded_model.predict_proba(OldData)
        result = pd.DataFrame(result)
        result = 100*result
        result = result.astype(int)
        listresult = list(result[1])
    
        # Analyse graphique de deux variables au choix :
        st.markdown("<h2 style='text-align: center; color: green;'>Analyses des variables importantes :</h1>", unsafe_allow_html=True)
    
        Var1 = st.selectbox('Veuillez choisir la variable N°1 : ', GoodVariables(ShapValues, OldData))
        Var2 = st.selectbox('Veuillez choisir la variable N°2 : ', GoodVariables(ShapValues, OldData))
        
        if Var1 == ' ' or Var2 == ' ' :
            st.write('')
        
        else :
            def GoodPlots(Var1, Var2) :
                fig = plt.figure(figsize = (10,8))
                ax = fig.subplot_mosaic("""
                                        AB
                                        CC
                                        """)
                sns.kdeplot(OldData, x = Var1, hue = Target, multiple="stack", ax = ax['A'])
                ax["A"].axvline(DataClient[Var1].values, linewidth = 2, color='r')
                sns.kdeplot(OldData, x = Var2, hue = Target, multiple="stack", ax = ax['B'])
                ax["B"].axvline(DataClient[Var2].values, linewidth = 2, color='r')
                ax['C'] = sns.scatterplot(OldData, x = Var1, y = Var2, hue = listresult, palette="blend:red,green")
                ax['C'] = sns.scatterplot(DataClient, x = Var1, y = Var2, s=400, hue = Var2, palette = ['blue'], marker = '*')
                ax['C'] = plt.legend('')
                return st.pyplot(fig)
            
            GoodPlots(Var1, Var2)
            