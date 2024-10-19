def print_hi(name) :
    import turtle

    # Funcția pentru desenarea unui pătrat (baza casei)
    def draw_square(t, size) :
        for _ in range(4) :
            t.forward(size)
            t.left(90)

    # Funcția pentru desenarea acoperișului (triunghi)
    def draw_triangle(t, size) :
        for _ in range(3) :
            t.forward(size)
            t.left(120)

    # Funcția pentru desenarea unei case (pătrat + acoperiș)
    def draw_house(t, size) :
        # Desenăm baza casei
        t.fillcolor("lightblue")
        t.begin_fill()
        draw_square(t, size)
        t.end_fill()

        # Mutăm Turtle deasupra casei pentru acoperiș
        t.left(90)
        t.forward(size)
        t.right(90)

        # Desenăm acoperișul casei (triunghi echilateral)
        t.fillcolor("brown")
        t.begin_fill()
        draw_triangle(t, size)
        t.end_fill()

    # Funcția pentru desenarea unui copac complet (trunchi + frunze)
    def draw_tree(t, size) :
        # Desenăm trunchiul copacului
        t.fillcolor("#8B4513")
        t.begin_fill()
        for _ in range(2) :
            t.forward(size * 0.2)
            t.left(90)
            t.forward(size)
            t.left(90)
        t.end_fill()

        # Ridicăm pixul pentru a muta Turtle fără a lăsa urme
        t.penup()

        # Mutăm Turtle la centrul cercului pentru a desena coroana
        t.left(90)
        t.forward(size)
        t.right(90)

        # Mutăm Turtle mai sus și înainte pentru a centra cercul
        t.forward(size * 0.1)
        t.right(90)
        t.forward(size * 0.25)

        # Coborâm pixul pentru a desena cercul
        t.left(90)
        t.pendown()

        # Desenăm frunzele (un cerc centrat deasupra trunchiului)
        t.fillcolor("green")
        t.begin_fill()
        t.circle(size * 0.5)
        t.end_fill()

    # Funcția pentru desenarea soarelui
    def draw_sun(t, x, y, size) :
        # Mergem la poziția specificată pentru soare
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Desenăm cercul pentru soare
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(size)
        t.end_fill()

        # Desenăm razele galbene
        t.pencolor("yellow")  # Setăm culoarea stiloului pentru raze
        t.penup()
        for _ in range(12) :  # 12 raze
            t.goto(x, y + size)
            t.pendown()
            t.forward(size + 20)  # Lungimea razelor
            t.penup()
            t.goto(x, y)
            t.right(30)  # Ne rotim pentru următoarea rază

        # Resetăm culoarea stiloului la negru sau altă culoare dorită (opțional)
        t.pencolor("black")

    # Funcția pentru desenarea unui munte (triunghi mare)
    def draw_mountain(t, x, y, size) :
        """
        Desenează un munte sub formă de triunghi la coordonatele specificate
        """
        t.penup()
        t.goto(x, y)
        t.pendown()

        # Desenăm muntele ca un triunghi mare
        t.fillcolor("grey")
        t.begin_fill()
        for _ in range(3) :
            t.forward(size)
            t.left(120)
        t.end_fill()

    # Funcția pentru desenarea unui lac (oval)
    def draw_lake(t, x, y, width, height) :
        """
        Desenează un lac sub formă de oval alungit la coordonatele (x, y)
        """
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor("blue")
        t.begin_fill()

        # Desenăm ovalul prin combinarea cercurilor
        t.setheading(45)  # Ne rotim pentru a începe ovalul
        for _ in range(2) :
            t.circle(width, 90)  # Partea rotundă
            t.circle(height, 90)  # Partea lungă
        t.end_fill()

    # Funcția pentru desenarea unui peisaj complet
    def draw_scene(t, x, y, house_size, tree_size) :
        """
        Desenează o scenă cu o casă și un copac la pozițiile specificate
        """
        # Desenăm casa
        t.penup()
        t.goto(x, y)
        t.pendown()
        draw_house(t, house_size)

        # Desenăm copacul lângă casă
        t.penup()
        t.goto(x + house_size + 30, y)  # Mai mult spațiu între casă și copac
        t.pendown()
        draw_tree(t, tree_size)

    # Setup pentru Turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)  # Setăm dimensiunile ferestrei
    screen.bgcolor("skyblue")
    t = turtle.Turtle()
    t.speed(0)  # Viteză maximă pentru desenare

    # Desenăm munții în fundal, la coordonate mai mari și centrate
    draw_mountain(t, -300, -50, 300)  # Primul munte
    draw_mountain(t, 0, -50, 300)  # Al doilea munte
    draw_mountain(t, 300, -50, 300)  # Al treilea munte

    # Desenăm soarele centrat la coordonatele (0, 150) cu dimensiunea de 50
    draw_sun(t, 0, 150, 50)

    # Centrarea caselor și copacilor pe ecran
    start_x = -150  # Începem de la -150 pentru a centra mai bine casele
    start_y = -150
    space_between = 200  # Spațiu egal între case și copaci
    for i in range(4) :
        draw_scene(t, start_x + i * space_between, start_y, 80, 100)

    # Desenăm un lac în stânga
    draw_lake(t, -400, -200, 100, 150)  # Lacul sub formă de oval

    # Finalizarea desenului
    turtle.done()


if __name__ == '__main__' :
    print_hi('PyCharm')
