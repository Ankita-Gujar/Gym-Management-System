import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk  
from db.add_equipments import add_equipment
from ui.view_all_equipment import open_view_all_equipment



ENTRY_STYLE = {
    "relief": "solid",
    "bd": 1,
    "highlightthickness": 1,
    "highlightbackground": "#B0B0B0",
    "highlightcolor": "#1E90FF"
}

BORDER_COLOR = "#B0B3D6"
CARD_BG = "#E6E7F5"


def open_calendar(icon_btn, entry):
    cal_win = tk.Toplevel()
    cal_win.overrideredirect(True)
    cal_win.grab_set()
    cal_win.configure(bg="white")

    x = icon_btn.winfo_rootx()
    y = icon_btn.winfo_rooty() + icon_btn.winfo_height()
    cal_win.geometry(f"+{x}+{y}")

    cal = Calendar(
        cal_win,
        selectmode="day",
        date_pattern="yyyy-mm-dd",
        selectbackground="#3A2D8F",
        selectforeground="white"
    )
    cal.pack(padx=6, pady=6)

    def pick(event=None):
        entry.delete(0, tk.END)
        entry.insert(0, cal.get_date())
        cal_win.destroy()

    cal.bind("<<CalendarSelected>>", pick)


def date_entry(parent):
    outer = tk.Frame(parent, **ENTRY_STYLE, bg="#B0B0B0")
    outer.pack(fill="x")

    inner = tk.Frame(outer, bg="white")
    inner.pack(fill="both")

    entry = tk.Entry(
        inner,
        font=("Segoe UI", 10),
        relief="flat",
        bd=0
    )
    entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(6, 0))

    img = Image.open("imgs/icons/calendar.png")
    img = img.resize((18, 18))
    calendar_icon = ImageTk.PhotoImage(img)

    btn = tk.Button(
        inner,
        image=calendar_icon,
        bg="white",
        bd=0,
        cursor="hand2",
        command=lambda: open_calendar(btn, entry)
    )
    btn.image = calendar_icon
    btn.pack(side="right", padx=6)

    def on_focus_in(e):
        outer.config(bg="#1E90FF")

    def on_focus_out(e):
        outer.config(bg="#B0B0B0")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

    return entry


def show_equipment(content_frame, MAIN_BG):

    for w in content_frame.winfo_children():
        w.destroy()

    card_border = tk.Frame(content_frame, bg=BORDER_COLOR, padx=2, pady=2)
    card_border.place(relx=0.5, rely=0.5, anchor="center")

    card = tk.Frame(card_border, bg=CARD_BG, width=450, height=500)
    card.pack()
    card.pack_propagate(False)

    tk.Label(
        card,
        text="Equipment",
        font=("Segoe UI", 18, "bold"),
        bg=CARD_BG,
        fg="#2F2F8F"
    ).pack(pady=(12, 8))

    form = tk.Frame(card, bg=CARD_BG)
    form.pack(padx=30, pady=(5, 0), fill="both", expand=True)

    def field(label, widget, ipady=0):
        tk.Label(
            form,
            text=label,
            bg=CARD_BG,
            font=("Segoe UI", 10)
        ).pack(anchor="w", pady=(6, 2))
        widget.pack(fill="x", ipady=ipady)

    equip_name_entry = tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE)
    field("Equipment Name *", equip_name_entry, 4)

    txt_desc = tk.Text(
        form,
        height=4,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground="#B0B0B0",
        highlightcolor="#1E90FF"
    )
    field("Description *", txt_desc)

    muscle_entry = tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE)
    field("Muscles Used *", muscle_entry, 4)

    tk.Label(
        form,
        text="Delivery Date *",
        bg=CARD_BG,
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(6, 2))

    date_ent = date_entry(form)

    cost_entry = tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE)
    field("Cost *", cost_entry, 4)

    def validate_and_save():
        if not equip_name_entry.get().strip():
            messagebox.showerror("Validation Error", "Equipment Name is required")
            return

        if not txt_desc.get("1.0", tk.END).strip():
            messagebox.showerror("Validation Error", "Description is required")
            return

        if not muscle_entry.get().strip():
            messagebox.showerror("Validation Error", "Muscles Used is required")
            return

        if not date_ent.get().strip():
            messagebox.showerror("Validation Error", "Delivery Date is required")
            return

        cost = cost_entry.get().strip()
        if not cost.isdigit():
            messagebox.showerror("Validation Error", "Cost must be numeric")
            return

        data = (
            equip_name_entry.get().strip(),
            txt_desc.get("1.0", tk.END).strip(),
            muscle_entry.get().strip(),
            date_ent.get().strip(),
            int(cost)
        )

        try:
            add_equipment(data)
            messagebox.showinfo("Success", "Equipment saved successfully!")

            # reset form
            equip_name_entry.delete(0, tk.END)
            txt_desc.delete("1.0", tk.END)
            muscle_entry.delete(0, tk.END)
            date_ent.delete(0, tk.END)
            cost_entry.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    btn_frame = tk.Frame(card, bg=CARD_BG)
    btn_frame.pack(pady=(8, 12))

    tk.Button(
        btn_frame,
        text="Save",
        width=10,
        bg="#3A2D8F",
        fg="white",
        command=validate_and_save
    ).grid(row=0, column=0, padx=6)

    tk.Button(btn_frame, text="Reset", width=10)\
        .grid(row=0, column=1, padx=6)

    tk.Button(
    btn_frame,
    text="View All Equipments",
    width=18,
    command=open_view_all_equipment
    ).grid(row=0, column=2, padx=6)


