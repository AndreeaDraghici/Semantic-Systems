import pandas as pd


def creeaza_tabel() :
    # Crearea tabelului de informații
    data = {
        "Nume" : ["Marius", "Petre", "Ana", "Maria", "Nicu"],
        "Varsta" : [33, 27, 20, 39, 45],
        "Studii" : ["Postliceale", "Superioare", "Superioare", "Postliceale", "Liceale"],
        "Vechime" : [8, 5, 0, 14, 19],
        "Certificat_formator" : ["DA", "NU", "DA", "NU", "NU"]
    }
    return pd.DataFrame(data)


def indeplineste_conditii(row) :
    # Condițiile de angajare
    return row["Varsta"] < 40 and row["Studii"] in ["Superioare", "Postliceale"] and row["Vechime"] > 0


def aproximare_inferioara(row) :
    # Aparține sigur dacă îndeplinește condițiile și are Certificat formator = "DA"
    return row["Conditii"] and row["Certificat_formator"] == "DA"


def aproximare_superioara(row) :
    # Poate aparține dacă îndeplinește condițiile
    return row["Conditii"]


def main() :
    # Crearea tabelului
    df = creeaza_tabel()
    print("Tabelul inițial de informații:")
    print(df)

    # Adăugarea unei coloane pentru condiții
    df["Conditii"] = df.apply(indeplineste_conditii, axis=1)

    # Definirea mulțimii X
    X = df[df["Conditii"]]

    # Calcularea aproximărilor
    X_lower = df[df.apply(aproximare_inferioara, axis=1)]  # Aproximarea inferioară
    X_upper = df[df.apply(aproximare_superioara, axis=1)]  # Aproximarea superioară
    X_boundary = X_upper[~X_upper["Nume"].isin(X_lower["Nume"])]  # Regiunea de frontieră

    # Afișarea rezultatelor
    print("\nMulțimea X (persoanele care îndeplinesc condițiile):")
    print(X)

    print("\nAproximarea Inferioară:")
    print(X_lower)

    print("\nAproximarea Superioară:")
    print(X_upper)

    print("\nRegiunea de Frontieră:")
    print(X_boundary)


if __name__ == "__main__" :
    main()
