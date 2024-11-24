class SistemNutritieFitness :
    def __init__(self) :
        # 20 Initial Facts
        self.fapte = {
            "sedentar" : True,
            "consum_grasimi_saturate" : True,
            "hipertensiune" : True,
            "stres" : True,
            "doreste_pierdere_in_greutate" : True,
            "energie_scazuta" : True,
            "consum_proteine_scazut" : True,
            "consum_fibre_scazut" : True,
            "imc_peste_30" : True,
            "fumeaza" : True,
            "consum_alcool_excesiv" : True,
            "diabet_tip_2" : True,
            "consum_zahar_ridicat" : True,
            "exercitii_regulate" : False,
            "somn_inadecvat" : True,
            "nivel_colesterol_mare" : True,
            "anxietate" : True,
            "varsta_peste_50" : False,
            "istoric_cardiovascular" : True,
            "deficit_vitamina_d" : True
        }

        # 10 Rules
        self.reguli = [
            {"if" : ["sedentar", "consum_grasimi_saturate"], "then" : "risc_colesterol_crescut", "cf" : 0.9},
            {"if" : ["risc_colesterol_crescut", "hipertensiune"], "then" : "recomandare_reducere_grasimi_exercitii",
             "cf" : 0.8},
            {"if" : ["stres", "energie_scazuta"], "then" : "recomandare_yoga_meditatie", "cf" : 0.7},
            {"if" : ["doreste_pierdere_in_greutate", "imc_peste_30"], "then" : "recomandare_dieta_fitness",
             "cf" : 0.85},
            {"if" : ["fumeaza", "consum_alcool_excesiv"], "then" : "recomandare_consiliere_renuntare", "cf" : 0.9},
            {"if" : ["diabet_tip_2", "consum_fibre_scazut"], "then" : "recomandare_fibre_carbohidrati", "cf" : 0.8},
            {"if" : ["nivel_colesterol_mare", "istoric_cardiovascular"], "then" : "recomandare_control_cardiologic",
             "cf" : 0.95},
            {"if" : ["somn_inadecvat", "anxietate"], "then" : "recomandare_terapie_psihologica", "cf" : 0.85},
            {"if" : ["deficit_vitamina_d", "sedentar"], "then" : "recomandare_suplimente_vitamina_d", "cf" : 0.7},
            {"if" : ["varsta_peste_50", "hipertensiune", "istoric_cardiovascular"],
             "then" : "recomandare_monitorizare_medicala", "cf" : 0.9},
        ]

        # Deduced facts and explanations
        self.fapte_deduse = {}
        self.explicatii = {}

    # Motor de inferenta: Forward chaining
    def inlantuire_inainte(self) :
        reguli_aplicate = True
        while reguli_aplicate :
            reguli_aplicate = False
            for regula in self.reguli :
                if all(self.fapte.get(conditie, False) or conditie in self.fapte_deduse for conditie in regula["if"]) :
                    concluzie = regula["then"]
                    if concluzie not in self.fapte_deduse :
                        # Deduce conclusion
                        self.fapte_deduse[concluzie] = regula["cf"]
                        reguli_aplicate = True
                        # Check if conclusion is derived directly or via intermediates
                        direct = all(cond in self.fapte for cond in regula["if"])
                        tip = "direct din faptele inițiale" if direct else "prin concluzii intermediare"
                        self.explicatii[
                            concluzie] = f"Regula aplicata: Daca {regula['if']} atunci {concluzie} (CF: {regula['cf']}). Concluzie obținută {tip}."

    # Motor de inferenta: Backward chaining
    def inlantuire_inapoi(self, scop) :
        if scop in self.fapte :
            return self.fapte[scop]
        if scop in self.fapte_deduse :
            return self.fapte_deduse[scop]

        for regula in self.reguli :
            if regula["then"] == scop :
                if all(self.inlantuire_inapoi(conditie) for conditie in regula["if"]) :
                    self.fapte_deduse[scop] = regula["cf"]
                    # Check if conclusion is derived directly or via intermediates
                    direct = all(cond in self.fapte for cond in regula["if"])
                    tip = "direct din faptele inițiale" if direct else "prin concluzii intermediare"
                    self.explicatii[
                        scop] = f"Regula aplicata: Daca {regula['if']} atunci {scop} (CF: {regula['cf']}). Concluzie obținută {tip}."
                    return regula["cf"]
        return False

    # Metoda pentru rularea inferenței înainte
    def rulare_inferenta_inainte(self) :
        print("\n--- Rulare Inferență Înainte ---")
        print("Pornim de la faptele inițiale pentru a deduce concluzii noi...\n")
        self.inlantuire_inainte()
        if self.fapte_deduse :
            print("Rezultatele inferenței înainte:")
            for concluzie in self.fapte_deduse :
                print(f"- {concluzie} (CF: {self.fapte_deduse[concluzie]})")
                print(f"  Explicație: {self.explica(concluzie)}\n")
        else :
            print(" Nu s-au putut deduce concluzii noi.")

    # Metoda pentru rularea inferenței înapoi
    def rulare_inferenta_inapoi(self) :
        print("\n--- Rulare Inferență Înapoi ---")
        print("Verificăm concluziile folosind backward chaining...\n")
        for regula in self.reguli :
            scop = regula["then"]
            print(f"Interogare pentru scop: '{scop}'")
            rezultat = self.inlantuire_inapoi(scop)
            if rezultat :
                print(f"'{scop}' este adevărat (CF: {self.fapte_deduse.get(scop, 'N/A')}).")
                print(f"  Explicație: {self.explica(scop)}\n")
            else :
                print(f"'{scop}' nu poate fi dedus din faptele existente.\n")
        # Explicatii pentru concluzii

    def explica(self, concluzie) :
        return self.explicatii.get(concluzie, "Nu exista explicatie pentru concluzia ceruta.")
