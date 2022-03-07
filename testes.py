import unittest
from main import Main

class TestClass(unittest.TestCase):
  
  def test_mediana(self):
    array = [9, 2, 1, 4, 6]
    self.assertEqual(Main.pares_inteiros(array), 4 , "Falha")

  def test_pares_inteiros(self):
    array = [1, 5, 3, 4, 2]
    self.assertEqual(Main.pares_inteiros(array, 2), 3 , "Falha")

  def test_grid(self):
    texto = "tenha um bom dia"
    texto2 = "ola mundo"
    self.assertEqual(Main.grid(texto), "taoa eum nmd hbi" , "Falha")
    self.assertEqual(Main.grid(texto2), "omd luo an" , "Falha")

if __name__ == "__main__":
    unittest.main()
    