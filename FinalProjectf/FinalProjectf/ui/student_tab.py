import tkinter as tk
from tkinter import ttk, messagebox


class StudentTab: #report and search panels for reporting lost items
    def __init__(self, parent, controller):
        self.controller = controller
        self.frame = tk.Frame(parent, bg="#f3f6fb")

        self.item_type = tk.StringVar(value="lost")
        self.search_var = tk.StringVar()

        self.build()

    def build(self):
        container = tk.Frame(self.frame, bg="#f3f6fb")
        container.pack(fill="both", expand=True, padx=10, pady=10)

    
        top = tk.Frame(container, bg="#f3f6fb")
        top.pack(fill="x")

        
        report = tk.Frame(top, bg="white", bd=1, relief="solid")
        report.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(report,
                 text="Report Items",
                 font=("Times New Roman", 18, "bold"),
                 bg="white", fg="#2a4d8f").pack(pady=10)

        form = tk.Frame(report, bg="white")
        form.pack(padx=20, pady=10, fill="x") #area to report items

        
        tk.Label(form, text="Item Description", bg="white").grid(row=0, column=0, sticky="w")
        self.desc = tk.Entry(form, width=60)
        self.desc.grid(row=0, column=1, pady=5)

       
        tk.Label(form, text="Where You Lost It", bg="white").grid(row=1, column=0, sticky="w")
        self.loc = tk.Entry(form, width=60)
        self.loc.grid(row=1, column=1, pady=5)

        
        tk.Label(form, text="Contact Info", bg="white").grid(row=2, column=0, sticky="w")
        self.contact = tk.Entry(form, width=60)
        self.contact.grid(row=2, column=1, pady=5)

        
        type_frame = tk.Frame(form, bg="white")
        type_frame.grid(row=3, column=1, pady=10, sticky="w")

        tk.Label(form, text="Item Type", bg="white").grid(row=3, column=0, sticky="w")

        ttk.Radiobutton(type_frame, text="Lost Items",
                        variable=self.item_type, value="lost").pack(side="left")

        ttk.Radiobutton(type_frame, text="Found Items",
                        variable=self.item_type, value="found").pack(side="left", padx=10)

       
        tk.Button(report,
                  text="Submit Report",
                  bg="#3c7d3c",
                  fg="white",
                  width=20,
                  command=self.submit).pack(pady=15)

        guide = tk.Frame(top, bg="white", bd=1, relief="solid", width=250)
        guide.pack(side="right", fill="y")

        tk.Label(guide,
                 text="Guidelines:",
                 font=("Arial", 12, "bold"),
                 bg="white",
                 fg="#2f6b2f").pack(anchor="w", padx=10, pady=10)

        guidelines = [
            "• Use specific item details.",
            "• Give exact location.",
            "• Provide valid contact info.",
            "• Only claim if you can prove ownership."
        ]

        for g in guidelines:
            tk.Label(guide, text=g, bg="white", anchor="w", justify="left").pack(anchor="w", padx=10, pady=2)

        bottom = tk.Frame(container, bg="white", bd=1, relief="solid")
        bottom.pack(fill="both", expand=True, pady=10)

        tk.Label(bottom,
                 text="Search Available Items",
                 font=("Times New Roman", 16, "bold"),
                 fg="#2f6b2f",
                 bg="white").pack(pady=10)

        search_bar = tk.Frame(bottom, bg="white")
        search_bar.pack(pady=5) #search bar to search for lost item to claim

        tk.Entry(search_bar, textvariable=self.search_var, width=40).pack(side="left", padx=5)

        tk.Button(search_bar,
                  text="Claim Selected Item",
                  bg="#2f5fa3",
                  fg="white",
                  command=self.claim).pack(side="left", padx=10)

        
        self.tree = ttk.Treeview(
            bottom,
            columns=("ID", "Type", "Description", "Location"),
            show="headings",
            height=10
        ) # table showing all reports

        self.tree.heading("ID", text="ID")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Location", text="Location")

        self.tree.column("ID", width=50)
        self.tree.column("Type", width=100)
        self.tree.column("Description", width=300)
        self.tree.column("Location", width=200)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.refresh()

    def submit(self): 
        if not self.desc.get() or not self.loc.get() or not self.contact.get():
            messagebox.showerror("Error", "Fill all fields") #make sure all necessary information is provided
            return

        new_id = self.controller.add_item(
            self.item_type.get(),
            self.desc.get(),
            self.loc.get(),
            self.contact.get()
        )

        messagebox.showinfo("Success", f"Item ID: {new_id}")
        self.refresh()

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.controller.get_available_items():
            self.tree.insert("", "end", values=(
                item.get_id(),
                item.get_type(),
                item.get_description(),
                item.get_location()
            ))

    def claim(self):
        selected = self.tree.selection()
        if not selected:
            return #prevent failure even if nothing selected

        item_id = int(self.tree.item(selected[0])["values"][0])
        self.controller.claim_item(item_id)

        messagebox.showinfo("Claimed", "Item claimed")
        self.refresh()