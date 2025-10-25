import turtle
import time
import random

# === LIGHT FEMININE PINK THEME ===
# Color Palette: Soft Pink, Lavender, Rose, Gold, Purple
bg = turtle.Screen()
bg.setup(width=800, height=700)
bg.title("Happy Birthday Aya 💕")
bg.bgcolor("#2C0E18")  # lavender blush background

# Force window to foreground (macOS)
try:
    import os
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
except:
    pass

# Initial delay so window appears before drawing starts
time.sleep(1.5)

turtle.speed(0)  # fastest for main cake
turtle.hideturtle()  # hide from start

# === REALISTIC LAYERED CAKE - PINK LUXURY ===
turtle.pensize(2)

# Bottom cake layer (largest) - light purple
turtle.penup()
turtle.goto(-120,-100)
turtle.color("#DA70D6")  # orchid outline
turtle.fillcolor("#E6B0E6")  # light purple fill
turtle.begin_fill()
turtle.pendown()
for _ in range(2):
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

# Frosting border on bottom layer - hot pink
turtle.penup()
turtle.goto(-120,-50)
turtle.color("#FF1493")  # deep pink frosting
turtle.pensize(8)
turtle.pendown()
turtle.forward(240)

# Middle cake layer - rose pink
turtle.pensize(2)
turtle.penup()
turtle.goto(-100,-50)
turtle.color("#FF69B4")
turtle.fillcolor("#FFB6C1")  # light pink
turtle.begin_fill()
turtle.pendown()
for _ in range(2):
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

# Frosting border on middle layer - orchid
turtle.penup()
turtle.goto(-100,0)
turtle.color("#DA70D6")  # orchid frosting
turtle.pensize(8)
turtle.pendown()
turtle.forward(200)

# Top cake layer - pale pink
turtle.pensize(2)
turtle.penup()
turtle.goto(-80,0)
turtle.color("#FF69B4")
turtle.fillcolor("#FFC0CB")  # pink
turtle.begin_fill()
turtle.pendown()
for _ in range(2):
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

# Frosting border on top layer - hot pink
turtle.penup()
turtle.goto(-80,50)
turtle.color("#FF1493")
turtle.pensize(8)
turtle.pendown()
turtle.forward(160)

# Decorative dots on cake layers - pink and purple tones
turtle.pensize(1)
dot_colors = ["#FF69B4", "#FFB6C1", "#DDA0DD", "#FF1493"]
# Bottom layer dots
for x in range(-110, 110, 30):
    turtle.penup()
    turtle.goto(x, -75)
    turtle.dot(12, dot_colors[0])
# Middle layer dots
for x in range(-90, 90, 30):
    turtle.penup()
    turtle.goto(x, -25)
    turtle.dot(12, dot_colors[1])
# Top layer dots
for x in range(-70, 70, 30):
    turtle.penup()
    turtle.goto(x, 25)
    turtle.dot(12, dot_colors[2])

# === PRETTY CANDLES WITH FLAMES ===
candle_positions = [-60, -30, 0, 30, 60]
candle_colors = ["#FF69B4", "#DDA0DD", "#FFB6C1", "#FF1493", "#DA70D6"]  # pink/purple tones

for i, x_pos in enumerate(candle_positions):
    # Candle body (thicker) - pretty colors
    turtle.penup()
    turtle.goto(x_pos-3, 50)
    turtle.color("#FF1493")
    turtle.fillcolor(candle_colors[i])
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(0)
    for _ in range(2):
        turtle.forward(6)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
    turtle.end_fill()
    
    # Flame (teardrop shape) - orange/gold
    turtle.penup()
    turtle.goto(x_pos, 80)
    turtle.setheading(90)
    turtle.color("#FFA500")
    turtle.fillcolor("#FFD700")  # gold flame
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(5, 180)
    turtle.left(90)
    turtle.circle(5, 180)
    turtle.end_fill()

# === HEARTS AROUND THE CARD - BETTER POSITIONED ===
heart_positions = [(-220, 140), (220, 140), (-220, 60), (220, 60),
                   (-180, 220), (180, 220), (-150, -20), (150, -20)]

def draw_heart(size):
    turtle.fillcolor("#FF1493")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(size)
    turtle.circle(-size/2, 200)
    turtle.setheading(60)
    turtle.circle(-size/2, 200)
    turtle.forward(size)
    turtle.end_fill()

for pos in heart_positions:
    turtle.penup()
    turtle.goto(pos[0], pos[1])
    turtle.setheading(0)
    turtle.color("#FF69B4")
    draw_heart(20)

turtle.speed(12)

def draw_star(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

star_positions = [(-240, 180), (240, 180), (-240, 0), (240, 0),
                  (-120, 240), (120, 240), (0, 250)]
star_colors = ["#FFD700", "#FFB6C1", "#DDA0DD", "#FFD700", "#FF69B4", "#DDA0DD", "#FFD700"]

for i, pos in enumerate(star_positions):
    turtle.penup()
    turtle.goto(pos[0], pos[1])
    turtle.setheading(0)
    turtle.color(star_colors[i])
    draw_star(15, star_colors[i])

# for _ in range(30):
#     x = random.randint(-250, 250)
#     y = random.randint(-200, 250)
#     color = random.choice(["#FF69B4", "#FFB6C1", "#DDA0DD", "#FF1493", "#DA70D6", "#FFD700", "#FFC0CB"])
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.dot(random.randint(5, 10), color)

turtle.speed(0) 

turtle.penup()
turtle.goto(0, 165)
turtle.color("#FF1493") 
turtle.pendown()
turtle.write("Happy Birthday!", align="center", font=("Brush Script MT", 32, "bold"))


turtle.penup()
turtle.goto(0, 110)  
turtle.color("#DA70D6")  
turtle.pendown()
turtle.write("Queen Ayoya 👑", align="center", font=("Brush Script MT", 30, "bold"))

turtle.done()