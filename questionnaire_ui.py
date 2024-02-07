"""
Ce module contient les importations nécessaires pour le script.
"""
import cx_Oracle
from imports import tk, ttk, pd, FigureCanvasTkAgg, plt

def execute_query(query):
    """
    Exécute une requête SQL et retourne un DataFrame contenant les résultats.

    Cette fonction prend en entrée une requête SQL, se connecte à la base de données Oracle, exécute la requête,
    récupère les résultats sous forme de DataFrame pandas, puis ferme la connexion.

    :param query: Requête SQL à exécuter.
    :type query: str
    :return: Un DataFrame contenant les résultats de la requête.
    :rtype: pandas.DataFrame
    """
    connection = cx_Oracle.connect("system", "root", "//localhost:1521/xe")
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return pd.DataFrame(data, columns=columns)

def test_connection():
    """
    Teste la connexion à la base de données Oracle.

    Cette fonction tente d'établir une connexion à la base de données Oracle en utilisant les paramètres
    spécifiés. Elle exécute ensuite une requête simple pour vérifier que la connexion fonctionne correctement.

    :return: Aucune valeur de retour explicite. Affiche un message de réussite ou d'erreur à la console.
    """
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

def question_1():
    """
    Répond à la question 1 en récupérant et affichant les trois fromages les plus vendus.

    Cette fonction exécute une requête SQL pour obtenir les noms des trois fromages les plus vendus
    ainsi que le total des quantités vendues pour chacun d'eux. Le résultat est affiché sous forme de DataFrame.

    Requiert une connexion à la base de données via la fonction execute_query.

    :return: Aucune valeur de retour explicite. Le résultat est affiché via la fonction print.
    """
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
    """
    Répond à la question 2 en fournissant la date et le chiffre d'affaires le plus élevé pour une journée donnée.

    Cette fonction exécute une requête SQL complexe utilisant une CTE (Common Table Expression) pour calculer le chiffre d'affaires
    total pour chaque jour, classe les jours par chiffre d'affaires décroissant, et renvoie la date et le chiffre d'affaires
    pour la journée avec le chiffre d'affaires le plus élevé.

    Requiert une connexion à la base de données via la fonction execute_query.

    :return: Aucune valeur de retour explicite. Le résultat est affiché via la fonction print.
    """
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
    """
    Répond à la question 3 en comptant le nombre de fromages par famille.

    Cette fonction exécute une requête SQL pour compter le nombre de fromages dans chaque famille de fromages.
    Le résultat est stocké dans un DataFrame qui peut être utilisé ou affiché ultérieurement.

    Requiert une connexion à la base de données via la fonction execute_query.

    :return: Aucune valeur de retour explicite. Le résultat est stocké dans le DataFrame result_df.
    """
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
    ax1.pie(result_df['POURCENTAGE'], labels=result_df['FROMAGE_FAMILLES'], autopct='%1.1f%%', startangle=90, pctdistance=0.8)
    ax1.set_title("100% de la BDD", loc='center', pad=20)
    
    # Ajuster la position du camembert vers le haut
    ax1.set_position([0.05, 0.25, 0.4, 0.6])

    # Ajout d'une légende pour le premier camembert en bas à gauche
    legend_labels1 = [f"{label} : {result_df[result_df['FROMAGE_FAMILLES'] == label]['POURCENTAGE'].iloc[0]:.1f}%" for label in result_df['FROMAGE_FAMILLES']]
    legend2 = ax1.legend(legend_labels1, title="% BDD des 'Familles' > 5%")

    # Ajuster la position de la légende
    legend2.set_bbox_to_anchor((0.8, 0.0))
    legend2.get_title().set_fontsize('10')
    # Ajustement de la taille des étiquettes
    for text in legend2.get_texts():
        text.set_fontsize('8')

    # Création du deuxième diagramme en camembert pour la famille "Autres"
    if 'Autres' in result_df['FROMAGE_FAMILLES'].values:
        other_data = other_data.loc[mask, :]
        ax2.pie(other_data['POURCENTAGE'], labels=other_data['FROMAGE_FAMILLES'], autopct='%1.1f%%', startangle=90, pctdistance=0.8)
        ax2.set_title("100% des Autres", loc='center', pad=20)

        # Ajuster la position du camembert vers le haut
        ax2.set_position([0.5, 0.25, 0.4, 0.6])

        # Ajout d'une légende pour le deuxième camembert
        legend_labels2 = [f"{label} : {other_data.loc[other_data['FROMAGE_FAMILLES'] == label, 'POURCENTAGE'].iloc[0]:.1f}%" for label in other_data['FROMAGE_FAMILLES']]
        legend3 = ax2.legend(legend_labels2, title="% BDD des 'Autres'")

        # Ajuster la position de la légende
        legend3.set_bbox_to_anchor((0.8, 0.0))
        legend3.get_title().set_fontsize('10')
        # Ajustement de la taille des étiquettes
        for text in legend3.get_texts():
            text.set_fontsize('8')

    # Affichage du graphique dans une fenêtre Tkinter
    show_plot(fig, 1000, 600)

def show_plot(fig, width, height):
    """
    Affiche un graphique Matplotlib dans une fenêtre Tkinter.

    Cette fonction prend un objet de figure Matplotlib (fig) ainsi que les dimensions (width, height) souhaitées
    pour la fenêtre Tkinter qui affichera le graphique. La fenêtre est centrée à l'écran en mode plein écran.

    :param fig: Objet de figure Matplotlib à afficher.
    :param width: Largeur de la fenêtre Tkinter.
    :param height: Hauteur de la fenêtre Tkinter.
    :return: Aucune valeur de retour explicite. La fenêtre Tkinter est créée et affiche le graphique.
    """
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

def handle_choice():
    """
    Gère la sélection de question dans l'interface graphique.

    Cette fonction est appelée lorsqu'un utilisateur choisit une question dans le menu déroulant de l'interface graphique.
    Elle récupère la question sélectionnée et appelle la fonction correspondante pour afficher la réponse.

    :return: Aucune valeur de retour explicite.
    """
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

# Définir la largeur du menu déroulant
question_menu.configure(width=60)  # Ajustez la largeur selon vos besoins

question_menu.pack(pady=10)

# Bouton de validation
validate_button = tk.Button(root, text='Valider', command=handle_choice)
validate_button.pack(pady=10)

def close_fullscreen():
    """
    Ferme la fenêtre en mode plein écran.

    Cette fonction désactive le mode plein écran de la fenêtre racine Tkinter (root) et la détruit.

    :return: Aucune valeur de retour explicite.
    """
    root.attributes('-fullscreen', False)
    root.destroy()

# Bouton pour fermer la fenêtre en mode plein écran
close_fullscreen_button = tk.Button(root, text="Fermer la fenêtre", command=close_fullscreen)
close_fullscreen_button.pack(pady=10)

# Lancement de l'interface graphique
root.mainloop()