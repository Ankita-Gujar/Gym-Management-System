import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
from ui.dashboard_page import show_dashboard
from ui import new_member, new_staff, equipments, search_member, delete_member



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


# ---------------- MAIN AREA ----------------
main_area = tk.Frame(root, bg=MAIN_BG)
main_area.pack(side="right", fill="both", expand=True)

 #---------------- HEADER BACKGROUND ----------------
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

## ---------------- DASHBOARD CONTENT ----------------
content_frame = tk.Frame(main_area, bg=MAIN_BG)
content_frame.pack(fill="both", expand=True, padx=30, pady=20)

def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

active_btn = None

def set_active(btn):
    global active_btn
    if active_btn:
        active_btn.config(bg=BTN_BG)
    btn.config(bg=BTN_HOVER)
    active_btn = btn

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


# ---------------- SIDEBAR BUTTON FUNCTION ----------------
def menu_button(text, icon, command, is_active=False):
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
        command=lambda: (set_active(btn), command())
    )
    btn.pack(fill="x", pady=6)

    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_BG if btn != active_btn else BTN_HOVER))

    if is_active:
        btn.config(bg=BTN_HOVER)
        active_btn = btn

    return btn



# ---------------- MENU ITEMS ----------------
menu_button(
    "Dashboard",
    icons["dashboard"],
    lambda: show_dashboard(content_frame, MAIN_BG),
    True
)

menu_button(
    "New Member",
    icons["member"],
    lambda: new_member.show_member(content_frame, MAIN_BG)
)

menu_button(
    "New Staff",
    icons["staff"],
    lambda: new_staff.show_staff(content_frame, MAIN_BG)
)

menu_button("Equipments", 
            icons["equipment"],  
            lambda: equipments.show_equipment(content_frame, MAIN_BG))

menu_button("Search Member", 
            icons["search"], 
            lambda: search_member.show_search(content_frame, MAIN_BG))
menu_button("Delete Member", icons["delete"],
            lambda: delete_member.show_delete(content_frame, MAIN_BG))

tk.Label(sidebar, bg=SIDEBAR_BG).pack(expand=True)

menu_button("Logout", icons["logout"], root.quit)

show_dashboard(content_frame, MAIN_BG)


root.mainloop()