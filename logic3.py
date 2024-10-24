invest = int (input('Сумма инвестиций:'))
maikl = int (input('Сумма инвестиций Майкла:'))
ivan = int (input('Сумма инвестийций Ивана:'))
if (invest>=maikl) and (invest>=ivan) and (invest<= (maikl+ivan)):
    print ('1')
elif  (invest <= maikl):
    print ('mike')
elif (invest <= ivan):
    print ('ivan')
else:
    print ('0')

