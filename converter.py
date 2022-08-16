numerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


class Converter:
    def intToRoman(self, num: str) -> str:
        self.num = num

        digits = []
        # loop through and convert each digit back to int
        for char in self.num:
            digits.append(int(char))

        # can append each numeral for each digit
        result = ""

        # reverse so first digit is lowest (in orders of magnitude, not as an int)
        digits.reverse()

        count = 0
        for digit in digits:
            if count == 0:
                numeral = numerals[1]
                five = numerals[5]
                nine = f"{numerals[1]}{numerals[10]}"
            if count == 1:
                numeral = numerals[10]
                five = numerals[50]
                nine = f"{numerals[10]}{numerals[100]}"
            if count == 2:
                numeral = numerals[100]
                five = numerals[500]
                nine = f"{numerals[100]}{numerals[1000]}"
            if count == 3:
                numeral = numerals[1000]
                # five and nine not needed in this case as numbers above 3999 will not be tested

            if digit < 4:
                result = f"{numeral * digit}{result}"
            elif digit == 4:
                result = f"{numeral}{five}{result}"
            elif digit == 5:
                result = f"{five}{result}"
            elif digit > 5 and digit < 9:
                result = f"{five}{numeral * (digit - 5)}{result}"
            elif digit == 9:
                result = f"{nine}{result}"

            count += 1

        return result
