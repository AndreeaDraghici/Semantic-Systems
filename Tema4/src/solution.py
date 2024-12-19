import pandas as pd


def filtreaza_produse(df, criterii) :
    """Filtreaza produsele folosind criteriile specificate."""
    conditii = {
        'Categorie' : df['Categorie'] == criterii['categorie'],
        'Preț ($)' : df['Preț ($)'] <= criterii['pret_max'],
        'Stoc' : df['Stoc'] == criterii['stoc'],
        'Rating mediu' : df['Rating mediu'] >= criterii['rating_min'],
        'Vândut online' : df['Vândut online'] == criterii['vandut_online'],
        'An lansare' : df['An lansare'] >= criterii['an_min']
    }

    # filtru pentru aproximarea inferioară si superioara
    filtru_inferior = pd.Series([True] * len(df))
    filtru_superior = pd.Series([False] * len(df))

    for key, value in conditii.items() :
        filtru_inferior &= value
        filtru_superior |= value

    aproximare_inferioara = df[filtru_inferior]
    aproximare_superioara = df[filtru_superior]
    regiune_frontiera = aproximare_superioara[~aproximare_superioara.index.isin(aproximare_inferioara.index)]

    return aproximare_inferioara, aproximare_superioara, regiune_frontiera


def afiseaza_rezultate(aprox_inferioara, aprox_superioara, reg_frontiera) :
    """Afiseaza rezultatele filtrarii."""
    print("Aproximare inferioară:")
    print(aprox_inferioara)
    print("\nAproximare superioară:")
    print(aprox_superioara)
    print("\nRegiune de frontieră:")
    print(reg_frontiera)


def main() :
    data = {
        'ID' : [1, 2, 3, 4, 5, 6, 7, 9],
        'Produs' : ['Telefon mobil Samsung', 'Tabletă Samsung', 'Laptop Asus', 'Smartwatch', 'Consolă Gaming',
                    'Laptop Dell', 'Telefon iPhone', 'Camera Canon'],
        'Categorie' : ['Smartphone', 'Tabletă', 'Laptop', 'Ceas', 'Gaming', 'Laptop', 'Smartphone', 'Aparat Compact'],
        'Preț ($)' : [300, 450, 800, 200, 350, 750, 350, 400],
        'Stoc' : ['DA', 'NU', 'DA', 'NU', 'NU', 'DA', 'DA', 'DA'],
        'Vândut online' : ['DA', 'DA', 'NU', 'DA', 'NU', 'DA', 'DA', 'DA'],
        'Rating mediu' : [4.7, 4.0, 4.8, 4.0, 4.5, 4.3, 5.0, 4.3],
        'An lansare' : [2021, 2020, 2022, 2023, 2023, 2022, 2024, 2021]
    }

    df = pd.DataFrame(data)

    criterii = {
        'categorie' : input("Introduceți categoria produsului (ex. Laptop, Smartphone): "),
        'pret_max' : int(input("Introduceți prețul maxim dorit: ")),
        'stoc' : input("Produsul trebuie să fie în stoc? (DA/NU): "),
        'rating_min' : float(input("Introduceți ratingul minim dorit: ")),
        'vandut_online' : input("Produsul trebuie să fie vândut online? (DA/NU): "),
        'an_min' : int(input("Introduceți anul minim de lansare: "))
    }

    # Aplica filtrarea
    aprox_inferioara, aprox_superioara, reg_frontiera = filtreaza_produse(df, criterii)

    # Afiseaza rezultatele
    afiseaza_rezultate(aprox_inferioara, aprox_superioara, reg_frontiera)


if __name__ == "__main__" :
    main()
