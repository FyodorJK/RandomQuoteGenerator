import sqlite3

class AdatbazisKezelo:
    def __init__(self, db_name="adatbazis.db"):
        self.db_name = db_name
        self.adatbazis_letrehozo()

    def adatbazis_letrehozo(self):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('''
            CREATE TABLE IF NOT EXISTS quotes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')
        kapcsolat.commit()
        kapcsolat.close()

    def adat_beszuro(self, quote, author):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('''
            INSERT INTO quotes (quote, author) VALUES (?, ?)
        ''', (quote, author))
        kapcsolat.commit()
        kapcsolat.close()

    def osszes_adat_lekerdezo(self):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('SELECT * FROM quotes')
        adatok = kurzor.fetchall()
        kapcsolat.close()
        return adatok

    def adat_torlo(self, id):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('DELETE FROM quotes WHERE id = ?', (id,))
        kapcsolat.commit()
        kapcsolat.close()

    def adat_frissito(self, id, quote, author):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('''
            UPDATE quotes SET quote = ?, author = ? WHERE id = ?
        ''', (quote, author, id))
        kapcsolat.commit()
        kapcsolat.close()

    def adat_kereso(self, id):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('SELECT * FROM quotes WHERE id = ?', (id,))
        adat = kurzor.fetchone()
        kapcsolat.close()
        return adat

    def random_quote_kereso(self):
        kapcsolat = sqlite3.connect(self.db_name)
        kurzor = kapcsolat.cursor()
        kurzor.execute('SELECT quote, author FROM quotes ORDER BY RANDOM() LIMIT 1')
        adat = kurzor.fetchone()
        kapcsolat.close()
        if adat:
            return f'"{adat[0]}" - {adat[1]}'
        else:
            return "Üres az adatbázis."