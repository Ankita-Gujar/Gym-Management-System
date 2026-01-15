import tkinter as tk
from tkinter import ttk, messagebox
from db.member_search import search_member_by_email


def show_search(content_frame, MAIN_BG):

    # clear old content
    for w in content_frame.winfo_children():
        w.destroy()

    # ================= MAIN CARD =================
    card_border = tk.Frame(
        content_frame,
        bg="#B0B3D6",
        padx=3,
        pady=3
    )
    card_border.place(relx=0.5, rely=0.5, anchor="center")

    card = tk.Frame(
        card_border,
        bg="#D9DBEE",
        width=950,
        height=520
    )
    card.pack()
    card.pack_propagate(False)

    # ================= TITLE =================
    tk.Label(
        card,
        text="Search Member",
        bg="#D9DBEE",
        fg="#2F2F8F",
        font=("Segoe UI", 20, "bold"),
        padx=25,
        pady=6
    ).place(relx=0.5, y=10, anchor="n")

    # ================= SEARCH AREA =================
    search_frame = tk.Frame(card, bg="#D9DBEE")
    search_frame.pack(pady=90)

    tk.Label(
        search_frame,
        text="Email ID :",
        bg="#D9DBEE",
        fg="black",
        font=("Segoe UI", 11)
    ).grid(row=0, column=0, padx=10)

    email_var = tk.StringVar()
    tk.Entry(
        search_frame,
        textvariable=email_var,
        width=35,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    ).grid(row=0, column=1, padx=10, ipady=4)

    # ================= TABLE AREA =================
    table_frame = tk.Frame(card, bg="#F4F5FB")
    table_frame.pack(fill="both", expand=True, padx=15, pady=15)

    columns = (
        "fname", "lname", "gender", "dob", "email",
        "contact", "join", "membership", "address"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=10
    )

    headings = [
        "First Name", "Last Name", "Gender", "Date of Birth",
        "Email", "Contact No", "Join Date",
        "Membership Type", "Address"
    ]

    for col, head in zip(columns, headings):
        tree.heading(col, text=head)
        tree.column(col, width=130, anchor="center")

    y_scroll = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    x_scroll = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    tree.grid(row=0, column=0, sticky="nsew")
    y_scroll.grid(row=0, column=1, sticky="ns")
    x_scroll.grid(row=1, column=0, sticky="ew")

    table_frame.grid_rowconfigure(0, weight=1)
    table_frame.grid_columnconfigure(0, weight=1)

    # ================= SEARCH FUNCTION (CORRECT PLACE) =================
    def search_action():
        tree.delete(*tree.get_children())

        email = email_var.get().strip()

        if not email:
            messagebox.showwarning("Input Error", "Please enter Email ID")
            return

        results = search_member_by_email(email)

        if not results:
            messagebox.showinfo("No Record", "Member not found")
            return

        for row in results:
            tree.insert("", "end", values=row)

    # ================= SEARCH BUTTON =================
    tk.Button(
        search_frame,
        text="Search",
        bg="#4B2BBE",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        width=12,
        cursor="hand2",
        command=search_action
    ).grid(row=0, column=2, padx=15)
