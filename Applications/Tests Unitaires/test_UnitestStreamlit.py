
import pytest
import sys
import os
import pandas as pd
import numpy as np

# Ajoutez le chemin du répertoire parent au chemin de recherche de Python
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from AppStreamlit import load_data,  ListeNewClient, GoodPlots

def test_load_data(): # bon format de la DF
    try :
        df = load_data("C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\OldDataP7s.csv")
    except :
        df = load_data("OldDataP7s.csv")
    assert isinstance(df, pd.DataFrame) # si l'objet uploadé est une DF
    assert df.shape[1] == 620 # si l'objet à bien 560 colonnes (ne marche pas avec la DF initiale)

def test_liste_new_client():
    try :
        listeNC, _ = ListeNewClient("C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\listNewClients.csv")
    except :
        listeNC, _ = ListeNewClient("listNewClients.csv")
    assert listeNC
    assert isinstance(listeNC, list)
    assert len(listeNC) > 0
    
def test_good_plots():
    Var1 = 'DAYS_EMPLOYED'
    Var2 = 'EXT_SOURCE_3'
    try :
        OldData = pd.read_csv("C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\OldDataP7s.csv")
        DataClient = pd.read_csv('C:\\Users\\Johan\\Formation Data Science\\Projet 7\\ProjetDSN7\\ShortNewDataP7.csv', nrows = 1)
    except :
        OldData = pd.read_csv("OldDataP7s.csv")
        DataClient = pd.read_csv('ShortNewDataP7.csv', nrows = 1)
        
    Target = OldData['TARGET']
    # fausse listresult :
    listresult = list(np.random.randint(0, 101, 7884))

    # Appelez la fonction que vous testez
    result = GoodPlots(Var1, Var2, Target, OldData, DataClient, listresult)

    # Vérifiez que la fonction n'a pas levé d'exceptions
    assert result is not None

if __name__ == '__main__':
    pytest.main()