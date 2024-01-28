"""
Ce module contient les importations nécessaires pour le script.
"""
from imports import sqlite3

class AcheteurFromageManager:
    """
    Gère l'accès à la base de données pour les acheteurs de fromage.

    Attributes:
        conn (sqlite3.Connection): Connexion à la base de données SQLite.
        cur (sqlite3.Cursor): Curseur pour exécuter des requêtes SQL.
    """
    def __init__(self):
        self.conn = sqlite3.connect('fromages_bdd.sqlite')
        self.cur = self.conn.cursor()

    def creer_table_acheteur_fromage(self):
        """
        Crée une table 'acheteur_fromage' dans la base de données.

        Si la table existe déjà, elle est supprimée avant la création.
        La table contient les colonnes 'id' (clé primaire auto-incrémentée),
        'nom', 'prenom', et 'age'.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS acheteur_fromage")
        self.cur.execute("""CREATE TABLE acheteur_fromage(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            prenom TEXT,
            age INTEGER
            )""")
        self.conn.commit()

    # manager.creer_table_acheteur_fromage()

    def insertion_directe(self, nom, prenom, age):
        """
        Insère un acheteur de fromage dans la table 'acheteur_fromage'.

        Args:
            nom (str): Nom de l'acheteur.
            prenom (str): Prénom de l'acheteur.
            age (int): Âge de l'acheteur.

        La méthode insère un nouvel enregistrement avec les informations spécifiées.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("""INSERT INTO acheteur_fromage (nom, prenom, age)
            VALUES (?, ?, ?)""", (nom, prenom, age))
        self.conn.commit()

    # Appel de la fonction avec des valeurs spécifiques
    # manager.insertion_directe(1, 'REVIRON', 'Jérôme', 37)

    def insertion_tuple(self, acheteur):
        """
        Insère un acheteur de fromage dans la table 'acheteur_fromage' à partir d'un tuple.

        Args:
            acheteur (tuple): Tuple contenant les informations de l'acheteur.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("""INSERT INTO acheteur_fromage (nom, prenom, age)
            VALUES (?, ?, ?)""", acheteur)
        self.conn.commit()

    # Ordre des values importantes
    # manager.insertion_tuple(('DUPONT', 'Pierre', 42))

    def insertion_dict(self, acheteur):
        """
        Insère un acheteur de fromage dans la table 'acheteur_fromage' à partir d'un dictionnaire.

        Args:
            acheteur (dict): Dictionnaire contenant les informations de l'acheteur.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("""INSERT INTO acheteur_fromage (nom, prenom, age)
            VALUES (:nom, :prenom, :age)""", acheteur)
        self.conn.commit()

    # Ordre des values au choix
    # manager.insertion_dict({'nom': 'CAPITAIN', 'prenom': 'Crochet', 'age': 75})

    def insert_multiple_list(self, liste_acheteurs):
        """
        Insère plusieurs acheteurs dans la table 'acheteur_fromage' à partir d'une liste de tuples.

        Args:
            liste_acheteurs (list): Liste contenant des tuples avec les informations des acheteurs.
        """
        self.cur = self.conn.cursor()
        for acheteur in liste_acheteurs:
            self.cur.execute("""INSERT INTO acheteur_fromage (nom, prenom, age)
                VALUES (?, ?, ?)""", acheteur)
        self.conn.commit()

    # Exemple d'appel de la fonction
    # autre_acheteur = [
    #     ('MARTIN', 'Adeline', 16),
    #     ('RICHARD', 'Lucas', 35),
    #     ('GRANGER', 'Louise', 48)
    # ]

    # manager.insert_multiple_list(autre_acheteur)

    def insert_multiple_list_executemany(self,liste_acheteurs):
        """
        Insère plusieurs acheteurs dans la table 'acheteur_fromage' à partir d'une liste de tuples
        en utilisant la méthode executemany.

        Args:
            liste_acheteurs (list): Liste contenant des tuples avec les informations des acheteurs.
        """
        self.cur = self.conn.cursor()
        self.cur.executemany("""INSERT INTO acheteur_fromage (nom, prenom, age)
            VALUES (?, ?, ?)""", liste_acheteurs)
        self.conn.commit()

    # Exemple d'appel de la fonction
    # autre_acheteur2 = [
    #     ('LUPIN', 'Marius', 28),
    #     ('DODET', 'Lola', 89),
    #     ('JACKSON', 'Lise', 55),
    #     ('DISCHAMPS', 'Aurélien', 22)
    # ]

    # manager.insert_multiple_list_executemany(autre_acheteur2)

    def insert_multiple_from_dict_executemany(self, dict_acheteurs):
        """
        Insère plusieurs acheteurs dans la table à partir d'une liste de dictionnaires
        en utilisant la méthode executemany.

        Args:
            dict_acheteurs : Liste contenant des dictionnaires avec les informations des acheteurs.
        """
        self.cur = self.conn.cursor()
        self.cur.executemany("""INSERT INTO acheteur_fromage (nom, prenom, age)
            VALUES (:nom, :prenom, :age)""", dict_acheteurs)
        self.conn.commit()

    # Exemple d'appel de la fonction
    # autre_acheteur3 = [
    #     {'nom': 'SALSA', 'prenom': 'Diego', 'age': 25},
    #     {'nom': 'POTTER', 'prenom': 'Harry', 'age': 49},
    #     {'nom': 'QUEEN', 'prenom': 'Elisabeth', 'age': 93},
    #     {'nom': 'MERCURY', 'prenom': 'Freddy', 'age': 100}
    # ]

    # manager.insert_multiple_from_dict_executemany(autre_acheteur3)

    def select_all_and_fetchall(self):
        """
        Sélectionne tous les enregistrements de la table et utilise fetchall pour les résultats.

        Returns:
            list: Liste des enregistrements récupérés.
        """
        # Sélection de tous les enregistrements et utilisation de fetchall
        self.cur = self.conn.cursor()
        res1 = self.cur.execute("SELECT * FROM acheteur_fromage")
        result_set_local = res1.fetchall()
        return result_set_local

    # manager.print(select_all_and_fetchall())

    def select_all_list(self):
        """
        Sélectionne tous les enregistrements de la table et les convertit en liste.

        Returns:
            list: Liste des enregistrements convertis en liste.
        """
        # Sélection de tous les enregistrements et conversion en liste
        self.cur = self.conn.cursor()
        res2 = self.cur.execute("SELECT * FROM acheteur_fromage")
        result_list_local = list(res2)
        return result_list_local

    # manager.print(select_all_list())

    def select_fetchone(self):
        """
        Sélectionne tous les enregistrements de la table 'acheteur_fromage' et utilise fetchone.

        Returns:
            Any: Premier enregistrement sous forme de tuple.
        """
        # Sélection de tous les enregistrements et utilisation de fetchone
        self.cur = self.conn.cursor()
        res3 = self.cur.execute("SELECT * FROM acheteur_fromage")
        result_one_local = res3.fetchone()
        return result_one_local

    # manager.print(select_fetchone())

    def select_fetchmany(self, n):
        """
        Sélectionne tous les enregistrements de la table 'acheteur_fromage' et utilise fetchmany.

        Args:
            n (int): Nombre d'enregistrements à récupérer.

        Returns:
            List: Liste des enregistrements sous forme de tuples.
        """
        # Sélection de tous les enregistrements et utilisation de fetchmany avec le nombre souhaité
        self.cur = self.conn.cursor()
        res4 = self.cur.execute("SELECT * FROM acheteur_fromage")
        result_many_local = res4.fetchmany(n)
        return result_many_local

    # manager.print(select_fetchmany(3))

    def select_nom_tuple(self, nom):
        """
        Sélectionne les enregistrements par nom avec fetchall.

        Args:
            nom (str): Nom à rechercher dans la table 'acheteur_fromage'.

        Returns:
            List: Liste des enregistrements correspondant au nom sous forme de tuples.
        """
        # Sélection des enregistrements par nom avec fetchall
        self.cur = self.conn.cursor()
        res5 = self.cur.execute("""SELECT id, nom, prenom, age
                            FROM acheteur_fromage
                            WHERE nom = ?""", (nom,))
        result_select_nom_tuple_local = res5.fetchall()
        return result_select_nom_tuple_local

    # manager.select_nom_tuple()
    # NOM_RECHERCHER = 'DUPONT'
    # print(select_nom_tuple(NOM_RECHERCHER))

    def select_nom_dict(self, nom):
        """
        Sélectionne les enregistrements par nom avec fetchall.

        Args:
            nom (str): Nom à rechercher dans la table 'acheteur_fromage'.

        Returns:
            List[Dict[str, Any]]: Liste des enregistrements
            correspondant au nom sous forme de dictionnaires.
        """
        # Sélection des enregistrements par nom avec fetchall
        self.cur = self.conn.cursor()
        res6 = self.cur.execute("""SELECT id, nom, prenom, age
                            FROM acheteur_fromage
                            WHERE nom = :nom""", {'nom': nom})
        columns = [col[0] for col in res6.description]
        result_select_nom_dict_local = [dict(zip(columns, row)) for row in res6.fetchall()]
        return result_select_nom_dict_local

        # manager.select_nom_dict()
        # nom_a_rechercher = 'REVIRON'
        # print(select_nom_dict(nom_a_rechercher))

    def get_buyer_names(self, nom):
        """
        Sélectionne les acheteurs par nom avec fetchall.

        Args:
            nom (str): Nom à rechercher dans la table 'acheteur_fromage'.

        Returns:
            List: Liste des acheteurs correspondant au nom sous forme de tuples.
        """
        # Sélection des acheteurs par nom avec fetchall
        self.cur = self.conn.cursor()
        res7 = self.cur.execute("""SELECT id, nom, prenom, age
                            FROM acheteur_fromage
                            WHERE nom = ?""", (nom,))
        acheteurs = res7.fetchall()
        return acheteurs

    # manager.get_buyer_names()
    # nom_a_rechercher = 'POTTER'
    # print(get_buyer_names(nom_a_rechercher))

    def sort_name(self):
        """
        Trie les enregistrements de la table 'acheteur_fromage' par nom.

        Returns:
            List: Liste triée des enregistrements de la table.
        """
        self.cur = self.conn.cursor()
        res8 = self.cur.execute("SELECT * FROM acheteur_fromage ORDER BY nom")
        result_set_local = res8.fetchall()
        return result_set_local

    # manager.sort_name()
    # print("\nAvant la suppression:")
    # print(sort_name())

    def delete_buyer_name(self, nom):
        """
        Supprime les enregistrements de la table 'acheteur_fromage' correspondant à un nom donné.

        Args:
            nom (str): Nom de l'acheteur à supprimer.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("""DELETE FROM acheteur_fromage WHERE nom = ?""", (nom,))
        self.conn.commit()

    # manager.delete_buyer_name('MERCURY')
    # print("\nAprès la suppression:")
    # print(sort_name())

    def modify_age_by_name(self, nom, nouvel_age):
        """
        Modifie l'âge d'un acheteur dans la table 'acheteur_fromage' en spécifiant son nom.

        Args:
            nom (str): Nom de l'acheteur dont l'âge doit être modifié.
            nouvel_age (int): Nouvel âge à attribuer à l'acheteur.
        """
        self.cur = self.conn.cursor()
        self.cur.execute("""UPDATE acheteur_fromage SET age = ? WHERE nom = ?""", (nouvel_age, nom))
        self.conn.commit()

    # manager.modify_age_by_name('DUPONT', 35)
    # print("\nAprès la modification d'âge:")
    # print(sort_name())

    def sort_ascending_age(self):
        """
        Sélectionne tous les enregistrements dans la table et trie par âge de manière ascendante.

        Returns:
            list: Liste des enregistrements triés par âge de manière ascendante.
        """
        self.cur = self.conn.cursor()
        res = self.cur.execute("SELECT * FROM acheteur_fromage ORDER BY age ASC")
        result_set_local = res.fetchall()
        return result_set_local

    # print(sort_ascending_age())

    def sort_descending_age(self):
        """
        Sélectionne tous les enregistrements dans la table et trie par âge de manière descendante.

        Returns:
            list: Liste des enregistrements triés par âge de manière descendante.
        """
        self.cur = self.conn.cursor()
        res = self.cur.execute("SELECT * FROM acheteur_fromage ORDER BY age DESC")
        result_set_local = res.fetchall()
        return result_set_local

    # print(sort_descending_age())

    def close_connection(self):
        """
        Ferme la connexion à la base de données.

        La méthode ferme la connexion à la base de données SQLite.
        """
        self.conn.close()

