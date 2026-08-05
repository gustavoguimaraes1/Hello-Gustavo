print (' '*35)
print (' '*4,'='*7,'PROJETO: Bolsa de Valores Python','='*7)
print (' '*35)
print ('1)', ' '*0,'Cadastro Inicial')
print (' '*35)
nome = input ('Nome de Usuário:')
idade = (input ('Data de nascimento:'))
print (' '*35)
print ('PERFIL \nUsuário:{} \nData de Nascimento:{}'.format(nome,idade))
print (' '*35)
print ('2',' '*0,'Conversor de Dinheiro')
print (' '*35)
reais =  float(input('Quantos reais você quer converter? R$'))
r = reais
d = r / 5.24
e = r / 6.14
i = r / 0.034
l = r / 7.07
ru = r / 0.068
y = r / 0.76
rp = r / 0.058
print ('Com  a conversão de R$ {:.2f}, você terá: \nEm Dólar Americano US$ {:.2f} '.format(r, d))
print ('Em Euro EUR¢ {:.2f} \nEm Iene Japonês JPY¥ {:.2f}'.format(e, i))
print ('Em Libra Esterlina GBP£ {:.2f} \nEm Rubro Russo RUB₽ {:.2f} '.format(ru, l))
print ('Em Yuan Chinês CNY¥ {:.2f} \nEm Rupia Indiana INR₹ {:.2f}'.format (y, rp))
print (' '*35)
end = input('Quer encerrar?')
print (' '*35,'\nConfirmação:{}'.format(end), ' '*35,'\nBolsa de Valores Python! \nVolte Sempre:)')
