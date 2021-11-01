import turtle as t
import random
import colorgram

# Extract colors from out image and clean all data with don't need


def clean_colors():
    dirty_colors = colorgram.extract('image.jpg', 10)
    colors = []
    for i in range(len(dirty_colors)):
        rgb = dirty_colors[i].rgb
        colors.append((rgb.r, rgb.g, rgb.b))
    return colors


def create_paint(tim, colors):
    # Put tim in a good position
    tim.setheading(230)
    tim.forward(300)
    tim.setheading(0)
    dots = 100

    # Let's make some art 🎨
    for dot in range(1, dots + 1):
        tim.dot(20, random.choice(colors))
        tim.forward(50)

        # Put Tim in the starting line
        if dot % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


if __name__ == '__main__':
    tim = t.Turtle()
    tim.speed("fastest")
    t.bgcolor("#c9c9c9")
    t.colormode(255)
    tim.penup()
    tim.hideturtle()
    colors = clean_colors()
    create_paint(tim, colors)

    screen = t.Screen()
    screen.exitonclick()
