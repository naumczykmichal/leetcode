class Solution(object):
    def maximumWealth(self, accounts):
        maxWealthSoFar =0
        
        for  customer in accounts:
            currentCustomerWealth =0
            
            for bank in customer:
                currentCustomerWealth+=bank
            
            maxWealthSoFar=max(maxWealthSoFar,currentCustomerWealth)
        return maxWealthSoFar
        



lista =[10,2,3],[2,3,4],[50,60,1]


new =Solution.maximumWealth(object,lista)
print(new)
