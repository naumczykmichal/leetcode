class Solution(object):
    def isHappy(self, n):
        p =None
        ans =[]
        num =n
        while p is None:
            x=[int(a) * int(a) for a in str(num)]
            x_sum= sum(x)
            if x_sum==1:
                p=True
            elif x_sum in ans:
                p=False
            else:
                ans.append(num)
                num=x_sum
        return p
    
    
    
list = [4,5]

new=Solution.isHappy(object,list)
print(new)
        