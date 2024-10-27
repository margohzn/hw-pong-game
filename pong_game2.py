from tkinter import *
from tkinter import messagebox
import random
import time

window = Tk()
window.title("Horizontal Pong Game!")
window.resizable(0, 0)

canvas = Canvas(window, width=600, height=500, bg="black", bd=1, highlightthickness=1)
canvas.grid(row=1, column=1)
canvas.create_line(0, 250, 600, 250, fill="white")  # Middle line for horizontal layout
score_label = canvas.create_text(300, 30, font=("times", 40), text="0 : 0", fill="white")
window.update()

class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):
        self.canvas = canvas
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.color = color
        self.id = canvas.create_oval(10, 10, 30, 30, fill=self.color)
        self.canvas.move(self.id, 300, 250)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[2]
        self.score1 = 0
        self.score2 = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def draw_ball(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 4
            self.score2 += 1
            canvas.itemconfigure(score_label, text=str(self.score1) + " : " + str(self.score2))
        if pos[2] >= self.canvas_width:
            self.x = -4
            self.score1 += 1
            canvas.itemconfigure(score_label, text=str(self.score1) + " : " + str(self.score2))

        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4

        if self.hit_paddle1(pos):
            self.y = -4
        if self.hit_paddle2(pos):
            self.y = 4

    def hit_paddle1(self, pos):     
        paddle_pos = self.canvas.coords(self.paddle1.id)     # side 1 = top, side 3 = bottom, side 0 = left, side 2 = right
        if pos[0] >= paddle_pos[1] and pos[0] <= paddle_pos[3]:
            if pos[1] <= paddle_pos[0] and pos[3] >= paddle_pos[2]:
                return True
        return False

    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[0] >= paddle_pos[1] and pos[0] <= paddle_pos[3]:
            if pos[1] <= paddle_pos[0] and pos[3] >= paddle_pos[2]:
                return True
        return False


class Paddle1:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_rectangle(100, 10, 200, 25, fill=self.color)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("a", self.move_left)
        self.canvas.bind_all("d", self.move_right)

    def move_left(self, event):
        self.x = -4

    def move_right(self, event):
        self.x = 4

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


class Paddle2:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.id = self.canvas.create_rectangle(100, 475, 200, 490, fill=self.color)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def move_left(self, event):
        self.x = -4

    def move_right(self, event):
        self.x = 4

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

paddle1 = Paddle1(canvas, color = "pink")
paddle2 = Paddle2(canvas, color = "purple")
ball = Ball(canvas, paddle1, paddle2, "white")

while 1:
    if ball.score1 == 5 or ball.score2 == 5:
        messagebox.showinfo("Game Complete", "Score paddle 1 = " +str(ball.score1) + ", Score paddle 2 = " +str(ball.score2))
        break
       
    ball.draw_ball()
    paddle1.draw()
    paddle2.draw()
    time.sleep(0.1)
    window.update()


window.mainloop()