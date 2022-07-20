from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.x_start = 0
        self.y_start = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def reset_snake(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("red")

    def add_segment(self, position):
        body = Turtle("square")
        body.penup()
        body.color("white")
        body.goto(position)
        self.segments.append(body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Movement
        for num in range(len(self.segments) - 1, 0, -1):
            # Get the position of the segment 1 (Head) and then tell the segment 2 to go there and segment 3 follows up
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement key
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
