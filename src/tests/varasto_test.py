import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_alustaminen_negatiivisena_nollaa(self):
        self.varasto = Varasto(-10)

        # kun varasto yritetään luoda negatiivisella tilavuudella, tulisi tilavuuden olla 0
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alkusaldo(self):
        self.varasto = Varasto(10, -5)

        # kun varasto yritetään luoda negatiivisella alkusaldolla, tulisi alkusaldon olla 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alkusaldo_tilavuutta_suurempi(self):
        self.varasto = Varasto(10, 15)

        # kun varasto yritetään luoda alkusaldolla joka on tilavuutta suurempi, tulisi alkusaldon olla sama kuin tilavuus
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_lisaaminen_ei_toimi(self):
        saldo_alussa = self.varasto.saldo

        self.varasto.lisaa_varastoon(-5)

        # kun varastoon yritetään lisätä negatiivinen määrä, määrän ei tulisi muuttua
        self.assertAlmostEqual(self.varasto.saldo, saldo_alussa)

    def test_ota_enemman_kuin_on_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(14)

        # kun varastosta yritetään ottaa enemmän kuin siellä on, otetaan pois kaikki mitä löytyy
        self.assertAlmostEqual(saatu_maara, 8)

    def test_lisaa_enemman_kuin_on_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(15)

        # kun varastosta yritetään lisätä enemmän kuin siellä on vapaata tilaa, pitäisi lisätä mitä mahtuu ja heittää loput pois
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaamalla_tasan_tayteen(self):
        self.varasto.lisaa_varastoon(10)

        # kun varastoon lisätään sama määrä kuin on vapaata tilaa, tulisi varaston tulla täyteen
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivisen_maaran_otto(self):
        self.varasto.lisaa_varastoon(2)

        saatu_maara = self.varasto.ota_varastosta(-1)

        # kun varastosta yritetään ottaa nollaa pienempi määrä, tulisi saada nolla
        self.assertAlmostEqual(saatu_maara, 0)

    def test_stringiksi_tietoa(self):
        self.varasto.lisaa_varastoon(2)

        saatu_string = self.varasto.__str__()

        # tarkistetaa että __str__ printtaa oikeanlaisen stringin
        self.assertEqual(saatu_string, "saldo = 2, vielä tilaa 8")
        