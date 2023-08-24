import streamlit as st
from PIL import Image
import pandas as pd
from sklearn import datasets
from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset
from evidently.test_preset import DataQualityTestPreset
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset, DataQualityPreset, RegressionPreset
from evidently.metrics.base_metric import generate_column_metrics
from evidently.metrics import *
import random
import pickle
import re
import seaborn as sns
import matplotlib.pyplot as plt

# Suppression des warnings pour SHAP :
from numba.core.errors import NumbaDeprecationWarning, NumbaPendingDeprecationWarning
import warnings
warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
import shap
shap.initjs()

# Information de l'onglet application:
st.set_page_config(page_title = 'Scoring Nouveau Client')

OldData = pd.read_csv('OldDataP7s.csv')
Variables = list(OldData.columns)

# Création d'onglets :
option = st.sidebar.selectbox(
    "Sommaire :",
    ("Page d'accueil", "Informations Clients", "Data Drift")
)


# Onglet N°1 : Page d'accueil :
if option == "Page d'accueil" :
    # En tête :
    st.markdown("<h1 style='text-align: center; color: red;'>Bonjour</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: red;'>Bienvenue sur : </h1>", unsafe_allow_html=True)
    st.markdown('')
    st.markdown('')
    st.markdown('')

    # Logo Entreprise :
    col1, col2, col3 = st.columns(3) # Division en colonne pour centrer l'image.
    with col2 :
        image = Image.open('LogoEntreprise.png')
        st.image(image, width=300)
        
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
    listNewClients = pd.read_csv('listNewClients.csv')
    listNewClients.reset_index(inplace = True)
    listeNC = listNewClients['SK_ID_CURR']
    
    Client = st.selectbox('Veuillez choisir le numéro de votre client : ', listeNC)
    IndexClient = list(listNewClients[listNewClients['SK_ID_CURR'] == Client]['index'].values)
    for i in IndexClient:
        IndexClient = i
    IndexOther = list(listNewClients['index'])
    IndexOther.remove(IndexClient+1)
    IndexOther.remove(0)
    
        # Slice du client sur la DF NewClient (moins lourd à ouvrir)
    DataClient = pd.read_csv('NewDataP7.csv', skiprows = IndexOther, nrows = 1)
    DataClient = DataClient.rename(columns = lambda x:re.sub('[^A-Za-z0-9_]+', '', x))
    DataClient = DataClient.drop(columns = 'TARGET')
    NumClient = DataClient['SK_ID_CURR'].values
    for i in NumClient:
        NumClient = i
    st.write('**N° Client :** ', NumClient)
    
    
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

    # Résultats models :
    loaded_model = pickle.load(open('ModelGrid.sav', 'rb'))
    Variables.remove('TARGET')
    result = loaded_model.predict(DataClient[Variables])
    result2 = loaded_model.predict_proba(DataClient[Variables])
    st.write("Vous avez", str(int(round(result2[0][1],2)*100))+"%", "de rembourser ce prêt.")
    col1, col2, col3 = st.columns(3) # Division en colonne pour centrer l'image.
    with col2 :
        if result == 1:
            image = Image.open('PouceVert.png')
            st.image(image, width=300)
        if result == 0:
            image = Image.open('PouceRouge.png')
            st.image(image, width=300)

    # Feature importance locale :
    st.markdown("<h2 style='text-align: center; color: green;'>Variables impliquées dans le résultat :</h1>", unsafe_allow_html=True)
        # Explainer :
    explainer = shap.TreeExplainer(loaded_model, OldData[Variables])
        # Visualisation :
    shap_values = explainer(DataClient[Variables])
    shap.waterfall_plot(shap_values[0], max_display = 10)
    st.set_option('deprecation.showPyplotGlobalUse', False) # Option pour enlever l'erreur PyplotGlobalUseWarning
    st.pyplot(bbox_inches = 'tight')
    
    # Récupération des variables importantes du client :
    Columns = OldData[Variables]
    BestVariables = pd.DataFrame(zip(shap_values[0].values, Columns))
    BestVariables[0] = abs(BestVariables[0]).round(2)
    BestVariables = BestVariables.sort_values(0, ascending = False)
    BestVariables = list(BestVariables.iloc[:10][1])

    # Analyse graphique de deux variables au choix :
    st.markdown("<h2 style='text-align: center; color: green;'>Analyses des variables :</h1>", unsafe_allow_html=True)

    Var1 = st.selectbox('Veuillez choisir la variable N°1 : ', BestVariables)
    Var2 = st.selectbox('Veuillez choisir la variable N°2 : ', BestVariables)
    
    fig, ax = plt.subplots()
    ax = sns.scatterplot(OldData[Variables], x = Var1, y = Var2, hue = OldData['TARGET'], palette=['green','orange'])
    ax = sns.scatterplot(DataClient[Variables], x = Var1, y = Var2, s=400, hue = Var2, palette = ['red'], marker = '*')
    ax = plt.title("Etude de l'impact des variables {} et {} sur le score du client.".format(Var1, Var2))
    ax = plt.legend('')
    st.pyplot(fig)



#if option == "Data Drift" :
#    # Suppression des colonnes TARGET :
#    OD = OldData[OldData['TARGET'].notna()]
#    ND = NewData[NewData['TARGET'].notna()]
    
#    data_stability = TestSuite(tests=[DataStabilityTestPreset()])
#    data_stability.run(current_data = ND.iloc[:,:10], reference_data = OD.iloc[:,:10], column_mapping = None)
#    data_stability.show(mode='inline') 
