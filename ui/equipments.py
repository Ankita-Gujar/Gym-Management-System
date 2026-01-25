import tkinter as tk
from tkcalendar import Calendar
from PIL import Image, ImageTk   # pip install pillow

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

    # Header (Cancel Button)
    header = tk.Frame(cal_win, bg="white")
    header.pack(fill="x")

    cancel_btn = tk.Button(
        header,
        text="✕",
        font=("Segoe UI", 10, "bold"),
        bg="white",
        fg="red",
        bd=0,
        cursor="hand2",
        command=cal_win.destroy
    )
    cancel_btn.pack(side="right", padx=6, pady=4)

    # Calendar
    cal = Calendar(
        cal_win,
        date_pattern="yyyy-mm-dd",
        background="black",
        foreground="white",
        headersbackground="black",
        headersforeground="white",
        selectbackground="black"
    )
    cal.pack(padx=6, pady=6)

    def pick(event=None):
        entry.delete(0, tk.END)
        entry.insert(0, cal.get_date())
        cal_win.destroy()

    cal.bind("<<CalendarSelected>>", pick)


def date_entry(parent):
    # Border frame (entry style)
    outer = tk.Frame(
        parent,**ENTRY_STYLE,
        bg="#B0B0B0",
        padx=0,
        pady=0
    )
    outer.pack(fill="x")

    # Inner white area
    inner = tk.Frame(outer, bg="white")
    inner.pack(fill="both")

    entry = tk.Entry(
        inner,
        font=("Segoe UI", 10),
        relief="flat",
        bd=0
    )
    entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(6, 0))

    # Calendar image
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

    # Focus effect (blue border)
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

    field("Equipment Name *",
          tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE), 4)

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

    field("Muscles Used *",
          tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE), 4)

    tk.Label(
        form,
        text="Delivery Date *",
        bg=CARD_BG,
        font=("Segoe UI", 10)
    ).pack(anchor="w", pady=(6, 2))

    date_entry(form)

    field("Cost *",
          tk.Entry(form, font=("Segoe UI", 10), **ENTRY_STYLE), 4)

    btn_frame = tk.Frame(card, bg=CARD_BG)
    btn_frame.pack(pady=(8, 12))

    tk.Button(btn_frame, text="Save", width=10,
              bg="#3A2D8F", fg="white").grid(row=0, column=0, padx=6)

    tk.Button(btn_frame, text="Reset", width=10)\
        .grid(row=0, column=1, padx=6)

    tk.Button(btn_frame, text="View All Equipments", width=18)\
        .grid(row=0, column=2, padx=6)
