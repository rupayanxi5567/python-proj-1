from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def retstart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shuttingdown():
    os.system("shutdown /s /t 1")



shut_down = Tk()

shut_down.title("Shutdown, Restart your PC")
shut_down.geometry("500x500")
shut_down.config(bg="black")



restart_button = Button(shut_down, text="Restart", font=("Time New Roman", 15 , "bold"), relief=RAISED, cursor="plus", command=restart )

restart_button.place(x=200, y=60, height=50, width=150)


restart_time_button = Button(shut_down, text="Restart in time", font=("Time New Roman", 15 , "bold"), relief=RAISED, cursor="plus", command=retstart_time )

restart_time_button.place(x=200, y=150, height=50, width=150)


log_out_button = Button(shut_down, text="Log-Out", font=("Time New Roman", 15 , "bold"), relief=RAISED, cursor="plus", command=logout )

log_out_button.place(x=200, y=240, height=50, width=150)


shut_down_button = Button(shut_down, text="Shut Down", font=("Time New Roman", 15 , "bold"), relief=RAISED, cursor="plus", command=shuttingdown )

shut_down_button.place(x=200, y=330, height=50, width=150)



shut_down.mainloop()