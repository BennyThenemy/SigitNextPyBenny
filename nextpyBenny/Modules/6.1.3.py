import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
# create the image
img = ImageTk.PhotoImage(Image.open("pythonmaster.jpg").resize((200, 260)))
secret_image = tk.Label(image=img)


def button_clicked():
    secret_image.pack(side='bottom', anchor='s')


def main():
    window.title("The answer to everything")
    window.geometry("400x300")  # width x height

    # Create label
    label = tk.Label(window, text="Who is the almighty python master?")
    label.pack()

    # Create button
    button = tk.Button(window, text="Click for the answer", command=button_clicked)
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
