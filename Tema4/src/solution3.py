from itertools import combinations

import pandas as pd

# Crearea sistemului de informații (tabel inițial)
data = {
    "Nume" : ["Marius", "Petre", "Ana", "Maria", "Nicu"],
    "Varsta" : [33, 27, 20, 39, 45],
    "Studii" : ["Postliceale", "Superioare", "Superioare", "Postliceale", "Liceale"],
    "Vechime" : [8, 5, 0, 14, 19],
    "Certificat_formator" : ["DA", "NU", "DA", "NU", "NU"]
}


def creeaza_tabel() :
    return pd.DataFrame(data)


def calculeaza_decizie(row) :
    # Condițiile de decizie
    return row["Varsta"] < 40 and row["Studii"] in ["Superioare", "Postliceale"] and row["Vechime"] > 0


def indiscernabilitate(df, atribute) :
    """Gruparea în clase de echivalență în funcție de atributele specificate."""
    echivalente = {}
    for _, row in df.iterrows() :
        cheie = tuple(row[atribut] for atribut in atribute)
        if cheie not in echivalente :
            echivalente[cheie] = []
        echivalente[cheie].append(row["Nume"])
    return echivalente


def aproximare_inferioara_superioara(clase_echivalenta, X) :
    """Calculează aproximarea inferioară, superioară și identifică regiunea de frontieră."""
    aproximare_inferioara = set()
    aproximare_superioara = set()
    regiune_frontiera = set()

    for clasa in clase_echivalenta.values() :
        clasa_set = set(clasa)
        print(f"Clasă: {clasa_set}, Intersecție cu X: {clasa_set & X}")  # Debugging
        if clasa_set.issubset(X) :
            aproximare_inferioara.update(clasa_set)
        if clasa_set & X :
            aproximare_superioara.update(clasa_set)
        if clasa_set & X and not clasa_set.issubset(X) :
            regiune_frontiera.update(clasa_set - X)

    return aproximare_inferioara, aproximare_superioara, regiune_frontiera


def genereaza_reguli(clase_echivalenta, atribut_decizie, df) :
    reguli_certe = []
    reguli_posibile = []

    for cheie, clasa in clase_echivalenta.items() :
        clasa_decizii = set(df[df["Nume"].isin(clasa)][atribut_decizie])
        if len(clasa_decizii) == 1 :
            reguli_certe.append((cheie, list(clasa_decizii)[0]))
        else :
            reguli_posibile.append((cheie, clasa_decizii))

    return reguli_certe, reguli_posibile


def calculeaza_reduct_nucleu(df, atribut_decizie) :
    """Calculează reductele și nucleul sistemului de decizie."""
    atribute = [col for col in df.columns if col not in ["Nume", atribut_decizie]]
    toate_reductele = []

    # Generăm toate combinațiile posibile de atribute
    for lungime in range(1, len(atribute) + 1) :
        for subset in combinations(atribute, lungime) :
            subset = list(subset)
            clase_echivalenta = indiscernabilitate(df, subset)

            # Verificăm dacă reductul păstrează deciziile
            valid = True
            for clasa in clase_echivalenta.values() :
                decizii = set(df[df["Nume"].isin(clasa)][atribut_decizie])
                if len(decizii) > 1 :
                    valid = False
                    break

            if valid :
                toate_reductele.append(set(subset))
                print(f"Reduct valid: {subset}")  # Debugging

    # Calculăm nucleul ca intersecția tuturor reductelor
    if toate_reductele :
        print(f"Toate reductele: {toate_reductele}")  # Debugging
        nucleu = set.intersection(*toate_reductele)
    else :
        nucleu = set()

    return toate_reductele, nucleu


def calculeaza_regiunea_positiva(df, clase_echivalenta, atribut_decizie) :
    """Calculează regiunea pozitivă pentru sistemul de decizie."""
    regiune_positiva = set()
    for clasa in clase_echivalenta.values() :
        decizii = set(df[df["Nume"].isin(clasa)][atribut_decizie])
        if len(decizii) == 1 :  # Dacă toate elementele clasei au aceeași decizie
            regiune_positiva.update(clasa)
    return regiune_positiva


def functii_apartinenta_rough(clase_echivalenta, X) :
    """Calculează funcțiile de apartenență rough pentru fiecare element."""
    apartenenta = {}
    for clasa in clase_echivalenta.values() :
        clasa_set = set(clasa)
        intersectie = clasa_set & X
        for element in clasa :
            apartenenta[element] = len(intersectie) / len(clasa_set) if len(clasa_set) > 0 else 0
    return apartenenta


def main() :
    # Crearea tabelului
    df = creeaza_tabel()
    df["Decizie"] = df.apply(calculeaza_decizie, axis=1)

    # Definirea atributelor pentru echivalență
    atribute = ["Varsta", "Studii", "Vechime"]

    # Gruparea în clase de echivalență
    clase_echivalenta = indiscernabilitate(df, atribute)

    # Definirea mulțimii X (persoanele cu Decizie = True)
    X = set(df[df["Decizie"]]["Nume"])

    # Calcularea aproximărilor și a regiunii de frontieră
    aprox_inferioara, aprox_superioara, frontiera = aproximare_inferioara_superioara(clase_echivalenta, X)

    # Generarea regulilor
    reguli_certe, reguli_posibile = genereaza_reguli(clase_echivalenta, "Decizie", df)

    # Calcularea reductelor și nucleului
    reducte, nucleu = calculeaza_reduct_nucleu(df, "Decizie")

    # Calcularea regiunii pozitive
    regiune_positiva = calculeaza_regiunea_positiva(df, clase_echivalenta, "Decizie")

    # Calcularea funcțiilor de apartenență rough
    apartenenta = functii_apartinenta_rough(clase_echivalenta, X)

    # Afișarea rezultatelor
    print("Tabelul inițial de informații:")
    print(df)

    print("\nClase de echivalență:")
    for cheie, valoare in clase_echivalenta.items() :
        print(f"{cheie}: {valoare}")

    print("\nAproximarea inferioară:", aprox_inferioara)
    print("Aproximarea superioară:", aprox_superioara)
    print("Regiunea de frontieră:", frontiera)

    print("\nReguli certe:")
    for regula in reguli_certe :
        print(f"IF {regula[0]} THEN Decizie={regula[1]}")

    print("\nReguli posibile:")
    for regula in reguli_posibile :
        print(f"IF {regula[0]} THEN Decizie poate fi {regula[1]}")

    print("\nReducte:")
    for reduct in reducte :
        print(reduct)

    print("\nNucleul:", nucleu)

    print("\nRegiunea pozitivă:", regiune_positiva)

    print("\nFuncții de apartenență rough:")
    for element, val in apartenenta.items() :
        print(f"{element}: {val}")


if __name__ == "__main__" :
    main()
