import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    '''
    Testit varaston eri käyttötapauksia varten
    '''

    def setUp(self):
        '''setUp'''
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        '''testataan että konstruktori luo tyhjän varaston'''
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        '''testataan että uudella varastolla on oikea koko'''
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        '''testataan että saldon lisääminen toimii'''
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        '''testataan että varaston vapaa tila vähenee saldoa lisätessä varastoon'''
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        '''testataan että varastossa otettaessa saldoa saadaan oikea määrä saldoa'''
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        '''testataan että varastosta ottaminen vapauttaa tilaa varastosta otetun saldon verran'''
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alustaminen_negatiivisena_nollaa(self):
        '''testi tapaukseen jossa varaston tilavuudeksi annetaan negatiivinen arvo'''
        self.varasto = Varasto(-10)

        # kun varasto yritetään luoda negatiivisella tilavuudella, tulisi tilavuuden olla 0
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        '''testi tapaukseen jossa alkusaldolle annetaan negatiivinen alkuarvo'''
        self.varasto = Varasto(10, -5)

        # kun varasto yritetään luoda negatiivisella alkusaldolla, tulisi alkusaldon olla 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alkusaldo_tilavuutta_suurempi(self):
        '''testi tapaukseen jossa alkusaldo on varaston tilavuutta suurempi'''
        self.varasto = Varasto(10, 15)

        # kun varasto luodaan ja alkusaldo > tilavuus, alkusaldo = tilavuus
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_lisaaminen_ei_toimi(self):
        '''testi tapaukseen jossa yritetään lisätä negatiivinen määrä saldoa'''
        saldo_alussa = self.varasto.saldo

        self.varasto.lisaa_varastoon(-5)

        # kun varastoon yritetään lisätä negatiivinen määrä, määrän ei tulisi muuttua
        self.assertAlmostEqual(self.varasto.saldo, saldo_alussa)

    def test_ota_enemman_kuin_on_saldoa(self):
        '''testi tapaukseen jossa yritetään ottaa enemmän saldoa kuin varastossa on saldoa'''
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(14)

        # kun varastosta yritetään ottaa enemmän kuin siellä on, otetaan pois kaikki mitä löytyy
        self.assertAlmostEqual(saatu_maara, 8)

    def test_lisaa_enemman_kuin_on_vapaata_tilaa(self):
        '''testi tapaukseen jossa yritetään lisätä enemmän saldoa kuin varastossa on tilaa'''
        self.varasto.lisaa_varastoon(15)

        # kun yritetään lisätä enemmän saldoa kuin on vapaata tilaa, pitää lisätä vain mikä mahtuu
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaamalla_tasan_tayteen(self):
        '''testi tapaukseen jossa varasto tulee täsmälleen täyteen'''
        self.varasto.lisaa_varastoon(10)

        # kun varastoon lisätään sama määrä kuin on vapaata tilaa, tulisi varaston tulla täyteen
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_otto(self):
        '''testi tapaukseen jossa varastosta yritetään ottaa negatiivinen määrä saldoa'''
        self.varasto.lisaa_varastoon(2)

        saatu_maara = self.varasto.ota_varastosta(-1)

        # kun varastosta yritetään ottaa nollaa pienempi määrä, tulisi saada nolla
        self.assertAlmostEqual(saatu_maara, 0)

    def test_stringiksi_tietoa(self):
        '''testataan __str__ testisyötettä vastaan'''
        self.varasto.lisaa_varastoon(2)
  
        # tarkistaa että __str__ printtaa oikeanlaisen stringin
        self.assertEqual(self.varasto.__str__(), "saldo = 2, vielä tilaa 8")
