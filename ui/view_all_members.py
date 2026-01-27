import tkinter as tk
from tkinter import ttk, messagebox
from db.member_fetch import get_all_members


def open_view_all_members():
    win = tk.Toplevel()
    win.title("View All Members")
    win.geometry("1100x450")
    win.configure(bg="#F5F6FA")

    # -------- TITLE --------
    tk.Label(
        win,
        text="All Members",
        font=("Segoe UI", 18, "bold"),
        bg="#F5F6FA",
        fg="#2F2F8F"
    ).pack(pady=10)

    # -------- TABLE FRAME --------
    table_frame = tk.Frame(win)
    table_frame.pack(fill="both", expand=True, padx=15, pady=10)

    # -------- SCROLLBARS --------
    scroll_x = tk.Scrollbar(table_frame, orient="horizontal")
    scroll_y = tk.Scrollbar(table_frame, orient="vertical")

    # -------- TREEVIEW --------
    columns = (
        "SR", "First Name", "Last Name", "Gender", "DOB",
        "Email", "Contact", "Join Date", "Membership", "Address"
    )

    tree = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
    )

    scroll_x.config(command=tree.xview)
    scroll_y.config(command=tree.yview)

    scroll_x.pack(side="bottom", fill="x")
    scroll_y.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    # -------- HEADINGS --------
    tree.heading("SR", text="SR No")
    tree.column("SR", width=60, anchor="center")

    for col in columns[1:]:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    tree.column("Address", width=220)

  
    def load_data():
        tree.delete(*tree.get_children())

        try:
            records = get_all_members()
            for i, row in enumerate(records, start=1):
                tree.insert("", "end", values=(i, *row[1:]))  
        except Exception as e:
            messagebox.showerror("Error", str(e))

    load_data()
