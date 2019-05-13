#PF-Assgn-29
#day 4
def calculate(distance,no_of_passengers):
        #Remove pass and write your logic here
    expenditure=(distance*70)/10
    cost=no_of_passengers*80
    if(cost>expenditure):
        profit=cost-expenditure
    else:
        profit=-1
    return profit
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
