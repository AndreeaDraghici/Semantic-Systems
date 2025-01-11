import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree


class ID3Tree :
    def __init__(self) :
        self.tree = None

    def calculeaza_entropia(self, y) :
        valori_unice, frecvente = np.unique(y, return_counts=True)
        probabilitati = frecvente / len(y)
        entropia = -np.sum(probabilitati * np.log2(probabilitati))
        return entropia

    def castig_informational(self, y, feature) :
        entropie_initiala = self.calculeaza_entropia(y)
        valori_unice, frecvente = np.unique(feature, return_counts=True)
        entropie_conditionala = 0

        for valoare, frecventa in zip(valori_unice, frecvente) :
            subset = y[feature == valoare]
            entropie_conditionala += (frecventa / len(feature)) * self.calculeaza_entropia(subset)

        gain = entropie_initiala - entropie_conditionala
        return entropie_initiala, gain

    def alege_cel_mai_bun_atribut(self, X, y) :
        castiguri = {}
        entropii_initiale = {}
        for col in X.columns :
            entropii_initiale[col], castiguri[col] = self.castig_informational(y, X[col])

        cel_mai_bun = max(castiguri, key=castiguri.get)
        print("\nEntropii inițiale pentru fiecare atribut:")
        for atribut, entropie in entropii_initiale.items() :
            print(f" {atribut}: {entropie:.4f}")

        print("\nCâștiguri informaționale pentru fiecare atribut:")
        for atribut, castig in castiguri.items() :
            print(f" {atribut}: {castig:.4f}")

        print(f"\nCel mai bun atribut: {cel_mai_bun}")
        return cel_mai_bun

    def construieste_arbore(self, X, y) :
        # Dacă toate valorile țintă sunt identice, returnează acea valoare
        if len(np.unique(y)) == 1 :
            return y.iloc[0]

        # Dacă nu mai sunt atribute disponibile, returnează clasa majoritară
        if X.empty :
            return y.mode()[0]

        # Alege cel mai bun atribut pentru splitting
        cel_mai_bun_atribut = self.alege_cel_mai_bun_atribut(X, y)
        arbore = {cel_mai_bun_atribut : {}}

        # Creează ramuri pentru fiecare valoare a atributului
        for valoare in np.unique(X[cel_mai_bun_atribut]) :
            subset_X = X[X[cel_mai_bun_atribut] == valoare].drop(columns=[cel_mai_bun_atribut])
            subset_y = y[X[cel_mai_bun_atribut] == valoare]

            # Construiește recursiv arborele pentru fiecare subset
            arbore[cel_mai_bun_atribut][valoare] = self.construieste_arbore(subset_X, subset_y)

        return arbore

    def fit(self, X, y) :
        self.tree = self.construieste_arbore(X, y)

    def predict_sample(self, sample, tree) :
        if not isinstance(tree, dict) :
            return tree

        atribut = next(iter(tree))
        valoare = sample[atribut]

        if valoare in tree[atribut] :
            return self.predict_sample(sample, tree[atribut][valoare])
        else :
            return None  # Valoarea nu există în arbore

    def predict(self, X) :
        return X.apply(lambda sample : self.predict_sample(sample, self.tree), axis=1)

    def print_tree(self, tree=None, indent="", depth=0) :
        if tree is None :
            tree = self.tree

        if not isinstance(tree, dict) :
            print("  " * depth + f"[Leaf] {tree}")
            return

        for key, value in tree.items() :
            print("  " * depth + f"{key}:")
            for subkey, subtree in value.items() :
                print("  " * (depth + 1) + f"{subkey} ->")
                self.print_tree(subtree, indent, depth + 2)

    def export_if_then(self, tree=None, indent="IF ") :
        if tree is None :
            tree = self.tree

        if not isinstance(tree, dict) :
            print(indent + f" THEN {tree}")
            return

        for key, value in tree.items() :
            for subkey, subtree in value.items() :
                self.export_if_then(subtree, indent + f"{key} = {subkey} AND ")


# Exemplu de utilizare
def main() :
    # Set de date extins pentru exemplificare
    set_date = {
        "Experiență" : [5, 2, 7, 10, 1, 4, 6, 3, 8, 9, 12, 15, 1, 2, 4, 5, 7, 3, 10, 11],
        "Educație" : ["Licență", "Liceu", "Master", "Doctorat", "Liceu", "Licență", "Master", "Liceu", "Licență",
                      "Doctorat", "Master", "Doctorat", "Liceu", "Liceu", "Licență", "Licență", "Master", "Liceu",
                      "Doctorat", "Licență"],
        "Ore_suplimentare" : ["Da", "Nu", "Da", "Nu", "Nu", "Da", "Nu", "Nu", "Da", "Da", "Nu", "Nu", "Nu", "Da", "Nu",
                              "Da", "Nu", "Nu", "Da", "Nu"],
        "Departament" : ["IT", "HR", "IT", "Management", "HR", "IT", "Management", "HR", "IT", "Management", "IT", "HR",
                         "Management", "HR", "IT", "IT", "Management", "HR", "IT", "Management"],
        "Promovat" : ["Da", "Nu", "Da", "Da", "Nu", "Da", "Nu", "Nu", "Da", "Da", "Nu", "Da", "Nu", "Nu", "Da", "Da",
                      "Nu", "Nu", "Da", "Nu"]
    }

    df = pd.DataFrame(set_date)

    # Convertim valorile categorice în numerice (dacă este cazul)
    df = pd.get_dummies(df, columns=["Educație", "Ore_suplimentare", "Departament"], drop_first=True)

    X = df.drop(columns=["Promovat"])
    y = df["Promovat"]

    # Convertim toate coloanele în tip numeric
    X = X.apply(pd.to_numeric)

    # Construim arborele decizional folosind DecisionTreeClassifier pentru grafic
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
    clf.fit(X, y)

    # Vizualizăm arborele decizional ca grafic
    plt.figure(figsize=(9, 6))
    plot_tree(clf, feature_names=X.columns, class_names=clf.classes_, filled=True, rounded=True)
    plt.title("Arborele Decizional - Vizualizare Grafică")
    plt.show()

    # Construim arborele decizional folosind ID3Tree
    id3 = ID3Tree()
    id3.fit(X, y)

    # Afișăm arborele în format text
    print(f"Numărul total de noduri: {clf.tree_.node_count}")
    print(f"Numărul de frunze: {clf.get_n_leaves()}")
    print(f"Adâncimea maximă a arborelui: {clf.get_depth()}")

    # Exportăm regulile arborelui în format IF-THEN
    print("\nReguli IF-THEN ale arborelui decizional:")
    id3.export_if_then()

    # 2. Distribuția clasei țintă
    plt.figure(figsize=(6, 4))
    y.value_counts().plot(kind="bar", color="skyblue")
    plt.title("Distribuția clasei țintă")
    plt.xlabel("Clasă")
    plt.ylabel("Frecvență")
    plt.show()

    # 3. Matricea de corelație pentru date numerice
    plt.figure(figsize=(10, 5))
    sns.heatmap(X.corr(), annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Matricea de corelație între caracteristicile numerice")
    plt.show()

    # 4. Boxplot pentru caracteristici numerice
    plt.figure(figsize=(8, 8))
    sns.boxplot(data=X)
    plt.title("Boxplot pentru caracteristicile numerice")
    plt.show()


if __name__ == "__main__" :
    main()
