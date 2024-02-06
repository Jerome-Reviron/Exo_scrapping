import pandas as pd

# Chemin des fichiers CSV
fromages_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\fromages_table.csv'
cheeses_sales_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\cheeses_sales.csv'
output_merged_csv_path = r'C:\Users\HB\Desktop\Git Exo_Scrapping\csv\fusion_fromages_ventes.csv'

# Charger les fichiers CSV dans des DataFrames
df_fromages = pd.read_csv(fromages_csv_path, delimiter=',')
df_cheeses_sales = pd.read_csv(cheeses_sales_csv_path, delimiter=';')

# Afficher les noms de colonnes pour vérification
print("Colonnes dans df_fromages:", df_fromages.columns)
print("Colonnes dans df_cheeses_sales:", df_cheeses_sales.columns)

# Fusionner les DataFrames en utilisant la colonne 'fromage_names' comme clé
merged_df = pd.merge(df_fromages, df_cheeses_sales, left_on='fromage_names', right_on='cheeses', how='left')

# Enregistrer le DataFrame fusionné dans un nouveau fichier CSV
merged_df.to_csv(output_merged_csv_path, index=False, encoding='utf-8', sep=',')

print(f"Données fusionnées avec succès dans {output_merged_csv_path}")
