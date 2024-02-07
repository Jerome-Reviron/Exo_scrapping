import cx_Oracle
from imports import tk, ttk, messagebox, pd, Figure, FigureCanvasTkAgg, plt, BytesIO, Image, ImageTk

# Fonction pour exécuter une requête SQL et retourner un DataFrame
def execute_query(query):
    connection = cx_Oracle.connect("system", "root", "//localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return pd.DataFrame(data, columns=columns)

def test_connection():
    try:
        connection = cx_Oracle.connect("system", "root", "//localhost:1521/xe")
        cursor = connection.cursor()
        cursor.execute("SELECT 1 FROM dual")
        print("La connexion à la base de données a réussi.")
        cursor.close()
        connection.close()
    except cx_Oracle.DatabaseError as e:
        print("Il y a eu une erreur lors de la connexion à la base de données.")
        print(e)

test_connection()

def question_1():
    # Requête pour la question 1
    query = """
    SELECT D_FROMAGE_NAMES, SUM(QUANTITES_VENDUES) AS TOTAL_VENTES
    FROM F_VENTE
    JOIN D_FROMAGE ON F_VENTE.D_FROMAGE_FK = D_FROMAGE.D_FROMAGE_NAMES
    GROUP BY D_FROMAGE_NAMES
    ORDER BY TOTAL_VENTES DESC
    FETCH FIRST 3 ROWS ONLY
    """
    result_df = execute_query(query)
    print(result_df)

    # Affichage du graphique
    fig, ax = plt.subplots(figsize=(10, 6))

    # Utilisez autopct pour afficher les valeurs
    ax.pie(result_df['TOTAL_VENTES'], labels=result_df['D_FROMAGE_NAMES'], autopct='%1.1f%%', startangle=90)
    ax.set_title('Top 3 des fromages les plus vendus')

    # Ajouter une légende avec les valeurs de TOTAL_VENTES
    legend_labels = [f"{name} ({value})" for name, value in zip(result_df['D_FROMAGE_NAMES'], result_df['TOTAL_VENTES'])]
    legend1 = ax.legend(legend_labels, title='Fromages')
    
    # Ajuster la position de la légende
    legend1.set_bbox_to_anchor((0.3, 0.15))
    legend1.get_title().set_fontsize('10')
    # Ajustement de la taille des étiquettes
    for text in legend1.get_texts():
        text.set_fontsize('8')

    # Afficher le graphique dans une fenêtre Tkinter
    show_plot(fig, 1000, 600)

def question_2():
    # Requête pour la question 2
    query = """
    WITH classement_chiffre_affaires AS (
        SELECT
            TO_CHAR(d.epochtimestamp, 'YYYY-MM-DD') AS jour,
            SUM(v.quantites_vendues * f.prix) AS chiffre_affaires,
            RANK() OVER (ORDER BY SUM(v.quantites_vendues * f.prix) DESC) AS classement
        FROM
            F_VENTE v
        JOIN
            D_FROMAGE f ON v.d_fromage_fk = f.d_fromage_names
        JOIN
            D_DATES_DE_VENTES d ON v.d_dates_de_ventes_fk = d.epochtimestamp
        GROUP BY
            TO_CHAR(d.epochtimestamp, 'YYYY-MM-DD')
        HAVING
            SUM(v.quantites_vendues * f.prix) IS NOT NULL
    )
    SELECT jour, chiffre_affaires
    FROM classement_chiffre_affaires
    WHERE classement = 1
    """
    result_df = execute_query(query)
    result_day = result_df.iloc[0]['JOUR']

    # Spécifier des couleurs individuelles pour chaque barre
    colors = ['red', 'blue']

    # Affichage du graphique à barres verticales
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(result_df['JOUR'], result_df['CHIFFRE_AFFAIRES'], color=colors)
    ax.set_title('Jour(s) du plus gros CA')

    # Ajouter les valeurs au-dessus des barres
    for index, value in enumerate(result_df['CHIFFRE_AFFAIRES']):
        ax.text(index, value, f'{value:.1f}', ha='center', va='top')

    # Afficher le graphique dans une fenêtre Tkinter
    show_plot(fig, 1000, 600)

def question_3():
    # Requête pour la question 3
    query = """
    SELECT FROMAGE_FAMILLES, COUNT(*) AS NOMBRE_DE_FROMAGES
    FROM D_FROMAGE
    GROUP BY FROMAGE_FAMILLES
    """
    result_df = execute_query(query)

    # Calcul du pourcentage de chaque famille de fromages
    total = result_df['NOMBRE_DE_FROMAGES'].sum()
    result_df['POURCENTAGE'] = (result_df['NOMBRE_DE_FROMAGES'] / total) * 100

    # Création d'une copie des données originales pour le deuxième graphique
    other_data = result_df.copy()

    # Regroupement des familles de fromages avec moins de 5% dans "Autres"
    mask = result_df['POURCENTAGE'] < 5
    result_df.loc[mask, 'FROMAGE_FAMILLES'] = 'Autres'
    result_df = result_df.groupby('FROMAGE_FAMILLES').sum().reset_index()

    # Création du diagramme en camembert
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))

    # Création du premier diagramme en camembert avec toutes les familles et "Autres" regroupés
    wedges1, texts1, autotexts1 = ax1.pie(result_df['POURCENTAGE'], labels=result_df['FROMAGE_FAMILLES'], autopct='%1.1f%%', startangle=90)
    ax1.set_title("100% de la BDD", loc='center', pad=10)

    # Ajout d'une légende pour le premier camembert en bas à gauche
    legend_labels1 = [f"{label} : {result_df[result_df['FROMAGE_FAMILLES'] == label]['POURCENTAGE'].iloc[0]:.1f}%" for label in result_df['FROMAGE_FAMILLES']]
    legend2 = ax1.legend(legend_labels1, title="% BDD des 'Familles' > 5%")

    # Ajuster la position de la légende
    legend2.set_bbox_to_anchor((0.3, 0.15))
    legend2.get_title().set_fontsize('10')
    # Ajustement de la taille des étiquettes
    for text in legend2.get_texts():
        text.set_fontsize('8')

    # Création du deuxième diagramme en camembert pour la famille "Autres"
    if 'Autres' in result_df['FROMAGE_FAMILLES'].values:
        other_data = other_data.loc[mask, :]
        wedges2, texts2, autotexts2 = ax2.pie(other_data['POURCENTAGE'], labels=other_data['FROMAGE_FAMILLES'], autopct='%1.1f%%', startangle=90)
        ax2.set_title("100% des Autres", loc='center', pad=10)

        # Ajout d'une légende pour le deuxième camembert
        legend_labels2 = [f"{label} : {other_data.loc[other_data['FROMAGE_FAMILLES'] == label, 'POURCENTAGE'].iloc[0]:.1f}%" for label in other_data['FROMAGE_FAMILLES']]
        legend3 = ax2.legend(legend_labels2, title="% BDD des 'Autres'")

        # Ajuster la position de la légende
        legend3.set_bbox_to_anchor((0.0, 0.15))
        legend3.get_title().set_fontsize('10')
        # Ajustement de la taille des étiquettes
        for text in legend3.get_texts():
            text.set_fontsize('8')

    # Affichage du graphique dans une fenêtre Tkinter
    show_plot(fig, 1000, 600)

