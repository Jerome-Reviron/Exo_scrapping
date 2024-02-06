import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("C:\\Users\\HB\\Desktop\\Git Exo_Scrapping\\csv\\fromages_table.csv")

# Calculer la longueur maximale de la colonne "fromage_names"
longueur_max = df['fromage_names'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'fromage_names' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "fromage_familles"
longueur_max = df['fromage_familles'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'fromage_familles' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "pates"
longueur_max = df['pates'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'pates' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "url_info_fromages"
longueur_max = df['url_info_fromages'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'url_info_fromages' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "descriptions"
longueur_max = df['descriptions'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'descriptions' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "note_moyenne"
longueur_max = df['note_moyenne'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'note_moyenne' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "nb_avis"
longueur_max = df['nb_avis'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'nb_avis' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "prix"
longueur_max = df['prix'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'prix' est : {longueur_max}")

# Calculer la longueur maximale de la colonne "images_fromage"
longueur_max = df['images_fromage'].apply(lambda x: len(str(x))).max()

print(f"La longueur maximale dans la colonne 'images_fromage' est : {longueur_max}")

# Charger le fichier CSV
df_sales = pd.read_csv("C:\\Users\\HB\\Desktop\\Git Exo_Scrapping\\csv\\cheeses_sales.csv", delimiter=';')

# Calculer la longueur maximale de la colonne "transaction"
longueur_max_transaction = df_sales['transaction'].apply(lambda x: len(str(x))).max()
print(f"La longueur maximale dans la colonne 'transaction' est : {longueur_max_transaction}")

# Calculer la longueur maximale de la colonne "cheeses"
longueur_max_cheeses = df_sales['cheeses'].apply(lambda x: len(str(x))).max()
print(f"La longueur maximale dans la colonne 'cheeses' est : {longueur_max_cheeses}")

# Calculer la longueur maximale de la colonne "dates"
longueur_max_dates = df_sales['dates'].apply(lambda x: len(str(x))).max()
print(f"La longueur maximale dans la colonne 'dates' est : {longueur_max_dates}")

# Calculer la longueur maximale de la colonne "quantities"
longueur_max_quantities = df_sales['quantities'].apply(lambda x: len(str(x))).max()
print(f"La longueur maximale dans la colonne 'quantities' est : {longueur_max_quantities}")