# Exemple d'utilisation
manager = AcheteurFromageManager()
manager.creer_table_acheteur_fromage()
manager.insertion_directe('REVIRON', 'Jérôme', 37)
manager.insertion_tuple(('DUPONT', 'Pierre', 42))
manager.insertion_dict({'nom': 'CAPITAIN', 'prenom': 'Crochet', 'age': 75})

autre_acheteur = [
    ('MARTIN', 'Adeline', 16),
    ('RICHARD', 'Lucas', 35),
    ('GRANGER', 'Louise', 48)
]

manager.insert_multiple_list(autre_acheteur)

autre_acheteur2 = [
    ('LUPIN', 'Marius', 28),
    ('DODET', 'Lola', 89),
    ('JACKSON', 'Lise', 55),
    ('DISCHAMPS', 'Aurélien', 22)
]

manager.insert_multiple_list_executemany(autre_acheteur2)

autre_acheteur3 = [
        {'nom': 'SALSA', 'prenom': 'Diego', 'age': 25},
        {'nom': 'POTTER', 'prenom': 'Harry', 'age': 49},
        {'nom': 'QUEEN', 'prenom': 'Elisabeth', 'age': 93},
        {'nom': 'MERCURY', 'prenom': 'Freddy', 'age': 100}
    ]

