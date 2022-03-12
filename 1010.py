cod1,num1,val1 = input().split(' ')
cod2,num2,val2 = input().split(' ')
num1 = float(num1)
val1 = float(val1)
num2 = float(num2)
val2 = float(val2)
total = num1 * val1 + num2 * val2
print('VALOR A PAGAR: R$ {:.2f}'.format(total))
