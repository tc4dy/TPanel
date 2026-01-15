import tkinter as tk
import sys

def exit_bsod(event):
    root.destroy()
    sys.exit()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='#0078D7')
root.bind('<Escape>', exit_bsod)
root.bind('<Button-1>', exit_bsod)

label_sad = tk.Label(root, text=":(", font=("Segoe UI", 100), fg="white", bg="#0078D7", justify="left")
label_sad.place(x=100, y=100)

msg_text = """Your PC ran into a problem and needs to restart.
We're just collecting some error info, and then we'll restart for you.

20% complete"""

label_text = tk.Label(root, text=msg_text, font=("Segoe UI", 25), fg="white", bg="#0078D7", justify="left")
label_text.place(x=100, y=300)

qr_text = """
For more information about this issue and possible fixes, visit https://www.windows.com/stopcode

If you call a support person, give them this info:
Stop code: CRITICAL_PROCESS_DIED
"""
label_qr = tk.Label(root, text=qr_text, font=("Segoe UI", 14), fg="white", bg="#0078D7", justify="left")
label_qr.place(x=100, y=500)

root.mainloop()