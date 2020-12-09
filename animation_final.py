import importlib
import time
import turtle as tt
import sys

def utkani():
    importlib.reload(tt) # reload libraries in order to work in main program
    # create window to play animation in
    window = tt.Screen()
    window.title("Střet rytířů")
    window.setup(width=1900, height=300)
    window.bgcolor("#bebebe")
    window.reset()

    # variables for pictures
    ryt1 = r"C:\Users\pvesely\Coding\Knight_game\rytir1.gif"
    ryt2 = r"C:\Users\pvesely\Coding\Knight_game\rytir2.gif"
    ryt3 = r"C:\Users\pvesely\Coding\Knight_game\rytir3.gif"

    ryt11 = r"C:\Users\pvesely\Coding\Knight_game\ryt11.gif"
    ryt22 = r"C:\Users\pvesely\Coding\Knight_game\ryt22.gif"
    ryt33 = r"C:\Users\pvesely\Coding\Knight_game\ryt33.gif"

    exploze = (r"C:\Users\pvesely\Coding\Knight_game\jinaexploze-0.gif")
    exploze1 = (r"C:\Users\pvesely\Coding\Knight_game\jinaexploze-1.gif")
    exploze2 = (r"C:\Users\pvesely\Coding\Knight_game\jinaexploze-2.gif")
    exploze3 = (r"C:\Users\pvesely\Coding\Knight_game\jinaexploze-3.gif")

    #registering pictures
    window.register_shape(ryt1)
    window.register_shape(ryt2)
    window.register_shape(ryt3)

    window.register_shape(ryt11)
    window.register_shape(ryt22)
    window.register_shape(ryt33)

    window.register_shape(exploze)
    window.register_shape(exploze1)
    window.register_shape(exploze2)
    window.register_shape(exploze3)

    # classes for knights, two because of mirrored images 
    class Rytir(tt.Turtle):

        def __init__(self):
            tt.Turtle.__init__(self)
            self.penup()
            self.shape(ryt1)
            self.frame = 0
            self.frames = [ryt1, ryt2, ryt3]
            self.casovac = 0

        # the animation function
        def animate(self):
            print("duc duc")
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0
            self.shape(self.frames[self.frame])
            self.casovac += 1
            if self.casovac < 32:
                window.ontimer(self.animate, 60)

    class Rytir2(tt.Turtle):

        def __init__(self):
            tt.Turtle.__init__(self)
            self.penup()
            self.shape(ryt11)
            self.frame = 0
            self.frames = [ryt11, ryt22, ryt33]
            self.casovac = 0

        def animate(self):
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0
            self.shape(self.frames[self.frame])
            self.casovac += 1
            if self.casovac < 32:
                window.ontimer(self.animate, 60)

    vybuchy = [exploze, exploze1, exploze2, exploze3]

    # move knights apart
    rytir1 = Rytir()
    rytir1.setpos(800, 0)

    rytir2 = Rytir2()
    rytir2.setpos(-800, 0)

    faceoff = False

    # knights running
    rytir1.animate()
    rytir2.animate()

    #knights coming towards each other
    for i in range(69):
        rytir1.forward(-10)
        rytir2.forward(10)
        if i == 68:  # when the knights are close -> explosion
            vybuch = tt.Turtle()
            for i in vybuchy:
                vybuch.shape(i)
                time.sleep(0.1)
            faceoff = True

    window.bye() # close window
