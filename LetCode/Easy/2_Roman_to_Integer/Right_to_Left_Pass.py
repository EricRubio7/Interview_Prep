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
        total = values.get(s[-1]) #Gets the last value
        for i in reversed(range(len(s) - 1)): #Loops in reverse excluding the last
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total
                
        
        
#Time complexity: O(1) since the biggest number we can describe with our values is 3999 MMMCMXCIX
#This time complexity assumes O(1) look up time into the values dictionary
#Spoace complexity: O(1): Since we only use single-value variables

#Lessons:
#1 Using the right data structure can make the algorithm we write much simpler
#2 ...We can use reversed to loop in reverse
#3 Thinking different about the logic of our solution, could lead to simpler implementation
