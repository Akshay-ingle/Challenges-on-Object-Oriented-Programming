class RomanConverter:
    def __init__(self):
        # Define the mapping of integers to Roman numerals
        self.roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    
    def int_to_roman(self, num):
        roman_numeral = ""
        for value, symbol in self.roman_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Example usage
if __name__ == "__main__":
    converter = RomanConverter()
    number = int(input("Enter an integer: "))
    print("Roman Numeral:", converter.int_to_roman(number))
