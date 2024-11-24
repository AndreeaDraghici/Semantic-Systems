# Functia main
from src.solution import SistemNutritieFitness


# Functia main
def main():

    # Instantierea sistemului
    sistem = SistemNutritieFitness()

    # Rularea inferenței înainte
    sistem.rulare_inferenta_inainte()

    # Rularea inferenței înapoi
    sistem.rulare_inferenta_inapoi()


# Apelam functia main
if __name__ == "__main__" :
    main()
