import tkinter as tk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from db.member_insert import insert_member
from ui.view_all_members import open_view_all_members
from tkinter import messagebox
import re

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
TEXT_WIDTH = 22


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
        selectmode="day",
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


# ---------------- DATE ENTRY + ICON ----------------
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

    img = Image.open("imgs/icons/calendar.png")
    img = img.resize((18, 18))
    cal_icon = ImageTk.PhotoImage(img)

    btn = tk.Button(
        inner,
        image=cal_icon,
        bg="white",
        bd=0,
        cursor="hand2",
        command=lambda: open_calendar_below(btn, entry)
    )
    btn.image = cal_icon
    btn.pack(side="right", padx=6)

    return entry


# ---------------- MAIN FORM ----------------
def show_member(content_frame, MAIN_BG):

    for w in content_frame.winfo_children():
        w.destroy()

    card_border = tk.Frame(content_frame, bg=BORDER_COLOR, padx=2, pady=2)
    card_border.pack(pady=20)

    card = tk.Frame(card_border, bg=CARD_BG)
    card.pack()

    tk.Label(
        card,
        text="Add Member",
        font=("Segoe UI", 18, "bold"),
        bg=CARD_BG,
        fg="#2F2F8F"
    ).pack(pady=10)

    form = tk.Frame(card, bg=CARD_BG)
    form.pack(padx=25, pady=10)

    def label_entry(parent, text):
        tk.Label(parent, text=text, bg=CARD_BG).pack(anchor="w")
        entry = tk.Entry(parent, width=ENTRY_WIDTH, font=("Segoe UI", 12), **ENTRY_STYLE)
        entry.pack(anchor="w", pady=(2, 14), ipady=3)
        return entry

    # -------- RESET FUNCTION --------
    def reset_form():
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        dob_entry.delete(0, tk.END)
        join_entry.delete(0, tk.END)
        gender.set("Male")
        membership_var.set("Monthly")
        address_text.delete("1.0", tk.END)
        fname_entry.focus_set()

    # -------- LEFT COLUMN --------
    left = tk.Frame(form, bg=CARD_BG)
    left.grid(row=0, column=0, padx=25, sticky="n")

    fname_entry = label_entry(left, "First Name *")

    tk.Label(left, text="Gender *", bg=CARD_BG).pack(anchor="w")
    gender = tk.StringVar(value="Male")
    tk.Radiobutton(left, text="Male", variable=gender, value="Male", bg=CARD_BG).pack(anchor="w")
    tk.Radiobutton(left, text="Female", variable=gender, value="Female", bg=CARD_BG).pack(anchor="w", pady=(0, 10))

    email_entry = label_entry(left, "Email *")
    join_entry = date_entry_with_icon(left, "Join Date *")

    tk.Label(left, text="Membership Type *", bg=CARD_BG).pack(anchor="w")
    membership_var = tk.StringVar(value="Monthly")
    tk.OptionMenu(left, membership_var, "Monthly", "Quarterly", "Yearly").pack(anchor="w", fill="x", pady=(2, 10))

    # -------- RIGHT COLUMN --------
    right = tk.Frame(form, bg=CARD_BG)
    right.grid(row=0, column=1, padx=25, sticky="n")

    lname_entry = label_entry(right, "Last Name *")
    dob_entry = date_entry_with_icon(right, "Date of Birth *")
    contact_entry = label_entry(right, "Contact No *")
    time_entry = label_entry(right, "Time *")

    tk.Label(right, text="Address *", bg=CARD_BG).pack(anchor="w")
    address_text = tk.Text(right, width=TEXT_WIDTH, height=2, **ENTRY_STYLE)
    address_text.pack(anchor="w", pady=(3, 10))

    # -------- SAVE FUNCTION WITH VALIDATION --------
    def save_member():
        fname = fname_entry.get().strip()
        lname = lname_entry.get().strip()
        email = email_entry.get().strip()
        contact = contact_entry.get().strip()
        time = time_entry.get().strip()
        dob = dob_entry.get().strip()
        join = join_entry.get().strip()
        address = address_text.get("1.0", "end").strip()

        # REQUIRED FIELD CHECK
        if not all([fname, lname, email, contact, time, dob, join, address]):
            messagebox.showwarning("Validation Error", "All fields are required")
            return

        # NAME VALIDATION
        if not fname.isalpha() or not lname.isalpha():
            messagebox.showerror("Validation Error", "Name must contain only letters")
            return

        # EMAIL VALIDATION
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            messagebox.showerror("Validation Error", "Invalid email format")
            return

        # CONTACT VALIDATION
        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Validation Error", "Contact number must be 10 digits")
            return

        data = (
            fname, lname, gender.get(), dob, email,
            contact, join, membership_var.get(), address
        )

        try:
            insert_member(data)
            messagebox.showinfo("Success", "Member added successfully")
            reset_form()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -------- BUTTONS --------
    btn_frame = tk.Frame(card, bg=CARD_BG)
    btn_frame.pack(pady=(8, 12))

    tk.Button(btn_frame, text="Save", width=12, bg="#3A2D8F", fg="white", command=save_member).grid(row=0, column=0, padx=10)
    tk.Button(btn_frame, text="Reset", width=12, command=reset_form).grid(row=0, column=1, padx=10)
    tk.Button(
    btn_frame,
    text="View All Members",
    width=18,
    command=open_view_all_members
    ).grid(row=0, column=2, padx=1)