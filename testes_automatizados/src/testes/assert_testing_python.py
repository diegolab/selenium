import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.Numero1 = 575
        self.Numero2 = 575
        self.Numero3 = 857
        self.Texto = "Teste de texto"
        self.Lista = [1, 2, 3, 4, 5]
        self.Dicionario = {"a": 1, "b": 2, "c": 3}
        

    def test_1(self):
        self.Resultado = self.Numero2 + self.Numero3
        # self.assertEqual(1, 1)

    def tearDown(self):
        # self.assertEqual(self.Numero1, self.Numero2, "Os números não são iguais")
        # self.assertNotEqual(self.Numero2, self.Numero3, "Os números são iguais")
        # self.assertTrue(self.Resultado == 1432, f"O resultado não é 1450, o resultado é {self.Resultado}")
        self.assertFalse(self.Resultado == 1432, f"O resultado é {self.Resultado}")

 
if __name__ == '__main__':
    unittest.main()

