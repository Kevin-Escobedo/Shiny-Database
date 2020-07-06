import sqlite3

class ShinyDatabase:
    def __init__(self):
        '''Sets up connection to the database file'''
        self.db = sqlite3.connect("shiny.db")
        self.cursor = self.db.cursor()
        self.num = self.get_num()

    def create_table(self) -> None:
        '''Creates the table to store data'''
        self.cursor.execute("CREATE TABLE IF NOT EXISTS SHINY(NUM INTEGER PRIMARY KEY, TARGET TEXT, COUNT INTEGER, METHOD TEXT, GEN INTEGER, CHARM INTEGER)")
        self.db.commit()

    def get_num(self) -> int:
        '''Gets the length of the database'''
        try:
            self.cursor.execute("SELECT * FROM SHINY")
            return len(self.cursor.fetchall())
        except sqlite3.OperationalError:
            return 0

    def insert(self, target:str, count:int, method:str, gen:int, charm:bool) -> None:
        '''Insert data into the database'''
        try:
            self.num += 1
            if charm:
                charm = 1
            else:
                charm = 0
            self.cursor.execute("INSERT INTO SHINY(NUM, TARGET, COUNT, METHOD, GEN, CHARM) VALUES(?, ?, ?, ?, ?, ?)", (self.num, target, count, method, gen, charm))
        except sqlite3.IntegrityError:
            self.num += 1
            if charm:
                charm = 1
            else:
                charm = 0
            self.cursor.execute("INSERT INTO SHINY(NUM, TARGET, COUNT, METHOD, GEN, CHARM) VALUES(?, ?, ?, ?, ?, ?)", (self.num, target, count, method, gen, charm))

    def close(self) -> None:
        '''Closes the connection to the database file'''
        self.db.commit()
        self.db.close()

if __name__ == "__main__":
    sd = ShinyDatabase()
    sd.create_table()
    """
    sd.insert("Scorbunny", 431, "Masuda", 8, False)
    sd.insert("Dreepy", 225, "Masuda", 8, False)
    sd.insert("Sobble", 122, "Masuda", 8, False)
    sd.insert("Nickit", 605, "Masuda", 8, True)
    sd.insert("Rookidee", 33, "Masuda", 8, True)
    sd.insert("Mudkip", 50, "Soft Reset", 6, False)
    sd.insert("Rayquaza", 587, "Soft Reset", 7, True)
    sd.insert("Regigigas", 207, "Soft Reset", 7, True)
    sd.insert("Celebi", 1784, "Soft Reset", 2, False)
    sd.insert("Groudon", 9, "Soft Reset", 7, True)
    sd.insert("Ho-Oh", 1834, "Soft Reset", 2, False)
    sd.insert("Eevee", 325, "Masuda", 7, True)
    sd.insert("Cresselia", 3705, "Soft Reset", 7, True)
    sd.insert("Charmander", 664, "Masuda", 7, True)
    sd.insert("Rockruff", 114, "Masuda", 7, True)
    sd.insert("Litten", 16, "Masuda", 7, True)
    sd.insert("Ho-Oh", 1129, "Soft Reset", 6, True)
    sd.insert("Poliwag", 23, "SOS", 7, True)
    sd.insert("Totodile", 240, "Masuda", 7, True)
    sd.insert("Eevee", 339, "Masuda", 7, True)
    sd.insert("Numel", 136, "Masuda", 7, True)
    sd.insert("Charmander", 264, "Masuda", 7, True)
    sd.insert("Popplio", 323, "Masuda", 7, True)
    sd.insert("Salandit", 63, "SOS", 7, True)
    sd.insert("Fennekin", 52, "Masuda", 7, True)
    sd.insert("Magnemite", 78, "Masuda", 7, True)
    sd.insert("Riolu", 13, "Masuda", 7, True)
    sd.insert("Rockruff", 232, "Masuda", 7, True)
    sd.insert("Minior", 99, "Masuda", 7, True)
    sd.insert("Alolan Vulpix", 24, "Masuda", 7, True)
    sd.insert("Beldum", 55, "Masuda", 7, True)
    sd.insert("Rowlet", 1, "Masuda", 7, False)
    sd.insert("Litten", 1579, "Masuda", 7, False)
    sd.insert("Tirtouga", 2, "Masuda", 6, True)
    sd.insert("Porygon", 224, "Masuda", 6, True)
    sd.insert("Torchic", 5, "Masuda", 6, True)
    sd.insert("Piplup", 84, "Masuda", 6, True)
    sd.insert("Mareep", 424, "Masuda", 6, True)
    sd.insert("Buneary", 103, "Masuda", 6, True)
    sd.insert("Eevee", 127, "Masuda", 6, True)
    sd.insert("Ponyta", 497, "Masuda", 6, True)
    sd.insert("Bulbasaur", 222, "Masuda", 6, True)
    sd.insert("Charmander", 125, "Masuda", 6, True)
    sd.insert("Litwick", 1226, "Masuda", 6, True)
    sd.insert("Froakie", 1010, "Masuda", 6, True)
    sd.insert("Cyndaquil", 576, "Masuda", 6, True)
    """
    sd.close()
