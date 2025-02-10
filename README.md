# 📊 Projet N°6 : Implémentez un modèle de scoring

## **📌 Contexte et Objectif**

**Entreprise :** Prêt à Dépenser  
**Logo :** ![Logo](PhotosReadme/LogoP6.png)  

### **🎯 Objectif**
Développer un **modèle de scoring de crédit** permettant de **prédire la capacité de remboursement des clients** n'ayant pas ou peu d'historique bancaire.

### **📂 Jeux de données**
- 📊 **Données :** [Base de Données](https://www.kaggle.com/c/home-credit-default-risk/data)
- 🔍 **Missions du projet :**
  - Construire un **modèle de scoring** capable de prédire la probabilité de défaut de paiement.
  - Développer un **dashboard interactif** pour aider les gestionnaires de crédits à interpréter les prédictions.
  - Mettre en production le modèle via une **API Flask**, intégrée au dashboard.

---

## **🚀 Réalisations et Méthodologie**

### **1️⃣ Analyse des Données**
- Ouverture et exploration des fichiers
- Préparation des données :
  - **Création et transformation** des variables (dummisation, factorisation)
  - **Fusion des fichiers** et simplification des datasets lourds
  - Sélection des **nouveaux clients** pour l'application

---

### **2️⃣ Gestion du Déséquilibre des Données et Sélection du Modèle**
- 📊 **Techniques de gestion du déséquilibre** :
  - **SMOTE**, **Class_Weight**, **Undersampling**, **Oversampling**
  
  ![Unbalanced](PhotosReadme/Variationunbalanced.png)
  
- ⚙ **Comparaison des modèles de Machine Learning** :
  - **DummyClassifier, LogisticRegression, RandomForestClassifier, LGBMClassifier**
  - **KNN et XGBOOST** (trop longs à exécuter)

- 🔧 **Optimisation des hyperparamètres** via **GridSearchCV**
- 🏆 **Meilleur modèle sélectionné : LGBMClassifier**

  ![Poids](PhotosReadme/Variationpoids.png)

---

### **3️⃣ Optimisation du Modèle et Interprétation**
- **Réduction des variables** (seuil < 70% de NaNs)
- **Évaluation des performances** :
  - **Matrice de confusion** pour validation des résultats

  ![MC](PhotosReadme/MatriceConfusion.png)
  
  - **Optimisation du seuil de probabilité** pour améliorer la métrique de scoring

  ![Proba](PhotosReadme/Variationproba.png)

- **Analyse des variables les plus importantes** :
  - **Feature Importances, SHAP globale et locale**

  ![SHAP](PhotosReadme/SHAPlocale.png)

---

### **4️⃣ Déploiement du Modèle**
✅ **Mise en production sur une API Flask hébergée sur Heroku**  
✅ **Développement d'une application Streamlit** intégrant l'API  

🖥 **Interface utilisateur :**
  
  ![Interface](PhotosReadme/InterfaceApplication.png)

📊 **Exemple de prédiction pour un client :**
  
  ![Prediction](PhotosReadme/PredictionApplication.png)

📉 **Graphiques explicatifs des prédictions :**
  
  ![Graphiques](PhotosReadme/GraphiquesApplica.png)

---

### **5️⃣ Étude du Data Drift**
- **Objectif :** Analyser la stabilité du modèle au fil du temps  
- **Variables utilisées :** **Top 20 features les plus influentes**
  
  ![DD2](PhotosReadme/Datadrift2.png)  
  ![DD1](PhotosReadme/Datadrift.png)  

---

## **🛠️ Technologies et Outils Utilisés**
- **Langage :** Python 🐍  
- **Librairies :** Pandas, Seaborn, Matplotlib, Scikit-learn, LightGBM, MLflow  
- **Déploiement :** Flask (API) sur **Heroku**, Dashboard **Streamlit**  
- **Méthodes utilisées :** Machine Learning, SHAP, Feature Engineering, Data Drift Analysis  

---

## **📬 Contact et Feedback**
💡 Ce projet a été réalisé dans le cadre de ma **formation Data Science**. N’hésitez pas à **laisser vos suggestions** ou à **me contacter** pour en discuter !  

📩 **Contact :**  
📧 [johan.rocheteau@hotmail.fr](mailto:johan.rocheteau@hotmail.fr)  
🔗 [LinkedIn](https://www.linkedin.com/in/johan-rocheteau)
