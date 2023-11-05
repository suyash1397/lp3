class Item:
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight
def knapsac(w,arr):
    finalvalue =0.0
    arr.sort(key=lambda x:(x.profit/x.weight),reverse = True )
    for i in arr:
        if i.weight<=w:
            w-=i.weight
            finalvalue+=i.profit
        else:
            finalvalue += i.profit*w / i.weight
            break
    return finalvalue

arr = [Item(25,18),Item(24,15),Item(15,10)]
w=20
print(knapsac(w,arr))
