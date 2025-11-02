from tkinter import *

def sayaç(toplam_saniye):
    if toplam_saniye >= 0:
        saat, kalan = divmod(toplam_saniye, 3600)
        dakika, saniye = divmod(kalan, 60)
        zaman_str = f"{saat:02d}:{dakika:02d}:{saniye:02d}"

        label.config(text=zaman_str)
        window.after(1000, sayaç, toplam_saniye - 1)
    else:
        label.config(text="Süre doldu!")


window = Tk()
window.title("Zaman Sayacı")
window.geometry("400x200")
window.configure(bg="black")

label = Label(window, font=("ds-digital", 50), bg="black", fg="white")
label.pack(anchor="center", pady=50)

zaman = 10
sayaç(zaman)

window.mainloop()
