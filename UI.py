import tkinter as tk
from tkinter import ttk, messagebox


class LostandFoundInventoryUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("HKMU Lost & Found Inventory Management")
        self.window.geometry("1400x820")
        self.window.minsize(1180, 720)
        self.window.configure(bg="#0f172a")
        self.window.option_add("*Font", ("Times New Roman", 12))

        self.entries = {}
        self.lost_entries = {}
        self.found_entries = {}
        self.total_label = None
        self.pending_label = None
        self.claimed_label = None
        self.current_page = tk.StringVar(value="report")
        self.item_type = tk.StringVar(value="lost")
        self.search_var = tk.StringVar()

        self.setup_styles()
        self.build_layout()
        self.show_page("report")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Primary.TButton",
            font=("Times New Roman", 12, "bold"),
            padding=(16, 10),
            background="#2563eb",
            foreground="white"
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#1d4ed8"), ("pressed", "#1e40af")],
            foreground=[("active", "white"), ("pressed", "white")]
        )

        style.configure(
            "Success.TButton",
            font=("Times New Roman", 12, "bold"),
            padding=(16, 10),
            background="#16a34a",
            foreground="white"
        )
        style.map(
            "Success.TButton",
            background=[("active", "#15803d"), ("pressed", "#166534")],
            foreground=[("active", "white"), ("pressed", "white")]
        )

        style.configure(
            "Danger.TButton",
            font=("Times New Roman", 12, "bold"),
            padding=(16, 10),
            background="#dc2626",
            foreground="white"
        )
        style.map(
            "Danger.TButton",
            background=[("active", "#b91c1c"), ("pressed", "#991b1b")],
            foreground=[("active", "white"), ("pressed", "white")]
        )

        style.configure(
            "Treeview",
            rowheight=30,
            font=("Times New Roman", 11),
            background="#ffffff",
            foreground="#0f172a",
            fieldbackground="#ffffff"
        )
        style.configure(
            "Treeview.Heading",
            font=("Times New Roman", 12, "bold"),
            background="#2563eb",
            foreground="white"
        )
        style.map(
            "Treeview",
            background=[("selected", "#dbeafe")],
            foreground=[("selected", "#111827")]
        )

    def build_layout(self):
        self.root = tk.Frame(self.window, bg="#0f172a")
        self.root.pack(fill="both", expand=True)

        self.sidebar = tk.Frame(self.root, bg="#111827", width=260)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.content = tk.Frame(self.root, bg="#e2e8f0")
        self.content.pack(side="right", fill="both", expand=True)

        self.build_sidebar()
        self.build_header()
        self.build_pages()

    def build_sidebar(self):
        tk.Label(
            self.sidebar,
            text="HKMU Lost & Found",
            font=("Times New Roman", 22, "bold"),
            bg="#111827",
            fg="white"
        ).pack(anchor="w", padx=22, pady=(24, 6))

        tk.Label(
            self.sidebar,
            text="Dashboard Navigation",
            font=("Times New Roman", 12),
            bg="#111827",
            fg="#94a3b8"
        ).pack(anchor="w", padx=22, pady=(0, 22))

        nav = tk.Frame(self.sidebar, bg="#111827")
        nav.pack(fill="x", padx=14)

        self.nav_buttons = {}

        for key, label in [("report", "Report & Search"), ("admin", "Admin Panel")]:
            btn = tk.Button(
                nav,
                text=label,
                command=lambda k=key: self.show_page(k),
                font=("Times New Roman", 13, "bold"),
                bg="#1f2937",
                fg="#e5e7eb",
                activebackground="#2563eb",
                activeforeground="white",
                bd=0,
                relief="flat",
                padx=16,
                pady=14,
                anchor="w"
            )
            btn.pack(fill="x", pady=8)
            self.nav_buttons[key] = btn

        tk.Label(
            self.sidebar,
            text="Use this app to report, search, claim, and manage HKMU lost and found records.",
            font=("Times New Roman", 11),
            bg="#111827",
            fg="#94a3b8",
            wraplength=210,
            justify="left"
        ).pack(anchor="w", padx=22, pady=18)

    def build_header(self):
        self.header = tk.Frame(self.content, bg="#e2e8f0")
        self.header.pack(fill="x", padx=18, pady=(18, 10))

        left = tk.Frame(self.header, bg="#e2e8f0")
        left.pack(side="left")

        tk.Label(
            left,
            text="HKMU Lost & Found Inventory Management",
            font=("Times New Roman", 24, "bold"),
            bg="#e2e8f0",
            fg="#0f172a"
        ).pack(anchor="w")

        tk.Label(
            left,
            text="Modern dashboard for reporting, searching, claiming, and admin control",
            font=("Times New Roman", 12),
            bg="#e2e8f0",
            fg="#475569"
        ).pack(anchor="w", pady=(4, 0))

        self.status_label = tk.Label(
            self.header,
            text="● Checking connection...",
            font=("Times New Roman", 12, "bold"),
            bg="#dbeafe",
            fg="#1d4ed8",
            padx=16,
            pady=10
        )
        self.status_label.pack(side="right")

    def build_pages(self):
        self.page_host = tk.Frame(self.content, bg="#e2e8f0")
        self.page_host.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        self.report_page = tk.Frame(self.page_host, bg="#e2e8f0")
        self.admin_page = tk.Frame(self.page_host, bg="#e2e8f0")

        self.build_report_page()
        self.build_admin_page()

    def make_card(self, parent, title, subtitle=None, title_color="#0f172a"):
        card = tk.Frame(
            parent,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#cbd5e1"
        )

        tk.Label(
            card,
            text=title,
            font=("Times New Roman", 18, "bold"),
            bg="#ffffff",
            fg=title_color
        ).pack(anchor="w", padx=20, pady=(18, 2))

        if subtitle:
            tk.Label(
                card,
                text=subtitle,
                font=("Times New Roman", 11),
                bg="#ffffff",
                fg="#64748b"
            ).pack(anchor="w", padx=20, pady=(0, 14))

        body = tk.Frame(card, bg="#ffffff")
        body.pack(fill="both", expand=True, padx=20, pady=(0, 18))
        return card, body

    def build_report_page(self):
        page = self.report_page

        top = tk.Frame(page, bg="#e2e8f0")
        top.pack(fill="x")

        report_card, report_body = self.make_card(
            top,
            "Report an Item",
            "Add a lost or found item with clear contact details.",
            "#1d4ed8"
        )
        report_card.pack(side="left", fill="both", expand=True, padx=(0, 12))

        guide_card, guide_body = self.make_card(
            top,
            "Guidelines",
            "Follow these tips for a better report.",
            "#15803d"
        )
        guide_card.pack(side="left", fill="y", padx=(12, 0))

        self.report_form = tk.Frame(report_body, bg="#ffffff")
        self.report_form.pack(fill="x")

        tk.Label(
            self.report_form,
            text="Item Type",
            font=("Times New Roman", 12, "bold"),
            bg="#ffffff",
            fg="#0f172a"
        ).grid(row=0, column=0, sticky="w", pady=10, padx=(0, 14))

        radio_wrap = tk.Frame(self.report_form, bg="#ffffff")
        radio_wrap.grid(row=0, column=1, sticky="w", pady=10)

        ttk.Radiobutton(
            radio_wrap,
            text="Lost Item",
            variable=self.item_type,
            value="lost",
            command=self.build_report_fields
        ).pack(side="left", padx=(0, 16))

        ttk.Radiobutton(
            radio_wrap,
            text="Found Item",
            variable=self.item_type,
            value="found",
            command=self.build_report_fields
        ).pack(side="left")

        self.dynamic_fields_frame = tk.Frame(self.report_form, bg="#ffffff")
        self.dynamic_fields_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.report_form.columnconfigure(1, weight=1)

        self.build_report_fields()

        ttk.Button(
            report_body,
            text="Submit Report",
            command=self.submit_report,
            style="Success.TButton"
        ).pack(anchor="e", pady=(18, 0))

        rules = [
            "Use specific item details.",
            "Give the exact location where the item was lost or found.",
            "Provide a valid phone number or email.",
            "Only submit a claim if you can prove ownership."
        ]

        for text in rules:
            tk.Label(
                guide_body,
                text=f"• {text}",
                font=("Times New Roman", 12),
                bg="#ffffff",
                fg="#334155",
                wraplength=240,
                justify="left"
            ).pack(anchor="w", pady=8)

        search_card, search_body = self.make_card(
            page,
            "Search Available Items",
            "Claimed items are hidden from the student list.",
            "#15803d"
        )
        search_card.pack(fill="both", expand=True, pady=(16, 0))

        toolbar = tk.Frame(search_body, bg="#ffffff")
        toolbar.pack(fill="x", pady=(0, 12))

        tk.Label(
            toolbar,
            text="Search",
            font=("Times New Roman", 12, "bold"),
            bg="#ffffff",
            fg="#0f172a"
        ).pack(side="left", padx=(0, 10))

        search_entry = tk.Entry(
            toolbar,
            textvariable=self.search_var,
            width=40,
            font=("Times New Roman", 12),
            bg="#f8fafc",
            fg="#0f172a",
            insertbackground="#0f172a",
            relief="solid",
            bd=1
        )
        search_entry.pack(side="left", padx=(0, 12), ipady=6)
        search_entry.bind("<KeyRelease>", lambda event: self.search_bar())

        ttk.Button(
            toolbar,
            text="Claim Selected Item",
            command=self.claim_item,
            style="Primary.TButton"
        ).pack(side="left")

        table_frame = tk.Frame(search_body, bg="#ffffff")
        table_frame.pack(fill="both", expand=True)

        columns = ("ID", "Type", "Description", "Location", "Date", "Contact")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor="w")

        self.tree.column("Description", width=320)
        self.tree.column("Location", width=200)
        self.tree.column("Date", width=180)
        self.tree.column("Contact", width=180)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def build_report_fields(self):
        for widget in self.dynamic_fields_frame.winfo_children():
            widget.destroy()

        self.entries.clear()
        self.lost_entries.clear()
        self.found_entries.clear()

        if self.item_type.get() == "lost":
            self.build_lost_fields()
        else:
            self.build_found_fields()

    def create_input_row(self, parent, row, label_text, target_dict, key):
        tk.Label(
            parent,
            text=label_text,
            font=("Times New Roman", 12, "bold"),
            bg="#ffffff",
            fg="#0f172a"
        ).grid(row=row, column=0, sticky="w", pady=10, padx=(0, 14))

        entry = tk.Entry(
            parent,
            width=52,
            font=("Times New Roman", 12),
            bg="#f8fafc",
            fg="#0f172a",
            insertbackground="#0f172a",
            relief="solid",
            bd=1
        )
        entry.grid(row=row, column=1, sticky="ew", pady=10, ipady=6)
        target_dict[key] = entry
        parent.columnconfigure(1, weight=1)

    def build_lost_fields(self):
        self.create_input_row(self.dynamic_fields_frame, 0, "Lost Item Description", self.lost_entries, "description")
        self.create_input_row(self.dynamic_fields_frame, 1, "Where You Lost It", self.lost_entries, "location")
        self.create_input_row(self.dynamic_fields_frame, 2, "Contact Number", self.lost_entries, "contact")

    def build_found_fields(self):
        self.create_input_row(self.dynamic_fields_frame, 0, "Found Item Description", self.found_entries, "description")
        self.create_input_row(self.dynamic_fields_frame, 1, "Where You Found It", self.found_entries, "location")
        self.create_input_row(self.dynamic_fields_frame, 2, "Contact Number", self.found_entries, "contact")

        tk.Label(
            self.dynamic_fields_frame,
            text="Additional Notes",
            font=("Times New Roman", 12, "bold"),
            bg="#ffffff",
            fg="#0f172a"
        ).grid(row=3, column=0, sticky="nw", pady=10, padx=(0, 14))

        notes = tk.Text(
            self.dynamic_fields_frame,
            width=52,
            height=5,
            font=("Times New Roman", 12),
            bg="#f8fafc",
            fg="#0f172a",
            insertbackground="#0f172a",
            relief="solid",
            bd=1
        )
        notes.grid(row=3, column=1, sticky="ew", pady=10)
        self.found_entries["notes"] = notes
        self.dynamic_fields_frame.columnconfigure(1, weight=1)

    def build_admin_page(self):
        page = self.admin_page

        stats = tk.Frame(page, bg="#e2e8f0")
        stats.pack(fill="x")

        total_card, self.total_label = self.make_stat_card(stats, "Total Reports", "#2563eb")
        pending_card, self.pending_label = self.make_stat_card(stats, "Pending Reports", "#f59e0b")
        claimed_card, self.claimed_label = self.make_stat_card(stats, "Claimed Reports", "#16a34a")

        total_card.pack(side="left", fill="x", expand=True, padx=(0, 10))
        pending_card.pack(side="left", fill="x", expand=True, padx=(0, 10))
        claimed_card.pack(side="left", fill="x", expand=True)

        admin_card, admin_body = self.make_card(
            page,
            "Manage All Reports",
            "Refresh, review, and delete records.",
            "#1d4ed8"
        )
        admin_card.pack(fill="both", expand=True, pady=(16, 0))

        topbar = tk.Frame(admin_body, bg="#ffffff")
        topbar.pack(fill="x", pady=(0, 12))

        ttk.Button(
            topbar,
            text="Refresh Data",
            command=self.refresh_from_source,
            style="Primary.TButton"
        ).pack(side="left", padx=(0, 10))

        ttk.Button(
            topbar,
            text="Delete Selected",
            command=self.delete_selected_item,
            style="Danger.TButton"
        ).pack(side="left")

        columns = ("ID", "Type", "Description", "Location", "Date", "Status", "Claimed By", "Claimed At")
        self.admin_tree = ttk.Treeview(admin_body, columns=columns, show="headings", height=16)

        for col in columns:
            self.admin_tree.heading(col, text=col)
            self.admin_tree.column(col, width=130, anchor="w")

        self.admin_tree.column("Description", width=260)
        self.admin_tree.column("Location", width=200)
        self.admin_tree.column("Claimed By", width=160)
        self.admin_tree.column("Claimed At", width=160)

        scrollbar = ttk.Scrollbar(admin_body, orient="vertical", command=self.admin_tree.yview)
        self.admin_tree.configure(yscrollcommand=scrollbar.set)

        self.admin_tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.admin_tree.tag_configure("claimed", background="#dcfce7")
        self.admin_tree.tag_configure("pending", background="#eff6ff")

    def make_stat_card(self, parent, title, color):
        card = tk.Frame(
            parent,
            bg="#ffffff",
            bd=0,
            highlightthickness=1,
            highlightbackground="#cbd5e1"
        )

        body = tk.Frame(card, bg="#ffffff")
        body.pack(fill="both", expand=True, padx=18, pady=16)

        tk.Label(
            body,
            text=title,
            font=("Times New Roman", 12, "bold"),
            bg="#ffffff",
            fg="#64748b"
        ).pack(anchor="w")

        value = tk.Label(
            body,
            text="0",
            font=("Times New Roman", 24, "bold"),
            bg="#ffffff",
            fg=color
        )
        value.pack(anchor="w", pady=(10, 0))

        return card, value

    def show_page(self, page):
        self.current_page.set(page)

        self.report_page.pack_forget()
        self.admin_page.pack_forget()

        if page == "report":
            self.report_page.pack(fill="both", expand=True)
        else:
            self.admin_page.pack(fill="both", expand=True)

        self.refresh_nav_state()

    def refresh_nav_state(self):
        for key, btn in self.nav_buttons.items():
            if key == self.current_page.get():
                btn.configure(bg="#2563eb", fg="white")
            else:
                btn.configure(bg="#1f2937", fg="#e5e7eb")

    def claim_item(self):
        claim_win = tk.Toplevel(self.window)
        claim_win.title("Claim Item")
        claim_win.geometry("780x640")
        claim_win.configure(bg="#0f172a")
        claim_win.transient(self.window)
        claim_win.grab_set()

        shell = tk.Frame(claim_win, bg="#0f172a")
        shell.pack(fill="both", expand=True, padx=18, pady=18)

        card, body = self.make_card(shell, "Claim Selected Item", "Provide proof to complete the claim.", "#1d4ed8")
        card.pack(fill="both", expand=True)

        form = tk.Frame(body, bg="#ffffff")
        form.pack(fill="x")

        tk.Label(form, text="Your Full Name", font=("Times New Roman", 12, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", pady=10)
        tk.Entry(form, width=46, font=("Times New Roman", 12), bg="#f8fafc", relief="solid", bd=1).grid(row=0, column=1, sticky="ew", pady=10, ipady=6)

        tk.Label(form, text="Your Contact", font=("Times New Roman", 12, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", pady=10)
        tk.Entry(form, width=46, font=("Times New Roman", 12), bg="#f8fafc", relief="solid", bd=1).grid(row=1, column=1, sticky="ew", pady=10, ipady=6)

        tk.Label(form, text="Proof of Ownership", font=("Times New Roman", 12, "bold"), bg="#ffffff").grid(row=2, column=0, sticky="nw", pady=10)
        tk.Text(form, width=46, height=8, font=("Times New Roman", 12), bg="#f8fafc", relief="solid", bd=1).grid(row=2, column=1, sticky="ew", pady=10)

        form.columnconfigure(1, weight=1)

        button_row = tk.Frame(body, bg="#ffffff")
        button_row.pack(fill="x", pady=(18, 0))

        ttk.Button(button_row, text="Submit Claim", command=lambda: None, style="Success.TButton").pack(side="left", padx=(0, 10))
        ttk.Button(button_row, text="Cancel Claim", command=claim_win.destroy, style="Primary.TButton").pack(side="left")

    def submit_report(self):
        messagebox.showinfo("UI Demo", "Submit button clicked.")

    def search_bar(self):
        pass

    def refresh_from_source(self):
        pass

    def delete_selected_item(self):
        pass

    def run(self):
        self.window.mainloop()


application = LostandFoundInventoryUI()
application.run()
