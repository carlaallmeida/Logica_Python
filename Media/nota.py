print('Calcule sua Média')

nota_1 = float(input('Digite a primeira nota:'));
nota_2 = float(input('Digite a segunda nota:'));
nota_3 = float(input('Digite a terceira nota:'));
nota_4 = float(input('Digite a quarta nota:'));
media = (nota_1 + nota_2 + nota_3 + nota_4)/4
print ('Sua media nesse semestre foi: ',media);
if(media >= 6):
  print('Parabéns você está aprovado!');
elif(media >= 4):
  print('Você está de exame!');
else:
  print('Terá que se esforçar mais!');""