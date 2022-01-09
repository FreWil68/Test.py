import sqlite3
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

# Main Window creation
main = Tk()
main.title("Gestion appartement")
main.geometry("1000x700")
main.config(background="lightgrey")

# Variables definition
date_facture_electricite = IntVar()
montant_facture_electricite = IntVar()


# Create database named "Appartement_database"
def send_data_to_electricite_table():
    conn = sqlite3.connect('Appartement_database.db')

    with conn: cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS Electricite (date_facture_electricite TEXT,montant_facture_electricite TEXT)')
    print("Database created successfully")

    date_fact_electricite = date_facture_electricite.get()
    montant_fact_electricite = montant_facture_electricite.get()

    cursor.execute('INSERT INTO Electricite (date_facture_electricite,montant_facture_electricite) VALUES(?,?)',
                   (date_fact_electricite, montant_fact_electricite,))
    print("Electricity table updated successfully")
    print(cursor.fetchall())
    conn.commit()

def create_window_electricite():
    # electricity window creation
    window_electricite = Tk()
    window_electricite.title("Dépenses en électricité")
    window_electricite.geometry("800x500")
    window_electricite.config(background="lightgrey")

    # date entry
    label_date_facture_elec = Label(window_electricite, text="Date de la facture", bg="lightgrey")
    label_date_facture_elec.place(x=20, y=80)

    entry_date_facture_elec = DateEntry(window_electricite, selectmode="day", textvar=date_facture_electricite)
    entry_date_facture_elec.place(x=130, y=80)

    # entry of the invoice amount
    label_montant_facture_elec = Label(window_electricite, text="Montant", bg="lightgrey")
    label_montant_facture_elec.place(x=20, y=110)
    entry_montant_facture_elec = Entry(window_electricite, width=30, textvar=montant_facture_electricite)
    entry_montant_facture_elec.place(x=130, y=110)

    # display database in a frame
    frame_electricite = Frame(window_electricite, height=450, width=400, bg="white")
    frame_electricite.place(x=370, y=20)

    bouton1 = Button(window_electricite, text="Ajouter", command=send_data_to_electricite_table)
    bouton1.place(x=50, y=180)

    bouton2 = Button(window_electricite, text="Supprimer")
    bouton2.place(x=112, y=180)

    bouton1 = Button(window_electricite, text="Modifier")
    bouton1.place(x=190, y=180)


# Création de la fenetre principale nommée main
def create_main_window():
    # Création d'une barre de menu dans la fenêtre main :
    menubar = Menu(main)
    main.config(menu=menubar)

    # Ajouter le menu Fichier et son sous-menu "Exit" dans la barre de menu
    menufichier = Menu(menubar)
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_cascade(label='Exit', command=main.destroy, )

    # Ajouter le menu Affichage dans la barre de menu
    menuaffichage = Menu(menubar)
    menubar.add_cascade(label="Affichage", menu=menuaffichage)

    # Ajouter Menu "Dépenses" avec ses sous-menus dans "menuaffichage"
    sub_menu = Menu(menuaffichage)
    sub_menu.add_command(label="Electricité", command=create_window_electricite)
    sub_menu.add_command(label="2")
    sub_menu.add_command(label="3")
    menuaffichage.add_cascade(label='Dépenses', menu=sub_menu)

    # Ajouter le menu "Recettes" dans "menuaffichage"
    menuaffichage.add_command(label='Recettes', command=main.destroy, )

    # Affichage de la fenêtre créée :
    main.mainloop()


# Création de la fenetre  "password_window"
def create_password_window():
    password_window = Tk()
    password_window.title("Connexion")
    password_window.geometry("400x120")
    password_window.resizable(width=False, height=False)
    password_window.config(background="lightgrey")

    # pour saisir l'identifiant
    username_label = Label(password_window, text="Utilisateur", background="lightgrey")
    username_entry = Entry(password_window, width=30)
    username_label.place(x=60, y=20)
    username_entry.place(x=140, y=20)

    # pour saisir le mot de passe
    password_label = Label(password_window, text="Mot de passe", background="lightgrey")
    pasword_entry = Entry(password_window, width=30)
    password_label.place(x=60, y=50)
    pasword_entry.place(x=140, y=50)

    def validate_password():  # Validation du mot de passe si bouton "Connexion" est cliqué
        username = "admin"
        motdepasse = "123"
        if username_entry.get() == username and pasword_entry.get() == motdepasse:
            password_window.destroy()
            create_main_window()

        else:
            messagebox.showwarning("Message", "Identifiant ou mot de passe incorrect")

    # Bouton "Connexion" pour valider le mot de passe
    bouton = Button(password_window, text="Connexion", command=validate_password)
    bouton.pack()
    bouton.place(x=170, y=85)

    password_window.mainloop()


# create_password_window()
create_main_window()
