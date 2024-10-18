
# Funcția pentru desenarea unui triunghi (munte)
def draw_triangle(t, size):
    """
    Desenează un triunghi echilateral.
    """
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Funcția pentru desenarea unui munte
def draw_mountain(t, size):
    """
    Desenează un munte (triunghi mare).
    """
    t.fillcolor("grey")
    draw_triangle(t, size)

# Funcția pentru desenarea unui copac
def draw_tree(t, size):
    """
    Desenează un copac simplu.
    """
    # Trunchiul copacului
    t.fillcolor("#8B4513")
    t.begin_fill()
    for _ in range(2):
        t.forward(size * 0.2)  # Lățimea trunchiului
        t.left(90)
        t.forward(size)  # Înălțimea trunchiului
        t.left(90)
    t.end_fill()

    # Frunzele copacului (un cerc deasupra trunchiului)
    t.left(90)
    t.forward(size)
    t.right(90)
    t.fillcolor("green")
    t.begin_fill()
    t.circle(size * 0.5)  # Desenăm frunzele ca un cerc
    t.end_fill()

# Funcția pentru desenarea unei case
def draw_house(t, size):
    """
    Desenează o casă cu un pătrat ca bază și un triunghi ca acoperiș.
    """
    # Baza casei (pătrat)
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()

    # Acoperișul (triunghi deasupra pătratului)
    t.fillcolor("brown")
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

# Funcția pentru desenarea unei persoane
def draw_person(t, size):
    """
    Desenează o persoană stilizată (cap, corp, brațe și picioare).
    """
    # Capul (cerc)
    t.penup()
    t.forward(size * 0.1)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(size * 0.1)
    t.end_fill()

    # Corpul (linie verticală)
    t.penup()
    t.goto(t.xcor(), t.ycor() - size * 0.2)
    t.pendown()
    t.forward(size * 0.5)

    # Brațele
    t.left(45)
    t.forward(size * 0.2)
    t.backward(size * 0.2)
    t.right(90)
    t.forward(size * 0.2)
    t.backward(size * 0.2)
    t.left(45)

    # Picioarele
    t.forward(size * 0.3)
    t.left(45)
    t.forward(size * 0.2)
    t.backward(size * 0.2)
    t.right(90)
    t.forward(size * 0.2)

# Funcția pentru multiplicarea peisajului
def draw_scene(t, x, y, size):
    """
    Desenează o scenă completă cu munte, copac, casă și persoană.
    """
    # Desenăm muntele
    t.penup()
    t.goto(x, y)
    t.pendown()
    draw_mountain(t, size)

    # Desenăm copacul
    t.penup()
    t.goto(x + size * 1.5, y - size * 0.3)
    t.pendown()
    draw_tree(t, size * 0.5)

    # Desenăm casa
    t.penup()
    t.goto(x + size * 0.5, y - size * 0.7)
    t.pendown()
    draw_house(t, size * 0.5)

    # Desenăm persoana
    t.penup()
    t.goto(x + size * 0.3, y - size * 1.5)
    t.pendown()
    draw_person(t, size * 0.5)