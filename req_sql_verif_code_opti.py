"""
Ce module contient les importations nécessaires pour le script.
"""
from imports import sqlite3, pd

class Verification:
    """
    Gère l'accès à la base de données pour les acheteurs de fromage.

    Attributes:
        conn (sqlite3.Connection): Connexion à la base de données SQLite.
        cur (sqlite3.Cursor): Curseur pour exécuter des requêtes SQL.
    """
    def __init__(self):
        self.conn = sqlite3.connect('fromages_bdd.sqlite')
        self.cur = self.conn.cursor()

    def compter_colonnes_fromages_table(self):
        """
        Compte le nombre de colonnes dans la table 'fromages_table'.

        Returns:
        - int: Le nombre de colonnes dans la table.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM fromages_table LIMIT 0")
        columns_info = self.cur.description
        return len(columns_info)

    # controleur.compter_colonnes_fromages_table()

    def compter_lignes_fromage_names(self):
        """
        Compte le nombre de lignes dans la colonne 'fromage_names' de la table 'fromages_table'.

        Returns:
        - int: Le nombre de lignes dans la colonne 'fromage_names'.
        """
        self.cur.execute("SELECT COUNT(fromage_names) FROM fromages_table")
        num_rows = self.cur.fetchone()[0]
        return num_rows

    # controleur.compter_lignes_fromage_names()

    def compter_lignes_fromage_familles(self):
        """
        Compte le nombre de lignes dans la colonne 'fromage_names' de la table 'fromages_table'.

        Returns:
        - int: Le nombre de lignes dans la colonne 'fromage_names'.
        """
        self.cur.execute("SELECT COUNT(fromage_names) FROM fromages_table")
        num_rows = self.cur.fetchone()[0]
        return num_rows

    # controleur.compter_lignes_fromage_familles()

    def compter_lignes_pates(self):
        """
        Compte le nombre de lignes dans la colonne 'pates' de la table 'fromages_table'.

        Returns:
        - int: Le nombre de lignes dans la colonne 'pates'.
        """
        self.cur.execute("SELECT COUNT(pates) FROM fromages_table")
        num_rows = self.cur.fetchone()[0]
        return num_rows

    # controleur.compter_lignes_pates()

    def compter_lignes_url_info_fromages(self):
        """
        Compte le nombre de lignes dans la colonne 'fromage_names' de la table 'fromages_table'.

        Returns:
        - int: Le nombre de lignes dans la colonne 'fromage_names'.
        """
        self.cur.execute("SELECT COUNT(fromage_names) FROM fromages_table")
        num_rows = self.cur.fetchone()[0]
        return num_rows

    # controleur.compter_lignes_url_info_fromages()

    def obtenir_lignes_vides_url_info_fromages(self):
        """
        Obtient la liste des lignes avec des valeurs vides dans la colonne 'url_info_fromages'.

        Returns:
        - list: Liste des lignes avec des valeurs vides dans la colonne 'url_info_fromages'.
        """
        self.cur.execute("""SELECT fromage_names FROM fromages_table
            WHERE url_info_fromages IS NULL OR url_info_fromages = ''""")
        empty_rows_fromage_names = self.cur.fetchall()
        return empty_rows_fromage_names

    # controleur.obtenir_lignes_vides_url_info_fromages()

    def get_fromages_without_images(self):
        """
        Obtient la liste des fromages sans image associée.

        Returns:
        - list: Liste des noms de fromages sans image associée.
        """
        try:
            # Exécution de la requête pour récupérer les noms de fromages sans image associée
            query = "SELECT fromage_names FROM fromages_table WHERE images_fromage IS NULL"
            self.cur.execute(query)

            # Récupération des résultats
            fromages_without_images = self.cur.fetchall()

            # Transformation de la liste de tuples en une liste simple
            fromages_without_images_list = [item[0] for item in fromages_without_images]

            return fromages_without_images_list

        except sqlite3.Error as error:
            print("Erreur lors de l'accès à la base de données:", error)

    # controleur.get_fromages_without_images()

    def print_description_row(self, row_number=7):
        """
        Imprime la donnée dans la colonne 'description' de la ligne spécifiée.

        Parameters:
        - row_number (int): Le numéro de la ligne à afficher.

        Returns:
        - str: La donnée dans la colonne 'description'.
        """
        query = f"SELECT descriptions FROM fromages_table WHERE rowid = {row_number}"
        self.cur.execute(query)
        description_row = self.cur.fetchone()

        if description_row:
            print(f"Donnée 'description' de la ligne {row_number}: {description_row[0]}")
            return description_row[0]
        else:
            print(f"La ligne spécifiée ({row_number}) n'existe pas dans la table.")
            return None

    # controleur.print_description_row()

    def get_data_for_fromage(self, fromage_name='Abondance'):
        """
        Obtient les données des colonnes spécifiées pour un fromage donné.

        Parameters:
        - fromage_name (str): Le nom du fromage.

        Returns:
        - pd.DataFrame: Un DataFrame avec les colonnes spécifiées pour le fromage donné.
        """
        try:
            query = """SELECT note_moyenne, nb_avis, prix 
                FROM fromages_table WHERE fromage_names = ?"""
            self.cur.execute(query, (fromage_name,))
            data_for_fromage = self.cur.fetchone()
            
            return data_for_fromage

        except sqlite3.Error as error:
            print("Erreur lors de l'accès à la base de données:", error)

    # controleur.get_data_for_fromage()

    def get_data_multi_fromages(self, fromage_names=None):
        """ 
        Obtient les données des colonnes spécifiées pour une liste de fromages. 
        Parameters: 
        - fromage_names (list): Liste des noms de fromages. 
        Returns: 
        - pd.DataFrame: Un DataFrame avec les colonnes spécifiées pour les fromages donnés. 
        """
        if fromage_names is None:
            fromage_names = ['Abondance']

        try:
            query = f"""SELECT fromage_names, note_moyenne, nb_avis, prix
                FROM fromages_table WHERE fromage_names IN ({','.join(['?']*len(fromage_names))})"""
            self.cur.execute(query, fromage_names)
            data_for_fromages = self.cur.fetchall()
            return data_for_fromages
        except sqlite3.Error as error:
            print("Erreur lors de l'accès à la base de données:", error)

    # controleur.get_data_for_multi_fromages()

    def close_connection(self):
        """
        Ferme la connexion à la base de données.

        La méthode ferme la connexion à la base de données SQLite.
        """
        self.conn.close()

# Exemple d'utilisation
controleur = verification()

# Compter le nombre de colonnes de 'fromage_names'
nombre_colonnes = controleur.compter_colonnes_fromages_table()
print(f"Le nombre de colonnes de table 'fromages_table' est : {nombre_colonnes}")

# Compter le nombre de lignes de colonne 'fromage_names'
nombre_lignes_fromage_names = controleur.compter_lignes_fromage_names()
print(f"Le nombre de lignes de colonne 'fromage_names' est : {nombre_lignes_fromage_names}")

# Compter le nombre de lignes de colonne 'fromage_familles'
nombre_lignes_fromage_familles = controleur.compter_lignes_fromage_familles()
print(f"Le nombre de lignes de colonne 'fromage_familles' est : {nombre_lignes_fromage_familles}")

# Compter le nombre de lignes de colonne 'pates'
nombre_lignes_pates = controleur.compter_lignes_pates()
print(f"Le nombre de lignes de colonne 'pates' est : {nombre_lignes_pates}")

# Compter le nombre de lignes de colonne 'url_info_fromages'
nombre_lignes_url_info_fromages = controleur.compter_lignes_url_info_fromages()
print(f"Le nombre de lignes de colonne 'url_info_fromages' est : {nombre_lignes_url_info_fromages}")

# Obtenir la liste des 'fromage_names' avec des valeurs vides dans 'url_info_fromages'
fromage_names_lignes_vides_url_info_fromages = controleur.obtenir_lignes_vides_url_info_fromages()
print("Liste des 'fromage_names' avec des valeurs vides dans 'url_info_fromages':")
for row in fromage_names_lignes_vides_url_info_fromages:
    print(row[0])

# Utilisation de la fonction pour obtenir la liste des fromages sans image
fromages_sans_images = controleur.get_fromages_without_images()
df = pd.DataFrame({"Fromage sans image associée": fromages_sans_images})
print(df)

# Utilisation de la fonction pour obtenir la liste de la lligne en paramètre
description_ligne_8 = controleur.print_description_row()
print(description_ligne_8)

# Utilisation de la fonction pour obtenir les données pour le fromage
FROMAGE_CHOISI = 'Abondance'  
data_for_abondance = controleur.get_data_for_fromage(FROMAGE_CHOISI)
columns = ['note_moyenne', 'nb_avis', 'prix']
data_list = [FROMAGE_CHOISI] + list(data_for_abondance)
df = pd.DataFrame([data_list], columns=['fromage_name'] + columns)
print(df)

# Utilisation de la fonction pour obtenir les données pour plusieurs fromages
fromage_mutli_choix = ['Angors','Pardou']
data_multi_fromages = controleur.get_data_multi_fromages(fromage_mutli_choix)
columns = ['fromage_name', 'note_moyenne', 'nb_avis', 'prix']
df = pd.DataFrame(data_multi_fromages, columns=columns)
print(df)

# Fermer connexion
controleur.close_connection()