def show_plot(fig, width, height):
    # Créer une fenêtre Tkinter pour afficher le graphique
    window = tk.Toplevel(root)
    window.title('Graphique')

    # Centrer la fenêtre au milieu de l'écran en mode plein écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

    # Convertir le graphique en widget Tkinter
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # Ajouter le widget Tkinter à la fenêtre
    canvas.get_tk_widget().pack()

    # Fermer la fenêtre Tkinter en cas de clic
    window.bind('<Button-1>', lambda e: window.destroy())

# Fonction pour gérer le choix de l'utilisateur
def handle_choice():
    selected_question = question_var.get()

    if selected_question == "Quels sont les trois fromages représentant le plus de vente ?":
        question_1()
    elif selected_question == "Quel est le jour ayant réalisé le plus de chiffre d'affaire ?":
        question_2()
    elif selected_question == "Quel est le nombre de fromage par famille ?":
        question_3()

# Création de l'interface graphique Tkinter
root = tk.Tk()
root.title('Interface Graphique')

# Ouvrir la fenêtre en plein écran
root.attributes('-fullscreen', True)

# Options pour le menu déroulant
questions = {
    "Quels sont les trois fromages représentant le plus de vente ?": question_1,
    "Quel est le jour ayant réalisé le plus de chiffre d'affaire ?": question_2,
    "Quel est le nombre de fromage par famille ?": question_3
}

# Menu déroulant pour les questions
question_var = tk.StringVar()
question_var.set("Choisissez votre question")  # Valeur par défaut

question_menu = ttk.Combobox(root, textvariable=question_var, values=list(questions.keys()), state='readonly')
question_menu.pack(pady=10)

# Bouton de validation
validate_button = tk.Button(root, text='Valider', command=handle_choice)
validate_button.pack(pady=10)

# Fonction pour fermer la fenêtre en mode plein écran
def close_fullscreen():
    root.attributes('-fullscreen', False)
    root.destroy()

# Bouton pour fermer la fenêtre en mode plein écran
close_fullscreen_button = tk.Button(root, text="Fermer la fenêtre", command=close_fullscreen)
close_fullscreen_button.pack(pady=10)

# Lancement de l'interface graphique
root.mainloop()
