import turtle

from src.solution import draw_mountain, draw_scene, draw_sun, draw_lake, draw_cloud, draw_grass


def run_setup() :
    """
    Functia principala care initializeaza ecranul si deseneaza peisajul complet
    cu munti, soare, case, copaci si un lac.

    """

    # Setup pentru Turtle
    screen = turtle.Screen()  # Cream o noua fereastra pentru desenare
    screen.setup(width=800, height=600)  # Setam dimensiunea ferestrei
    screen.bgcolor("skyblue")  # Setam culoarea de fundal
    t = turtle.Turtle()  # Cream un nou obiect Turtle pentru desen
    t.speed(0)  # Setam viteza de desenare la maxim

    # Desenam iarba la baza ecranului
    draw_grass(t, -400, -250, 800, 50)

    # Desenam muntii in fundal
    draw_mountain(t, -300, -50, 300)  # Primul munte
    draw_mountain(t, 0, -50, 300)  # Al doilea munte
    draw_mountain(t, 300, -50, 300)  # Al treilea munte

    # Desenam soarele
    draw_sun(t, 0, 150, 50)  # Soare in centru, sus

    # Desenam trei nori de dimensiuni diferite
    draw_cloud(t, -200, 200, 30)  # Primul nor mic
    draw_cloud(t, 100, 250, 50)  # Al doilea nor mare
    draw_cloud(t, 300, 200, 40)  # Al treilea nor mediu

    # Desenam scena completa cu casa si copac
    draw_scene(t, -300, -150, 100, 140)  # Prima casa si copac
    draw_scene(t, -50, -150, 80, 100)  # A doua casa si copac
    draw_scene(t, 200, -100, 60, 70)  # A treia casa si copac
    draw_scene(t, 350, -200, 40, 50)  # A patra casa si copac

    # Desenam un lac in partea stanga
    draw_lake(t, -400, -300, 100, 150)  # Lac in stanga

    # Finalizam desenul
    turtle.done()  # Inchidem fereastra Turtle la final


if __name__ == '__main__' :
    run_setup()  # Apelam functia principala daca rulam programul direct
