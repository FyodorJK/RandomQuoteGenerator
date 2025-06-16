import tkinter as tk
from Adatbazis_kezelo import AdatbazisKezelo
from tkinter import messagebox

def GUI_kezelo():
    class RandomQuoteGenerator:
        def __init__(self, master):
            self.master = master
            self.master.title("Random Quote Generátor")
            self.adatbazisom = AdatbazisKezelo()

            self.quote_szoveg = tk.Label(master, text="Quote:")
            self.quote_szoveg.pack()

            self.quote_bemeno = tk.Entry(master)
            self.quote_bemeno.pack()

            self.iro_szoveg = tk.Label(master, text="Író:")
            self.iro_szoveg.pack()

            self.iro_bemenet = tk.Entry(master)
            self.iro_bemenet.pack()

            self.hozzaado_gomb = tk.Button(master, text="Hozzáadás", command=self.quote_hozzaadasa)
            self.hozzaado_gomb.pack()

            self.mutato_gomb = tk.Button(master, text="Összes quote mutatása", command=self.quote_mutatas)
            self.mutato_gomb.pack()

            self.mutato_gomb = tk.Button(master, text="Random quote", command=self.random_quote)
            self.mutato_gomb.pack()

        def quote_hozzaadasa(self):
            quote = self.quote_bemeno.get()
            iro = self.iro_bemenet.get()
            if quote and iro:
                self.adatbazisom.adat_beszuro(quote, iro)
                messagebox.showinfo("Siker", "Quote sikeresen hozzáadva!")
                self.quote_bemeno.delete(0, tk.END)
                self.iro_bemenet.delete(0, tk.END)
            else:
                messagebox.showwarning("Hiba", "Mind kettő mezőt ki kell tölteni.")

        def quote_mutatas(self):
            quoteok = self.adatbazisom.osszes_adat_lekerdezo()
            if quoteok:
                quoteok_szoveg = "\n".join([f"{q[1]} - {q[2]}" for q in quoteok])
                messagebox.showinfo("Osszes quote", quoteok_szoveg)
            else:
                messagebox.showinfo("Nincs quote", "Nincs quote az adatbázisban.")

        def random_quote(self):
            quote = self.adatbazisom.random_quote_kereso()
            if quote:
                messagebox.showinfo("Random Quote", quote)
            else:
                messagebox.showinfo("Nincs quote", "Nincs quote az adatbázisban.")

    alap = tk.Tk()
    app = RandomQuoteGenerator(alap)
    alap.mainloop()
