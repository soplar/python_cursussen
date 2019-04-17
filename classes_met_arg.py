class Persoon:

    def __init__(self, naam, geboorte_datum,
                 geslacht, bsn):
        
        self.__naam = naam
        self.__geboorte_datum = geboorte_datum
        self.__geslacht = geslacht
        self.__bsn = bsn

    @property
    def naam(self):
        return self.__naam

    @property
    def geboorte_datum(self):
        return self.__geboorte_datum

    @property
    def geslacht(self):
        return self.__geslacht

    @property
    def bsn(self):
        return self.__bsn

    def verander_naam(self, naam):
        self.__naam = naam.lower()

    def verander_leeftijd(self, leeftijd):
        if 100 > leeftijd > 18:
            self.__leeftijd = leeftijd
        else:
            raise Exception(f'De leeftijd {leeftijd} is ongeldig')

    def __repr__(self):
        return f'{self.naam} {self.leeftijd}'

    def __str__(self):
        return f"{self.naam:<15}{self.geboorte_datum:<15}{self.geslacht:<10}{self.bsn:<10}"
    
class Docent(Persoon):

    def __init__(self, pnummer, *args, lesbevoegd=False):
        super().__init__(*args)
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
    d = Docent('007', 'Cor',20)
    d.verleenBevoegdheid()
    print(d)
