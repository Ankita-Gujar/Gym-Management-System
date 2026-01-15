import tkinter as tk

def show_dashboard(content_frame, MAIN_BG):
    # clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    def info_card(parent, title, value):
        card = tk.Frame(parent, bg="white", width=220, height=110)
        card.pack(side="left", padx=15)
        card.pack_propagate(False)

        tk.Label(
            card,
            text=title,
            bg="white",
            fg="#555",
            font=("Segoe UI", 11)
        ).pack(pady=(20, 5))

        tk.Label(
            card,
            text=value,
            bg="white",
            fg="#2B2B2B",
            font=("Segoe UI", 22, "bold")
        ).pack()

    cards_frame = tk.Frame(content_frame, bg=MAIN_BG)
    cards_frame.pack(fill="x", pady=10)

    info_card(cards_frame, "Total Members", "120")
    info_card(cards_frame, "Active Members", "95")
    info_card(cards_frame, "Inactive Members", "25")