manager.insert_multiple_from_dict_executemany(autre_acheteur3)

# Sélectionner tous les enregistrements et utiliser fetchall
result_set_global = manager.select_all_and_fetchall()
print(result_set_global)

# Sélectionner tous les enregistrements et convertir en liste
result_list_global = manager.select_all_list()
print(result_list_global)

# Sélectionner tous les enregistrements et utiliser fetchone
result_one_global = manager.select_fetchone()
print(result_one_global)

# Sélectionner tous les enregistrements et utiliser fetchmany avec le nombre souhaité
result_many_global = manager.select_fetchmany(3)
print(result_many_global)

# Sélectionner les enregistrements par nom avec fetchall
NOM_RECHERCHER = 'DUPONT'
result_select_nom_tuple_global = manager.select_nom_tuple(NOM_RECHERCHER)
print(result_select_nom_tuple_global)

# Sélectionner les enregistrements par nom avec fetchall
NOM_A_RECHERCHER = 'REVIRON'
result_select_nom_dict_global = manager.select_nom_dict(NOM_A_RECHERCHER)
print(result_select_nom_dict_global)

# Sélectionner les acheteurs par nom avec fetchall
NOM_A_RECHERCHER = 'POTTER'
acheteurs_global = manager.get_buyer_names(NOM_A_RECHERCHER)
print(acheteurs_global)

# Trier les enregistrements par nom
result_set_sorted = manager.sort_name()
print("\nAvant la suppression:")
print(result_set_sorted)

# Modifier l'âge d'un acheteur
NOM = 'DUPONT'
NOUVEL_AGE = 35
manager.modify_age_by_name(NOUVEL_AGE, NOM)
# Afficher la liste triée après la modification d'âge
result_set_sorted = manager.sort_name()
print("\nAprès la modification d'âge:")
print(result_set_sorted)

# Appel de la fonction pour trier par âge de manière ascendante
result_set_ascending_age = manager.sort_ascending_age()
print("\nTri par âge de manière ascendante:")
print(result_set_ascending_age)

# Appel de la fonction pour trier par âge de manière descendante
result_set_descending_age = manager.sort_descending_age()
print("\nTri par âge de manière descendante:")
print(result_set_descending_age)

# Fermer la connexion
manager.close_connection()
