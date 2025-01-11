import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree


def main() :
    set_date = {
        "Experiență" : [5, 2, 7, 10, 1, 4, 6, 3],  # Ani de experiență
        "Educație" : ["Licență", "Liceu", "Master", "Doctorat", "Liceu", "Licență", "Master", "Liceu"],
        "Ore_suplimentare" : ["Da", "Nu", "Da", "Nu", "Da", "Da", "Nu", "Nu"],
        "Vârstă" : [29, 22, 35, 45, 19, 30, 40, 25],
        "Departament" : ["IT", "HR", "IT", "Management", "HR", "IT", "Management", "HR"],
        "Promovat" : ["Da", "Nu", "Da", "Da", "Nu", "Da", "Nu", "Nu"]
    }

    # Convertim valorile categorice în valori numerice
    set_date = pd.DataFrame(set_date)
    set_date = pd.get_dummies(set_date, columns=["Educație", "Ore_suplimentare", "Departament"], drop_first=True)

    # Separăm caracteristicile de țintă
    X = set_date.drop("Promovat", axis=1)
    y = set_date["Promovat"]

    # Creăm și antrenăm arborele decizional
    model = DecisionTreeClassifier(criterion="entropy", random_state=42, max_depth=4)
    model.fit(X, y)

    # Funcție pentru calcularea entropiei
    def calculeaza_entropia(y) :
        valori_unice, frecvente = np.unique(y, return_counts=True)
        probabilitati = frecvente / len(y)
        entropia = -np.sum(probabilitati * np.log2(probabilitati))
        return entropia

    # Exemplu entropie
    entropie_initiala = calculeaza_entropia(y)
    print(f"\nEntropia setului inițial: {entropie_initiala}")

    # Vizualizăm arborele decizional
    def vizualizeaza_arbore(model, feature_names) :
        plt.figure(figsize=(9, 8))
        plot_tree(model, feature_names=feature_names, class_names=model.classes_, filled=True)
        plt.show()

    vizualizeaza_arbore(model, X.columns)

    # Exportăm regulile arborelui
    tree_rules = export_text(model, feature_names=list(X.columns))
    print("\nReguli ale arborelui decizional:")
    print(tree_rules)

    # Calculează câștigul informațional
    def castig_informational(y, feature) :
        entropie_initiala = calculeaza_entropia(y)
        valori_unice, frecvente = np.unique(feature, return_counts=True)
        entropie_conditionala = 0

        for valoare, frecventa in zip(valori_unice, frecvente) :
            subset = y[feature == valoare]
            entropie_conditionala += (frecventa / len(feature)) * calculeaza_entropia(subset)

        return entropie_initiala - entropie_conditionala

    # Exemplu calcul câștig informațional
    castiguri = {col : castig_informational(y, X[col]) for col in X.columns}
    print("\nCâștiguri informaționale pentru fiecare caracteristică:")
    print(castiguri)

    # Histogramă pentru fiecare caracteristică numerică
    X.hist(bins=10, figsize=(10, 8), color='skyblue', edgecolor='black')
    plt.suptitle("Histogramă pentru fiecare caracteristică numerică", fontsize=12)
    plt.show()

    # Pairplot pentru relațiile dintre caracteristici numerice
    sns.pairplot(set_date, diag_kind="kde", corner=True)
    plt.suptitle("Relații între caracteristici (Pairplot)", fontsize=12)
    plt.show()


if __name__ == "__main__" :
    main()
