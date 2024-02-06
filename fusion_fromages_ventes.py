import pandas as pd

# Chemin des fichiers CSV
fromages_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\fromages_table.csv'
cheeses_sales_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\cheeses_sales.csv'
output_merged_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\fusion_fromages_ventes.csv'

# Charger les fichiers CSV dans des DataFrames
df_fromages = pd.read_csv(fromages_csv_path, delimiter=';')
df_cheeses_sales = pd.read_csv(cheeses_sales_csv_path, delimiter=';')

# Renommer la colonne 'cheeses' en 'fromage_names' dans le DataFrame df_cheeses_sales
df_cheeses_sales = df_cheeses_sales.rename(columns={'cheeses': 'fromage_names'})

# Fusionner les DataFrames en utilisant la colonne 'fromage_names' comme clé
merged_df = pd.merge(df_fromages, df_cheeses_sales, on='fromage_names', how='left')

# Renommer les colonnes 'dates' et 'quantities' dans le DataFrame fusionné
merged_df = merged_df.rename(columns={'dates': 'dates de ventes', 'quantities': 'quantites vendues'})

# Convertir la colonne 'dates de ventes' en timestamps avec un format flexible
merged_df['dates de ventes'] = pd.to_datetime(merged_df['dates de ventes'], errors='coerce')

# Enregistrer le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv(output_merged_csv_path, index=False, encoding='utf-8', sep=',', na_rep='NULL')

print(f"Données fusionnées avec succès dans {output_merged_csv_path}")
