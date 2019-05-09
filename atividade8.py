c = 0
maior50 = 0
altura50 = 0
olhosa = 0
ruivos = 0
x = 0
while c <= 6:
    idade = int(input("digite sua idade: "))
    peso = str(input ("digite seu pesso: "))
    altura = str(input ("digite sua altura: "))
    cor = str(input("digite a cor de seus olhos: (a - azul/ p - preto/ v - verde)"))
    corc = str(input ("digite a cor de seus cabelhos: (p - preto/ c - castanho/ l - louro/ r - ruivo)"))
    if idade < '50' and peso > '60.0':
        maior50 += 1
    if altura < '1.50' :
      altura50 = idade + altura50
      x = x + 1
    if cor == 'A' or cor == 'a':
        olhosa += 1
    if corc == 'r' or corc == 'R' and cor != 'a' or cor != 'A':
        ruivos += 1
    c+=1
t = altura50/x
z = 6 * (olhosa/ 100)
print(" as pessoas com peso menor que 60 e a idade maior que 50 ", maior50 )
print(" a media das idades das pessoas com altura inferior a 1,50m ", t)
print (" a porcentagem de pessoas com olhos azuis ", z  )
print(" a quantidade de pessoas ruivas sem olhos azuis ", ruivos)
