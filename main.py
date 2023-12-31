import turtle
import random
import pygame.mixer

pygame.mixer.init()

# Inisialisasi suara ketika makanan dimakan
eat_sound = pygame.mixer.Sound('eat.wav')

# Inisialisasi suara ketika permainan berakhir
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Atur warna latar belakang layar
turtle.bgcolor("black")

h = [0]  # Arah kepala ular (0: kanan, 90: atas, 180: kiri, 270: bawah)
a = [0]  # Skor pemain
b = [0]  # Panjang ular
fcoord = [0, 0, 0]  # Koordinat makanan
pos = []  # Posisi tubuh ular

def home(x, y):
    x = 0
    y = 0
    a[0] = 0
    b[0] = 0
    h[0] = 0
    fcoord[2] = 0
    pos[:] = []
    turtle.hideturtle()
    turtle.clear()
    turtle.pu()
    turtle.color("white")
    turtle.goto(0, 0)
    turtle.write("Play")
    turtle.title("Snake")
    turtle.onscreenclick(start)
    turtle.mainloop()

def level_1():
    # Menggambar batas layar permainan
    turtle.clear()
    turtle.pu()
    turtle.speed(0)
    turtle.pensize(10)
    turtle.color("grey")
    turtle.goto(-220, 220)
    turtle.pd()
    turtle.goto(220, 220)
    turtle.goto(220, -220)
    turtle.goto(-220, -220)
    turtle.goto(-220, 220)
    turtle.pu()
    turtle.goto(0, 0)

def start(x, y):
    # Inisialisasi permainan
    turtle.onscreenclick(None)
    level_1()
    tfood = turtle.Turtle()
    tfood.hideturtle()
    tfood.pu()
    tfood.speed(0)
    tfood.shape("square")
    tfood.color("red")
    tscore = turtle.Turtle()
    tscore.hideturtle()
    tscore.pu()
    tscore.speed(0)
    tscore.goto(100, -250)
    tscore.color("white")
    
    def update_score():
        # Mengupdate tampilan skor pemain
        tscore.clear()
        tscore.write("Score: " + str(a[0]), align="center", font=("Arial", 20, "normal"))

    update_score()
    
    while x > -210 and x < 210 and y > -210 and y < 210:
        if fcoord[2] == 0:
            food(tfood)
            fcoord[2] = 1
        turtle.onkey(u, "Up")
        turtle.onkey(l, "Left")
        turtle.onkey(r, "Right")
        turtle.onkey(d, "Down")
        turtle.listen()
        move()
        x = turtle.xcor()
        y = turtle.ycor()
        if x > fcoord[0] * 20 - 5 and x < fcoord[0] * 20 + 5 and y > fcoord[1] * 20 - 5 and y < fcoord[1] * 20 + 5:
            fcoord[2] = 0
            tfood.clear()
            a[0] += 1
            update_score()
            eat_sound.play()  # Memainkan suara ketika makanan dimakan
        
        if len(pos) > 1:
            for i in range(1, len(pos)):
                if x < pos[i][0] + 5 and x > pos[i][0] - 5 and y < pos[i][1] + 5 and y > pos[i][1] - 5:
                    tfood.clear()
                    gameover()  # Permainan berakhir jika bertabrakan dengan tubuh ular
    tfood.clear()
    gameover()

def food(tfood):
    x = random.randrange(-8, 8, 1)
    y = random.randrange(-8, 8, 1)
    fcoord[0] = x
    fcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape("square")
    tfood.color(random.choice(["red", "green", "blue", "orange", "purple"]))  # Pilih warna makanan secara acak
    tfood.goto(x * 20, y * 20)
    tfood.stamp()

def u():
    if h[0] == 270:
        pass
    else:
        h[0] = 90

def d():
    if h[0] == 90:
        pass
    else:
        h[0] = 270

def l():
    if h[0] == 0:
        pass
    else:
        h[0] = 180

def r():
    if h[0] == 180:
        pass
    else:
        h[0] = 0

def move():
    turtle.pensize(1)
    turtle.color("green")
    turtle.pu()
    turtle.speed(1)
    turtle.setheading(h[0])
    turtle.shape("circle")
    turtle.stamp()
    turtle.fd(20)
    x = turtle.xcor()
    y = turtle.ycor()
    if b[0] > a[0]:
        turtle.clearstamps(1)
        pos.insert(0, [round(x), round(y)])
        pos.pop(-1)
    else:
        pos.insert(0, [round(x), round(y)])
        b[0] += 1

def gameover():
    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.pu()
    turtle.goto(0, 150)
    turtle.color("red")
    turtle.write("Game Over", align="center", font=("Arial", 30, "bold"))
    turtle.goto(0, 50)
    turtle.write("Score: " + str(a[0]), align="center", font=("Arial", 20, "normal"))
    turtle.goto(0, -20)
    turtle.color("white")
    turtle.write("Click anywhere to return to the main menu", align="center", font=("Arial", 10, "normal"))
    game_over_sound.play()  # Memainkan suara ketika permainan berakhir
    turtle.onscreenclick(home)
    turtle.mainloop()

if __name__ == '__main__':
    home(0, 0)
