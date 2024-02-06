from imports import sqlite3, csv, os

# Spécifiez le chemin du dossier où vous souhaitez enregistrer le CSV
output_folder = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv'

# Assurez-vous que le dossier existe, sinon, créez-le
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Connexion à la base de données SQLite
conn = sqlite3.connect('fromages_bdd.sqlite')
cursor = conn.cursor()

# Exécution de la requête pour récupérer toutes les données de la table
cursor.execute('SELECT * FROM fromages_table')

# Récupération de toutes les lignes de résultats
rows = cursor.fetchall()

# Fermeture de la connexion à la base de données
conn.close()

# Nom du fichier CSV de sortie
csv_filename = os.path.join(output_folder, 'fromages_table.csv')

# Écriture des données dans le fichier CSV
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Écriture de l'en-tête du fichier CSV
    csv_writer.writerow(['fromage_names', 'fromage_familles', 'pates', 'url_info_fromages',
                        'descriptions', 'note_moyenne', 'nb_avis', 'prix', 'images_fromage', 'creation_date'])
    
    # Écriture des données dans le fichier CSV
    csv_writer.writerows(rows)

print(f"Données extraites avec succès dans {csv_filename}")
