"""
Ce module contient les importations nécessaires pour le script.
"""
from imports import sqlite3, urlopen, Request, urlretrieve, BeautifulSoup, pd, datetime, os, timeit

class FromageETL:
    """
    Une classe dédiée à l'extraction, la transformation et le chargement (ETL) de données
    relatives aux fromages. Cette classe permet de récupérer des données depuis une source,
    de les traiter, de les stocker dans une base de données SQLite, et d'effectuer diverses
    opérations sur ces données.
    
    Attributes :
    - url (str) : L'URL à partir de laquelle les données peuvent être extraites.
    - data (pd.DataFrame) : Un DataFrame pandas contenant les données sur les fromages.
    """

    def __init__(self, url):
        """
        Initialise une instance de la classe FromageETL.

        Parameters:
        - url (str): L'URL à partir de laquelle les données sur les fromages seront extraites.
        """
        self.url = url
        self.data = None

    def extract(self):
        """
        Extrait les données à partir de l'URL spécifiée et les stocke dans self.data.
        """
        data = urlopen(self.url)
        self.data = data.read()

    def extract_description(self, url):
        """
        Extrait la description d'une page web spécifique.

        Parameters:
        - url (str): L'URL de la page web à partir de laquelle la description sera extraite.

        Returns:
        - description (str): La description extraite.
        """
        try:
            # Ouvrir l'URL et lire le contenu HTML
            data = urlopen(url)
            html_content = data.read()
        except Exception as e:
            print(f"Erreur lors de l'ouverture de l'URL {url} : {e}")
            return ""

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trouver l'élément <div> avec la classe "woocommerce-product-details__short-description"
        description_div = soup.find('div', {'class': 'woocommerce-product-details__short-description'})

        # Initialiser une liste vide pour stocker les paragraphes de la description
        description_paragraphs = []

        # Vérifier si l'élément <div> a été trouvé
        if description_div:
            # Trouver tous les éléments <p> dans le <div>
            p_elements = description_div.find_all('p')

            # Parcourir tous les éléments <p> trouvés
            for p in p_elements:
                # Vérifier si le texte de l'élément <p> n'est pas vide
                if p.text.strip() != '':
                    # Ajouter le texte de l'élément <p> à la liste des paragraphes de la description
                    description_paragraphs.append(p.text.strip())
        else:
            print(f"Aucun élément <div> trouvé dans l'URL {url}")

        # Joindre tous les paragraphes de la description en une seule chaîne de caractères
        description = ' '.join(description_paragraphs)

        return description

    def extract_rating_and_reviews(self, url):
        """
        Extrait la note moyenne et le nombre d'avis d'une page web spécifique.

        Parameters:
        - url (str): L'URL de la page web à partir de laquelle les informations seront extraites.

        Returns:
        - note_moyenne (float): La note moyenne du fromage.
        - nb_avis (int): Le nombre d'avis sur le fromage.
        """
        # Ouvrir l'URL et lire le contenu HTML
        data = urlopen(url)
        html_content = data.read()

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trouver l'élément <div> avec la classe "woocommerce-product-rating"
        rating_div = soup.find('div', {'class': 'woocommerce-product-rating'})

        # Initialiser la note moyenne et le nombre d'avis comme None
        note_moyenne = None
        nb_avis = None

        # Vérifier si l'élément <div> a été trouvé
        if rating_div:
            # Trouver l'élément <strong> avec la classe "rating" pour la note moyenne
            rating_strong = rating_div.find('strong', {'class': 'rating'})
            if rating_strong:
                note_moyenne = float(rating_strong.text.strip())

            # Trouver l'élément <span> avec la classe "rating" pour le nombre d'avis
            rating_span = rating_div.find('span', {'class': 'rating'})
            if rating_span:
                nb_avis = int(rating_span.text.strip())

        return note_moyenne, nb_avis

    def extract_price(self, url):
        """
        Extrait le prix d'une page web spécifique.

        Parameters:
        - url (str): L'URL de la page web à partir de laquelle les informations seront extraites.

        Returns:
        - prix (float): Le prix du fromage.
        """
        # Ouvrir l'URL et lire le contenu HTML
        data = urlopen(url)
        html_content = data.read()

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trouver la balise parente <p class="price">
        parent_tag = soup.find('p', class_='price')

        # Initialiser le prix comme None
        prix = None

        # Vérifier si la balise parente a été trouvée
        if parent_tag:
            # Trouver l'élément <bdi> à l'intérieur de la balise parente
            price_bdi = parent_tag.find('bdi')

            # Vérifier si l'élément <bdi> a été trouvé
            if price_bdi:
                # Extraire le texte de l'élément <bdi> et le convertir en float
                prix_text = price_bdi.text.strip()
                # Supprimer le symbole € et le caractère non-breaking space ( )
                prix_text = prix_text.replace('€', '').replace('\xa0', '')

                try:
                    # Convertir le texte en float
                    prix = float(prix_text)
                except ValueError as e:
                    print(f"Erreur lors de la conversion du prix en float : {e}")

        return prix

    def extract_and_save_image(self, url, save_dir='./images_fromage/'):
        """
        Extrait l'URL de l'image d'une page web spécifique
        et sauvegarde l'image dans un dossier local.

        Parameters:
        - url (str): L'URL de la page web à partir de laquelle l'URL de l'image sera extraite.
        - save_dir (str): Le chemin du dossier où l'image sera sauvegardée.

        Returns:
        - image_filename (str): Le nom du fichier de l'image sauvegardée.
        """
        # Ouvrir l'URL et lire le contenu HTML
        data = urlopen(url)
        html_content = data.read()

        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(html_content, 'html.parser')

        # Trouver le <div> avec la classe "woocommerce-product-gallery__wrapper"
        div_tag = soup.find('div', {'class': 'woocommerce-product-gallery__wrapper'})

        # Initialiser le nom du fichier de l'image comme None
        image_filename = None

        # Vérifier si le <div> a été trouvé
        if div_tag:
            # Trouver l'élément <a> à l'intérieur du <div>
            a_tag = div_tag.find('a')

            # Vérifier si l'élément <a> a été trouvé
            if a_tag:
                # Extraire l'URL de l'image à partir de l'attribut 'href' de l'élément <a>
                image_url = a_tag['href']

                # Extraire le nom du fichier de l'image à partir de l'URL de l'image
                image_filename = os.path.basename(image_url)

                # Créer le dossier s'il n'existe pas déjà
                os.makedirs(save_dir, exist_ok=True)

                # Créer le chemin complet du fichier de l'image
                image_filepath = os.path.join(save_dir, image_filename)

                print("Téléchargement de l'image depuis l'URL :", image_url)

                # Télécharger et sauvegarder l'image
                urlretrieve(image_url, image_filepath)

        return image_filename

    def transform(self):
        """
        Transforme les données extraites en un DataFrame pandas structuré.

        Le processus implique l'analyse HTML des données,
        la récupération des informations sur les fromages
        à partir de la table HTML, et la création d'un DataFrame avec les colonnes 'fromage_names', 
        'fromage_familles', 'pates', 'url_info_fromage', 'descriptions',
        'note_moyenne', 'nb_avis', 'prix', et 'images_fromage'.
        """
        soup = BeautifulSoup(self.data, 'html.parser')
        cheese_dish = soup.find('table')

        fromage_names = []
        fromage_familles = []
        pates = []
        url_info_fromages = []
        descriptions = []
        note_moyennes = []
        nb_aviss = []
        prixs = []
        images_fromage = []

        for row in cheese_dish.find_all('tr'):
            columns = row.find_all('td')

            if columns[0].text.strip() == "Fromage":
                continue

            if columns:
                fromage_name = columns[0].text.strip()
                fromage_famille = columns[1].text.strip()
                pate = columns[2].text.strip()

                # Chercher le lien dans la même cellule que "fromage_name"
                link = columns[0].find('a')
                url_info_fromage = "https://www.laboitedufromager.com" + link['href'] if link else ""

                # Initialiser tout à None
                description = ""
                note_moyenne = None
                nb_avis = None
                prix = None
                image_filename = None

                # Vérifier si l'URL est présente
                if url_info_fromage:
                    # Extraire tout du fichier de l'image depuis l'URL
                    description = self.extract_description(url_info_fromage)
                    note_moyenne, nb_avis = self.extract_rating_and_reviews(url_info_fromage)
                    prix = self.extract_price(url_info_fromage)
                    image_filename = self.extract_and_save_image(url_info_fromage)

                # Ignore les lignes vides
                if fromage_name != '' and fromage_famille != '' and pate != '':
                    fromage_names.append(fromage_name)
                    fromage_familles.append(fromage_famille)
                    pates.append(pate)
                    url_info_fromages.append(url_info_fromage)
                    descriptions.append(description)
                    note_moyennes.append(note_moyenne)
                    nb_aviss.append(nb_avis)
                    prixs.append(prix)
                    images_fromage.append(image_filename)

                # # Imprime la longueur de chaque liste
                # print("Nombre de fromage_names: ", len(fromage_names))
                # print("Nombre de fromage_familles: ", len(fromage_familles))
                # print("Nombre de pates: ", len(pates))
                # print("Nombre de url_info_fromages: ", len(url_info_fromages))
                # print("Nombre de descriptions: ", len(descriptions))
                # print("Nombre de note_moyennes: ", len(note_moyennes))
                # print("Nombre de nb_aviss: ", len(nb_aviss))
                # print("Nombre de prixs: ", len(prixs))
                print("Nombre de images_fromage: ", len(images_fromage))

            self.data = pd.DataFrame({
                'fromage_names': fromage_names,
                'fromage_familles': fromage_familles,
                'pates': pates,
                'url_info_fromages': url_info_fromages,
                'descriptions': descriptions,
                'note_moyenne': note_moyennes,
                'nb_avis': nb_aviss,
                'prix' : prixs,
                'images_fromage': images_fromage
            })
            self.data['creation_date'] = datetime.now()

            # print(self.data)

    def load(self, database_name, table_name):
        """
        Charge les données dans une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table dans laquelle charger les données.
        """
        con = sqlite3.connect(database_name)
        self.data.to_sql(table_name, con, if_exists="replace", index=False)
        con.close()
        return self.data

    def read_from_database(self, database_name, table_name):
        """
        Lit les données à partir d'une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à lire.

        Returns:
        - pd.DataFrame: Un DataFrame contenant les données de la table.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT * from {table_name}", con)
        con.close()
        return data_from_db

    def get_fromage_names(self, database_name, table_name):
        """
        Récupère les noms de fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'fromage_names'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT fromage_names from {table_name}", con)
        con.close()
        return data_from_db

    def get_fromage_familles(self, database_name, table_name):
        """
        Récupère les familles de fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'fromage_familles'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT fromage_familles from {table_name}", con)
        con.close()
        return data_from_db

    def get_pates(self, database_name, table_name):
        """
        Récupère les types de pâtes des fromages depuis une table SQLite spécifiée.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant la colonne 'pates'.
        """
        con = sqlite3.connect(database_name)
        data_from_db = pd.read_sql_query(f"SELECT pates from {table_name}", con)
        con.close()
        return data_from_db

    def connect_to_database(self, database_name):
        """
        Établit une connexion à une base de données SQLite.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.

        Returns:
        - sqlite3.Connection: Objet de connexion à la base de données.
        """
        con = sqlite3.connect(database_name)
        return con

    def add_row(self, fromage_name, fromage_famille, pate):
        """
        Ajoute une nouvelle ligne à l'ensemble de données avec les informations spécifiées.

        Parameters:
        - fromage_name (str): Nom du fromage à ajouter.
        - fromage_famille (str): Famille du fromage à ajouter.
        - pate (str): Type de pâte du fromage à ajouter.
        """
        new_row = pd.DataFrame({'fromage_names': [fromage_name],
            'fromage_familles': [fromage_famille], 'pates': [pate]})
        self.data = pd.concat([self.data, new_row], ignore_index=True)

    def sort_ascending(self):
        """
        Trie l'ensemble de données par ordre croissant des noms de fromages.
        """
        self.data = self.data.sort_values(by=['fromage_names'])

    def sort_descending(self):
        """
        Trie l'ensemble de données par ordre décroissant des noms de fromages.
        """
        self.data = self.data.sort_values(by=['fromage_names'], ascending=False)

    def total_count(self):
        """
        Retourne le nombre total de lignes dans l'ensemble de données.

        Returns:
        - int: Nombre total de lignes.
        """
        return len(self.data)

    def count_by_letter(self):
        """
        Compte le nombre de fromages par lettre initiale dans les noms.

        Returns:
        - pd.Series: Série contenant le décompte des fromages par lettre initiale.
        """
        return self.data['fromage_names'].str[0].value_counts()

    def update_fromage_name(self, old_name, new_name):
        """
        Met à jour le nom d'un fromage dans l'ensemble de données.

        Parameters:
        - old_name (str): Ancien nom du fromage à mettre à jour.
        - new_name (str): Nouveau nom à attribuer au fromage.
        """
        self.data.loc[self.data.fromage_names == old_name, 'fromage_names'] = new_name

    import sqlite3

    def delete_row(self, fromage_name):
        """
        Supprime une ligne de l'ensemble de données basée sur le nom du fromage.

        Parameters:
        - fromage_name (str): Nom du fromage à supprimer.
        """
        self.data = self.data[self.data.fromage_names != fromage_name]

    def group_and_count_by_first_letter(self, database_name, table_name):
        """
        Regroupe les fromages par la première lettre de la famille,
        et compte le nombre de fromages par groupe.

        Parameters:
        - database_name (str): Le nom de la base de données SQLite.
        - table_name (str): Le nom de la table à interroger.

        Returns:
        - pd.DataFrame: Un DataFrame contenant les colonnes 'fromage_familles' et 'fromage_nb'.
        """
        # Utilisez la fonction get_fromage_familles pour récupérer les familles de fromages
        data_from_db = self.get_fromage_familles(database_name, table_name)

        # Créez une nouvelle colonne 'lettre_alpha'
        data_from_db['lettre_alpha'] = data_from_db['fromage_familles'].str[0]

        # Utilisez groupby pour regrouper par 'fromage_familles' et compter les fromages
        grouped_data = data_from_db.groupby('fromage_familles').size().reset_index(name='fromage_nb')

        return grouped_data

# Utilisation de la classe
start = timeit.default_timer()
A = 'https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/'
fromage_etl = FromageETL(A)
fromage_etl.extract()
fromage_etl.transform()
fromage_etl.load('fromages_bdd.sqlite', 'fromages_table')
data_from_db_external = fromage_etl.read_from_database('fromages_bdd.sqlite', 'fromages_table')

# Afficher le DataFrame
print(data_from_db_external)
print(timeit.default_timer() - start)

    # def count_filled_image_rows(database_path='fromages_bdd.sqlite'):
    #     try:
    #         # Connexion à la base de données
    #         connection = sqlite3.connect(database_path)
    #         cursor = connection.cursor()

    #         # Exécution de la requête pour compter les lignes avec une valeur non nulle dans la colonne image_fromage
    #         query = "SELECT COUNT(*) FROM fromages_table WHERE images_fromage IS NOT NULL"
    #         cursor.execute(query)

    #         # Récupération du résultat
    #         count = cursor.fetchone()[0]

    #         # Fermeture de la connexion
    #         connection.close()

    #         return count

    #     except sqlite3.Error as error:
    #         print("Erreur lors de l'accès à la base de données:", error)

    # # Utilisation de la fonction
    # nombre_lignes_remplies = count_filled_image_rows()
    # print(f"Nombre de lignes remplies dans la colonne image_fromage : {nombre_lignes_remplies}")

    # def get_images_fromage_df(database_path='fromages_bdd.sqlite'):
    #     try:
    #         connection = sqlite3.connect(database_path)
    #         cursor = connection.cursor()

    #         # Exécution de la requête pour récupérer les données de la colonne image_fromage
    #         query = "SELECT images_fromage FROM fromages_table"
    #         cursor.execute(query)

    #         # Récupération des résultats
    #         images_fromage = cursor.fetchall()

    #         # Fermeture de la connexion
    #         connection.close()

    #         # Transformation de la liste de tuples en une liste simple
    #         images_fromage_list = [item[0] for item in images_fromage]

    #         # Création d'un DataFrame Pandas
    #         df = pd.DataFrame(images_fromage_list, columns=['images_fromage'])

    #         return df

    #     except sqlite3.Error as error:
    #         print("Erreur lors de l'accès à la base de données:", error)

    # # Utilisation de la fonction pour obtenir le DataFrame
    # images_fromage_df = get_images_fromage_df()

    # # Affichage du DataFrame dans le terminal
    # print(images_fromage_df)

    # def get_fromages_without_images(database_path='fromages_bdd.sqlite'):
    #     try:
    #         connection = sqlite3.connect(database_path)
    #         cursor = connection.cursor()

    #         # Exécution de la requête pour récupérer les noms de fromages sans image associée
    #         query = "SELECT fromage_names FROM fromages_table WHERE images_fromage IS NULL"
    #         cursor.execute(query)

    #         # Récupération des résultats
    #         fromages_without_images = cursor.fetchall()

    #         # Fermeture de la connexion
    #         connection.close()

    #         # Transformation de la liste de tuples en une liste simple
    #         fromages_without_images_list = [item[0] for item in fromages_without_images]

    #         return fromages_without_images_list

    #     except sqlite3.Error as error:
    #         print("Erreur lors de l'accès à la base de données:", error)

    # # Utilisation de la fonction pour obtenir la liste des fromages sans image
    # fromages_sans_images = get_fromages_without_images()
    
    # # Création d'un DataFrame pandas
    # df = pd.DataFrame({"Fromage sans image associée": fromages_sans_images})

    # # Affichage du DataFrame dans le terminal
    # print(df)