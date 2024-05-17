import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta


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

    def __init__(self):
        super().__init__()
        # add a date entry
        self.date_entry_widget = DateEntry(self, mindate=datetime(year=2020, month=1, day=1), locale="fr_FR")
        self.date_entry_widget.grid(column=0, row=0)
        # run the app
        self.mainloop()


if __name__ == "__main__":
    # ApplicationCalendar()
    ApplicationDateEntry()
