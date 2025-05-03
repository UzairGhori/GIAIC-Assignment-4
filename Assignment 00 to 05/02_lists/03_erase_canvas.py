
import tkinter as tk

Canvas_Width = 400
Canvas_Height = 400
Cell_Size = 40

def create_grid(canvas):
    cells = []
    for row in range(0, Canvas_Height, Cell_Size):
        row_cells = []
        for col in range(0, Canvas_Width, Cell_Size):
            rect = canvas.create_rectangle(
                col, row, col + Cell_Size, row + Cell_Size,
                fill="blue", outline="black"
            )
            row_cells.append(rect)
        cells.append(row_cells)
    return cells

def erase_canvas(event):
    x, y = event.x, event.y
    row = y // Cell_Size
    col = x // Cell_Size

    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        canvas.itemconfig(grid[row][col], fill="white")

def main():
    global canvas, grid

    root = tk.Tk()
    root.title("Grid Erase Canvas")

    canvas = tk.Canvas(root, width=Canvas_Width, height=Canvas_Height, bg="white")
    canvas.bind("<Button-1>", erase_canvas)  # ✅ Corrected "Button-1"
    canvas.pack()

    grid = create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()
