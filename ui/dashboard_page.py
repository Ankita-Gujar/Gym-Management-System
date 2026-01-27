import tkinter as tk
from db.dashboard_db import fetch_dashboard_data

def show_dashboard(content_frame, MAIN_BG):

    # ---------- CLEAR OLD CONTENT ----------
    for widget in content_frame.winfo_children():
        widget.destroy()

    # get data from DB
    total, active, inactive, expiring, joined_today, attendance = fetch_dashboard_data()

    main = tk.Frame(content_frame, bg=MAIN_BG)
    main.pack(fill="both", expand=True)

    # ==================================================
    # TOP STAT CARDS
    # ==================================================
    top_frame = tk.Frame(main, bg=MAIN_BG)
    top_frame.pack(pady=30)

    def big_card(parent, title, value):
        shadow = tk.Frame(parent, bg="#DADADA")
        shadow.pack(side="left", padx=20)

        card = tk.Frame(shadow, bg="white", width=230, height=120)
        card.pack(padx=2, pady=2)
        card.pack_propagate(False)

        tk.Label(card, text=title, bg="white", fg="#777",
                 font=("Segoe UI", 11)).pack(pady=(25, 5))

        tk.Label(card, text=value, bg="white", fg="#111",
                 font=("Segoe UI", 26, "bold")).pack()

    big_card(top_frame, "Total Members", total)
    big_card(top_frame, "Active Members", active)
    big_card(top_frame, "Inactive Members", inactive)

    # ==================================================
    # TODAY'S OVERVIEW
    # ==================================================
    tk.Label(
        main, text="TODAY'S OVERVIEW",
        bg=MAIN_BG, fg="#444",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=(15, 10))

    mid_frame = tk.Frame(main, bg=MAIN_BG)
    mid_frame.pack()

    def small_card(parent, title, value, color):
        shadow = tk.Frame(parent, bg="#E5E5E5")
        shadow.pack(side="left", padx=15)

        card = tk.Frame(shadow, bg="white", width=200, height=95)
        card.pack(padx=2, pady=2)
        card.pack_propagate(False)

        tk.Label(card, text=title, bg="white", fg="#666",
                 font=("Segoe UI", 10)).pack(pady=(20, 4))

        tk.Label(card, text=value, bg="white", fg=color,
                 font=("Segoe UI", 22, "bold")).pack()

    small_card(mid_frame, "Expiring in 7 Days", expiring, "#E63946")
    small_card(mid_frame, "Joined Today", joined_today, "#1D3557")
    small_card(mid_frame, "Today's Attendance", attendance, "#2A9D8F")

    # ==================================================
    # MEMBERSHIP OFFERS
    # ==================================================
    tk.Label(
        main,
        text="MEMBERSHIP OFFERS",
        bg=MAIN_BG,
        fg="#444",
        font=("Segoe UI", 12, "bold")
    ).pack(pady=(35, 15))

    offer_frame = tk.Frame(main, bg=MAIN_BG)
    offer_frame.pack()

    def offer_card(parent, title, price, offer_text, highlight=False):

        shadow = tk.Frame(parent, bg="#C7C7C7")
        shadow.pack(side="left", padx=25)

        card_bg = "#F5F7FF" if highlight else "white"
        top_bar = "#6C63FF" if highlight else "#2A9D8F"

        card = tk.Frame(shadow, bg=card_bg, width=240, height=150)
        card.pack(padx=2, pady=2)
        card.pack_propagate(False)

        tk.Frame(card, bg=top_bar, height=6).pack(fill="x")

        tk.Label(card, text=title,
                 bg=card_bg, fg="#1D3557",
                 font=("Segoe UI", 12, "bold")).pack(pady=(15, 5))

        tk.Label(card, text=price,
                 bg=card_bg, fg="#2A9D8F",
                 font=("Segoe UI", 24, "bold")).pack()

        tk.Label(card, text=offer_text,
                 bg=card_bg, fg="#555",
                 font=("Segoe UI", 10)).pack(pady=5)

        if highlight:
            tk.Label(card, text="⭐ MOST POPULAR",
                     bg=card_bg, fg="#6C63FF",
                     font=("Segoe UI", 9, "bold")).pack()

    offer_card(offer_frame, "Monthly Plan", "₹1,200", "Limited Time Offer")
    offer_card(offer_frame, "Quarterly Plan", "₹3,200", "Save ₹400", highlight=True)
    offer_card(offer_frame, "Yearly Plan", "₹10,000", "Best Value")
