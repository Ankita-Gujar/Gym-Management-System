import tkinter as tk
from tkinter import ttk, messagebox
from db.staff_fetch import get_all_staff


def open_view_all_staff():
    win = tk.Toplevel()
    win.title("View All Staff")
    win.geometry("1100x450")
    win.configure(bg="#F5F6FA")

    tk.Label(
        win,
        text="All Staff",
        font=("Segoe UI", 18, "bold"),
        bg="#F5F6FA",
        fg="#2F2F8F"
    ).pack(pady=10)

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=15, pady=10)

    scroll_x = tk.Scrollbar(frame, orient="horizontal")
    scroll_y = tk.Scrollbar(frame, orient="vertical")

    columns = (
        "SR", "First Name", "Last Name", "Gender", "DOB",
        "Email", "Contact", "Join Date", "State", "City"
    )

    tree = ttk.Treeview(
        frame,
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

    tree.heading("SR", text="SR No")
    tree.column("SR", width=60, anchor="center")

    for col in columns[1:]:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    def load_data():
        tree.delete(*tree.get_children())
        try:
            records = get_all_staff()
            for i, row in enumerate(records, start=1):
                tree.insert("", "end", values=(i, *row[1:]))  # skip DB id
        except Exception as e:
            messagebox.showerror("Error", str(e))

    load_data()
