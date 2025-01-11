import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


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

    # Împărțim datele în seturi de antrenare și test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Creăm și antrenăm arborele decizional
    model = DecisionTreeClassifier(criterion="entropy", random_state=42, max_depth=4)
    model.fit(X_train, y_train)

    # Vizualizăm arborele decizional
    def vizualizeaza_arbore(model, feature_names) :
        plt.figure(figsize=(9, 8))
        plot_tree(model, feature_names=feature_names, class_names=model.classes_, filled=True)
        plt.title("Arbore Decizional - Vizualizare Grafică")
        plt.show()

    vizualizeaza_arbore(model, X.columns)

    # Evaluarea modelului pe setul de testare
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAcuratețea modelului pe setul de testare: {accuracy:.2f}")

    print("\nRaportul de clasificare:")
    print(classification_report(y_test, y_pred))

    # Matricea de confuzie
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title("Matricea de confuzie")
    plt.xlabel("Clase prezise")
    plt.ylabel("Clase reale")
    plt.show()


if __name__ == "__main__" :
    main()
