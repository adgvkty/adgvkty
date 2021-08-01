import random as ra

for i in range(100, 1500):
    amountModifier = (i / 1000)
    
    amountModifier = 2 - amountModifier
        
    price = 100 * amountModifier
    print(f'weight {i} price {price}')