import tkinter as tk
from tkinter import ttk
from ui.student_tab import StudentTab
from ui.admin_tab import AdminTab


class MainWindow:
    def __init__(self, controller):
        self.controller = controller

        self.window = tk.Tk()
        self.window.title("HKMU Lost & Found Management System")
        self.window.geometry("1280x780")
        self.window.configure(bg="#f3f6fb")

        self.setup_styles()

        outer = tk.Frame(self.window, bg="#f3f6fb")
        outer.pack(fill="both", expand=True, padx=18, pady=18)

        header = tk.Frame(outer, bg="#f3f6fb")
        header.pack(fill="x")

        tk.Label(header,
                 text="HKMU Lost & Found Management System",
                 font=("Times New Roman", 26, "bold"),
                 bg="#f3f6fb").pack(anchor="w")

        notebook = ttk.Notebook(outer, style="App.TNotebook")
        notebook.pack(fill="both", expand=True)

        self.student_tab = StudentTab(notebook, controller)
        self.admin_tab = AdminTab(notebook, controller)

        notebook.add(self.student_tab.frame, text=" Reporting & Searching ")
        notebook.add(self.admin_tab.frame, text=" Administrator ")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("App.TNotebook.Tab",
                        font=("Times New Roman", 12, "bold"),
                        padding=(20, 10))

    def run(self):
        self.window.mainloop()