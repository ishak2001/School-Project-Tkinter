from tkinter import *
from local.System_app import *
from local.Kunde import *
from turtle import bgcolor, color
import mysql.connector

# SQL Verbindung
verbindung = mysql.connector.connect (host="localhost", user="root", passwd="", database="deutschebahn")

# Main Fenster
window = Tk()
window.geometry("450x450")

#Aktueller Standort Neuss
Zugliste = []
Zugliste.append(System_app("13:30 Uhr", "15:08", "3", "Grevenbroich"))
Zugliste.append(System_app("13:35 Uhr", "15:10", "6", "Neuss Norf"))
Zugliste.append(System_app("13:40 Uhr", "15:20", "7", "Kaarster See"))
Zugliste.append(System_app("14:00 Uhr", "15:25", "5", "Düsseldorf"))
Zugliste.append(System_app("14:10 Uhr", "15:45", "8", "Dormagen"))
Zugliste.append(System_app("14:30 Uhr", "16:00", "1", "Köln"))

# Seite 1
def Startseite():
    
    window.title("DB Navigator")

    ueberschrift = Label(window, text="Herzlich Willkommen in der Deutschen Bahn App")
    ueberschrift.place(relx=0.5, rely=0.05, anchor='center')

    beschreibung = Label(window, text="Möchtest du die Pläne Online oder Local nachschauen?")
    beschreibung.place(relx=0.5, rely=0.10, anchor='center')

    local_button = Button(window, text="Online", command=Online)
    local_button.grid(column=0, row=3)
    local_button.place(relx=0.6, rely=0.5, anchor='center')
    
    online_button = Button(window, text="Local", command=Local)
    online_button.grid(column=0, row=3)
    online_button.place(relx=0.4, rely=0.5, anchor='center')
    
    admin_bereich = Button(text="Administrator Bereich", command=Administrator, bg='red', font='w', fg='black')
    admin_bereich.pack(fill=X, expand=TRUE, anchor='s')

    window.mainloop()

# Offline Anzeige
def Local():
    window.destroy() #<- Startseite
    
    locale_anzeige = Tk()
    locale_anzeige.geometry("510x450")
    locale_anzeige.title("Locale Anzeige")
    
    i = -1
    
    for Anzeige in Zugliste:
        
        a = i + 1

        p = Zugliste[a].liefereAnkunftZeit()
        h = Zugliste[a].liefereAbfahrtsZeit()
        o = Zugliste[a].liefereGleis()
        q = Zugliste[a].liefereNach()
        
        i = i + 1
        
        Anzeige = Label(locale_anzeige,text="Ankunft: " + p + "| Nach: " + q + "| Auf Gleis: " + o + "| Abfahrt um " + h + " Uhr" )
        Anzeige.grid(row=i)
    
# Online Anzeige (Datenbank)
def Online():
    
    window.destroy() #<- Startseite
    
    online_anzeige = Tk()
    online_anzeige.geometry("460x450")
    online_anzeige.title("Online Anzeige")

    abfrage = verbindung.cursor()
    abfrage.execute("SELECT * FROM liste")

    ergebnis = abfrage.fetchall()
    
    i = 0
    for id_bahn, bahn, ankunft, abfahrt, gleis, reise_nach in ergebnis:
        a = i + 1
        i = i+1
        ergebnis = Label(online_anzeige, text=str(id_bahn) + ") " + " Die: " + bahn + " Nach:" + reise_nach + " Ankunft: " + ankunft + " Uhr " + " Abfahrt: " + abfahrt + " Auf Gleis: " + gleis)
        ergebnis.grid(row=i)

# Admin Daten Ändern
def Administrator():
    
    window.destroy() #<- Startseite
    
    login = Tk()
    login.geometry("450x450")
    login.title("DB Login")
    
    login_title = Label(login, text="Melde dich bitte mit deinen Daten an")
    login_title.place(relx=0.5, rely=0.10, anchor='center')
    
    # Nutzername
    Nutzername = Label(login, text="Nutzername: ")
    Nutzername.grid(row = 0, column = 0)
    Nutzername.place(relx=0.2, rely=0.44, anchor='center')
    
    # Nutzername Eingabe
    Nutzername_eingabe = Entry(login, bd=3, width=30)
    Nutzername_eingabe.grid(row = 3, column = 0)
    Nutzername_eingabe.place(relx=0.5, rely=0.44, anchor='center')
    
    # Passwort
    Passwort = Label(login, text="Passwort: ")
    Passwort.grid(row = 3, column = 0)
    Passwort.place(relx=0.2, rely=0.5, anchor='center')
    
    # Passwort Eingabe
    passwort_eingabe = Entry(login, bd=3, width=30)
    passwort_eingabe.grid(row = 3, column = 0)
    passwort_eingabe.place(relx=0.5, rely=0.5, anchor='center')
    
    #Anmelden Button
    Anmelden = Button(login, text='Anmelden', command=admin_seite)
    Anmelden.grid(row = 3, column = 0)
    Anmelden.place(relx=0.4, rely=0.6, anchor='center')
    
    #Abrechen Button
    Abrechen = Button(login, text='Abrechen', command=quit)
    Abrechen.grid(row = 3, column = 0)
    Abrechen.place(relx=0.6, rely=0.6, anchor='center')
    
def admin_seite():
    
    admin_fenster = Tk()
    admin_fenster.geometry("450x450")
    admin_fenster.title("DB Login")
    
    admin_button = Button(admin_fenster, text='Tabelle Erstellen', command="")
    admin_button.grid(row = 3, column = 0)
    
    admin_button = Button(admin_fenster, text='Tabelle Erstellen', command="")
    admin_button.grid(row = 4, column = 0)

Startseite()