import tkinter as tk
from tkinter import ttk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        # disable resizing
        self.resizable(False, False)
        self.geometry("800x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # main frame
        self.mainframe = ttk.Frame(self)
        self.mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        # add 5 rows of 5 buttons that delete themselves on click
        # keep the buttons stacked on the left of the grid
        self.buttons_matrix = []
        self.id_counter = 0
        for row_index in range(5):
            matrix_row = []
            for column_index in range(5):
                matrix_button = {}
                matrix_button["id"] = self.id_counter
                matrix_button["button"] = ttk.Button(
                    self.mainframe,
                    text=f"button row#{row_index} col#{column_index}",
                    command=lambda button_id=self.id_counter: self.delete_button(button_id)
                )
                matrix_button["button"].grid(column=column_index, row=row_index, padx=10, pady=10)
                matrix_row.append(matrix_button)
                self.id_counter += 1
            self.buttons_matrix.append(matrix_row)
        # run the app
        self.mainloop()

    def delete_button(self, button_id):
        # print(f"deleting button with id#{button_id}")
        # find the position of the button to delete
        for row_index in range(len(self.buttons_matrix)):
            for column_index in range(len(self.buttons_matrix[row_index])):
                if self.buttons_matrix[row_index][column_index]["id"] == button_id:
                    button_coords = {
                        "x": column_index,
                        "y": row_index
                    }
                    break
        # print(button_coords)
        # delete the button
        # self.buttons_matrix[row_index][column_index].destroy()
        self.buttons_matrix[button_coords["y"]].pop(button_coords["x"])["button"].destroy()
        # regrid the buttons on the right of the deleted buttons
        for column_index_right in range(button_coords["x"], len(self.buttons_matrix[button_coords["y"]])):
            # print(column_index_right)
            self.buttons_matrix[button_coords["y"]][column_index_right]["button"].grid(column=column_index_right, row=button_coords["y"])


if __name__ == "__main__":
    Application()
