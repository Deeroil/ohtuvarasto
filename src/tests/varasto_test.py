import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virhevarasto = Varasto(-10, -1)

    # rikottu testi
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        self.assertEqual(self.virhevarasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        self.assertEqual(self.virhevarasto.saldo, 0)

    def test_konstruktori_ei_tayta_yli_saldon(self):
        taysivarasto = Varasto(5, 11)
        self.assertEqual(taysivarasto.saldo, 5)

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

    def test_lisays_ei_toimi_jos_alle_nolla_kun_saldo_nolla(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_ei_toimi_jos_alle_nolla_kun_saldo_enemmän(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisays_ei_ylita_saldoa(self):
        self.varasto.lisaa_varastoon(100)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_ei_toimi_kun_maara_negatiivinen_saldo_nolla(self):
        otettu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu, 0)

    def test_ottaminen_ei_toimi_kun_maara_negatiivinen(self):
        self.varasto.lisaa_varastoon(2)
        otettu = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otettu, 0)
        self.assertAlmostEqual(self.varasto.saldo, 2)

    def test_ottaminen_antaa_max_saldon(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(otettu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikein(self):
        string = self.varasto.__str__()
        self.assertEqual(string, "saldo = 0, vielä tilaa 10")