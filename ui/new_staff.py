import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
import re

from db.add_staff import add_staff
from ui.view_all_staff import open_view_all_staff

# ---------------- STYLES ----------------
ENTRY_STYLE = {
    "relief": "solid",
    "bd": 1,
    "highlightthickness": 1,
    "highlightbackground": "#B0B0B0",
    "highlightcolor": "#1E90FF"
}

BORDER_COLOR = "#B0B3D6"
CARD_BG = "#D9DBEE"
ENTRY_WIDTH = 20

# ---------------- STATE,CITY DATA ----------------
STATE_CITY_MAP = {
    "Maharashtra": [
        "Pune", "Mumbai", "Nagpur", "Nashik",
        "Kolhapur", "Satara", "Solapur", "Aurangabad",
        "Amravati", "Akola"
    ],
    "Gujarat": [
        "Ahmedabad", "Surat", "Vadodara", "Rajkot",
        "Bhavnagar", "Junagadh", "Gandhinagar"
    ],
    "Karnataka": [
        "Bengaluru", "Mysuru", "Mangaluru",
        "Hubli", "Belagavi", "Shivamogga"
    ],
    "Delhi": [
        "New Delhi", "Dwarka", "Rohini",
        "Saket", "Karol Bagh"
    ],
    "Rajasthan": [
        "Jaipur", "Udaipur", "Jodhpur",
        "Kota", "Ajmer", "Bikaner"
    ]
}

# ---------------- CALENDAR POPUP ----------------
def open_calendar_below(icon_btn, entry):
    cal_win = tk.Toplevel()
    cal_win.overrideredirect(True)
    cal_win.grab_set()

    x = icon_btn.winfo_rootx()
    y = icon_btn.winfo_rooty() + icon_btn.winfo_height()
    cal_win.geometry(f"+{x}+{y}")

    cal = Calendar(
        cal_win,
        date_pattern="yyyy-mm-dd",
        selectbackground="#3A2D8F",
        selectforeground="white"
    )
    cal.pack(padx=6, pady=6)

    def pick_date(event=None):
        entry.delete(0, tk.END)
        entry.insert(0, cal.get_date())
        cal_win.destroy()

    cal.bind("<<CalendarSelected>>", pick_date)

def date_entry_with_icon(parent, label_text):
    tk.Label(parent, text=label_text, bg=CARD_BG).pack(anchor="w")

    outer = tk.Frame(parent, **ENTRY_STYLE, bg="#B0B0B0")
    outer.pack(anchor="w", pady=(2, 14))

    inner = tk.Frame(outer, bg="white")
    inner.pack(fill="x")

    entry = tk.Entry(
        inner,
        width=ENTRY_WIDTH - 3,
        font=("Segoe UI", 12),
        relief="flat",
        bd=0
    )
    entry.pack(side="left", ipady=6, padx=(6, 0))

    img = Image.open("imgs/icons/calendar.png").resize((18, 18))
    cal_icon = ImageTk.PhotoImage(img)

    btn = tk.Button(
        inner,
        image=cal_icon,
        bg="white",
        bd=0,
        command=lambda: open_calendar_below(btn, entry)
    )
    btn.image = cal_icon
    btn.pack(side="right", padx=6)

    return entry

