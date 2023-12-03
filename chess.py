# a function that load a png file and returns it as a PhotoImage object
def load_image(filename):
    from PIL import Image, ImageTk
    image = Image.open(filename)
    return ImageTk.PhotoImage(image)


   

# a function that draws an 8x8 grid on a canvas using the tkinter module in python
TABLE_SIZE = 800
def chess():
    from tkinter import Tk, Canvas
    root = Tk()
    canvas = Canvas(root, width=TABLE_SIZE, height=TABLE_SIZE)
    canvas.pack()
    for i in range(0, TABLE_SIZE, TABLE_SIZE//8):
        for j in range(0, TABLE_SIZE, TABLE_SIZE//8):
            if (i+j) % (TABLE_SIZE//4) == 0:
                canvas.create_rectangle(i, j, i+TABLE_SIZE//8, j+TABLE_SIZE//8, fill="black")
    canvas.create_image(TABLE_SIZE//2, TABLE_SIZE//2, image= load_image("./sprites/pieces.png")) 
    root.mainloop()


 
chess()

img = load_image("./sprites/pieces.png")
print('hello world')