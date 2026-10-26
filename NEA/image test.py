import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry('500x500')
root.resizable(False, False)
root.title('Image Test')

image = Image.open(r"C:\Users\ben\JetBrains\PycharmProjects\NEA\img\folder.png")
image = image.resize((10, 10))
image1 = ImageTk.PhotoImage(image)
file_explorer = tkinter.Button(root, image=image1, command=lambda: print("woo"))
file_explorer.pack()

root.mainloop()