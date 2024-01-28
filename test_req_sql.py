"""
Module de tests pour le script test_req_sql.py

Ce module contient des tests unitaires pour les fonctions
et requêtes SQL du script test_req_sql.py.
Les tests sont écrits en utilisant le framework de test pytest.

Avertissement :
- Ce module nécessite l'installation pytest.
- Certains tests peuvent nécessiter des modifications de la base de données,
veuillez faire attention lors de l'exécution.

Usage :
- Exécutez le script en utilisant pytest pour exécuter tous les tests définis dans ce module.

Exemple :
    pytest -s test_req_sql.py
"""
# test_req_sql.py
from imports import pytest, sqlite3
from req_sql import AcheteurFromageManager

@pytest.fixture(name="manager")
def manager_fixture():
    """
    Crée une instance de AcheteurFromageManager pour les tests unitaires.
    Returns:
        AcheteurFromageManager: Une instance de la classe AcheteurFromageManager.
    """
    return AcheteurFromageManager()

def test_creer_table_acheteur_fromage(manager):
    """
    Teste la création de la table 'acheteur_fromage' dans la base de données.
    Assure que la méthode creer_table_acheteur_fromage crée correctement la table
    avec les colonnes 'id', 'nom', 'prenom', et 'age'.
    """
    manager.creer_table_acheteur_fromage()
    manager.cur.execute("PRAGMA table_info(acheteur_fromage)")
    columns = manager.cur.fetchall()
    assert len(columns) == 4
    assert columns[0][1] == 'id'
    assert columns[1][1] == 'nom'
    assert columns[2][1] == 'prenom'
    assert columns[3][1] == 'age'

def test_insertion_directe(manager):
    """
    Teste l'insertion directe d'un acheteur dans la table 'acheteur_fromage'.
    Assure que la méthode insertion_directe fonctionne correctement.
    """
    manager.insertion_directe('REVIRON', 'Jérôme', 37)
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='REVIRON'")
    result = manager.cur.fetchone()
    assert result is not None
    assert result[1] == 'REVIRON'
    assert result[2] == 'Jérôme'
    assert result[3] == 37

def test_insertion_tuple(manager):
    """
    Teste l'insertion d'un acheteur à partir d'un tuple dans la table 'acheteur_fromage'.
    Assure que la méthode insertion_tuple fonctionne correctement.
    """
    acheteur_tuple = ('DUPONT', 'Pierre', 42)
    manager.insertion_tuple(acheteur_tuple)
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='DUPONT'")
    result = manager.cur.fetchone()
    assert result is not None
    assert result[1] == 'DUPONT'
    assert result[2] == 'Pierre'
    assert result[3] == 42

def test_insertion_dict(manager):
    """
    Teste l'insertion d'un acheteur à partir d'un dictionnaire dans la table 'acheteur_fromage'.
    Assure que la méthode insertion_dict fonctionne correctement.
    """
    acheteur_dict = {'nom': 'CAPITAIN', 'prenom': 'Crochet', 'age': 75}
    manager.insertion_dict(acheteur_dict)
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='CAPITAIN'")
    result = manager.cur.fetchone()
    assert result is not None
    assert result[1] == 'CAPITAIN'
    assert result[2] == 'Crochet'
    assert result[3] == 75

def test_insert_multiple_list(manager):
    """
    Teste l'insertion de plusieurs acheteurs dans la table 'acheteur_fromage'.
    Assure que la méthode insert_multiple_list fonctionne correctement.
    """
    autre_acheteur = [
        ('MARTIN', 'Adeline', 16),
        ('RICHARD', 'Lucas', 35),
        ('GRANGER', 'Louise', 48)
    ]
    manager.insert_multiple_list(autre_acheteur)
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='MARTIN'")
    result_martin = manager.cur.fetchone()
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='RICHARD'")
    result_richard = manager.cur.fetchone()
    manager.cur.execute("SELECT * FROM acheteur_fromage WHERE nom='GRANGER'")
    result_granger = manager.cur.fetchone()
    assert result_martin is not None
    assert result_richard is not None
    assert result_granger is not None

def test_insert_multiple_list_executemany(manager):
    """
    Teste l'insertion multiple d'acheteurs dans la table 'acheteur_fromage'
    en utilisant la méthode executemany.

    Assure que la méthode insert_multiple_list_executemany fonctionne correctement.
    """
    autre_acheteur2 = [
        ('LUPIN', 'Marius', 28),
        ('DODET', 'Lola', 89),
        ('JACKSON', 'Lise', 55),
        ('DISCHAMPS', 'Aurélien', 22)
    ]
    manager.insert_multiple_list_executemany(autre_acheteur2)
    for nom, prenom, age in autre_acheteur2:
        manager.cur.execute(f"SELECT * FROM acheteur_fromage WHERE nom='{nom}'")
        result = manager.cur.fetchone()
        assert result is not None
        assert result[2:] == (prenom, age)

def test_insert_multiple_from_dict_executemany(manager):
    """
    Teste l'insertion multiple d'acheteurs dans la table 'acheteur_fromage'
    à partir d'une liste de dictionnaires en utilisant la méthode executemany.

    Assure que la méthode insert_multiple_from_dict_executemany fonctionne correctement.
    """
    autre_acheteur3 = [
        {'nom': 'SALSA', 'prenom': 'Diego', 'age': 25},
        {'nom': 'POTTER', 'prenom': 'Harry', 'age': 49},
        {'nom': 'QUEEN', 'prenom': 'Elisabeth', 'age': 93},
        {'nom': 'MERCURY', 'prenom': 'Freddy', 'age': 100}
    ]
    manager.insert_multiple_from_dict_executemany(autre_acheteur3)
    for acheteur_dict in autre_acheteur3:
        nom = acheteur_dict['nom']
        manager.cur.execute(f"SELECT * FROM acheteur_fromage WHERE nom='{nom}'")
        result = manager.cur.fetchone()
        assert result is not None
        assert result[2:] == (acheteur_dict['prenom'], acheteur_dict['age'])

