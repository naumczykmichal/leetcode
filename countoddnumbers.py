#Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).
#Zwróć liczbę liczb nieparzystych



class Solution(object):
    def countOdds(self, low, high):
        result=(high-low)/2
        if high%2!=0 or low%2!=0:
            result+=1
        return result
        
    
    



test =Solution.countOdds(object,3,7)
print(test)

    
    
    
