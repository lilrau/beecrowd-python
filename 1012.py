A,B,C = input().split(' ')
A = float(A)
B = float(B)
C = float(C)
a = A * C / 2
b = 3.14159 * C **2
c = (A + B) * C / 2
d = B * B
e = A * B
print('TRIANGULO: {:.3f}\n'
      'CIRCULO: {:.3f}\n'
      'TRAPEZIO: {:.3f}\n'
      'QUADRADO: {:.3f}\n'
      'RETANGULO: {:.3f}'
      .format(a, b, c, d, e))
