# ProjetDSN7 : Implémentez un modèle de scoring

Vous êtes Data Scientist au sein d'une société financière, nommée "Prêt à dépenser", qui propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt.

L’entreprise souhaite mettre en œuvre un outil de “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé. Elle souhaite donc développer un algorithme de classification en s’appuyant sur des sources de données variées (données comportementales, données provenant d'autres institutions financières, etc.).

De plus, les chargés de relation client ont fait remonter le fait que les clients sont de plus en plus demandeurs de transparence vis-à-vis des décisions d’octroi de crédit. Cette demande de transparence des clients va tout à fait dans le sens des valeurs que l’entreprise veut incarner.

Prêt à dépenser décide donc de développer un dashboard interactif pour que les chargés de relation client puissent à la fois expliquer de façon la plus transparente possible les décisions d’octroi de crédit, mais également permettre à leurs clients de disposer de leurs informations personnelles et de les explorer facilement. 

Les données : https://www.kaggle.com/c/home-credit-default-risk/data

Votre mission

- Construire un modèle de scoring qui donnera une prédiction sur la probabilité de faillite d'un client de façon automatique.
- Construire un dashboard interactif à destination des gestionnaires de la relation client permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client des chargés de relation client.
- Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le dashboard interactif qui appelle l’API pour les prédictions.


Les fichiers :

- .github/workflows :
	- development.yml : tests unitaires via Actions de Github
	- workflow.yml : déploiement de FLASK sur HEROKU
- Applications :
	- Donneesgenerees :
		- ModelGrid.sav : modèle de ML final
		- OldDataP7s : petit morceau des données Anciens clients (25M max)
		- ShorNewDataP7 : données des 100 nouveaux clients
		- listNewClients : listes des 100 nouveaux clients
	- Images : 
		- Images utilisées par l'application Streamlit
	- Tests Unitaires : 
		- test_UnitestFlask.py : Tests unitaires pour Flask
		- test_UnitestStreamlit.py : Tests unitaires pour Streamlit
	- AppFlask.py : API FLASK utilisée lors du déploiement
	- Prenoms.csv : liste de prénoms pour l'application
	- patronymes.csv : liste de noms de familles pour l'application

- Notebook :
	- Donneesgenerees:
		- BestVariables : 20 meilleures variables pour le Data Drift
	- ResultatsDataDrift :
		- data_drift_report.html
		- data_stability.html
	- Data Drift.ipynb : Notebook d'analyse du DD
	- DonneesP7.ipynb : Nettoyage des merges des données
	- MLP7-ChoixModèle-Unbalance.ipynb : Notebook de modèlisation pour choix du traitement des données déséquilibrées et du modèle de ML.
	- MLP7-OptimisationModel.ipynb : Notebook d'optimisation du modèle (et tests de l'API)
- .gitignore : fichiers à ignorer dans le suivit du projet
- AppStreamlit.py : Application Streamlit (doit être à la racine pour être déployé sur Streamlit.io)
- Procfile : Fichier permettant de déployer FLASK sur Heroku.
- Readme.md : informations générales
- requirements.txt : librairies python à installer lors des déploiements automatiques
- runtime.txt : version de python