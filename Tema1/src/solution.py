import turtle  # Importam modulul turtle pentru a desena


# Functia pentru desenarea unui patrat (baza casei)
def draw_square(t, size) :
    """
    Deseneaza un patrat cu laturile de dimensiunea specificata.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Lungimea laturii patratului.
    """
    for _ in range(4) :  # Repetam de 4 ori pentru cele 4 laturi
        t.forward(size)  # Mergem inainte cu lungimea specificata
        t.left(90)  # Ne rotim la stanga cu 90 de grade pentru a forma coltul


# Functia pentru desenarea acoperisului (triunghi)
def draw_triangle(t, size) :
    """
    Deseneaza un triunghi echilateral cu laturile de dimensiunea specificata.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Lungimea laturii triunghiului.
    """
    for _ in range(3) :  # Repetam de 3 ori pentru cele 3 laturi
        t.forward(size)  # Mergem inainte cu lungimea specificata
        t.left(120)  # Ne rotim la stanga cu 120 de grade pentru triunghi


# Functia pentru desenarea unei case (patrat + acoperis)
def draw_house(t, size) :
    """
    Deseneaza o casa formata dintr-un patrat (baza) si un triunghi (acoperis).

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Dimensiunea laturii bazei casei.
    """
    # Desenam baza casei
    t.fillcolor("lightblue")  # Setam culoarea de umplere pentru casa
    t.begin_fill()  # Incepem umplerea
    draw_square(t, size)  # Desenam baza casei (patrat)
    t.end_fill()  # Finalizam umplerea

    # Mutam Turtle deasupra casei pentru acoperis
    t.left(90)  # Rotim Turtle la stanga cu 90 de grade
    t.forward(size)  # Mutam Turtle deasupra casei
    t.right(90)  # Rotim Turtle la dreapta pentru a incepe acoperisul

    # Desenam acoperisul casei (triunghi echilateral)
    t.fillcolor("brown")  # Setam culoarea de umplere pentru acoperis
    t.begin_fill()  # Incepem umplerea
    draw_triangle(t, size)  # Desenam acoperisul casei
    t.end_fill()  # Finalizam umplerea


# Functia pentru desenarea unui copac complet (trunchi + frunze)
def draw_tree(t, size) :
    """
    Deseneaza un copac cu un trunchi dreptunghiular si frunze circulare.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        size (int): Inaltimea copacului (dimensiunea trunchiului si frunzelor).
    """
    # Desenam trunchiul copacului
    t.fillcolor("#8B4513")  # Setam culoarea de umplere pentru trunchi (maro)
    t.begin_fill()  # Incepem umplerea
    for _ in range(2) :  # Repetam de 2 ori pentru a desena dreptunghiul
        t.forward(size * 0.2)  # Latura scurta a trunchiului
        t.left(90)  # Rotim la stanga 90 de grade
        t.forward(size)  # Latura lunga a trunchiului
        t.left(90)  # Rotim la stanga din nou
    t.end_fill()  # Finalizam umplerea

    # Mutam Turtle la pozitia unde vor fi frunzele
    t.penup()  # Ridicam pixul pentru a nu desena
    t.left(90)  # Rotim Turtle la stanga
    t.forward(size)  # Mutam Turtle deasupra trunchiului
    t.right(90)  # Rotim Turtle la dreapta

    # Mutam Turtle mai sus si inainte pentru a centra frunzele
    t.forward(size * 0.1)  # Mutam Turtle usor inainte
    t.right(90)  # Rotim Turtle la dreapta
    t.forward(size * 0.25)  # Mutam Turtle sus pentru centru
    t.left(90)  # Rotim Turtle inapoi

    # Desenam frunzele (cercul deasupra trunchiului)
    t.pendown()  # Coboram pixul pentru a desena
    t.fillcolor("green")  # Setam culoarea de umplere pentru frunze
    t.begin_fill()  # Incepem umplerea
    t.circle(size * 0.5)  # Desenam cercul (frunzele)
    t.end_fill()  # Finalizam umplerea


# Functia pentru desenarea soarelui
def draw_sun(t, x, y, size) :
    """
    Deseneaza un soare la pozitia specificata, format dintr-un cerc si raze.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a pozitiei soarelui.
        y (int): Coordonata y a pozitiei soarelui.
        size (int): Dimensiunea soarelui (raza cercului).
    """
    # Mergem la pozitia specificata pentru soare
    t.penup()  # Ridicam pixul pentru a nu desena
    t.goto(x, y)  # Mutam Turtle la coordonatele specificate
    t.pendown()  # Coboram pixul pentru a desena

    # Desenam cercul pentru soare
    t.fillcolor("yellow")  # Setam culoarea de umplere pentru soare
    t.begin_fill()  # Incepem umplerea
    t.circle(size)  # Desenam cercul (soarele)
    t.end_fill()  # Finalizam umplerea

    # Desenam razele soarelui
    t.pencolor("yellow")  # Setam culoarea stiloului pentru raze
    t.penup()  # Ridicam pixul
    for _ in range(12) :  # Repetam pentru 12 raze
        t.goto(x, y + size)  # Pozitionam Turtle pentru raza
        t.pendown()  # Coboram pixul pentru a desena
        t.forward(size + 20)  # Desenam raza
        t.penup()  # Ridicam pixul inapoi
        t.goto(x, y)  # Revenim la centrul soarelui
        t.right(30)  # Rotim Turtle pentru urmatoarea raza

    # Resetam culoarea stiloului la negru (sau alta culoare dorita)
    t.pencolor("black")


