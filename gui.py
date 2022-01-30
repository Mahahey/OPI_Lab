import tkinter as tk
from tkinter import ttk

from event_source import Event, EventSource


class MainFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self._on_click_person_event_source = EventSource()
        self._on_add_event_source = EventSource()
        self.__fill_frame()

    @property
    def on_choose_person_event(self) -> Event:
        return self._on_click_person_event_source.event

    @property
    def on_add_event(self) -> Event:
        return self._on_add_event_source.event

    @property
    def person(self) -> str:
        return self._person_combobox.get()

    @property
    def new_person(self) -> str:
        return self._name_entry.get()

    @property
    def new_book(self) -> str:
        return self._book_entry.get()

    def update_combobox(self, list):
        str_list = [o.name for o in list]
        self._person_combobox.config(values=str_list)

    def load_books(self, books):
        if not self._books_listbox.size() == 0:
            self._books_listbox.delete(0, self._books_listbox.size() - 1)
        for book in books:
            self._books_listbox.insert(0, book.name)

    def __fill_frame(self):
        self._top_frame = tk.Frame(master=self)
        self._top_frame.pack()

        self._person_combobox = ttk.Combobox(master=self._top_frame)
        self._person_combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._person_combobox.bind(
            "<<ComboboxSelected>>",
            lambda x: self._on_click_person_event_source.notify_all()
        )

        self._books_listbox = tk.Listbox(master=self._top_frame)
        self._books_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self._bottom_frame = tk.Frame(master=self)
        self._bottom_frame.pack()

        name_label = tk.Label(master=self._bottom_frame, text="Person")
        name_label.pack(side=tk.LEFT)

        self._name_entry = tk.Entry(master=self._bottom_frame)
        self._name_entry.pack(side=tk.LEFT)

        book_label = tk.Label(master=self._bottom_frame, text="Book")
        book_label.pack(side=tk.LEFT)

        self._book_entry = tk.Entry(master=self._bottom_frame)
        self._book_entry.pack(side=tk.LEFT)

        self._add_button = tk.Button(
            master=self._bottom_frame,
            text="Add",
            command=self._on_add_event_source.notify_all
        )
        self._add_button.pack(side=tk.LEFT)


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._on_load_event_source = EventSource()
        self._on_close_event_source = EventSource()
        self.__fill_frame()
        self.after(100, self._on_load_event_source.notify_all)

    @property
    def on_load_event(self) -> Event:
        return self._on_load_event_source.event

    @property
    def on_close_event(self) -> Event:
        return self._on_close_event_source.event

    @property
    def main_frame(self) -> MainFrame:
        return self._main_frame

    def _on_close(self):
        self._on_close_event_source.notify_all()

    def __fill_frame(self):
        self._main_frame = MainFrame(self)
        self._main_frame.pack()


if __name__ == '__main__':
    from main_window_controller import MainWindowController
    root = MainWindow()
    main_controller = MainWindowController(root)
    root.mainloop()