# Submission.

class Solution:

    # Class-level constants/dictionaries.
    ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
    SUBTRACTIVE_REPLACEMENTS =  {"IV": "IIII", "IX": "IIIIIIIII", "XL": "XXXX", "XC": "XXXXXXXXX", "CD": "CCCC", "CM": "CCCCCCCCC"}

    # Method access modifier so pre-processing only accessible from within class.
    def _preprocess(self, roman_num: str) -> str:
        """Converts subtractive exceptions into simple additive roman numerals."""
        for edge, replacement in self.SUBTRACTIVE_REPLACEMENTS.items():
            if edge in roman_num:
                roman_num = roman_num.replace(edge, replacement)
        return roman_num
    
    def romanToInt(self, s: str) -> int:
        """Converts pre-processed roman numeral to integer."""
        processed_roman = self._preprocess(s)
        total_sum = 0
        for numeral in reversed(processed_roman):
            total_sum += self.ROMAN_VALUES[numeral]
        return total_sum
    
"""
Code Review.

Strengths:
- Clean declarative solution- avoids imperative programming, readable syntax.

Deficiencies: 
- Calling replace repeatedly on immutable strings generates new strings each time. For each subtractive exception in the loop in `_preprocess`, you do 6 full string scans and re-allocations.

Remarks: 
- If `n` is the length of the input string, then the code is O(n) time and O(n) space, but in practice, O(1) space due to problem constraints e.g. capped maximum integer.

Solution:
- A clean imperative solution would be to use the fact that any subtractive exception has its leftmost roman numeral smaller than the rightmost roman numeral.

"""

# An imperative solution.

class Solution:
    ROMAN_VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:

        total_value = 0
        previous_value = 0

        for char in reversed(s):
            current_value = self.ROMAN_VALUES[char]

            if current_value < previous_value:
                total_value -= current_value
            else:
                total_value += current_value

            previous_value = current_value
        
        return total_value
