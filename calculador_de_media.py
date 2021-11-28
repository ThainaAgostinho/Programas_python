#Faça	uma	função	que calcule a	média	de	um	aluno	de	acordo	com	o	critério	definido	neste	curso.	Além	disso,	 faça	uma	segunda	 função	que	informe	o	status	do	aluno	de	acordo	com	a	tabela	a	seguir:Nota	acima	de	6	à “Aprovado”Nota	entre	4	e	6	à Conceito	“Verificação	Suplementar”Nota	abaixo	de	4	à Conceito	“Reprovado”#


print("Olá, aluno! Vamos começar a calcular sua média!")
a = input("Digite a sua primeira nota! ")
nota1 = float(a)
b = input("Digite a sua segunda nota! ")
nota2 = float(b)
c = input("Digite a sua terceira nota! ")
nota3 = float(c)
d = input("Digite a sua quarta nota! ")
nota4 = float(d)
 

media = (nota1 + nota2 + nota3 + nota4)/4
if media > 6.0:
     print(f'Sua média foi {media}. Parabéns, você foi aprovado!!')
elif media < 4.0:
    print(f'Sua media foi {media}, você foi reprovado')
else: 
    print(f'Sua media foi {media}, você precisará de revisão complementar')