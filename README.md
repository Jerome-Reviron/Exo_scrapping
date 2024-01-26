# Exo_scrapping

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Scrapping de Fromages à partir d'une Url](#scrapping_fromage.py)
- [Test_scrapping de Fromages](#test_scrapping_fromages.py)
- [Interface fromage_UI](#fromage_UI.py)

## Introduction <a name="introduction"></a>
Ce répertoire est conçu durant ma formation POEI Développeur Applicatif Python, afin d'intégrer l'entreprise Pharma Pilot à Cournond'Auvergne.<br>
Accompagné par Human Booster et de nombreux intervenants, j'aurai à la suite de cette formation mon premier CDI de reconversion professionnelle Concepteur Développeur d'Applications.

## Installation <a name="installation"></a>
Ce répertoire à été installé durant la formation sur mon compte github personnel et a une visibilité public à des fins de collaborations optimales avec les collaborateurs, intervenants et collègues.

## Utilisation <a name="utilisation"></a>
Ce répertoire se dote d'un fichier "README.md" dans le but de proposer une explication de chaque exercice réaliser durant la formation.<br>
On aura donc dans le sommaire l'ajout permanent des liens vers les exercices avec les consignes et les mise en application des programmes.

## Contribuer <a name="contribuer"></a>
Toutes personnes à une visibilité sur l'entièreté du répertoire. En revanche, aucune modification n'est possible.<br>
Les véritables contributions se font lors de nos échanges en direct ou en visio, durant tout l'apprentissage de cet emploi.<br>
De nombreux cours théoriques et pratiques sont réalisés pour consolider notre culture et employabilité.

## Licence <a name="licence"></a>
Tout droit réservé à moi même, Monsieur Reviron Jérôme.

# Scrapping de Fromages à partir d'une Url <a name="scrapping_fromage.py"></a>
Ce script Python, scrapping_fromage.py, propose une solution complète pour extraire, transformer et charger (ETL) des données sur les fromages à partir d'une source en ligne. Voici un résumé des fonctionnalités et des spécificités de ce script.<br>
L'Url du site scrappé est : https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/.

### Fonctionnalités

-**Extraction, Transformation et Chargement des Données**:<br>

La classe FromageETL est conçue pour effectuer des opérations ETL sur les données relatives aux fromages. Elle permet de récupérer des données depuis une source, de les traiter, de les stocker dans une base de données SQLite, et d’effectuer diverses opérations sur ces données.

-**Initialisation**:<br>

L’instance de la classe FromageETL est initialisée avec une URL à partir de laquelle les données sur les fromages seront extraites.

-**Extraction des Données**:<br>

Les données sont extraites à partir de l’URL spécifiée et stockées dans self.data.

-**Transformation des Données**:<br>

Les données extraites sont transformées en un DataFrame pandas structuré. Le processus implique l’analyse HTML des données, la récupération des informations sur les fromages à partir de la table HTML, et la création d’un DataFrame avec les colonnes ‘fromage_names’, ‘fromage_familles’, ‘pates’, et ‘creation_date’.

-**Chargement des Données**:<br>

Les données sont chargées dans une table SQLite spécifiée. Il faut fournir le nom de la base de données SQLite et le nom de la table dans laquelle charger les données.

### Utilisation

1. Importez la classe FromageETL depuis le module scrapping_fromage.py.
2. Créez une instance de la classe FromageETL avec l’URL de votre choix.
3. Utilisez la méthode extract pour extraire les données.
4. Utilisez la méthode transform pour transformer les données extraites en un DataFrame structuré.
5. Utilisez la méthode load pour charger les données dans une base de données SQLite.

### Ensemble des fonctionnalités tests

- **Lecture de la Base de Données**:<br>
La méthode read_from_database permet de lire les données d’une table spécifique dans une base de données SQLite.

- **Obtention des Noms de Fromages**:<br>
La méthode get_fromage_names permet d’obtenir les noms de fromages d’une table spécifique dans une base de données SQLite.

- **Obtention des Familles de Fromages**:<br>
La méthode get_fromage_familles permet d’obtenir les familles de fromages d’une table spécifique dans une base de données SQLite.

- **Obtention des Pâtes de Fromages**:<br>
La méthode get_pates permet d’obtenir les types de pâtes de fromages d’une table spécifique dans une base de données SQLite.

- **Connexion à la Base de Données**:<br>
La méthode connect_to_database permet de se connecter à une base de données SQLite.

- **Ajout d’une Ligne**:<br>
La méthode add_row permet d’ajouter une nouvelle ligne de données au DataFrame.

- **Tri Ascendant**:<br>
La méthode sort_ascending permet de trier les données du DataFrame par ordre croissant de noms de fromages.

- **Tri Descendant**:<br>
La méthode sort_descending permet de trier les données du DataFrame par ordre décroissant de noms de fromages.

- **Compte Total**:<br>
La méthode total_count permet de compter le nombre total de lignes dans le DataFrame.
  
- **Comptage par Lettre**:<br>
La méthode count_by_letter compte le nombre de fromages par lettre initiale dans les noms.

- **Mise à Jour du Nom d’un Fromage**:<br>
La méthode update_fromage_name met à jour le nom d’un fromage dans l’ensemble de données.

- **Suppression d’une Ligne**:<br>
La méthode delete_row supprime une ligne de l’ensemble de données basée sur le nom du fromage.

- **Regroupement et Comptage par Première Lettre**:<br>
La méthode group_and_count_by_first_letter regroupe les fromages par la première lettre de la famille et compte le nombre de fromages par groupe.

### Particularités

-**Souplesse d’Utilisationn**:

La classe FromageETL est flexible et peut être utilisée pour extraire, transformer et charger des données depuis n’importe quelle URL contenant des informations sur les fromages.

-**Adaptabilité**:

La classe FromageETL est adaptable et peut être modifiée pour extraire, transformer et charger des données depuis d’autres sources ou pour traiter d’autres types de données.

-**Indépendance**:

La classe FromageETL est indépendante et ne dépend pas d’autres modules ou classes pour fonctionner correctement. Elle utilise uniquement les modules importés dans scrapping_fromage.py.

# Test de Scrapping de Fromages <a name="test_scrapping_fromages.py"></a>

Ce script Python, `test_scrapping_fromage.py`, propose une suite de tests pour vérifier les fonctionnalités de la classe `FromageETL` du script `scrapping_fromage.py`. Voici un résumé des tests effectués dans ce script.

### Tests

- **Instance ETL**:<br>
Le test `etl_instance` crée une instance de la classe `FromageETL` avec une URL spécifique.

- **Extraction des Données**:<br>
Le test `test_extract` vérifie que la méthode `extract` extrait correctement les données à partir de l'URL spécifiée.

- **Transformation des Données**:<br>
Le test `test_transform` vérifie que la méthode `transform` transforme correctement les données extraites en un DataFrame structuré.

- **Chargement et Lecture de la Base de Données**:<br>
Le test `test_load_and_read_from_database` vérifie que la méthode `load` charge correctement les données dans la base de données et que la méthode `read_from_database` lit correctement les données depuis la base de données.

- **Obtention des Noms de Fromages**:<br>
Le test `test_get_fromage_names` vérifie que la méthode `get_fromage_names` obtient correctement les noms de fromages d'une table spécifique dans une base de données SQLite.

- **Obtention des Familles de Fromages**:<br>
Le test `test_get_fromage_familles` vérifie que la méthode `get_fromage_familles` obtient correctement les familles de fromages d'une table spécifique dans une base de données SQLite.

- **Connexion à la Base de Données**:<br>
Le test `test_connect_to_database` vérifie que la méthode `connect_to_database` se connecte correctement à une base de données SQLite.

- **Ajout d’une Ligne**:<br>
Le test `test_add_row` vérifie que la méthode `add_row` ajoute correctement une nouvelle ligne de données au DataFrame.

- **Tri Ascendant**:<br>
Le test `test_sort_ascending` vérifie que la méthode `sort_ascending` trie correctement les données du DataFrame par ordre croissant de noms de fromages.

- **Tri Descendant**:<br>
Le test `test_sort_descending` vérifie que la méthode `sort_descending` trie correctement les données du DataFrame par ordre décroissant de noms de fromages.

- **Compte Total**:<br>
Le test `test_total_count` vérifie que la méthode `total_count` compte correctement le nombre total de lignes dans le DataFrame.

- **Comptage par Lettre**:<br>
Le test `test_count_by_letter` vérifie que la méthode `count_by_letter` compte correctement le nombre de fromages par lettre initiale dans les noms.

- **Suppression d’une Ligne**:<br>
Le test `test_delete_row` vérifie que la méthode `delete_row` supprime correctement une ligne de l'ensemble de données basée sur le nom du fromage.

- **Mise à Jour du Nom d’un Fromage**:<br>
Le test `test_update_fromage_name` vérifie que la méthode `update_fromage_name` met à jour correctement le nom d'un fromage dans l'ensemble de données.

- **Regroupement et Comptage par Première Lettre**:<br>
Le test `test_group_and_count_by_first_letter` vérifie que la méthode `group_and_count_by_first_letter` renvoie un DataFrame non vide avec les colonnes 'fromage_familles' et 'fromage_nb'.

### Utilisation

1. Importez le module `test_scrapping_fromage.py`.
2. Exécutez le script pour lancer la suite de tests.
3. Les résultats des tests seront affichés dans la console.

### Particularités

- **Tests Indépendants**:<br>
Chaque test est conçu pour être indépendant des autres. Cela signifie que l'échec d'un test n'affecte pas l'exécution des autres tests.

- **Utilisation de Mocks**:<br>
Pour certains tests, des mocks sont utilisés pour simuler le comportement de certaines fonctions ou méthodes. Cela permet de tester les fonctionnalités de la classe `FromageETL` sans dépendre de sources de données externes.

- **Tests Compréhensifs**:<br>
La suite de tests couvre toutes les principales fonctionnalités de la classe `FromageETL`, assurant ainsi que chaque fonctionnalité fonctionne comme prévu.

# Interface fromage_UI <a name="fromage_UI.py"></a>

Ce script Python, `fromage_ui.py`, propose une interface utilisateur pour afficher des informations sur les fromages. Voici un résumé des fonctionnalités de ce script.

### Fonctionnalités

-**Initialisation de l'Interface Utilisateur**:<br>
La méthode `__init__(self, master)` initialise l'interface graphique. Elle crée un bouton pour mettre à jour la base de données et un diagramme en camembert pour afficher les informations sur les fromages.

-**Mise à Jour de la Base de Données**:<br>
La méthode `update_database(self)` met à jour la base de données en extrayant, transformant et chargeant les données des fromages. Elle utilise la classe `FromageETL` pour extraire les données depuis une source en ligne, les transformer en un format approprié, et les charger dans une base de données SQLite.

-**Mise à Jour du Diagramme en Camembert**:<br>
La méthode `update_pie_chart(self, data)` met à jour le diagramme en camembert avec les ratios de fromages par famille. Cette méthode prend un DataFrame de données sur les fromages en paramètre, calcule le ratio de chaque famille de fromages, groupe les familles dont le ratio est inférieur à 5% sous la catégorie "Autres", et met à jour le diagramme en camembert en conséquence.

### Utilisation

1. Importez le module `fromage_ui.py`.
2. Exécutez le script pour lancer l'interface utilisateur.
3. Les résultats seront affichés dans l'interface utilisateur.

### Particularités

-**Interface Indépendante** :<br>

Chaque composant de l'interface est conçu pour être indépendant des autres. Cela signifie que la mise à jour d'un composant n'affecte pas le fonctionnement des autres composants.

-**Utilisation de Tkinter** :<br>

Pour l'interface utilisateur, le module Tkinter est utilisé pour simuler le comportement de certaines fonctions ou méthodes.<br>
Cela permet de tester les fonctionnalités de la classe `FromageUI` sans dépendre de sources de données externes.

-**Compréhensif** :<br>

Le script couvre toutes les principales fonctionnalités de la classe `FromageUI`, assurant ainsi que chaque fonctionnalité fonctionne comme prévu.

