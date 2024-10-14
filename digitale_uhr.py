
import tkinter
import time

def uhrzeit_aktualisieren():
    aktuelle_uhrzeit = time.strftime("%H:%M:%S")
    uhr_label.config(text=aktuelle_uhrzeit)
    uhr_label.after(1000, uhrzeit_aktualisieren)



main_window = tkinter.Tk()
uhr_label = tkinter.Label(main_window, font=("Helvetica, 48"), bg="whitesmoke", fg="grey")
uhr_label.pack(anchor="center")

main_window.title("Digitale Uhr")
main_window.geometry("300x100")

uhrzeit_aktualisieren()

main_window.mainloop()


