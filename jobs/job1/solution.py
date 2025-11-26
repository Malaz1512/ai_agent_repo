Here's a simple implementation of the snake game using Python's turtle module:

```Python
import turtle
import time
from threading import Thread

class SnakeGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.snake = turtle.Turtle()
        self.food = turtle.Turtle()
        self.pause = False
        self.score = 0
        self.highest_score = 0
        self.direction = "right"
        self.length = 1

    def start_game(self):
        self.window.setup(600, 400)
        self.snake.speed(0)
        self.food.speed(0)
        self.draw_snake()
        self.draw_food()
        self.window.onkey(self.turn_left, "w")
        self.window.onkey(self.turn_right, "s")
        self.window.onkey(self.turn_up, "a")
        self.window.onkey(self.turn_down, "d")
        self.window.listen()
        self.move_snake()

    def turn_left(self):
        if self.direction != "right":
            self.direction = "left"

    def turn_right(self):
        if self.direction != "left":
            self.direction = "right"

    def turn_up(self):
        if self.direction != "down":
            self.direction = "up"

    def turn_down(self):
        if self.direction != "up":
            self.direction = "down"

    def draw_snake(self):
        for i in range(self.length):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.penup()
            segment.goto(-i*20, 0)
            segment.pendown()
            if i == 0:
                segment.color("green")
            else:
                segment.color("black")

    def draw_food(self):
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(-100, -20)

    def move_snake(self):
        if not self.pause:
            if self.direction == "right":
                self.snake.setheading(0)
            elif self.direction == "left":
                self.snake.setheading(180)
            elif self.direction == "up":
                self.snake.setheading(90)
            elif self.direction == "down":
                self.snake.setheading(270)

            self.snake.forward(20)
            if self.snake.distance(self.food) < 10:
                self.score += 1
                self.length += 1
                self.draw_snake()
                self.food.goto(-100, -20)
            else:
                self.snake.penup()
                self.snake.goto(-self.length*20, 0)
                self.snake.pendown()

            if self.score > self.highest_score:
                self.highest_score = self.score

            self.window.title(f"Snake Game - Score: {self.score}, Highest Score: {self.highest_score}")
            self.window.ontimer(self.move_snake, 100)

    def pause_game(self):
        if not self.pause:
            self.pause = True
            self.window.listen()
        else:
            self.pause = False
            self.window.onkey(None, "p")

    def start_pause_thread(self):
        Thread(target=self.pause_game).start()

    def mainloop(self):
        while True:
            self.start_game()
            self.start_pause_thread()
            self.window.mainloop()
            if self.score == 0 and not self.pause:
                break

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
```

