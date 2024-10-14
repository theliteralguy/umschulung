
import tkinter

main_window = tkinter.Tk()
uhr_label = tkinter.Label(main_window, font = ('Helvetica, 48'), bg =  'whitesmoke' , fg = 'grey' )
uhr_label.pack(anchor = 'center')

main_window.title('Digitale Uhr')
main_window.geometry('300x100')

main_window.mainloop()