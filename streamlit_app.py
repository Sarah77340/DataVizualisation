import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import re



st.set_page_config(page_title="My project", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----- LOAD ASSETS ------
asset1 = load_lottieurl("https://lottie.host/70e2468a-0ced-49e3-b47b-84071d9d963b/wOBkMbU29O.json")

# ----- SIDEBAR SECTION ------
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Presentation", "Analyse", "Portofolio"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Presentation":
    st.title("La Journée Européenne du Patrimoine")
    
    st.write("""
    La Journée Européenne du Patrimoine, qui se déroule chaque année le troisième week-end de septembre, est un événement culturel majeur qui vise à sensibiliser le public à la richesse et à la diversité du patrimoine européen. 
    Initiée en 1991 par le Conseil de l'Europe et la Commission européenne, cette journée permet de découvrir des lieux souvent fermés au public, tels que des monuments historiques, des musées, des jardins et des sites archéologiques.
    """)

    # Ajoutez une image représentant des monuments historiques
    st.image("Chambord.jpg", caption="Découvrez des monuments historiques lors de la Journée Européenne du Patrimoine", use_column_width=True)

    st.write("""
    L'événement est marqué par une multitude d'activités gratuites, telles que des visites guidées, des expositions, des spectacles et des ateliers, mettant en avant l'histoire, l'art et les traditions des différentes régions. 
    Chaque édition a un thème spécifique qui encourage les participants à explorer des aspects variés du patrimoine culturel, qu'il soit matériel ou immatériel.
    """)

    st.image("visites.jpg", caption="Participez à des visites guidées et découvrez des trésors cachés", use_column_width=True)

    st.write("""
    La Journée Européenne du Patrimoine favorise également les échanges interculturels et renforce le sentiment d’appartenance à une communauté européenne. 
    Elle permet aux citoyens de mieux comprendre l'importance de la préservation de leur patrimoine et d’apprécier la diversité culturelle qui enrichit l'Europe. 
    En 2024, cet événement aura pour thème « Patrimoine vivant », mettant l'accent sur les traditions et savoir-faire qui perdurent à travers les générations.
    """)

    # Ajoutez une image symbolisant la diversité culturelle
    st.image("diversite.jpg", caption="Célébrez la diversité culturelle de l'Europe", use_column_width=True)


elif selected == "Analyse":
    file_path = 'Journees_europeennes_du_patrimoine_20160914_cleaned.csv'
    data = pd.read_csv(file_path)
    data['Durée'] = data['Horaires détaillés - FR'].str.extract(r'(\d{2}h\d{2})')

    
    st.title("Exploration des Journées Européennes du Patrimoine")
    st.write("")
    
    tab_selected = st.tabs(["Fréquence", "Accessibilité", "Type de visites", "Carte"])
    

    # Section 1: Fréquence des visites
    with tab_selected[0]:
        st.header("Fréquence des visites")
        
        st.write("La Journée Européenne du Patrimoine offre une opportunité unique d'explorer une multitude de sites culturels et historiques. La fréquence des visites varie en fonction des lieux, avec des horaires adaptés pour permettre aux visiteurs de profiter pleinement de chaque expérience.")

        with st.container():
            
            # Répartition temporelle des éléments selon le jour de la semaine
            st.subheader("Répartition temporelle des éléments selon le jour de la semaine")
            col1, col2 = st.columns(2)
            with col1:
                # Extraction des jours et correspondance avec les jours de la semaine
                data['Jour'] = data['Horaires détaillés - FR'].str.extract(r'(\d{2} septembre)')[0]

                # Dictionnaire de correspondance pour les jours
                day_mapping = {
                    '16 septembre': 'Vendredi',
                    '17 septembre': 'Samedi'
                }

                # Remplacer les dates par les noms des jours
                data['Jour'] = data['Jour'].replace(day_mapping)

                # Compter les événements par jour
                events_by_day = data['Jour'].value_counts()

                # Création du graphique
                fig, ax = plt.subplots(figsize=(3, 2)) 
                ax.bar(events_by_day.index, events_by_day.values, color='green')
                ax.set_ylabel('Nombre d\'événements')
                ax.set_title('Répartition des événements par jour')
                st.pyplot(fig)


                
            with col2:
                st.write(
                    "Nous conseillons vivement aux visiteurs de prévoir leurs sorties principalement le samedi pour bénéficier de la richesse des événements offerts."
                    "Ce jour-là, de nombreux événements seront ouverts au public, offrant une multitude d'activités à découvrir."
                )

        with st.container():
            
            # Répartition selon les lieux les plus mentionnés
            st.subheader("Répartition selon les lieux les plus mentionnés")
            col1, col2 = st.columns(2)
            with col1: 
                events_by_location = data['Ville'].value_counts()

                # Filtrer pour enlever la catégorie "unknown"
                events_by_location = events_by_location[events_by_location.index != 'Unknown']

                # Garder seulement le Top 5
                events_by_location_top5 = events_by_location.head(5)

                # Création du graphique
                fig, ax = plt.subplots(figsize=(3, 2))  # Réduire la taille du graphique
                ax.pie(events_by_location_top5.values, labels=events_by_location_top5.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
                ax.axis('equal')
                ax.set_title('Top 5 des lieux les plus mentionnés')
                st.pyplot(fig)
                
                st.write("\n\n\n\n\n")
                
               
            with col2:
                st.write(
                    "Pour profiter au maximum de la Journée Européenne du Patrimoine, dirigez-vous vers les grandes villes !\n\n"
                    "Ces métropoles offrent une multitude d'événements variés, des visites de monuments emblématiques aux expositions et spectacles. Vous y trouverez davantage d'activités culturelles et interactives, parfaites pour toute la famille."
                )

        
    # Section 2: Accessibilité
    with tab_selected[1]:
        st.header("Accessibilité")
        st.write("L'accessibilité, tant au niveau des horaires que des conditions tarifaires, est un aspect crucial de la Journée Européenne du Patrimoine.")
        col1, col2 = st.columns(2)
        n_top = 10

        def extract_opening_closing_hours(horaires):
            if isinstance(horaires, str):  # Vérifie si les horaires sont bien une chaîne de caractères
                heures = re.findall(r'(\d{2}h\d{2})', horaires)
                if len(heures) >= 2:
                    return heures[0], heures[-1]  # Première heure = ouverture, Dernière heure = fermeture
                elif len(heures) == 1:
                    return heures[0], heures[0]  # Si une seule heure, on considère qu'il s'agit de l'ouverture et fermeture
            return None, None
                        
        data['Heure Ouverture'], data['Heure Fermeture'] = zip(*data['Horaires détaillés - FR'].apply(extract_opening_closing_hours))

        # Filtrer les données valides
        data_opening = data.dropna(subset=['Heure Ouverture'])
        data_closing = data.dropna(subset=['Heure Fermeture'])

        with col1:
            # Répartition selon l'heure d'ouverture
            st.subheader(f"Répartition selon l'heure d'ouverture")
            events_by_opening = data_opening['Heure Ouverture'].value_counts().nlargest(n_top).sort_index()

            fig, ax = plt.subplots(figsize=(4, 3))
            ax.bar(events_by_opening.index, events_by_opening.values, color='green')
            ax.set_xlabel('Heure d\'ouverture')
            ax.set_ylabel('Nombre d\'événements')
            ax.set_title(f'Top {n_top} des événements selon l\'heure d\'ouverture')
            ax.set_xticklabels(events_by_opening.index, rotation=70)  
            st.pyplot(fig)
            
            # Répartition selon la durée d'ouverture
            st.subheader(f"Durée totale d'ouverture")
            events_by_duration = data['Durée'].value_counts().nlargest(n_top)

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.barh(events_by_duration.index, events_by_duration.values, color='purple')
            ax.set_xlabel('Nombre d\'événements')
            ax.set_title(f'Top {n_top} des événements selon la durée d\'ouverture')
            st.pyplot(fig)
            
            st.write("Les événements offrent généralement une durée d'ouverture de 10 heures pour la plupart des événements, ce qui vous laisse amplement le temps de visiter plusieurs sites dans une même journée. ")
       
            
                
        with col2:
            # Répartition selon l'heure de fermeture
            st.subheader(f"Répartition selon l'heure de fermeture")
            events_by_closing = data_closing['Heure Fermeture'].value_counts().nlargest(n_top).sort_index()

            fig, ax = plt.subplots(figsize=(4, 3))
            ax.bar(events_by_closing.index, events_by_closing.values, color='blue')
            ax.set_xlabel('Heure de fermeture')
            ax.set_ylabel('Nombre d\'événements')
            ax.set_title(f'Top {n_top} des événements selon l\'heure de fermeture')
            ax.set_xticklabels(events_by_closing.index, rotation=70)  
            st.pyplot(fig)


            # Répartition selon les conditions tarifaires (fictif, à remplir selon les données)
            st.subheader("Répartition selon la condition tarifaire")

            data['Tarif'] = data['Conditions tarifaires'].fillna('Gratuit')  # Ajouter une colonne "Tarif" si elle existe dans les données
            tarif_counts = data['Tarif'].value_counts()
            tarif_counts = tarif_counts[tarif_counts.index != 'Unknown']

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.pie(tarif_counts.values, labels=tarif_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("coolwarm"))
            ax.axis('equal')
            ax.set_title('Répartition selon les conditions tarifaires')

            st.pyplot(fig)
            
            st.write("La plupart des événements sont gratuits, ce qui en fait une excellente occasion de découvrir le patrimoine culturel sans dépenser. Cependant, il est important de noter que certains événements peuvent être payants.")
        

        
    # Section 3: Type de visites
    with tab_selected[2]:
        st.header("Type de visites")
        st.write("La variété des types de visites proposées lors de la Journée Européenne du Patrimoine permet à chacun de trouver son bonheur. ")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Répartition selon les thématiques patrimoniales
            st.subheader("Répartition selon les thématiques patrimoniales")
            tags = data['Tags du lieu'].str.split('|', expand=True).stack().value_counts().head(10)

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(tags.index, tags.values, color='red')
            ax.set_ylabel('Nombre d\'événements')
            ax.set_title('Top 10 des thématiques patrimoniales')
            ax.set_xticklabels(tags.index, rotation=70)  
            st.pyplot(fig)
                    
            # Répartition selon la région
            st.subheader("Répartition selon la région")
            region_counts = data['Région'].value_counts().head(10)
            region_counts = region_counts[region_counts.index != 'Unknown']

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(region_counts.index, region_counts.values, color='cyan')
            ax.set_ylabel('Nombre d\'événements')
            ax.set_title('Répartition des événements par région')
            ax.set_xticklabels(tags.index, rotation=70)  
            st.pyplot(fig)
            
            
        with col2:
            # Répartition selon le type d'événements
            st.subheader("Répartition selon le type d'événements")
            # Pour l'exemple, nous simulons les types d'événements, ajouter une colonne réelle si elle existe
            data['Type événement'] = data['Titre - FR'].apply(lambda x: 'Exposition' if 'exposition' in x.lower() else 'Visite')
            type_event_counts = data['Type événement'].value_counts()

            fig, ax = plt.subplots(figsize=(8, 6))
            ax.pie(type_event_counts.values, labels=type_event_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3"))
            ax.axis('equal')
            ax.set_title('Répartition selon le type d\'événements')

            st.pyplot(fig)
        
            
            # Répartition selon la ville
            st.subheader("Répartition selon la ville")
            city_counts = data['Ville'].value_counts().head(10)
            city_counts = city_counts[city_counts.index != 'Unknown']
            
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.barh(city_counts.index, city_counts.values, color='brown')
            ax.set_xlabel('Nombre d\'événements')
            ax.set_title('Répartition des événements par ville')

            st.pyplot(fig)

    ### Carte des événements par région ###
    with tab_selected[3]:
        st.header("Carte")
        st.write("Repérer et trier vous-même les sites qui vous interesse. Avec cet outil, vous pourrez explorer facilement les différentes activités proposées et maximiser votre temps de découverte.")
        
        # Ajout de filtres directement sur la page
        st.subheader("Filtres")

        # Filtre par région
        regions = data['Région'].unique().tolist()
        selected_region = st.selectbox("Sélectionner une région", options=["Tous"] + regions)

        # Filtre par ville
        cities = data['Ville'].unique().tolist()
        selected_city = st.selectbox("Sélectionner une ville", options=["Tous"] + cities)

        # Filtre par thématique patrimoniale
        if 'Tags du lieu' in data.columns:
            themes = data['Tags du lieu'].str.split('|').explode().unique().tolist()
            selected_theme = st.selectbox("Sélectionner une thématique", options=["Tous"] + themes)
        else:
            selected_theme = "Tous"

        # Filtre par type d'événement
        if 'Type événement' in data.columns:
            event_types = data['Type événement'].unique().tolist()
            selected_event_type = st.selectbox("Sélectionner un type d'événement", options=["Tous"] + event_types)
        else:
            selected_event_type = "Tous"

        # Filtre par conditions tarifaires
        if 'Conditions tarifaires' in data.columns:
            pricing_conditions = data['Conditions tarifaires'].unique().tolist()
            selected_pricing_condition = st.selectbox("Sélectionner une condition tarifaire", options=["Tous"] + pricing_conditions)
        else:
            selected_pricing_condition = "Tous"

        # Filtrer les données selon les sélections
        filtered_data = data.copy()

        if selected_region != "Tous":
            filtered_data = filtered_data[filtered_data['Région'] == selected_region]
        if selected_city != "Tous":
            filtered_data = filtered_data[filtered_data['Ville'] == selected_city]
        if selected_theme != "Tous":
            filtered_data = filtered_data[filtered_data['Tags du lieu'].str.contains(selected_theme, na=False)]
        if selected_event_type != "Tous":
            filtered_data = filtered_data[filtered_data['Type événement'] == selected_event_type]
        if selected_pricing_condition != "Tous":
            filtered_data = filtered_data[filtered_data['Conditions tarifaires'] == selected_pricing_condition]

        # Afficher la carte avec les données filtrées
        fig = px.scatter_mapbox(filtered_data, lat='Latitude', lon='Longitude', hover_name='Titre - FR', 
                                hover_data=['Région', 'Ville'],
                                color_discrete_sequence=["fuchsia"], zoom=4, height=500)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        st.plotly_chart(fig)
        
        st.header("Aperçu des données filtrées")
        st.dataframe(filtered_data.head(20))



    
    
elif selected == "Portofolio":
    # Titre
    st.title("Portfolio de Sarah Nguyen")

    # Informations de contact
    st.header("Informations de contact")
    st.write("📞 06 95 26 54 73")
    st.write("✉️ sarah.n77340@gmail.com")
    st.write("[LinkedIn](https://www.linkedin.com/in/sarah-nguyen-7b5123194)")
    st.write("[GitHub](https://github.com/Sarah77340)")

    # À propos de moi
    st.header("À propos de moi")
    st.write(
        "Actuellement en cycle ingénieur à l'Efrei, je suis à la recherche d'un stage d'une durée de 5 mois "
        "(de début novembre à début avril) pour mon année de M1, avec une spécialisation en Data Engineering."
    )

    # Expérience professionnelle
    st.header("Expérience professionnelle")
    st.subheader("Développeuse d'application web")
    st.write("**Daozhu Taiwan** (juin 2022 - août 2022 & juin 2021 - août 2021)")
    st.write("- Gestion de la préparation des commandes et gestion des stocks.")
    st.write("- Outils : Vue.js, Node.js, JavaScript, MySQL")

    st.subheader("Chargée de communication")
    st.write("**EnovNow SAS, Champs-sur-Marne, France** (juin 2021 - août 2021)")
    st.write("- Responsable de la refonte du site web et gestion des réseaux sociaux.")
    st.write("- Refonte du site web et préparation pour des expositions et interviews.")

    # Projets
    st.header("Projets")
    st.subheader("ABM/GAB : Guichet Automatique Bancaire")
    st.write("Durée : 3 semaines | Outils : Java, UML | Langue : anglais")
    st.write("- Conceptualisation et modélisation du projet avec des diagrammes UML et des cartes CRC.")
    st.write("- Implémentation d'une preuve de concept incluant tous les principaux cas d'utilisation.")
    st.write("- Utilisation de données d'échantillonnage en format JSON.")

    st.subheader("Jeu du Serpent")
    st.write("Durée : 2 semaines | Outils : Python")
    st.write("- Développement des fonctionnalités du jeu du serpent, y compris l'apparition d'objets et d'obstacles.")

    st.subheader("Brevets explicables en IA")
    st.write("Durée : 3 semaines | Outils : Python, TensorFlow, Pandas, NumPy")
    st.write("- Recherche et analyse de la littérature.")
    st.write("- Analyse et préparation des données brutes.")
    st.write("- Définition et implémentation d'un pipeline de traitement des données.")
    st.write("- Entraînement du modèle avec BERT.")

    # Formations
    st.header("Formations")
    st.subheader("Diplôme d'Ingénieur en Informatique")
    st.write("**Efrei Paris** (2023 - 2026)")
    st.write("- Cours en cours : Machine Learning, Data Visualization, Advanced Databases, Big Data Frameworks")
    st.write("- Programme de mobilité internationale : Université Concordia, Montréal, QC, Canada (janv. 2024 - mai 2024)")

    st.subheader("Licence en Informatique")
    st.write("**Université Gustave Eiffel, Institut Gaspard Monge, Champs-sur-Marne, France** (2020 - 2023)")

    # Certifications
    st.header("Certifications")
    st.write("- Certification PIX")
    st.write("- Certification CISCO Cybersecurity Essentials")

    # Compétences
    st.header("Compétences techniques")
    st.subheader("Langages de programmation")
    st.write("Java, C, C++, Python, Haskell, R")

    st.subheader("Outils de science des données")
    st.write("Matplotlib, TensorFlow, Pandas, NumPy")

    st.subheader("Bases de données")
    st.write("PostgreSQL, MySQL")

    st.subheader("Technologies web")
    st.write("HTML, CSS, JavaScript, PHP, Node.js, Vue.js")

    st.subheader("Conception de compilateur")
    st.write("GNU Bison, Flex, Nasm")

    st.subheader("Environnements de développement")
    st.write("Eclipse, Visual Studio Code, Visual Studio, Jupyter Notebook")

    st.subheader("Logiciels")
    st.write("VMWare, VirtualBox, Git")

    st.subheader("Systèmes d'exploitation")
    st.write("Windows, Linux")

    st.subheader("Modélisation")
    st.write("UML")

    # Langues
    st.header("Langues")
    st.write("Anglais : Niveau courant (TOEIC B2)")
    st.write("Chinois : Niveau courant (oral)")
    st.write("Japonais : Niveau scolaire")

    # Centres d'intérêt
    st.header("Centres d'intérêt")
    st.write("- Arts manuels")
    st.write("- Gastronomie")
    st.write("- Piano")
    st.write("- Manga")
    st.write("- Mode")
    st.write("- Lego")

    # Expériences associatives
    st.header("Expériences associatives")
    st.subheader("Animatrice (bénévolat)")
    st.write("**Centre Social et Culturel, Pontault-Combault, France** (décembre 2019)")
    st.write("- Préparation d'événements et animation du stand.")

    # Footer
    st.header("Merci!")
    st.write("N'hésitez pas à me contacter pour toute opportunité ou collaboration.")
