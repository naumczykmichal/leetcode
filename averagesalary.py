class Solution(object):
    def average(self, salary):
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)
        





lista=[48000,59000,99000,13000,78000,45000,31000,
       17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
new =Solution.average(object,lista)
print(new)