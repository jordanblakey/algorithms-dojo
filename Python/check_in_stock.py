stock = {'doll': 5, 'leggos': 1, 'boardgame': 10, 'football': 4}
merch = 'leggos'
n = 20

def check in stock(stock, merch, n):
    # Given a dictionary of items and # in stock, a string representing an ordered item, 
    # and int n representing quanitity desired, return a boolean indicating whether the order can be fulfilled. 
    print('stock: ', stock)
    print('merch: ', merch)
    print('n: ', n)
    if merch in stock and stock[merch] >= n: return True
    else: return False
    
# More succinctly:
def fillable2(stock, merch, n):
    if merch in stock and stock[merch] >= n: return True
    return False
    
# More succinctly:
def fillable3(stock, merch, n): return stock.get(merch, 0) >= n
