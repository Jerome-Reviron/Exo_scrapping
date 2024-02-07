# Exo_scrapping

## Table des Matières
- [Introduction](#introduction)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contribuer](#contribuer)
- [Licence](#licence)
- [Scrapping de Fromages à partir d'une Url](#scrapping_fromage.py)
- [Test_scrapping de Fromages](#test_scrapping_fromages.py)
- [Interface fromage_UI](#interface_fromage.py)
- [Création fromages_table.csv](#csv_fromages_table.py)
- [Création des Tables ODS](#create_table_ODS)
- [Création des Tables DWH](#create_table_DWH)
- [Interface questionnaire_UI](#interface_questionnaire.py)

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

![Tableau du résultat](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/scrapping_fromage.png)

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

![Fromages_bdd.sqlite](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/fromage_bdd_table.png)

# Test de Scrapping de Fromages <a name="test_scrapping_fromages.py"></a>

Ce script Python, `test_scrapping_fromage.py`, propose une suite de tests pour vérifier les fonctionnalités de la classe `FromageETL` du script `scrapping_fromage.py`. Voici un résumé des tests effectués dans ce script.

![Test_scrapping](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/test_scrapping.png)

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

![Groupby_fromage](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/groupby_fromage.png)

### Utilisation

1. Importez le module `test_scrapping_fromage.py`.
2. Exécutez le script pour lancer la suite de tests.
3. Les résultats des tests seront affichés dans la console.

![Rapport_xlsx_scrapping](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/rapport_xlsx_scrapping.png)

### Particularités

- **Tests Indépendants**:<br>
Chaque test est conçu pour être indépendant des autres. Cela signifie que l'échec d'un test n'affecte pas l'exécution des autres tests.

- **Utilisation de Mocks**:<br>
Pour certains tests, des mocks sont utilisés pour simuler le comportement de certaines fonctions ou méthodes. Cela permet de tester les fonctionnalités de la classe `FromageETL` sans dépendre de sources de données externes.

- **Tests Compréhensifs**:<br>
La suite de tests couvre toutes les principales fonctionnalités de la classe `FromageETL`, assurant ainsi que chaque fonctionnalité fonctionne comme prévu.

![Analyze_tes](https://github.com/Jerome-Reviron/Exo_scrapping/blob/main/images/rapport_test.png)

# Interface fromage_UI <a name="interface_fromage.py"></a>
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

# Création fromages_table.csv <a name="csv_fromages_table.py"></a>

Ce script Python, csv_fromages_table.py, a pour objectif d'extraire les données de la table "fromages_table" d'une base de données SQLite appelée "fromages_bdd.sqlite". Les données extraites sont ensuite exportées vers un fichier CSV nommé "fromages_table.csv". Voici un résumé des fonctionnalités, utilisations et particularités de ce script.

### Fonctionnalités

-**Connexion à la Base de Données**:<br>
Le script utilise le module sqlite3 pour se connecter à la base de données SQLite "fromages_bdd.sqlite" et initialiser un curseur pour exécuter des requêtes SQL.

-**Extraction des Données**:<br>
Une requête SQL est exécutée pour récupérer toutes les données de la table "fromages_table", incluant des informations telles que le nom du fromage, la famille, la pâte, l'URL des informations sur les fromages, les descriptions, la note moyenne, le nombre d'avis, le prix et l'image du fromage.

-**Création du Dossier de Sortie**:<br>
Avant d'écrire les données dans un fichier CSV, le script vérifie si le dossier de sortie spécifié (output_folder) existe. S'il n'existe pas, le script le crée.

-**Écriture dans un Fichier CSV**:<br>
Les données extraites sont ensuite écrites dans le fichier CSV "fromages_table.csv" avec le point-virgule comme séparateur.

### Utilisation

1. Assurez-vous d'avoir les bibliothèques requises installées en exécutant pip install pandas.
2. Modifiez le chemin du dossier de sortie dans le script (output_folder) si nécessaire.
3. Exécutez le script Python.

### Structure du Projet

-**csv_fromages_table.py**:<br>
Le script principal qui extrait les données de la base de données SQLite et les exporte vers un fichier CSV.

-**imports.py**:<br>
Fichier contenant les importations nécessaires pour le script.

### Particularités

-**Gestion de l'Exportation**:<br>
Le script crée le dossier de sortie s'il n'existe pas déjà, assurant ainsi que le fichier CSV peut être créé avec succès.

-**Séparateur Spécifique**:<br>
Le script utilise le point-virgule comme séparateur lors de l'écriture des données dans le fichier CSV, offrant une certaine flexibilité en matière de séparateurs de données.

### Prérequis

-**Python** : Le script est conçu pour fonctionner avec Python.
-**Bibliothèques** : Assurez-vous d'avoir installé les bibliothèques sqlite3, csv, os nécessaires répertoriées dans le fichier imports.py.

# Création des Tables ODS <a name="create_table_ODS"></a>

Ce fichier SQL, `create_table_ODS_fromages_ventes.sql`, contient les requêtes nécessaires pour créer deux tables dans le cadre du processus ODS (Operational Data Store). Les tables créées sont `ODS_fromages_table` et `ODS_cheeses_sales` à partir des deux fichiers 'fromages_table.csv' et 'cheeses_sales.csv'. Voici un résumé des fonctionnalités, utilisations et particularités de ces requêtes.

## Table ODS_fromages_table

- **Description**:<br>
  La table `ODS_fromages_table` est destinée à stocker des informations sur les fromages, comprenant des détails tels que le nom du fromage, la famille, la pâte, l'URL des informations sur les fromages, les descriptions, la note moyenne, le nombre d'avis, le prix et l'image du fromage.

- **Colonnes**:<br>
  - `fromage_names` (VARCHAR2(50)) : Nom du fromage (non nul).
  - `fromage_familles` (VARCHAR2(20)) : Famille du fromage.
  - `pates` (VARCHAR2(80)) : Type de pâte du fromage.
  - `url_info_fromages` (VARCHAR2(100)) : URL des informations sur le fromage.
  - `descriptions` (VARCHAR2(1500)) : Description du fromage.
  - `note_moyenne` (NUMBER(10,2)) : Note moyenne du fromage.
  - `nb_avis` (NUMBER(10,0)) : Nombre d'avis sur le fromage.
  - `prix` (NUMBER(10,2)) : Prix du fromage.
  - `images_fromage` (VARCHAR2(100)) : Chemin vers l'image du fromage.

## Table ODS_cheeses_sales

- **Description**:<br>
  La table `ODS_cheeses_sales` stocke des informations sur les ventes de fromages, incluant des détails tels que le numéro de transaction, le nom du fromage, la date de la transaction et les quantités vendues.

- **Colonnes**:<br>
  - `transaction` (VARCHAR2(50)) : Numéro de transaction (non nul).
  - `cheeses` (VARCHAR2(50)) : Nom du fromage.
  - `dates` (TIMESTAMP(6)) : Date de la transaction.
  - `quantities` (NUMBER(5)) : Quantités vendues.

## Utilisation

1. Connectez-vous dans Oracle SQL Developer après l'avoir installé ainsi et après avoir installé et confirguré Oracle Express
2. Exécutez le contenu du fichier `create_table_ODS_fromages_ventes.sql` dans Oracle SQL Developer pour créer les tables.

## Particularités

- **Structure ODS**:<br>
  Les tables créées suivent le modèle d'un Operational Data Store (ODS), stockant des données opérationnelles à des fins de reporting et d'analyse.

- **Colonnes Détaillées**:<br>
  Les colonnes sont spécifiées avec des détails précis pour chaque type de données, assurant une représentation adéquate des informations.

# Création des Tables DWH <a name="create_table_DWH"></a>

Ce fichier SQL, `create_table_DWH_fromages_ventes.sql`, contient les requêtes nécessaires pour créer trois tables dans le cadre du processus DWH (Data Warehouse). Les tables créées sont `D_Fromage`, `D_Dates_de_ventes` et `F_Vente`. Voici un résumé des fonctionnalités, utilisations et particularités de ces requêtes.

## Table dimension D_Fromage

- **Description**:<br>
  La table `D_Fromage` est une table de dimension destinée à stocker des informations sur les fromages. Elle inclut des détails tels que le nom du fromage, la famille, la pâte, l'URL des informations sur les fromages, les descriptions, la note moyenne, le nombre d'avis, le prix et l'image du fromage.

- **Colonnes**:<br>
  - `D_fromage_names` (VARCHAR2(50)) : Nom du fromage (non nul).
  - `fromage_familles` (VARCHAR2(20)) : Famille du fromage.
  - `pates` (VARCHAR2(80)) : Type de pâte du fromage.
  - `url_info_fromages` (VARCHAR2(100)) : URL des informations sur le fromage.
  - `descriptions` (VARCHAR2(1500)) : Description du fromage.
  - `note_moyenne` (NUMBER(10,2)) : Note moyenne du fromage.
  - `nb_avis` (NUMBER(10,0)) : Nombre d'avis sur le fromage.
  - `prix` (NUMBER(10,2)) : Prix du fromage.
  - `images_fromage` (VARCHAR2(100)) : Chemin vers l'image du fromage.
  
- **Clé Primaire**:<br>
  - La clé primaire est définie sur la colonne `D_fromage_names`.

## Table dimension D_Dates_de_ventes

- **Description**:<br>
  La table `D_Dates_de_ventes` est une table de dimension destinée à stocker des informations sur les dates de ventes. Elle inclut des détails tels que le timestamp, le jour, le mois et l'année de la vente.

- **Colonnes**:<br>
  - `EpochTimestamp` (TIMESTAMP(6)) : Timestamp de la vente (non nul).
  - `EpochDay` (NUMBER(2)) : Jour de la vente.
  - `EpochMonth` (NUMBER(2)) : Mois de la vente.
  - `EpochYear` (NUMBER(4)) : Année de la vente.
  
- **Clé Primaire**:<br>
  - La clé primaire est définie sur la colonne `EpochTimestamp`.

## Table de fait F_Vente

- **Description**:<br>
  La table `F_Vente` est une table de fait destinée à stocker des informations sur les ventes de fromages. Elle inclut des détails tels que le numéro de transaction, la clé étrangère vers la table `D_Fromage` (`D_Fromage_FK`), la clé étrangère vers la table `D_Dates_de_ventes` (`D_Dates_de_ventes_FK`) et les quantités vendues.

- **Colonnes**:<br>
  - `F_Transaction` (VARCHAR2(50)) : Numéro de transaction (non nul).
  - `D_Fromage_FK` (VARCHAR2(50)) : Clé étrangère vers la table `D_Fromage`.
  - `D_Dates_de_ventes_FK` (TIMESTAMP(6)) : Clé étrangère vers la table `D_Dates_de_ventes`.
  - `quantites_vendues` (NUMBER(5)) : Quantités vendues.
  
- **Clés Primaires et Étrangères**:<br>
  - La clé primaire est définie sur les colonnes `F_Transaction`, `D_Fromage_FK` et `D_Dates_de_ventes_FK`.
  - Il existe deux contraintes de clé étrangère, une référençant la table `D_Fromage` et l'autre référençant la table `D_Dates_de_ventes`.

## Utilisation

1. Connectez-vous dans Oracle SQL Developer après l'avoir installé ainsi et après avoir installé et configuré Oracle Express.
2. Exécutez le contenu du fichier `create_table_DWH_fromages_ventes.sql` dans Oracle SQL Developer pour créer les tables.

## Particularités

- **Structure DWH**:<br>
  Les tables créées suivent le modèle d'un Data Warehouse (DWH), stockant des données optimisées pour les requêtes analytiques.

- **Colonnes Détaillées**:<br>
  Les colonnes sont spécifiées avec des détails précis pour chaque type de données, assurant une représentation adéquate des informations.

- **Clés Primaires et Étrangères**:<br>
  La structure de clés primaires et étrangères garantit l'intégrité référentielle entre les tables, facilitant

## Interface `questionnaire_ui.py` <a name="interface_questionnaire.py"></a>

Ce script Python, `questionnaire_ui.py`, présente une interface utilisateur graphique pour répondre à différentes questions basées sur une base de données Oracle. Voici un résumé des fonctionnalités de ce script.

### Fonctionnalités

- **Importations Nécessaires:**
  - Le module contient les importations nécessaires pour le script, notamment les bibliothèques `cx_Oracle`, `tk`, `ttk`, `pd` (pandas), `FigureCanvasTkAgg`, et `plt` (Matplotlib).

- **Fonction d'Exécution de Requête:**
  - La fonction `execute_query(query)` se connecte à la base de données Oracle, exécute une requête SQL, récupère les résultats sous forme de DataFrame pandas, puis ferme la connexion.

- **Test de Connexion à la Base de Données:**
  - La fonction `test_connection()` tente d'établir une connexion à la base de données Oracle pour vérifier son bon fonctionnement.

- **Questions Spécifiques:**
  - Les fonctions `question_1()`, `question_2()`, et `question_3()` répondent à des questions spécifiques en exécutant des requêtes SQL complexes et en affichant les résultats sous forme de DataFrame.

- **Affichage de Graphiques Matplotlib dans une Interface Tkinter:**
  - La fonction `show_plot(fig, width, height)` affiche un graphique Matplotlib dans une fenêtre Tkinter.

- **Gestion du Choix de la Question:**
  - La fonction `handle_choice()` est appelée lorsqu'un utilisateur choisit une question dans le menu déroulant. Elle récupère la question sélectionnée et appelle la fonction correspondante pour afficher la réponse.

- **Interface Graphique Tkinter:**
  - Le script crée une interface graphique Tkinter avec un menu déroulant permettant de choisir une question, un bouton de validation, et un bouton pour fermer la fenêtre en mode plein écran.

### Utilisation

1. Importez le module `questionnaire_ui.py`.
2. Exécutez le script pour lancer l'interface utilisateur.
3. Choisissez une question dans le menu déroulant.
4. Cliquez sur le bouton "Valider" pour afficher la réponse correspondante.
5. Pour fermer la fenêtre en mode plein écran, cliquez sur le bouton "Fermer la fenêtre".

### Remarques

- Assurez-vous d'avoir les bibliothèques nécessaires installées, notamment `cx_Oracle`, `tkinter`, `pandas`, et `matplotlib`.
- La connexion à la base de données Oracle est configurée avec les paramètres "system", "root", et "//localhost:1521/xe". Vous pouvez ajuster ces paramètres selon votre configuration.
- Ce script propose une solution conviviale pour explorer des données de ventes de fromages stockées dans une base de données Oracle. N'hésitez pas à personnaliser les requêtes ou l'interface en fonction de vos besoins spécifiques.
