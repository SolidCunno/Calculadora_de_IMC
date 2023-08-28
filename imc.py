# input do usuário.
import sys
height = float(input('Digite sua altura: '))
weight = float(input('\nDigite seu peso'))

# cálculo 

IMC = weight / (height / 100)**2


# Statements para resultado do programa.

if IMC < 18.5:
    print(f' De acordo com o seu IMC {IMC}, é declarado estado de Magreza')

elif IMC >= 18.6 and IMC < 24.9:
    print(f' De acordo com o seu IMC {IMC}, o estado Normal foi declarado')

elif IMC >= 25 and IMC < 29.9:
    print(f' De acordo com o seu IMC {IMC}, é declarado estado de Sobrepeso')

elif IMC >= 30 and IMC < 34.9:
    print(f' De acordo com o seu IMC {IMC}, é declarado estado de Obesidade Grau I')

elif IMC >= 35 and IMC < 39.9:
    print(f' De acordo com o seu IMC {IMC}, é declarado estado de Obesidade Grau II')

else:
    print(f' De acordo com o seu IMC {IMC}, é declarado estado de Obesidade Grau III')

y = str(input('\n Digite ''y'' em caso de obtenção de um resultado de IMC alto e deseja mais informações para uma vida saudável'))

if y=='y':
    print(f' https://bvsms.saude.gov.br/bvs/dicas/215_obesidade.html acesse o site da biblioteca virtual da saúde para mais informações')
    

else:
    sys.exit


   
        