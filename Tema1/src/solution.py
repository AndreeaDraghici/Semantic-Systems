# Functia pentru desenarea unui patrat (folosit ca baza a casei)
def draw_square(t, size):
    """
    Deseneaza un patrat cu dimensiunea specificata.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Dimensiunea laturii patratului.
    """
    for _ in range(4):  # Repetam de 4 ori pentru a desena un patrat
        t.forward(size)  # Mergem inainte cu dimensiunea specificata
        t.left(90)  # Rotim la stanga 90 de grade pentru a forma colturile

# Functia pentru desenarea unui triunghi (folosit ca acoperisul casei)
def draw_triangle(t, size):
    """
    Deseneaza un triunghi echilateral cu latura specificata.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Dimensiunea laturii triunghiului.
    """
    for _ in range(3):  # Repetam de 3 ori pentru a desena un triunghi
        t.forward(size)  # Mergem inainte cu dimensiunea specificata
        t.left(120)  # Rotim la stanga 120 de grade pentru a forma triunghiul echilateral

# Functia pentru desenarea unei case (un patrat pentru baza + un triunghi pentru acoperis)
def draw_house(t, size):
    """
    Deseneaza o casa compusa dintr-un patrat (baza) si un triunghi (acoperis).

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Dimensiunea casei (latura patratului).
    """
    t.fillcolor("lightblue")  # Setam culoarea de umplere la albastru deschis pentru casa
    t.begin_fill()  # Incepem umplerea formei patratului
    draw_square(t, size)  # Desenam baza patrata a casei
    t.end_fill()  # Terminam umplerea

    # Mutam turtle la partea de sus a patratului pentru a incepe desenarea acoperisului
    t.left(90)
    t.forward(size)
    t.right(90)

    t.fillcolor("brown")  # Setam culoarea de umplere la maro pentru acoperis
    t.begin_fill()  # Incepem umplerea formei triunghiului
    draw_triangle(t, size)  # Desenam acoperisul triunghiular
    t.end_fill()  # Terminam umplerea

# Functia pentru desenarea unui copac complet (trunchi + frunze)
def draw_tree(t, size):
    """
    Deseneaza un copac compus dintr-un trunchi dreptunghiular si un cerc (frunzele).

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Dimensiunea copacului.
    """
    # Desenam trunchiul copacului (un dreptunghi maro)
    t.fillcolor("#8B4513")  # Setam culoarea de umplere la maro pentru trunchi
    t.begin_fill()  # Incepem umplerea formei dreptunghiului
    for _ in range(2):  # Repetam de 2 ori pentru a desena un dreptunghi
        t.forward(size * 0.2)  # Partea scurta a dreptunghiului (latimea trunchiului)
        t.left(90)  # Rotim la stanga 90 de grade
        t.forward(size)  # Partea lunga a dreptunghiului (inaltimea trunchiului)
        t.left(90)  # Rotim din nou la stanga
    t.end_fill()  # Terminam umplerea

    # Mutam turtle in pozitia de unde vor fi desenate frunzele
    t.penup()  # Ridicam stiloul pentru a nu desena in timp ce ne mutam
    t.left(90)  # Rotim turtle in sus
    t.forward(size)  # Mutam turtle deasupra trunchiului
    t.right(90)  # Rotim turtle la dreapta pentru a pregati desenarea frunzelor

    # Mutam turtle putin mai sus si inainte pentru a centra frunzele
    t.forward(size * 0.1)  # Mutam turtle usor inainte
    t.right(90)  # Rotim turtle la dreapta
    t.forward(size * 0.25)  # Mutam turtle in sus pentru a centra frunzele
    t.left(90)  # Rotim turtle inapoi la pozitia normala

    # Desenam frunzele copacului (un cerc verde)
    t.pendown()  # Coboram stiloul pentru a incepe desenarea
    t.fillcolor("green")  # Setam culoarea de umplere la verde pentru frunze
    t.begin_fill()  # Incepem umplerea cercului
    t.circle(size * 0.5)  # Desenam cercul care reprezinta frunzele
    t.end_fill()  # Terminam umplerea