# Functia pentru desenarea unui munte (triunghi mare)
def draw_mountain(t, x, y, size) :
    """
    Deseneaza un munte sub forma de triunghi la coordonatele specificate.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a bazei muntelui.
        y (int): Coordonata y a bazei muntelui.
        size (int): Dimensiunea laturii muntelui (triunghiului).
    """
    t.penup()  # Ridicam pixul
    t.goto(x, y)  # Mergem la pozitia specificata
    t.pendown()  # Coboram pixul pentru a desena

    # Desenam muntele ca un triunghi mare
    t.fillcolor("grey")  # Setam culoarea de umplere pentru munte
    t.begin_fill()  # Incepem umplerea
    for _ in range(3) :  # Repetam de 3 ori pentru triunghi
        t.forward(size)  # Desenam o latura a triunghiului
        t.left(120)  # Rotim Turtle pentru urmatoarea latura
    t.end_fill()  # Finalizam umplerea


# Functia pentru desenarea unui lac (oval)
def draw_lake(t, x, y, width, height) :
    """
    Deseneaza un lac sub forma de oval la coordonatele specificate.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a centrului lacului.
        y (int): Coordonata y a centrului lacului.
        width (int): Latimea lacului (raza mica).
        height (int): Inaltimea lacului (raza mare).
    """
    t.penup()  # Ridicam pixul
    t.goto(x, y)  # Mutam Turtle la pozitia specificata
    t.pendown()  # Coboram pixul pentru a desena
    t.fillcolor("blue")  # Setam culoarea de umplere pentru lac
    t.begin_fill()  # Incepem umplerea

    # Desenam ovalul prin combinarea cercurilor
    t.setheading(45)  # Setam unghiul pentru a incepe ovalul
    for _ in range(2) :  # Repetam de 2 ori pentru a desena ovalul
        t.circle(width, 90)  # Partea rotunda a ovalului
        t.circle(height, 90)  # Partea lunga a ovalului
    t.end_fill()  # Finalizam umplerea


# Functia pentru desenarea unui nor (format din cercuri suprapuse)
def draw_cloud(t, x, y, size) :
    """
    Deseneaza un nor format din cercuri suprapuse la pozitia specificata.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a norului.
        y (int): Coordonata y a norului.
        size (int): Dimensiunea de baza pentru nor.
    """
    t.penup()  # Ridicam pixul
    t.goto(x, y)  # Mergem la pozitia norului
    t.pendown()  # Coboram pixul pentru a desena

    # Setam culoarea norului
    t.fillcolor("white")

    # Desenam primul cerc al norului
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    # Desenam al doilea cerc usor in dreapta
    t.penup()
    t.goto(x + size * 0.7, y)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.8)
    t.end_fill()

    # Desenam al treilea cerc in stanga
    t.penup()
    t.goto(x - size * 0.7, y)
    t.pendown()
    t.begin_fill()
    t.circle(size * 0.6)
    t.end_fill()


# Functia pentru desenarea ierbii pe mai multe randuri
def draw_grass(t, start_x, start_y, width, height) :
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("green")

    for y_offset in range(0, height, 15) :  # Facem mai multe randuri de iarba
        for x_offset in range(0, width, 20) :
            t.penup()
            t.goto(start_x + x_offset, start_y + y_offset)
            t.pendown()

            # Fire de iarba de inaltimi variabile si unghiuri diferite
            grass_height = 10 + (x_offset % 5) * 2  # Inaltime variabila
            t.left(60 + (x_offset % 10) * 2)  # Unghiuri variabile
            t.forward(grass_height)
            t.backward(grass_height)
            t.right(120 + (x_offset % 10) * 2)
            t.forward(grass_height)
            t.backward(grass_height)
            t.left(60)  # Revenim la unghiul initial


# Functia pentru desenarea unei scene complete (o casa si un copac)
def draw_scene(t, x, y, house_size, tree_size) :
    """
    Deseneaza o scena completa cu o casa si un copac la pozitiile specificate.

    Args:
        t (Turtle): Obiectul Turtle care deseneaza.
        x (int): Coordonata x a bazei casei.
        y (int): Coordonata y a bazei casei.
        house_size (int): Dimensiunea casei.
        tree_size (int): Dimensiunea copacului.
    """
    # Desenam casa
    t.penup()  # Ridicam pixul
    t.goto(x, y)  # Mutam Turtle la pozitia specificata
    t.pendown()  # Coboram pixul pentru a desena
    draw_house(t, house_size)  # Desenam casa

    # Desenam copacul langa casa
    t.penup()  # Ridicam pixul
    t.goto(x + house_size + 30, y)  # Mutam Turtle pentru copac
    t.pendown()  # Coboram pixul pentru a desena
    draw_tree(t, tree_size)  # Desenam copacul
