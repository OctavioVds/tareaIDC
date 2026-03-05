import unittest
from main import saludar

class TestMain(unittest.TestCase):
    def test_saludar(self):
        # Comprueba que la función realmente responda "Hola Tec"
        self.assertEqual(saludar("Tec"), "Hola Tec")

if __name__ == '__main__':
    unittest.main()