class Persoon:

    def __init__(self, naam, leeftijd):
        self.__naam = naam
        self.__leeftijd = leeftijd

    @property
    def naam(self):
        return self.__naam

    @property
    def leeftijd(self):
        return self.__leeftijd

    def verander_naam(self, naam):
        self.__naam = naam.lower()

    def verander_leeftijd(self, leeftijd):
        if 100 > leeftijd > 18:
            self.__leeftijd = leeftijd
        else:
            raise Exception(f'De leeftijd {leeftijd} is ongeldig')

    def __str__(self):
        return f"{self.__naam:<10} {self.__leeftijd:<20}"

class Docent(Persoon):

    def __init__(self, naam, leeftijd, pnummer, lesbevoegd=False):
        super().__init__(naam, leeftijd)
        self.__pnummer = pnummer
        self.__lesbevoegd = lesbevoegd

    def verleenBevoegdheid(self):
        if self.leeftijd > 18:
            self.__lesbevoegd = True
        else:
            raise Exception(f'Deze persoon is maar {self.leeftijd} jaar, dat is te jong.')

    def __str__(self):
        return f"{self.__class__.__name__}('{self.__pnummer}',{self.__lesbevoegd}, {self.naam})"
        
if __name__ == '__main__':
    d = Docent('Cor', 17, '007')

    d.verleenBevoegdheid()
    print(d)

