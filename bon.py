def bonAppetit(bill,k,b):
    del bill[k]
    share = sum(bill) // 2
    
    if share == b:
        return "Bon Appetit"
    else:
        return b - share

    
    


print(bonAppetit([3,10,2,9],1,7))