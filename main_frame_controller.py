import tkinter as tk

from book import Book
from gui import MainFrame
import json

from person import Person


class MainFrameController():

    def __init__(self, main_frame: MainFrame):
        self._person_dict = dict()
        self._main_frame = main_frame
        self._main_frame.on_choose_person_event.add(self._on_choose_person)
        self._main_frame.on_add_event.add(self._on_add)

    def load_from_file(self):
        with open("list.txt", "r") as read_file:
            strings = json.load(read_file)
        for string in strings.keys():
            books = list(map(Book, strings[string]))
            self._person_dict[Person(string)] = books
        self._main_frame.update_combobox(list(self._person_dict.keys()))

    def save_to_file(self):
        with open("list.txt", "w") as write_file:
            strings = dict()
            for person in self._person_dict:
                books = self._person_dict[person]
                strings[person.name] = [o.name for o in books]
            write_file.write(json.dumps(strings, sort_keys=True, indent=4))

    def _on_choose_person(self):
        person_str = self._main_frame.person
        current_person = None

        for person in self._person_dict.keys():
            if person_str == person.name:
                current_person = person
        if current_person is not None:
            self._main_frame.load_books(self._person_dict[current_person])

    def _on_add(self):
        new_person_str = self._main_frame.new_person
        new_person = None
        for person in self._person_dict.keys():
            if new_person_str == person.name:
                new_person = person
        if new_person is None:
            new_person = Person(new_person_str)
        new_book = Book(self._main_frame.new_book)
        if new_person not in self._person_dict:
            self._person_dict[new_person] = []
        self._person_dict[new_person].append(new_book)
        self._main_frame.update_combobox(list(self._person_dict.keys()))
        self._on_choose_person()
