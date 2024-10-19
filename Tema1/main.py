import turtle

from src.solution import draw_mountain, draw_scene, draw_sun, draw_lake, draw_cloud, draw_grass


def run_setup() :
    """
    Functia principala care initializeaza ecranul si deseneaza peisajul complet
    cu munti, soare, case, copaci si un lac.
    """

    # Setup pentru Turtle
    screen = turtle.Screen()  # Cream o noua fereastra pentru desenare
    screen.setup(width=800, height=600)  # Setam dimensiunea ferestrei la 800x600 pixeli
    screen.bgcolor("skyblue")  # Setam culoarea de fundal a ferestrei la albastru deschis (cer)
    t = turtle.Turtle()  # Cream un nou obiect Turtle pentru desenare
    t.speed(0)  # Setam viteza de desenare la maxim (cea mai rapida)

    # Desenam un plan de iarba (un dreptunghi verde) la baza ecranului
    draw_grass(t, -400, -250, 800, 100)  # Iarba va acoperi partea de jos a ecranului (un dreptunghi verde)

    # Desenam muntii in fundal
    draw_mountain(t, -300, -50, 300)  # Primul munte (mare) in stanga
    draw_mountain(t, 0, -50, 300)  # Al doilea munte (central)
    draw_mountain(t, 300, -50, 300)  # Al treilea munte (dreapta)

    # Desenam soarele
    draw_sun(t, 0, 150, 50)  # Soare in centru, sus, de dimensiune medie

    # Desenam trei nori de dimensiuni diferite in diverse pozitii
    draw_cloud(t, -200, 200, 30)  # Primul nor (mic) in stanga
    draw_cloud(t, 100, 250, 50)  # Al doilea nor (mare) in centru
    draw_cloud(t, 300, 200, 40)  # Al treilea nor (mediu) in dreapta

    # Desenam cate o scena completa cu o casa si un copac in diverse pozitii
    draw_scene(t, -300, -150, 100, 140)  # Prima casa (mare) si copac, in stanga
    draw_scene(t, -50, -150, 80, 100)  # A doua casa (medie) si copac, in centru
    draw_scene(t, 200, -100, 60, 70)  # A treia casa (mica) si copac, in dreapta
    draw_scene(t, 350, -200, 40, 50)  # A patra casa (foarte mica) si copac, mai jos in dreapta

    # Desenam un lac in partea stanga a ecranului
    draw_lake(t, -400, -300, 100, 150)  # Lacul va fi oval si va fi in partea de jos stanga

    # Finalizam desenul
    turtle.done()  # Inchidem fereastra Turtle dupa ce desenul este complet


if __name__ == '__main__' :
    run_setup()  # Apelam functia principala
