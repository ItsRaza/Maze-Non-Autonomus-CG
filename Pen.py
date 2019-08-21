import turtle


screen = turtle.Screen()
screen.bgcolor('black')
screen.title('Maze game')
screen.setup(600, 600)


levels = [""]

level1 = [
    "XXXXXXXXXXXXXXXXXXXX",
    "XPXXXX           XXX",
    "X   XX  XXXXXXX   XX",
    "X   XX  XXXXXXX  XXX",
    "XXX  X           XXX",
    "XXX       XXXXXXXXXX",
    "XXXXXXXX   XXXXXXXXX",
    "XXXXXXXXXX          ",
    "XXXXXXXXXXXXXXXXXXXX",
]
levels.append(level1)
walls = []


def setMaze(level):
    for row in range(len(level)):
        for col in range(len(level[row])):
            char = level[row][col]
            screen_x = -288+(col*24)
            screen_y = 288-(row*24)

            if char == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if char == 'P':
                player.goto(screen_x, screen_y)


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.speed(0)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 24

        if (x, y) not in walls:
            self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 24

        if (x, y) not in walls:
            self.goto(x, y)

    def left(self):
        x = self.xcor() - 24
        y = self.ycor()

        if (x, y) not in walls:
            self.goto(x, y)

    def right(self):
        x = self.xcor() + 24
        y = self.ycor()

        if (x, y) not in walls:
            self.goto(x, y)


if __name__ == "__main__":
    pen = Pen()

    player = Player()

    setMaze(levels[1])

    # keyboard binding

    turtle.onkey(player.up, "Up")
    turtle.onkey(player.down, "Down")
    turtle.onkey(player.left, "Left")
    turtle.onkey(player.right, "Right")
    turtle.listen()

    while True:
        screen.update()
