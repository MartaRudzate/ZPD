

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

root = tk.Tk()
root.title("drawing lines")
vscrollbar = tk.Scrollbar(root)

# create the drawing canvas
canvas = tk.Canvas(root, width=1300, height=999, bg='white',
                   yscrollcommand=vscrollbar.set)
canvas.pack()

vscrollbar.config(command=canvas.yview)
vscrollbar.pack(side=tk.LEFT, fill=tk.Y)

f = tk.Frame(canvas)  # Create the frame which will hold the widgets

canvas.pack(side="left", fill="both", expand=True)

# Updated the window creation
canvas.create_window(0, 0, window=f, anchor='nw')
n = 1
w = 3


y1 = 0
y2 = 30000
for k in range(0, 200, 100):
    x1 = k
    x2 = k
    canvas.create_line(x1, y1, x2, y2, width=n, fill="white")

lis = [[[0, 1], [2, 1.0], [3, -1.5], [4, 2.0], [5, -2.5], [6, 3.0], [7, -3.5], [8, 4.0], [9, -4.5], [10, 5.0], [11, -5.5], [12, 6.0], [13, -6.5], [14, 7.0], [15, -7.5], [16, 8.0], [17, -8.5], [18, 9.0], [19, -9.5], [20, 10.0], [21, -10.5], [22, 11.0], [23, -11.5], [24, 12.0], [25, -12.5], [26, 13.0], [27, -13.5], [28, 14.0], [29, -14.5], [30, 15.0], [31, -15.5], [32, 16.0], [0, 33], [34, -17.0], [35, 17.5], [36, -18.0], [37, 18.5], [38, -19.0], [39, 19.5],
        [40, -20.0], [41, 20.5], [42, -21.0], [43, 21.5], [44, -22.0], [45, 22.5], [46, -23.0], [47, 23.5], [48, -24.0], [49, 24.5], [50, -25.0], [51, 25.5], [52, -26.0], [0, -53], [-54, 27.0], [-55, -27.5], [-56, 28.0], [-57, -28.5], [-58, 29.0], [-59, -29.5], [-60, 30.0], [-61, -30.5], [-62, 31.0], [-63, -31.5], [-64, 32.0], [-65, -32.5], [-66, 33.0], [-67, -33.5], [-68, 34.0], [-69, -34.5], [-70, 35.0], [-71, -35.5], [-72, 36.0], [-73, -36.5], [-74, 37.0]]]

x1 = 500
y1 = 100
x2 = 500
y2 = 100

for a in lis:
    x1 = 500
    x2 = 500
    for p in a:
        if p[0] == 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2, width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
        elif p[0] == 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2, width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
        elif p[0] < 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2 - (p[0] * 10), width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
            y2 -= (p[0] * 10)
            y1 = y2
        elif p[0] > 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2 - (p[0] * 10), width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
            y2 -= (p[0] * 10)
            y1 = y2
        elif p[0] < 0 and p[1] < 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2 - (p[0] * 10), width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
            y2 -= (p[0] * 10)
            y1 = y2
        elif p[0] > 0 and p[1] > 0:
            canvas.create_line(
                x1, y1, x2 + (p[1] * 10), y2 - (p[0] * 10), width=n, fill="black")
            x2 += (p[1] * 10)
            x1 = x2
            y2 -= (p[0] * 10)
            y1 = y2
    y1 += 2000
    y2 = y1


root.update()
canvas.config(scrollregion=canvas.bbox("all"))


root.mainloop()
