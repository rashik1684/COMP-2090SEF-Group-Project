import tkinter as tk
from tkinter import ttk


class AdminTab:
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#f3f6fb")

        self.total_label = tk.Label(self.frame, text="0", font=("Arial", 20))
        self.total_label.pack()

        self.tree = ttk.Treeview(
            self.frame,
            columns=("ID", "Type", "Status"),
            show="headings"
        )

        for col in ("ID", "Type", "Status"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill="both", expand=True)

        ttk.Button(self.frame, text="Refresh", command=self.refresh).pack()

        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        items = self.controller.items

        self.total_label.config(text=f"Total: {len(items)}")

        for item in items:
            self.tree.insert("", "end", values=(
                item.get_id(),
                item.get_type(),
                item.get_status()
            ))