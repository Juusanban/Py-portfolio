import tkinter as tk
from tkinter import ttk

from logic import *
from excel_export import export_excel
from anki_export import export_anki


root = tk.Tk()
root.title("Dictionary Builder")
root.geometry("1000x700")

root.option_add("*Font", "Arial 12")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


# HOME

home_tab = tk.Frame(notebook)
notebook.add(home_tab, text="Home")

tk.Label(
    home_tab,
    text="Vocabulary Builder",
    font=("Arial", 18)
).pack(pady=40)


def open_tab(name, japanese):

    for tab in notebook.tabs():
        if notebook.tab(tab, "text") == name:
            notebook.select(tab)
            return

    create_language_tab(name, japanese)


tk.Button(
    home_tab,
    text="English",
    width=20,
    command=lambda: open_tab("English", False)
).pack(pady=10)

tk.Button(
    home_tab,
    text="Japanese",
    width=20,
    command=lambda: open_tab("Japanese", True)
).pack(pady=10)


#  LANGUAGE TAB

def create_language_tab(name, japanese):

    tab = tk.Frame(notebook)
    notebook.add(tab, text=name)
    notebook.select(tab)

    tab.grid_rowconfigure(1, weight=1)
    tab.grid_columnconfigure(1, weight=1)

    # LIST

    listbox = tk.Listbox(tab, width=30)
    listbox.grid(row=0, column=0, rowspan=3, sticky="ns", padx=10, pady=10)

    # SEARCH BAR

    search_frame = tk.Frame(tab)
    search_frame.grid(row=0, column=1, columnspan=2)

    search_var = tk.StringVar()

    tk.Label(search_frame, text="Search").pack(side="left")

    search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
    search_entry.pack(side="left", padx=5)

    #  INPUT FIELDS

    form_frame = tk.Frame(tab)
    form_frame.grid(row=1, column=1, sticky="nw", padx=10, pady=200)

    tk.Label(form_frame, text="Word").grid(row=0, column=0, sticky="w")

    entry_word = tk.Entry(form_frame, width=30)
    entry_word.grid(row=0, column=1, pady=15)

    if japanese:

        tk.Label(form_frame, text="Reading").grid(row=1, column=0, sticky="w")

        entry_reading = tk.Entry(form_frame, width=30)
        entry_reading.grid(row=1, column=1, pady=15)

    else:

        entry_reading = None

    tk.Label(form_frame, text="Meaning").grid(row=2, column=0, sticky="w")

    entry_meaning = tk.Entry(form_frame, width=30)
    entry_meaning.grid(row=2, column=1, pady=15)

    #  EDIT BUTTONS

    button_frame = tk.Frame(tab)
    button_frame.grid(row=1, column=2, sticky="n", padx=30,pady=200)

    #  FUNCTIONS

    def refresh(data=None):

        listbox.delete(0, tk.END)

        if data is None:
            data = get_cards()

        for c in data:
            listbox.insert(tk.END, " | ".join(c))

    def select_card(event):

        if not listbox.curselection():
            return

        index = listbox.curselection()[0]

        card = get_cards()[index]

        entry_word.delete(0, tk.END)
        entry_word.insert(0, card[0])

        if japanese:

            entry_reading.delete(0, tk.END)
            entry_reading.insert(0, card[1])

            entry_meaning.delete(0, tk.END)
            entry_meaning.insert(0, card[2])

        else:

            entry_meaning.delete(0, tk.END)
            entry_meaning.insert(0, card[1])

    listbox.bind("<<ListboxSelect>>", select_card)

    def do_search():

        q = search_var.get()

        if q == "":
            refresh()
        else:
            refresh(search_cards(q))

    def add():

        word = entry_word.get()

        if not word:
            return

        if japanese:
            reading = entry_reading.get()
        else:
            reading = None

        meaning = entry_meaning.get()

        if not meaning:
            return

        add_card(word, reading, meaning)
        refresh()

    def update():

        if not listbox.curselection():
            return

        index = listbox.curselection()[0]

        word = entry_word.get()

        if japanese:
            reading = entry_reading.get()
        else:
            reading = None

        meaning = entry_meaning.get()

        update_card(index, word, reading, meaning)
        refresh()

    def delete():

        if not listbox.curselection():
            return

        index = listbox.curselection()[0]

        delete_card(index)
        refresh()

    #  BUTTONS

    tk.Button(search_frame, text="Search", command=do_search).pack(side="left", padx=5)

    tk.Button(button_frame, text="Add", width=10, command=add).pack(pady=5)

    tk.Button(button_frame, text="Update", width=10, command=update).pack(pady=5)

    tk.Button(button_frame, text="Delete", width=10, command=delete).pack(pady=5)

    #  EXPORT BUTTONS

    export_frame = tk.Frame(tab)
    export_frame.grid(row=2, column=2, sticky="se", padx=20, pady=20)

    tk.Button(
        export_frame,
        text="Excel",
        width=10,
        command=lambda: export_excel(get_cards())
    ).pack(side="left", padx=5)

    tk.Button(
        export_frame,
        text="Anki",
        width=10,
        command=lambda: export_anki(get_cards())
    ).pack(side="left", padx=5)

    refresh()


root.mainloop()