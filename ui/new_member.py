import tkinter as tk

def show_member(content_frame, MAIN_BG):
    # clear old content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # -------- TITLE --------
    tk.Label(
        content_frame,
        text="Add Member",
        font=("Segoe UI", 20, "bold"),
        bg=MAIN_BG
    ).pack(pady=10)

    form_frame = tk.Frame(content_frame, bg=MAIN_BG)
    form_frame.pack(pady=20)

    # -------- LEFT --------
    left = tk.Frame(form_frame, bg=MAIN_BG)
    left.grid(row=0, column=0, padx=40, sticky="n")

    tk.Label(left, text="First Name *", bg=MAIN_BG).pack(anchor="w")
    tk.Entry(left, width=30).pack(pady=5)

    tk.Label(left, text="Gender *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    gender = tk.StringVar(value="Male")
    tk.Radiobutton(left, text="Male", variable=gender, value="Male", bg=MAIN_BG).pack(anchor="w")
    tk.Radiobutton(left, text="Female", variable=gender, value="Female", bg=MAIN_BG).pack(anchor="w")

    tk.Label(left, text="Email *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Entry(left, width=30).pack(pady=5)

    tk.Label(left, text="Join Date *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Entry(left, width=30).pack(pady=5)

    tk.Label(left, text="Membership Type *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.OptionMenu(left, tk.StringVar(), "Monthly", "Quarterly", "Yearly").pack(fill="x")

    # -------- RIGHT --------
    right = tk.Frame(form_frame, bg=MAIN_BG)
    right.grid(row=0, column=1, padx=40, sticky="n")

    tk.Label(right, text="Last Name *", bg=MAIN_BG).pack(anchor="w")
    tk.Entry(right, width=30).pack(pady=5)

    tk.Label(right, text="Date of Birth *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Entry(right, width=30).pack(pady=5)

    tk.Label(right, text="Contact No *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Entry(right, width=30).pack(pady=5)

    tk.Label(right, text="Time *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Entry(right, width=30).pack(pady=5)

    tk.Label(right, text="Address *", bg=MAIN_BG).pack(anchor="w", pady=(10, 0))
    tk.Text(right, width=30, height=4).pack()

    # -------- BUTTONS --------
    btns = tk.Frame(content_frame, bg=MAIN_BG)
    btns.pack(pady=20)

    tk.Button(btns, text="Save", width=12, bg="#3A2D8F", fg="white").grid(row=0, column=0, padx=10)
    tk.Button(btns, text="Reset", width=12).grid(row=0, column=1, padx=10)
    tk.Button(btns, text="View All Members", width=18).grid(row=0, column=2, padx=10)
