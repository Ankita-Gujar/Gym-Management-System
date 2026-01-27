import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

# ---------------- FUNCTIONS ----------------
def login_button():
    user = username_entry.get().strip()
    pwd = password_entry.get().strip()

    if user == "" or pwd == "":
        messagebox.showerror("Error", "Username and Password required")
    elif user == "admin" and pwd == "123":
        root.destroy()
        import ui.dashboard_ui
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        eye_btn.config(image=eye_open)
    else:
        password_entry.config(show="*")
        eye_btn.config(image=eye_close)

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Gym Management - Login")
root.geometry("1280x700")
root.configure(bg="white")
root.resizable(True,True )

CARD_BG = "#D9DBEE"
PRIMARY = "#2F1C8F"

# ---------------- LOAD ICONS ----------------
user_icon = ImageTk.PhotoImage(Image.open("imgs/user.png").resize((20, 20)))
key_icon = ImageTk.PhotoImage(Image.open("imgs/key.png").resize((20, 20)))
eye_open = ImageTk.PhotoImage(Image.open("imgs/eye.png").resize((20, 20)))
eye_close = ImageTk.PhotoImage(Image.open("imgs/invisible.png").resize((20, 20)))

# ---------------- CARD ----------------
card = tk.Frame(root, bg=CARD_BG, width=420, height=420)
card.place(x=180, y=160)
card.pack_propagate(False)

tk.Label(
    card,
    text="Sign in",
    bg=CARD_BG,
    fg=PRIMARY,
    font=("Poppins", 20, "bold")
).pack(pady=25)

# ---------------- USERNAME FIELD ----------------
tk.Label(card, text="Username*", bg=CARD_BG).pack(anchor="w", padx=50)

user_frame = tk.Frame(card, bg="white", bd=1, relief="solid")
user_frame.pack(padx=50, fill="x", ipady=6, pady=5)

tk.Label(user_frame, image=user_icon, bg="white").pack(side="left", padx=8)
username_entry = tk.Entry(user_frame, bd=0, font=("Poppins", 11))
username_entry.pack(side="left", fill="x", expand=True)

# ---------------- PASSWORD FIELD ----------------
tk.Label(card, text="Password*", bg=CARD_BG).pack(anchor="w", padx=50, pady=(10, 0))

pwd_frame = tk.Frame(card, bg="white", bd=1, relief="solid")
pwd_frame.pack(padx=50, fill="x", ipady=6, pady=5)

# Key icon
tk.Label(pwd_frame, image=key_icon, bg="white").pack(side="left", padx=8)

password_entry = tk.Entry(pwd_frame, bd=0, show="*", font=("Poppins", 11))
password_entry.pack(side="left", fill="x", expand=True)

# Eye button
eye_btn = tk.Button(
    pwd_frame,
    image=eye_close,
    bd=0,
    bg="white",
    cursor="hand2",
    command=toggle_password
)
eye_btn.pack(side="right", padx=8)

# ---------------- LOGIN BUTTON ----------------
tk.Button(
    card,
    text="Login",
    bg=PRIMARY,
    fg="white",
    font=("Poppins", 12,"bold"),
    bd=0,
    height=2,
    cursor="hand2",
    command=login_button
).pack(padx=50, pady=30, fill="x")

# ---------------- RIGHT LOGO IMAGE ----------------
try:
    img = Image.open("imgs/logo.png")
    img = img.resize((500, 500))
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(root, image=logo, bg="white")
    logo_label.image = logo
    logo_label.place(x=700, y=100)
except:
    pass

root.mainloop()
