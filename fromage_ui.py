# fromage_ui.py
from imports import tk, messagebox, Figure, FigureCanvasTkAgg
from scrapping_fromage import FromageETL

class FromageUI:
    def __init__(self, master):
        self.master = master
        master.title("Interface Fromage")

        # Bouton pour mettre à jour la BDD
        self.update_button = tk.Button(master, text="Mettre à jour la BDD", command=self.update_database)
        self.update_button.pack()

        # Diagramme en camembert
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

    def update_database(self):
        # Appeler la méthode d'ETL pour mettre à jour la BDD
        etl = FromageETL(url="https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/")
        etl.extract()
        etl.transform()
        data = etl.load("fromages_bdd.sqlite", "fromages_table")
        messagebox.showinfo("Mise à jour", "La base de données a été mise à jour avec succès.")

        # Mettre à jour le diagramme en camembert
        self.update_pie_chart(data)

    def update_pie_chart(self, data):
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
