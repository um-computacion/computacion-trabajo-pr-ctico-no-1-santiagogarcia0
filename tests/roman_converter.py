import unittest

# def decimal_to_roman(n):
#     valores = [
#         (1000, "M"),
#         (900, "CM"),
#         (500, "D"),
#         (400, "CD"),
#         (100, "C"),
#         (90, "XC"),
#         (50, "L"),
#         (40, "XL"),
#         (10, "X"),
#         (9, "IX"),
#         (5, "V"),
#         (4, "IV"),
#         (1, "I")
#     ]
    
#     roman_numeral = "" 
    
#     for valor, simbolo in valores:
#         while n >= valor:
#             roman_numeral += simbolo 
#             n -= valor
#     return roman_numeral

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decimal_to_roman(1), "I")

    def test_2(self):
        self.assertEqual(decimal_to_roman(2), "II")

    def test_3(self):
        self.assertEqual(decimal_to_roman(3), "III")

    def test_4(self):
        self.assertEqual(decimal_to_roman(4), "IV")

    def test_5(self):
        self.assertEqual(decimal_to_roman(5), "V")

    def test_6(self):
        self.assertEqual(decimal_to_roman(6), "VI")

    def test_8(self):
        self.assertEqual(decimal_to_roman(8), "VIII")

    def test_9(self):
        self.assertEqual(decimal_to_roman(9), "IX")

    def test_10(self):
        self.assertEqual(decimal_to_roman(10), "X")

    def test_49(self):
        self.assertEqual(decimal_to_roman(49), "XLIX")

    def test_99(self):
        self.assertEqual(decimal_to_roman(99), "XCIX")

    def test_3999(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

def main():
    try:
        numero_decimal = int(input("Ingresa un número decimal: "))
        print(f"El número romano de {numero_decimal} es {decimal_to_roman(numero_decimal)}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == '__main__':
    unittest.main() 
