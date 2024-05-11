import tkinter as tk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Application de Gestion de Planning")
        self.geometry("800x600")
        self.configure(bg="#CCE2F3")
        self.pages = {"planning": PlanningPage, "Patient": PatientPage, "Médecin": MedecinPage}
        self.current_page = None
        self.create_navigation_bar()
        self.show_page("planning")

    def create_navigation_bar(self):
        navigation_bar = tk.Frame(self, bg="white", height=70)
        navigation_bar.pack(side="top", fill="x")
        for page_name in self.pages.keys():
            button = tk.Button(navigation_bar, text=page_name, command=(lambda page=page_name: self.show_page(page)),
                               font=("Arial", 16), width=10, height=2, bg="#CCE2F3")
            button.pack(side="left", padx=10, pady=10)

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = self.pages[page_name](self)
        self.current_page.pack(side="top", fill="both", expand=True)


class BasePage(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.configure(bg="#CCE2F3")


class PlanningPage(BasePage):

    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Page Planning", font=("Arial", 24), bg="#CCE2F3")
        label.pack(pady=20)
        consultation_button = tk.Button(self, text="État de consultation", command=self.etat_de_consultationPage,
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        consultation_button.place(x=50, y=200)
        ouverture_disponibilite_button = tk.Button(self, text="ouverture_disponibilite", command=self.ouverture_disponibilitePage,
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        ouverture_disponibilite_button.place(x=50, y=125)

    def etat_de_consultationPage(self):
        etat_de_consultation = tk.Toplevel(self)
        etat_de_consultation.title("État de consultation")
        etat_de_consultation.geometry("300x200")
        label = tk.Label(etat_de_consultation, text="état de consultation", font=("Arial", 16))
        label.pack(pady=20)

    def ouverture_disponibilitePage(self):
        ouverture_disponibilite = tk.Toplevel(self)
        ouverture_disponibilite.title("Ouverture Disponibilité")
        ouverture_disponibilite.geometry("300x200")
        label = tk.Label(ouverture_disponibilite, text="Ouverture Disponibilité", font=("Arial", 16))
        label.pack(pady=20)


class PatientPage(BasePage):

    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Page Patient", font=("Arial", 24), bg="#CCE2F3")
        label.pack(pady=20)
        modif_patient_button = tk.Button(self, text="Modifier", command=self.modif_patientPage,
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        modif_patient_button.place(x=50, y=450)
        supprimer_patient_button = tk.Button(self, text="Supprimer",
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        supprimer_patient_button.place(x=250, y=450)

    def modif_patientPage(self):
        modif_patient = tk.Toplevel(self)
        modif_patient.title("Modifier patient")
        modif_patient.geometry("300x200")
        label = tk.Label( modif_patient, text="modifier...", font=("Arial", 16))
        label.pack(pady=20)


class MedecinPage(BasePage):

    def __init__(self, master):
        super().__init__(master)
        label = tk.Label(self, text="Page Médecin", font=("Arial", 24), bg="#CCE2F3")
        label.pack(pady=20)
        modif_medecin_button = tk.Button(self, text="Modifier", command=self.modif_medecinPage,
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        modif_medecin_button.place(x=50, y=450)
        supprimer_medecin_button = tk.Button(self, text="Supprimer",
                                        font=("Arial", 12), bg="#305F82", bd=0, relief="flat", width=17, height=2)
        supprimer_medecin_button.place(x=250, y=450)
        Nv_medecin_button = tk.Button(self, text="Nouveaux medecins", command=self.Nv_medecinPage,
                                        font=("Arial", 12), bg="#009471", bd=0, relief="flat", width=17, height=2)
        Nv_medecin_button.place(x=550, y=450)

    def modif_medecinPage(self):
        modif_patient = tk.Toplevel(self)
        modif_patient.title("Modifier medecin")
        modif_patient.geometry("300x200")

        label = tk.Label( modif_patient, text="modifier...", font=("Arial", 16))
        label.pack(pady=20)

    def Nv_medecinPage(self):
        Nv_medecin = tk.Toplevel(self)
        Nv_medecin.title("Nouveaux medecin")
        Nv_medecin.geometry("300x200")

        label = tk.Label( Nv_medecin, text="Nouveaux medecin", font=("Arial", 16))
        label.pack(pady=20)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
    # print("after")

