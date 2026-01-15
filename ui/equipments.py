import tkinter as tk
from tkcalendar import DateEntry


def show_equipment(content_frame, MAIN_BG):
    # Clear old page
    for widget in content_frame.winfo_children():
        widget.destroy()

    # ---------------- CARD BORDER ----------------
    card_border = tk.Frame(
        content_frame,
        bg="#B0B3D6",
        padx=2,
        pady=2
    )
    card_border.place(relx=0.5, rely=0.5, anchor="center")

    # ---------------- CARD BODY ----------------
    card = tk.Frame(
        card_border,
        bg="#E6E7F5",
        width=420,
        height=520
    )
    card.pack()
    card.pack_propagate(False)

    # ---------------- TITLE ----------------
    tk.Label(
        card,
        text="Equipment",
        bg="#E6E7F5",
        fg="#3A2D8F",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=15)

    # ---------------- FORM ----------------
    form = tk.Frame(card, bg="#E6E7F5")
    form.pack(padx=25, fill="both", expand=True)

    def field(label, widget):
        tk.Label(
            form,
            text=label,
            bg="#E6E7F5",
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(8, 2))
        widget.pack(fill="x")

    # ---------------- FIELDS ----------------
    entry_name = tk.Entry(form, font=("Segoe UI", 10))
    field("Equipment Name *", entry_name)

    txt_desc = tk.Text(form, height=4, font=("Segoe UI", 10))
    field("Description *", txt_desc)

    entry_muscles = tk.Entry(form, font=("Segoe UI", 10))
    field("Muscles Used *", entry_muscles)

    delivery_date = DateEntry(
        form,
        font=("Segoe UI", 10),
        date_pattern="yyyy-mm-dd"
    )
    field("Delivery Date *", delivery_date)

    entry_cost = tk.Entry(form, font=("Segoe UI", 10))
    field("Cost *", entry_cost)

    # ---------------- BUTTONS ----------------
    btn_frame = tk.Frame(card, bg="#E6E7F5")
    btn_frame.pack(pady=15)

    tk.Button(
        btn_frame,
        text="Save",
        bg="#3A2D8F",
        fg="white",
        width=10
    ).grid(row=0, column=0, padx=6)

    tk.Button(
        btn_frame,
        text="Reset",
        width=10
    ).grid(row=0, column=1, padx=6)

    tk.Button(
        btn_frame,
        text="View All Equipment",
        width=18
    ).grid(row=0, column=2, padx=6)
