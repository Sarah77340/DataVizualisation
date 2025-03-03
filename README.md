# Analyse des Journées Européennes du Patrimoine

Accéder au projet : https://datavizualisation-journeepatrimoine.streamlit.app/

## Objectifs
Ce projet a pour but d'explorer et d'analyser les données des **Journées Européennes du Patrimoine**, un événement culturel majeur en Europe. Il repose sur **Streamlit** pour la visualisation interactive et utilise des bibliothèques de **data science** pour l'analyse des données.

Les principales fonctionnalités de l'application sont :
- Une interface interactive permettant d'explorer les données.
- Une **présentation** de l'événement et de son impact.
- Une **analyse des données** : fréquence des visites, accessibilité, types d'activités.
- Une **carte interactive** des lieux participant à l'événement.

## Améliorations apportées
- Ajout d'un **menu de navigation** pour faciliter l'exploration des sections.
- Intégration de **visualisations interactives** avec Plotly et Seaborn.
- Ajout d'un **filtrage avancé** pour les événements sur la carte.

## Documentation utilisateur
L'application est composée de trois sections principales :

1. **Présentation** :
   - Introduction aux Journées Européennes du Patrimoine.
   - Images et explications sur l'importance de l'événement.

2. **Analyse** :
   - **Fréquence des visites** : analyse des jours et horaires les plus populaires.
   - **Accessibilité** : analyse des horaires d'ouverture et des conditions tarifaires.
   - **Types d'activités** : répartition des thématiques et des types d'événements.

3. **Carte interactive** :
   - Localisation des événements.
   - Filtrage par **région**, **ville**, **type d'événement** et **tarification**.

## Documentation technique

### Bibliothèques utilisées
- **requests** → Chargement d'animations Lottie.
- **streamlit** → Création de l'interface utilisateur.
- **pandas** → Manipulation et nettoyage des données.
- **matplotlib / seaborn** → Visualisations statistiques.
- **plotly.express** → Graphiques et carte interactive.
- **re** → Extraction d'informations textuelles.

## Installation et exécution

1. Clonez le répertoire
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancez l'application Streamlit :
   ```bash
   streamlit run streamlit_app.py
   ```

## Auteur
Sarah Nguyen


