import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("cornsilk")
drawing_board.title("Python Turtle Game")
FONT = ("Verdana", 24, "normal")
score = 0
game_over = False

# turtle list
turtle_list = []

# score turtle
score_turtle = turtle.Turtle()

# countdown turtle
countdown_turtle = turtle.Turtle()

def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("green")
    score_turtle.penup()

    top_height = drawing_board.window_height() /2
    y = top_height * 0.8

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, font=FONT, align="center")

grid_size = 10

# Make many turtles
def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, font=FONT, align="center")

        #print(x,y)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x * grid_size,y * grid_size)
    turtle_list.append(t)           # bu şekilde her bir oluşturulan turtle ı bir dizide saklıyoruz böylece bütün turtle lara çok kolay ulaşabiliriz


x_coordinates = [-20,-10,0,10,20]
y_coordinates = [20,10,0,-10]

def setup_place_turtles():


    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

# recursive function      içinde kendisini çağırmak
def show_turtles_randomly():        # bu fonksiyon her çalıştığında ontimer bir daha çalışacak böylece verilen zamanda yer değişmiş olacak
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_board.ontimer(show_turtles_randomly, 500)



def countdown(time):
    global game_over

    countdown_turtle.hideturtle()
    countdown_turtle.color("DarkOliveGreen4")
    countdown_turtle.penup()

    top_height = drawing_board.window_height() / 2
    y = top_height * 0.9

    countdown_turtle.setposition(0,  y -90)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, font=FONT, align="center")
        drawing_board.ontimer(lambda: countdown(time -1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game over", move=False, font=FONT, align="center")


def start_game_up():
    turtle.tracer(0)            #direkt gelir animasyonlar sıfırlanır,  takip etmeyi burakıyoruz
    setup_score_turtle()
    setup_place_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1)            # bununla birlikte takip etmeyi başlatıyoruz


start_game_up()
turtle.mainloop()

















turtle.mainloop()