"""
Module d'interface utilisateur pour afficher des informations sur les fromages à l'aide de Tkinter.
"""
from imports import tk, messagebox, Figure, FigureCanvasTkAgg
from scrapping_fromage import FromageETL

class FromageUI:
    """
    Classe représentant l'interface utilisateur pour afficher des informations sur les fromages.
    """
    def __init__(self, master):
        """
        Initialisation de l'interface graphique de la classe FromageUI.

        Parameters:
        - master (Tk): Fenêtre principale de l'application.

        Cette méthode crée une interface utilisateur pour la gestion des fromages,
        comprenant un bouton pour mettre à jourla base de données (BDD),
        et un diagramme en camembert pour afficher visuellement,
        les informations sur les fromages.

        Usage:
        fromage_ui = FromageUI(master)
        """
        self.master = master
        master.title("Interface Fromage")

        # Bouton pour mettre à jour la BDD
        self.update_button = tk.Button(master, text="Mettre à jour la BDD",
            command=self.update_database)
        self.update_button.pack()

        # Diagramme en camembert
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

    def update_database(self):
        """
        Met à jour la base de données (BDD) en extrayant,
        transformant et chargeant les données des fromages.

        Cette méthode utilise la classe FromageETL pour
        extraire les données depuis une source en ligne, 
        les transformer en un format approprié, 
        et les charger dans une base de données SQLite. 
        Elle affiche ensuite une boîte de dialogue
        informant l'utilisateur du succès de la mise à jour.

        Usage:
        fromage_ui.update_database()
        """
        # Appeler la méthode d'ETL pour mettre à jour la BDD
        etl = FromageETL(url="https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/")
        etl.extract()
        etl.transform()
        data = etl.load("fromages_bdd.sqlite", "fromages_table")
        messagebox.showinfo("Mise à jour", "La base de données a été mise à jour avec succès.")

        # Mettre à jour le diagramme en camembert
        self.update_pie_chart(data)

    def update_pie_chart(self, data):
        """
        Met à jour le diagramme en camembert 
        avec les ratios de fromages par famille.

        Cette méthode prend un DataFrame de données
        sur les fromages en paramètre, 
        calcule le ratio de chaque famille de fromages, 
        groupe les familles dont le ratio est inférieur à 5%
        sous la catégorie "Autres", 
        et met à jour le diagramme en camembert en conséquence.

        Args:
            data (pd.DataFrame): Le DataFrame contenant les données.

        Usage:
        fromage_ui.update_pie_chart(data)
        """
        # Calculer le ratio de fromage par famille
        ratio = data['fromage_familles'].value_counts(normalize=True) * 100

        # Regrouper les données inférieures à 5% dans "Autres"
        mask = ratio < 5
        ratio['Autres'] = ratio[mask].sum()
        mask = mask.reindex(ratio.index, fill_value=False)
        ratio = ratio[~mask]

        # Créer le diagramme en camembert
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.pie(ratio, labels=ratio.index, autopct='%1.1f%%')
        self.canvas.draw()

        # Créer un deuxième diagramme en camembert pour "Autres"
        if 'Autres' in ratio:
            other_data = data['fromage_familles'].value_counts(normalize=True)[mask] * 100
            other_fig = Figure(figsize=(5, 5), dpi=100)
            other_canvas = FigureCanvasTkAgg(other_fig, master=self.master)
            other_canvas.get_tk_widget().pack()
            other_ax = other_fig.add_subplot(111)
            other_ax.pie(other_data, labels=other_data.index, autopct='%1.1f%%')
            other_canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = FromageUI(root)
    root.mainloop()
