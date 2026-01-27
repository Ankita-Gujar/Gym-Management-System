import tkinter as tk
from tkinter import ttk, messagebox
from db.equipment_fetch import get_all_equipment



def open_view_all_equipment():
    win = tk.Toplevel()
    win.title("View All Equipments")
    win.geometry("1000x450")
    win.configure(bg="#F5F6FA")

    tk.Label(
        win,
        text="All Equipments",
        font=("Segoe UI", 18, "bold"),
        bg="#F5F6FA",
        fg="#2F2F8F"
    ).pack(pady=10)

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True, padx=15, pady=10)

    scroll_x = tk.Scrollbar(frame, orient="horizontal")
    scroll_y = tk.Scrollbar(frame, orient="vertical")

    columns = (
        "SR", "Name", "Description", "Muscles",
        "Delivery Date", "Cost"
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
        tree.column(col, width=150, anchor="center")

    def load_data():
        tree.delete(*tree.get_children())
        try:
            records = get_all_equipment()
            for i, row in enumerate(records, start=1):
                tree.insert("", "end", values=(i, row[1], row[2], row[3], row[4], row[5]))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    load_data()