# Functia pentru desenarea soarelui cu raze
def draw_sun(t, x, y, size):
    """
    Deseneaza un soare la pozitia specificata, format dintr-un cerc si raze.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a pozitiei soarelui.
        y (int): Coordonata y a pozitiei soarelui.
        size (int): Raza soarelui (cercul).
    """
    # Mutam turtle la pozitia specificata pentru soare
    t.penup()  # Ridicam stiloul pentru a nu desena in timpul mutarii
    t.goto(x, y)  # Mutam turtle la coordonatele x si y specificate
    t.pendown()  # Coboram stiloul pentru a incepe desenarea soarelui

    # Desenam cercul pentru soare
    t.fillcolor("yellow")  # Setam culoarea de umplere la galben pentru soare
    t.begin_fill()  # Incepem umplerea cercului
    t.circle(size)  # Desenam cercul care reprezinta soarele
    t.end_fill()  # Terminam umplerea

    # Desenam razele soarelui
    t.pencolor("yellow")  # Setam culoarea stiloului la galben pentru raze
    t.penup()  # Ridicam stiloul din nou pentru a ne pozitiona pentru raze
    for _ in range(12):  # Desenam 12 raze in jurul soarelui
        t.goto(x, y + size)  # Mutam turtle la partea de sus a soarelui
        t.pendown()  # Coboram stiloul pentru a desena raza
        t.forward(size + 20)  # Desenam raza in afara cercului
        t.penup()  # Ridicam stiloul dupa ce am desenat raza
        t.goto(x, y)  # Revenim la centrul soarelui
        t.right(30)  # Rotim turtle cu 30 de grade pentru urmatoarea raza

    # Resetam culoarea stiloului la negru pentru desene viitoare
    t.pencolor("black")

# Functia pentru desenarea unui munte cu varf de zapada
def draw_mountain(t, x, y, size):
    """
    Deseneaza un munte sub forma de triunghi la coordonatele specificate.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a bazei muntelui.
        y (int): Coordonata y a bazei muntelui.
        size (int): Lungimea laturii muntelui (triunghiului).
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Desenam muntele principal ca un triunghi gri
    t.fillcolor("grey")  # Setam culoarea de umplere la gri pentru munte
    t.begin_fill()  # Incepem umplerea triunghiului
    for _ in range(3):  # Desenam cele 3 laturi ale triunghiului
        t.forward(size)
        t.left(120)
    t.end_fill()  # Terminam umplerea

    # Desenam varful cu zapada al muntelui
    t.fillcolor("white")
    t.begin_fill()
    t.goto(x + size * 0.35, y + size * 0.6)  # Desenam partea stanga a zapezii
    t.goto(x + size * 0.65, y + size * 0.6)  # Desenam partea dreapta a zapezii
    t.goto(x + size * 0.5, y + size * 0.85)  # Desenam varful zapezii
    t.goto(x, y)  # Revenim la baza muntelui
    t.end_fill()  # Terminam umplerea

# Functia pentru desenarea unui lac (forma ovala cu reflexii)
def draw_lake(t, x, y, width, height):
    """
    Deseneaza un lac in forma de oval la coordonatele specificate.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x de pornire.
        y (int): Coordonata y de pornire.
        width (int): Latimea lacului.
        height (int): Inaltimea lacului.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()

    # Desenam un oval combinand doua arcuri
    t.setheading(45)
    for _ in range(2):
        t.circle(width, 90)
        t.circle(height, 90)
    t.end_fill()

# Functia pentru desenarea unui nor cu umbra
def draw_cloud(t, x, y, size):
    """
    Deseneaza un nor la coordonatele specificate, compus din mai multe cercuri.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x de pornire.
        y (int): Coordonata y de pornire.
        size (int): Dimensiunea norului (raza cercului de baza).
    """
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Desenam cercurile care formeaza norul
    t.fillcolor("white")
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    t.penup()
    t.goto(x + size * 0.7, y)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.8)
    t.end_fill()

    t.penup()
    t.goto(x - size * 0.7, y)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.6)
    t.end_fill()

    # Desenam umbra norului
    t.penup()
    t.goto(x - size * 0.5, y - size * 0.2)
    t.pendown()
    t.fillcolor("lightgrey")
    t.begin_fill()
    t.circle(size * 0.5)
    t.end_fill()

# Functia pentru desenarea unui plan de iarba (un dreptunghi verde)
def draw_grass(t, start_x, start_y, width, height):
    """
    Deseneaza un plan de iarba sub forma de dreptunghi verde.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        start_x (int): Coordonata x de pornire.
        start_y (int): Coordonata y de pornire.
        width (int): Latimea planului de iarba.
        height (int): Inaltimea planului de iarba.
    """
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    t.fillcolor("green")
    t.begin_fill()
    for _ in range(2):  # Desenam un dreptunghi repetand de 2 ori
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Functia pentru desenarea unei scene complete (o casa si un copac)
def draw_scene(t, x, y, house_size, tree_size):
    """
    Deseneaza o scena completa, compusa dintr-o casa si un copac.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x pentru pozitionarea scenei.
        y (int): Coordonata y pentru pozitionarea scenei.
        house_size (int): Dimensiunea casei (latura).
        tree_size (int): Dimensiunea copacului.
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_house(t, house_size)  # Desenam casa la pozitia specificata

    # Pozitionam copacul la dreapta casei
    t.penup()
    t.goto(x + house_size + 30, y)  # Mutam la dreapta casei
    t.pendown()
    draw_tree(t, tree_size)  # Desenam copacul
