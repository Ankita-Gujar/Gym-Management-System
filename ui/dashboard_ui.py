import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from ui import new_member


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Iron Fitness Club - Dashboard")
root.state("zoomed")
root.configure(bg="#F4F5FB")

# ---------------- COLORS ----------------
SIDEBAR_BG = "#1E1E1E"
BTN_BG = "#2A2A2A"
BTN_HOVER = "#3A2D8F"
TEXT_COLOR = "white"
MAIN_BG = "#F4F5FB"
PRIMARY = "#2B2B2B"
ACCENT = "#FF8C00"

# ---------------- SIDEBAR ----------------
sidebar = tk.Frame(root, bg=SIDEBAR_BG, width=240)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# Logo
try:
    logo_img = Image.open("imgs/logo.png").resize((120, 120))
    logo = ImageTk.PhotoImage(logo_img)
    tk.Label(sidebar, image=logo, bg=SIDEBAR_BG).pack(pady=20)
except:
    tk.Label(sidebar, text="IRON\nFITNESS", fg=ACCENT,
             bg=SIDEBAR_BG, font=("Arial", 15, "bold")).pack(pady=20)

# ---------------- ICON LOADER ----------------
def load_icon(path):
    img = Image.open(path).resize((22, 22))
    return ImageTk.PhotoImage(img)

icons = {
    "dashboard": load_icon("imgs/icons/dashboard.png"),
    "member": load_icon("imgs/icons/user.png"),
    "staff": load_icon("imgs/icons/team.png"),
    "equipment": load_icon("imgs/icons/dumbbell.png"),
    "search": load_icon("imgs/icons/search.png"),
    "delete": load_icon("imgs/icons/delete.png"),
    "logout": load_icon("imgs/icons/logout.png")
}

active_btn = None

def set_active(btn):
    global active_btn
    if active_btn:
        active_btn.config(bg=BTN_BG)
    btn.config(bg=BTN_HOVER)
    active_btn = btn


# ---------------- SIDEBAR BUTTON FUNCTION ----------------
def menu_button(text, icon, is_active=False):
    global active_btn

    btn = tk.Button(
        sidebar,
        text="   " + text,
        image=icon,
        compound="left",
        bg=BTN_BG,
        fg=TEXT_COLOR,
        font=("Segoe UI", 11),
        relief="flat",
        anchor="w",
        padx=20,
        pady=12,
        cursor="hand2",
        command=lambda: set_active(btn)
    )
    btn.pack(fill="x", pady=6)

    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER if btn != active_btn else BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG if btn != active_btn else BTN_HOVER))

    if is_active:
        btn.config(bg=BTN_HOVER)
        active_btn = btn

    return btn


# ---------------- MENU ITEMS ----------------
menu_button("Dashboard", icons["dashboard"], is_active=True)
menu_button("New Member", icons["member"]).config(command=lambda: [set_active(active_btn), new_member.show_member(content_frame, MAIN_BG)])
menu_button("New Staff", icons["staff"])
menu_button("Equipment", icons["equipment"])
menu_button("Search Member", icons["search"])
menu_button("Delete Member", icons["delete"])

tk.Label(sidebar, bg=SIDEBAR_BG).pack(expand=True)

menu_button("Logout", icons["logout"])

# ---------------- MAIN AREA ----------------
main_area = tk.Frame(root, bg=MAIN_BG)
main_area.pack(side="right", fill="both", expand=True)

# ---------------- HEADER BACKGROUND ----------------
header_frame = tk.Frame(main_area, bg=PRIMARY, height=120)
header_frame.pack(fill="x")

header_frame.pack_propagate(False)

header = tk.Label(
    header_frame,
    text="WELCOME TO IRON FITNESS CLUB",
    fg="white",
    bg=PRIMARY,
    font=("Impact", 34)
)
header.pack(pady=(20, 5))

# ---------------- DATE ----------------
def update_date():
    now = datetime.now()
    date_lbl.config(text=now.strftime("%A, %d %B %Y"))
    root.after(1000, update_date)

date_lbl = tk.Label(
    header_frame,
    fg=ACCENT,
    bg=PRIMARY,
    font=("Segoe UI", 14)
)
date_lbl.pack()
update_date()

# ---------------- DASHBOARD CONTENT ----------------
content_frame = tk.Frame(main_area, bg=MAIN_BG)
content_frame.pack(fill="both", expand=True, padx=30, pady=20)

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ---------------- PAGE FUNCTIONS ----------------

def show_dashboard():
    clear_content()

    cards_frame = tk.Frame(content_frame, bg=MAIN_BG)
    cards_frame.pack(fill="x", pady=10)

    info_card(cards_frame, "Total Members", "120")
    info_card(cards_frame, "Active Members", "95")
    info_card(cards_frame, "Inactive Members", "25")


def show_member():
    clear_content()
    tk.Label(
        content_frame,
        text="NEW MEMBER PAGE",
        font=("Segoe UI", 24, "bold"),
        bg=MAIN_BG
    ).pack(pady=50)


def show_staff():
    clear_content()
    tk.Label(
        content_frame,
        text="STAFF PAGE",
        font=("Segoe UI", 24, "bold"),
        bg=MAIN_BG
    ).pack(pady=50)


def show_equipment():
    clear_content()
    tk.Label(
        content_frame,
        text="EQUIPMENT PAGE",
        font=("Segoe UI", 24, "bold"),
        bg=MAIN_BG
    ).pack(pady=50)


def show_search():
    clear_content()
    tk.Label(
        content_frame,
        text="SEARCH MEMBER PAGE",
        font=("Segoe UI", 24, "bold"),
        bg=MAIN_BG
    ).pack(pady=50)


def show_delete():
    clear_content()
    tk.Label(
        content_frame,
        text="DELETE MEMBER PAGE",
        font=("Segoe UI", 24, "bold"),
        bg=MAIN_BG
    ).pack(pady=50)


def info_card(parent, title, value):
    card = tk.Frame(parent, bg="white", width=220, height=110)
    card.pack(side="left", padx=15)
    card.pack_propagate(False)

    tk.Label(card, text=title, bg="white",
             fg="#555", font=("Segoe UI", 11)).pack(pady=(20, 5))
    tk.Label(card, text=value, bg="white",
             fg="#2B2B2B", font=("Segoe UI", 22, "bold")).pack()

# ---------------- SUMMARY CARDS ----------------
def show_dashboard():
    clear_content()

    cards_frame = tk.Frame(content_frame, bg=MAIN_BG)
    cards_frame.pack(fill="x", pady=10)

    info_card(cards_frame, "Total Members", "120")
    info_card(cards_frame, "Active Members", "95")
    info_card(cards_frame, "Inactive Members", "25")

    chart_frame = tk.Frame(content_frame, bg="white", height=300)
    chart_frame.pack(fill="x", pady=20)
    chart_frame.pack_propagate(False)

    tk.Label(
        chart_frame,
        text="Monthly Attendance Progress",
        bg="white",
        fg="#2B2B2B",
        font=("Segoe UI", 13, "bold")
    ).pack(anchor="w", padx=20, pady=10)

show_dashboard()

root.mainloop()
