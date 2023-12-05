from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha


def verify():
    global RANDOM
    x = t1.get("1.0", END).strip()
    if x.isdigit() and int(x) == int(RANDOM):
        messagebox.showinfo("Success", "verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()



def refresh():
    global RANDOM, data, photo
    t1.delete("1.0", END)
    RANDOM = str(randint(100000, 999999))
    data = image.generate(str(RANDOM))
    assert isinstance(data, BytesIO)
    image.write(str(RANDOM), 'out.png')
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.update()
    t1.config()


root = Tk()
root.title("CAPTCHA Generator and Verification")

root.configure(bg="#f0f0f0")
root.geometry("300x250")

image = ImageCaptcha()

RANDOM = str(randint(100000, 999999))
data = image.generate(str(RANDOM))
assert isinstance(data, BytesIO)
image.write(str(RANDOM), 'out.png')

photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=1, width=20, borderwidth=2, relief="solid")
b1 = Button(root, text="submit", command=verify, bg="#83A2FF", fg="white", relief="raised")
b2 = Button(root, text="refresh", command=refresh, bg="#C683D7", fg="white", relief="raised")

l1.pack(pady=10)
t1.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)
root.mainloop()
