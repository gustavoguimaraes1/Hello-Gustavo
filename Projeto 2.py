import math
msg = ' '*35
m = 'Projeto 2'
a = ' Calculadora.py (Teorema de Pitagoras)'
print ('{}'.format(msg))
print (' '*12 ,'{}'.format(m))
print ('{}'.format(a))
msg1 = ' '*35
print ('{}'.format(msg1))
c = float(input('Medida do cateto oposto:'))
d = float(input('Medida do cateto adjascente:'))
s = math.hypot(c,d)
print ('O valor da hipotenusa é {:.2f}'.format(s))







