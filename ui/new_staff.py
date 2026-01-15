import tkinter as tk

ENTRY_STYLE = {
    "relief": "solid",
    "bd": 1,
    "highlightthickness": 1,
    "highlightbackground": "#B0B0B0",
    "highlightcolor": "#1E90FF"
}

BORDER_COLOR = "#B0B3D6"
CARD_BG = "#D9DBEE"

ENTRY_WIDTH = 30
TEXT_WIDTH = 22


def show_staff(content_frame, MAIN_BG):

    for widget in content_frame.winfo_children():
        widget.destroy()

    # -------- CARD BORDER --------
    card_border = tk.Frame(content_frame, bg=BORDER_COLOR, padx=2, pady=2)
    card_border.pack(pady=20)

    # -------- CARD BODY --------
    card = tk.Frame(card_border, bg=CARD_BG)
    card.pack()

    # -------- TITLE --------
    tk.Label(
        card,
        text="Add Staff",
        font=("Segoe UI", 18, "bold"),
        bg=CARD_BG,
        fg="#2F2F8F"
    ).pack(pady=15)

    # -------- FORM --------
    form_frame = tk.Frame(card, bg=CARD_BG)
    form_frame.pack(padx=30, pady=10)

    def label_entry(parent, text):
        tk.Label(parent, text=text, bg=CARD_BG).pack(anchor="w")
        tk.Entry(parent, width=ENTRY_WIDTH, **ENTRY_STYLE)\
            .pack(anchor="w", pady=(2, 10))

    def label_dropdown(parent, text, values):
        tk.Label(parent, text=text, bg=CARD_BG).pack(anchor="w")
        var = tk.StringVar(value=values[0])
        tk.OptionMenu(parent, var, *values)\
            .pack(anchor="w", fill="x", pady=(2, 10))

    # -------- LEFT --------
    left = tk.Frame(form_frame, bg=CARD_BG)
    left.grid(row=0, column=0, padx=25, sticky="n")

    label_entry(left, "First Name *")

    tk.Label(left, text="Gender *", bg=CARD_BG).pack(anchor="w")
    gender = tk.StringVar(value="Male")
    tk.Radiobutton(left, text="Male", variable=gender, value="Male", bg=CARD_BG).pack(anchor="w")
    tk.Radiobutton(left, text="Female", variable=gender, value="Female", bg=CARD_BG)\
        .pack(anchor="w", pady=(0, 10))

    label_entry(left, "Email *")
    label_entry(left, "Join Date *")
    label_dropdown(left, "City *", ["Select City", "Pune", "Mumbai", "Nagpur"])


    # -------- RIGHT --------
    right = tk.Frame(form_frame, bg=CARD_BG)
    right.grid(row=0, column=1, padx=25, sticky="n")

    label_entry(right, "Last Name *")
    label_entry(right, "Date of Birth *")
    label_entry(right, "Contact No. *")

    label_dropdown(right, "State *", ["Select State", "Maharashtra", "Gujarat", "Karnataka"])
    
    # -------- BUTTONS --------
    btns = tk.Frame(card, bg=CARD_BG)
    btns.pack(pady=20)

    tk.Button(
        btns,
        text="Save",
        width=10,
        bg="#3A2D8F",
        fg="white"
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btns,
        text="Reset",
        width=10
    ).grid(row=0, column=1, padx=10)

    tk.Button(
        btns,
        text="View All Staff",
        width=16
    ).grid(row=0, column=2, padx=10)
