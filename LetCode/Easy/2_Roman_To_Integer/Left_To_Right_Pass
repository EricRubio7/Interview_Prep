#We hardcode the decimal values for the roman numbers 
#We do so using a dictionary
#To improve performance we add: CM, CD, XC, XL, IX, IV, which will be 2 characthers in lenght
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "CM": 900,
    "CD": 400,
    "XL": 40,
    "XC": 90,
    "IX": 9,
    "IV": 4,   
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in values: 
                total += values[s[i:i+2]]
                i += 2
            else:
                total += values[s[i]]
                i += 1
            print(total)
        return total
    
#Time complexity: O(1) since the biggest number we can describe with our values is 3999 MMMCMXCIX
#This time complexity assumes O(1) look up time into the values dictionary
#Spoace complexity: O(1): Since we only use single-value variables

#Lessons:
#1 Using the right data structure can make the algorithm we write much simpler
