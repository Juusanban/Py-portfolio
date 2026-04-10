import tkinter as tk
import random
import math

WIDTH = 900
HEIGHT = 600
PARTICLES = 60
MAX_DIST = 120

root = tk.Tk()
root.title("Particles test")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

particles = []

class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

        # speed a bit higher
        self.vx = random.uniform(-1.8, 1.8)
        self.vy = random.uniform(-1.8, 1.8)

for _ in range(PARTICLES):
    particles.append(Particle())

mouse_x = 0
mouse_y = 0

def mouse_move(event):
    global mouse_x, mouse_y
    mouse_x = event.x
    mouse_y = event.y

canvas.bind("<Motion>", mouse_move)

def update():

    canvas.delete("all")

    for p in particles:

        p.x += p.vx
        p.y += p.vy

        if p.x < 0 or p.x > WIDTH:
            p.vx *= -1
        if p.y < 0 or p.y > HEIGHT:
            p.vy *= -1

        canvas.create_oval(p.x-2, p.y-2, p.x+2, p.y+2, fill="white", outline="")

    for i in range(len(particles)):
        for j in range(i+1, len(particles)):

            p1 = particles[i]
            p2 = particles[j]

            dx = p1.x - p2.x
            dy = p1.y - p2.y
            dist = math.sqrt(dx*dx + dy*dy)

            if dist < MAX_DIST:
                alpha = int(255 * (1 - dist / MAX_DIST))
                color = f"#{alpha:02x}{alpha:02x}{alpha:02x}"

                canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill=color)

    # cursor reaction
    for p in particles:

        dx = mouse_x - p.x
        dy = mouse_y - p.y
        dist = math.sqrt(dx*dx + dy*dy)

        if dist < 100:
            p.x -= dx * 0.01
            p.y -= dy * 0.01

    root.after(16, update)

update()
root.mainloop()