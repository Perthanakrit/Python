tale = float(int(input()))
iron = float(int(input()))
lamp = float(int(input()))

priceTV = ('%.2f' % (0.12)) * ('%.2f'%(tale)) * ('%.2f' % (3.00))
priceIR = '%.2f' % (0.50) * '%.2f' % (iron) * '%.2f' % (3.00)
priceLamp = '%.2f' % (0.06) * '%.2f' % (lamp) * '%.2f' % (3.00)

print(priceTV + priceIR + priceLamp)




