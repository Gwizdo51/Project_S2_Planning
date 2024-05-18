import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta
import re


class ApplicationCalendar(tk.Tk):

    def __init__(self):
        super().__init__()
        # add a calendar
        self.calendar_widget = Calendar(self, mindate=datetime(year=2020, month=1, day=1), locale="fr_FR")
        self.calendar_widget.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # add an event on click
        self.calendar_widget.bind("<<CalendarSelected>>", self.print_selected_date)
        # run the app
        self.mainloop()

    def print_selected_date(self, event):
        print("date selected:", self.calendar_widget.get_date())
        self.selected_date = datetime.strptime(self.calendar_widget.get_date(), "%d/%m/%Y")
        print(self.selected_date)
        # get the day of the week
        # 0: monday
        # 6: sunday
        print("weekday number:", self.selected_date.weekday())
        # get the date of the monday of the selected week
        print("date of monday:", self.selected_date - timedelta(days=self.selected_date.weekday()))


class ApplicationDateEntry(tk.Tk):

    date_pattern = re.compile(r"^(\d{2})\/(\d{2})\/(\d{4})$")

    def __init__(self):
        super().__init__()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # add a mainframe
        self.mainframe = ttk.Frame(self, borderwidth=2, relief="solid")
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        # add a date entry
        self.selected_date = tk.StringVar()
        self.date_entry_widget = DateEntry(self.mainframe, textvariable=self.selected_date, mindate=datetime(year=2020, month=1, day=1), locale="fr_FR")
        self.date_entry_widget.grid(column=0, row=0, sticky=(tk.E, tk.W))
        # add a button to check the value of self.selected_date
        self.check_button = ttk.Button(self.mainframe, text="check", command=self.check_selected_date_validity)
        self.check_button.grid(column=0, row=1, sticky=(tk.E, tk.W))
        # run the app
        self.mainloop()

    def check_selected_date_validity(self):
        # print(self.selected_date.get())
        # check date format with regular expression
        # ^(\d{2})\/(\d{2})\/(\d{4})$
        match_obj = self.date_pattern.match(self.selected_date.get())
        # print(bool(match_obj))
        date_is_valid = False
        if match_obj:
            groups = match_obj.groups()
            day_number = int(groups[0])
            month_number = int(groups[1])
            year_number = int(groups[2])
            # print("day:", day_number, "- month:", month_number, "- year:", year_number)
            try:
                datetime(year_number, month_number, day_number)
                date_is_valid = True
            except ValueError as e:
                # print("the date is incorrect :", e)
                pass
        if date_is_valid:
            print("the date is valid")
        else:
            print("the date is not valid")


if __name__ == "__main__":
    # ApplicationCalendar()
    ApplicationDateEntry()
