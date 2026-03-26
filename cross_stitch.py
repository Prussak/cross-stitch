import tkinter as tk

CELL_SIZE = 30
ROWS = 15
COLS = 15

root = tk.Tk()
root.title("Cross Stitch Creator")

canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
canvas.pack()

# draw the grid
for i in range(ROWS):
    for j in range(COLS):
        x1 = j * CELL_SIZE
        y1 = i * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, outline="lightgray")

# function to draw the X
def draw_x(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE

    x1 = col * CELL_SIZE
    y1 = row * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE

    canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
    canvas.create_line(x1, y2, x2, y1, fill="black", width=2)

canvas.bind("<Button-1>", draw_x)

root.mainloop()
