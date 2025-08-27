# Credit-Scoring-Model-Deployment-2023

![Illustration](PhotosReadme/LogoP6.png)

Projet réalisé en 2023 dans le cadre de ma formation en Data Science.  
Objectif : développer un modèle de scoring de crédit pour prédire la probabilité de défaut de paiement de clients sans historique bancaire, et le déployer sous forme d’API et d’application web interactive.

## Objectifs

- Prédire le risque de défaut client (binaire : défaut / non défaut)
- Gérer le déséquilibre des classes dans les données
- Fournir une interface visuelle aux analystes crédit
- Mettre le modèle en production via une API Flask
- Intégrer le tout dans une application Streamlit

## Données

- **Source** : [Home Credit – Kaggle Competition](https://www.kaggle.com/c/home-credit-default-risk/data)

## Méthodologie

### 1. Préparation des données

- Nettoyage, fusion des tables
- Transformation des variables (encoding, réduction de dimensions)
- Sélection des nouveaux clients comme jeu d’inférence

### 2. Modélisation et sélection

- Gestion du déséquilibre avec :
  - SMOTE, Undersampling, Oversampling, Class Weight  
  ![Unbalanced](PhotosReadme/Variationunbalanced.png)

- Modèles comparés :
  - DummyClassifier, Logistic Regression, Random Forest, LightGBM
  - KNN et XGBoost testés mais trop coûteux

- Meilleur modèle : **LGBMClassifier**, optimisé avec GridSearchCV  
  ![Poids](PhotosReadme/Variationpoids.png)

### 3. Évaluation et interprétation

- Réduction des variables (suppression > 70% NaNs)
- Évaluation : matrice de confusion, score de validation  
  ![MC](PhotosReadme/MatriceConfusion.png)

- Ajustement du seuil de classification  
  ![Proba](PhotosReadme/Variationproba.png)

- Interprétation avec :
  - Feature Importance globale
  - SHAP globale et locale  
  ![SHAP](PhotosReadme/SHAPlocale.png)

### 4. Déploiement

- **API Flask** déployée sur Heroku
- **Application Streamlit** connectée à l’API

  ![Interface](PhotosReadme/InterfaceApplication.png)  
  ![Prediction](PhotosReadme/PredictionApplication.png)  
  ![Graphiques](PhotosReadme/GraphiquesApplica.png)

### 5. Analyse du Data Drift

- Suivi de l’évolution des 20 features principales dans le temps
- Visualisations comparatives avant/après  
  ![Drift 1](PhotosReadme/Datadrift2.png)  
  ![Drift 2](PhotosReadme/Datadrift.png)

## Technologies utilisées

- **Langage** : Python  
- **Bibliothèques** : pandas, seaborn, matplotlib, scikit-learn, LightGBM, SHAP, MLflow  
- **Déploiement** : Flask (API), Heroku (hébergement), Streamlit (interface)  
- **Méthodes** : Machine Learning, Interprétabilité, Feature Engineering, Data Drift Analysis

## Contact

Projet réalisé en 2023 dans le cadre de ma formation en Data Science.  
Pour toute remarque ou question :

- **Email** : [johan.rocheteau@hotmail.fr](mailto:johan.rocheteau@hotmail.fr)  
- **LinkedIn** : [linkedin.com/in/johan-rocheteau](https://www.linkedin.com/in/johan-rocheteau)
