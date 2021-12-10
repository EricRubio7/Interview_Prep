#We hardcode the decimal values for the roman numbers
#We do so using a dictionary
values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        #We hardcode the decimal values for the roman numbers
        #We do so using a dictionary
        total = 0
        i = 0
        while i < len(s):
            #If this is the substractive case
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total += values[s[i + 1]] - values[s[i]]
                i += 2
            #Else this is not the substractive case
            else:
                total += values[s[i]]
                i += 1
        return total

#Time complexity: O(1) since the biggest number we can describe with our values is 3999 MMMCMXCIX
#This time complexity assumes O(1) look up time into the values dictionary
#Spoace complexity: O(1): Since we only use single-value variables

#Lessons:
#1 Using the right data structure can make the algorithm we write much simpler