def test_select_all_and_fetchall(manager):
    """
    Teste la sélection de tous les enregistrements de la table 'acheteur_fromage'
    et l'utilisation de fetchall pour les résultats.
    Assure que la méthode select_all_and_fetchall fonctionne correctement.
    """
    result_set_local = manager.select_all_and_fetchall()
    assert len(result_set_local) > 0

def test_select_all_list(manager):
    """
    Teste la sélection de tous les enregistrements de la table 'acheteur_fromage'
    et la conversion en liste.
    Assure que la méthode select_all_list fonctionne correctement.
    """
    result_list_local = manager.select_all_list()
    assert len(result_list_local) > 0

def test_select_fetchone(manager):
    """
    Teste la sélection de tous les enregistrements de la table 'acheteur_fromage'
    et l'utilisation de fetchone pour obtenir le premier résultat.
    Assure que la méthode select_fetchone fonctionne correctement.
    """
    result_one_local = manager.select_fetchone()
    assert result_one_local is not None

def test_select_fetchmany(manager):
    """
    Teste la sélection de plusieurs enregistrements de la table 'acheteur_fromage'
    en utilisant fetchmany.
    Assure que la méthode select_fetchmany fonctionne correctement.
    """
    n = 3
    result_many_local = manager.select_fetchmany(n)
    assert len(result_many_local) == n

def test_select_nom_tuple(manager):
    """
    Teste la sélection des enregistrements par nom avec fetchall
    et les renvoie sous forme de tuples.
    Assure que la méthode select_nom_tuple fonctionne correctement.
    """
    nom_rechercher = 'DUPONT'
    result_select_nom_tuple_local = manager.select_nom_tuple(nom_rechercher)
    assert len(result_select_nom_tuple_local) > 0
    for result in result_select_nom_tuple_local:
        assert result[1] == nom_rechercher

def test_select_nom_dict(manager):
    """
    Teste la sélection des enregistrements par nom avec fetchall
    et les renvoie sous forme de dictionnaires.
    Assure que la méthode select_nom_dict fonctionne correctement.
    """
    nom_rechercher = 'REVIRON'
    result_select_nom_dict_local = manager.select_nom_dict(nom_rechercher)
    assert len(result_select_nom_dict_local) > 0
    for result in result_select_nom_dict_local:
        assert result['nom'] == nom_rechercher

def test_get_buyer_names(manager):
    """
    Teste la sélection des acheteurs par nom avec fetchall.
    Assure que la méthode get_buyer_names fonctionne correctement.
    """
    nom_a_rechercher = 'POTTER'
    acheteurs = manager.get_buyer_names(nom_a_rechercher)
    assert len(acheteurs) > 0
    for acheteur in acheteurs:
        assert acheteur[1] == nom_a_rechercher

def test_sort_name(manager):
    """
    Teste le tri des enregistrements de la table 'acheteur_fromage' par nom.
    Assure que la méthode sort_name fonctionne correctement.
    """
    result_set_sorted = manager.sort_name()
    assert len(result_set_sorted) > 0
    sorted_names = [record[1] for record in result_set_sorted]
    assert sorted_names == sorted(sorted_names)

def test_delete_buyer_name(manager):
    """
    Teste la suppression des enregistrements de la table correspondant à un nom donné.
    Assure que la méthode delete_buyer_name fonctionne correctement.
    """
    nom_a_supprimer = 'MERCURY'
    manager.delete_buyer_name(nom_a_supprimer)
    result_set_after_deletion = manager.sort_name()
    for record in result_set_after_deletion:
        assert record[1] != nom_a_supprimer

def test_modify_age_by_name(manager):
    """
    Teste la modification de l'âge d'un acheteur dans la table 'acheteur_fromage'
    en spécifiant son nom.
    Assure que la méthode modify_age_by_name fonctionne correctement.
    """
    nom_a_modifier = 'DUPONT'
    nouvel_age = 35
    manager.modify_age_by_name(nom_a_modifier, nouvel_age)
    result_set_after_modification = manager.sort_name()
    for record in result_set_after_modification:
        if record[1] == nom_a_modifier:
            assert record[3] == nouvel_age

def test_sort_ascending_age(manager):
    """
    Teste la sélection de tous les enregistrements dans la table
    et le tri par âge de manière ascendante.
    Assure que la méthode sort_ascending_age fonctionne correctement.
    """
    result_set_ascending = manager.sort_ascending_age()
    assert len(result_set_ascending) > 0
    sorted_ages = [record[3] for record in result_set_ascending]
    assert sorted_ages == sorted(sorted_ages)

def test_sort_descending_age(manager):
    """
    Teste la sélection de tous les enregistrements dans la table
    et le tri par âge de manière descendante.
    Assure que la méthode sort_descending_age fonctionne correctement.
    """
    result_set_descending = manager.sort_descending_age()
    assert len(result_set_descending) > 0
    sorted_ages = [record[3] for record in result_set_descending]
    assert sorted_ages == sorted(sorted_ages, reverse=True)

def test_close_connection(manager):
    """
    Teste la fermeture de la connexion à la base de données.
    Assure que la méthode close_connection ferme correctement la connexion.
    """
    manager.close_connection()
    with pytest.raises(sqlite3.ProgrammingError):
        # Tente d'exécuter une requête pour voir si la connexion est fermée
        manager.cur.execute("SELECT 1")

if __name__ == '__main__':
    pytest.main()