# ---------------- STAFF FORM ----------------
def show_staff(content_frame, MAIN_BG):

    for widget in content_frame.winfo_children():
        widget.destroy()

    card_border = tk.Frame(content_frame, bg=BORDER_COLOR, padx=2, pady=2)
    card_border.pack(pady=20)

    card = tk.Frame(card_border, bg=CARD_BG)
    card.pack()

    tk.Label(
        card,
        text="Add Staff",
        font=("Segoe UI", 18, "bold"),
        bg=CARD_BG,
        fg="#2F2F8F"
    ).pack(pady=10)

    form = tk.Frame(card, bg=CARD_BG)
    form.pack(padx=25, pady=10)

    # ---------- HELPERS ----------
    def label_entry(parent, text):
        tk.Label(parent, text=text, bg=CARD_BG).pack(anchor="w")
        entry = tk.Entry(
            parent,
            width=ENTRY_WIDTH,
            font=("Segoe UI", 12),
            **ENTRY_STYLE
        )
        entry.pack(anchor="w", pady=(2, 14), ipady=3)
        return entry

    def label_dropdown(parent, text, values, command=None):
        tk.Label(parent, text=text, bg=CARD_BG).pack(anchor="w")
        var = tk.StringVar(value=values[0])
        option = tk.OptionMenu(parent, var, *values, command=command)
        option.pack(anchor="w", fill="x", pady=(2, 14))
        return var, option

    # ---------- LEFT ----------
    left = tk.Frame(form, bg=CARD_BG)
    left.grid(row=0, column=0, padx=25, sticky="n")

    fname_entry = label_entry(left, "First Name *")

    tk.Label(left, text="Gender *", bg=CARD_BG).pack(anchor="w")
    gender = tk.StringVar(value="Male")
    tk.Radiobutton(left, text="Male", variable=gender, value="Male", bg=CARD_BG).pack(anchor="w")
    tk.Radiobutton(left, text="Female", variable=gender, value="Female", bg=CARD_BG).pack(anchor="w")

    email_entry = label_entry(left, "Email *")
    join_date_entry = date_entry_with_icon(left, "Join Date *")

    city_var, city_menu = label_dropdown(left, "City *", ["Select City"])

    # ---------- RIGHT ----------
    right = tk.Frame(form, bg=CARD_BG)
    right.grid(row=0, column=1, padx=25, sticky="n")

    lname_entry = label_entry(right, "Last Name *")
    dob_entry = date_entry_with_icon(right, "Date of Birth *")
    contact_entry = label_entry(right, "Contact No *")

    def update_city(selected_state):
        menu = city_menu["menu"]
        menu.delete(0, "end")
        city_var.set("Select City")

        if selected_state in STATE_CITY_MAP:
            for city in STATE_CITY_MAP[selected_state]:
                menu.add_command(
                    label=city,
                    command=lambda value=city: city_var.set(value)
                )

    state_var, _ = label_dropdown(
        right,
        "State *",
        ["Select State"] + list(STATE_CITY_MAP.keys()),
        command=update_city
    )

    # ---------- SAVE ----------
    def save_staff():
        fname = fname_entry.get().strip()
        lname = lname_entry.get().strip()
        email = email_entry.get().strip()
        contact = contact_entry.get().strip()
        dob = dob_entry.get().strip()
        join_date = join_date_entry.get().strip()

        if not fname.isalpha() or not lname.isalpha():
            messagebox.showerror("Error", "Name must contain only letters")
            return

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            messagebox.showerror("Error", "Invalid email format")
            return

        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Error", "Enter valid 10 digit contact number")
            return

        if dob == "" or join_date == "":
            messagebox.showerror("Error", "Please select dates")
            return

        if state_var.get().startswith("Select") or city_var.get().startswith("Select"):
            messagebox.showwarning("Warning", "Please select State and City")
            return

        data = (
            fname, lname, gender.get(), dob,
            email, contact, join_date,
            state_var.get(), city_var.get()
        )

        try:
            add_staff(data)
            messagebox.showinfo("Success", "Staff added successfully")
            reset_form()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # ---------- RESET ----------
    def reset_form():
        for e in [
            fname_entry, lname_entry, email_entry,
            contact_entry, dob_entry, join_date_entry
        ]:
            e.delete(0, tk.END)

        gender.set("Male")
        city_var.set("Select City")
        state_var.set("Select State")

    # ---------- BUTTONS ----------
    btn_frame = tk.Frame(card, bg=CARD_BG)
    btn_frame.pack(pady=12)

    tk.Button(
        btn_frame,
        text="Save",
        width=12,
        bg="#3A2D8F",
        fg="white",
        command=save_staff
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="Reset",
        width=12,
        command=reset_form
    ).grid(row=0, column=1, padx=10)

    tk.Button(
        btn_frame,
        text="View All Staff",
        width=18,
        command=open_view_all_staff
    ).grid(row=0, column=2, padx=10)
