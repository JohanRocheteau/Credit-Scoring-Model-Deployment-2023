
import pytest
import sys
import os
import pandas as pd
from PIL import Image
import numpy as np

# Ajoutez le chemin du répertoire parent au chemin de recherche de Python
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AppStreamlit import load_data, OpenPicture, ListeNewClient, GoodPlots

def test_load_data(): # bon format de la DF
    try :
        url = "C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\OldDataP7s.csv"
    except :
        url = "OldDataP7s.csv"
    df = load_data(url)
    assert isinstance(df, pd.DataFrame) # si l'objet uploadé est une DF
    assert df.shape[1] == 560 # si l'objet à bien 560 colonnes (ne marche pas avec la DF initiale)

def picture_ok(): # Vérification de l'ouverture des photos :
    url1 = 'C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\LogoEntreprise.png'
    pic1 = OpenPicture(url1)
    assert isinstance(pic1, Image.Image)
    assert pic1 is not None

def test_liste_new_client():
    try :
        listecsv = "C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\listNewClients.csv"
    except :
        listecsv = "listNewClients.csv"
    listeNC, _ = ListeNewClient(listecsv)
    assert listeNC
    assert isinstance(listeNC, list)
    assert len(listeNC) > 0
    
def test_good_plots():
    Var1 = 'DAYS_EMPLOYED'
    Var2 = 'EXT_SOURCE_3'
    OldData = pd.read_csv("C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\OldDataP7s.csv")
    DataClient = pd.read_csv('C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\NewDataP7.csv', nrows = 1)
    Target = OldData['TARGET']
    # fausse listresult :
    listresult = list(np.random.randint(0, 101, 8310))

    # Appelez la fonction que vous testez
    result = GoodPlots(Var1, Var2, Target, OldData, DataClient, listresult)

    # Vérifiez que la fonction n'a pas levé d'exceptions
    assert result is not None

if __name__ == '__main__':
    pytest.main()