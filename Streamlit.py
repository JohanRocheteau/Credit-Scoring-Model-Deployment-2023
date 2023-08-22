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

# Information de l'onglet application:
st.set_page_config(page_title = 'Scoring Nouveau Client')

# En tête :
st.markdown("<h1 style='text-align: center; color: red;'>Bonjour</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: red;'>Bienvenue sur l'application</h1>", unsafe_allow_html=True)


# Logo Entreprise :
col1, col2, col3 = st.columns(3) # Division en colonne pour centrer l'image.
with col2 :
    image = Image.open('LogoEntreprise.png')
    st.image(image)

st.markdown('#### But : Permettre aux clients et aux chargés de clientèles de comprendre les résultats.')

# Chargement des données :
#OldData = pd.read_csv('OldDataP7.csv')
#NewData = pd.read_csv('NewDataP7.csv')




# Using object notation
option = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Informations Nouveaux Clients", "Data Drift", "Home phone", "Mobile phone")
)

if option == "Informations Nouveaux Clients" :
    # Personalisation du client :
    Prenoms = pd.read_csv('Prenoms.csv', sep =';', encoding='latin-1')
    Prenoms = list(Prenoms[Prenoms['03_langage'] == 'french']['01_prenom'])
    Prenoms = [i.capitalize() for i in Prenoms]
    Prenoms = random.choice(Prenoms)
    st.markdown(Prenoms)
    
    Noms = pd.read_csv('patronymes.csv')
    Noms = Noms.dropna()
    Noms = list(Noms['patronyme'])
    Noms = random.choice(Noms)
    st.markdown(Noms)
    



'''if option == "Data Drift" :
    # Suppression des colonnes TARGET :
    OD = OldData[OldData['TARGET'].notna()]
    ND = NewData[NewData['TARGET'].notna()]
    
    data_stability = TestSuite(tests=[DataStabilityTestPreset()])
    data_stability.run(current_data = ND.iloc[:,:10], reference_data = OD.iloc[:,:10], column_mapping = None)
    data_stability.show(mode='inline') '''
