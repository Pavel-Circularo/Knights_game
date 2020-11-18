
import turtle as tt
import time

#create window to play animation in
window = tt.Screen()
window.title("Střet rytířů")
window.setup(width=1900, height=300)
window.bgcolor("#bebebe")

#variables for picture location
ryt1 = r"C:\Users\pvesely\Coding\Knight_game\rytir1.gif"
ryt2 = r"C:\Users\pvesely\Coding\Knight_game\rytir2.gif"
ryt3 = r"C:\Users\pvesely\Coding\Knight_game\rytir3.gif"

ryt11 = r"C:\Users\pvesely\Coding\Knight_game\ryt11.gif"
ryt22 = r"C:\Users\pvesely\Coding\Knight_game\ryt22.gif"
ryt33 = r"C:\Users\pvesely\Coding\Knight_game\ryt33.gif"

#registering pictures
window.register_shape(ryt1)
window.register_shape(ryt2)
window.register_shape(ryt3)
window.register_shape(ryt11)
window.register_shape(ryt22)
window.register_shape(ryt33)

class Rytir(tt.Turtle):

    def __init__(self):
        tt.Turtle.__init__(self)
        self.penup()
        self.shape(ryt1)
        self.frame = 0
        self.frames = [ryt1, ryt2, ryt3]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])
        # Set timer
        window.ontimer(self.animate, 60)

class Rytir2(tt.Turtle):

    def __init__(self):
        tt.Turtle.__init__(self)
        self.penup()
        self.shape(ryt11)
        self.frame = 0
        self.frames = [ryt11, ryt22, ryt33]

    def animate(self):
        self.frame += 1
        if self.frame >= len(self.frames):
            self.frame = 0
        self.shape(self.frames[self.frame])
        # Set timer
        window.ontimer(self.animate, 60)

rytir1 = Rytir()
rytir1.setpos(800, 0)

rytir2 = Rytir2()
rytir2.setpos(-800, 0)

rytir1.animate()
rytir2.animate()

for i in range(133):
    rytir1.forward(-5)
    rytir2.forward(5)

while True:
    window.update()
    print("main loop")
