import tkinter as tk
import random

direction = "up"
cell_size = 100
cell_count = 10

def draw_cell(canvas, x, y, color):
    x1 = x
    y1 = y
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

def update(canvas, snake, fruit):
    coords = canvas.coords(snake)
    new_ycoord = 0
    new_xcoord = 0
    if direction == "up":
        new_xcoord = coords[0]
        new_ycoord = cell_size * cell_count - cell_size if coords[1] == 0 else coords[1] - cell_size    
    elif direction == "down":
        new_xcoord = coords[0]
        new_ycoord = 0 if coords[3] == cell_size * cell_count else coords[1] + cell_size
    elif direction == "left":
        new_ycoord = coords[1]
        new_xcoord = cell_size * cell_count - cell_size if coords[0] == 0 else coords[0] - cell_size
    elif direction == "right":
        new_ycoord = coords[1]
        new_xcoord = 0 if coords[0] == cell_size * cell_count - cell_size else coords[0] + cell_size

    canvas.coords(snake, new_xcoord, new_ycoord, new_xcoord + cell_size, new_ycoord + cell_size)

    canvas.after(300, lambda: update(canvas, snake, fruit))

def on_key_press(event):
    global direction
    if event.keysym == "d":
        direction = "right"
    elif event.keysym == "w":
        direction = "up"
    elif event.keysym == "s":
        direction = "down"
    elif event.keysym == "a":
        direction = "left"

def main():
    root = tk.Tk()
    root.title("It is a snake!")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=cell_size * cell_count, height=cell_size * cell_count, bg="pink")
    canvas.pack()

    snake = draw_cell(canvas, 300, 300, "green")

    fruit = draw_cell(canvas, random.randint(0, cell_count - 1) * cell_size, random.randint(0, cell_count - 1) * cell_size, "red")

    root.bind("<d>", on_key_press)
    root.bind("<w>", on_key_press)  
    root.bind("<s>", on_key_press)
    root.bind("<a>", on_key_press)

    update(canvas, snake, fruit)

    root.mainloop()


if __name__ == "__main__":
    main()