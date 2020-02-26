import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# A. Manipulação de dados

# Considerando o dicionário Python data e a lista Python legenda:

data = {
 'animal': ['gato', 'gato', 'cobra', 'cachorro', 'cachorro', 'gato', 'cobra', 'gato', 'cachorro', 'cachorro'],
 'idade': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
 'visitas': [ 1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
 'prioridade': ['sim', 'sim', 'não', 'sim', 'não', 'não', 'não', 'sim', 'não', 'não']}

legenda = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Questão 1
#  Crie um DataFrame df a partir do dicionário data que possui como índice legenda.

df = pd.DataFrame(data, index=legenda)
print(df)
print(df.describe())

# Questão 2
# Retorne os dados nas linhas [3, 4, 8] e colunas ['animal', 'idade']

print(df.iloc[[3, 4, 8], [0, 1]])


# Questão 3
#  Retorne as linhas onde o número de visitas é maior do que 3

print(df[df.visitas > 2])

# Questão 4
# Calcule a idade média para cada animal no df.
print(df.groupby(['animal']).mean())

#Questão 5
# Insira uma nova linha 'k' a df com valores quaisquer a sua escolha para cada coluna. Então apague essa linha para voltar ao DataFrame original

df.loc['k'] = ["caranguejo", 2, 3, "não"]

# OU

# df2 = pd.DataFrame({"animal"        : ["caranguejo"],
#                     "idade"         : [2],
#                     "visitas"       : [3],
#                     "prioridade"    : ["não"]
#                     })

# OU

# df = df.append(df2, ignore_index=True)
# df.iat[10, 0] = 'Caranguejo'
# df.iat[10, 1] = 2
# df.iat[10, 2] = 3
# df.iat[10, 3] = 'não'
# df = df.drop(index='k')
# print(df)

# Questão 6
# Ordene df primeiro pelos valores de 'idade' em ordem decrescente, e então pelo valor da coluna 'visita' em ordem crescente.

df = df.sort_values(by=['idade','visitas'],ascending=[False, True])
print(df)

# Questão 7
#  A coluna 'prioridade' contém valores 'sim' e 'não'. Substitua esses por valores booleanos.

df = df.replace({'prioridade': {'sim': True,'não': False}})
print(df)

#print(df.dtypes)


# B. Plotagem

# Questão 8
#  Adim tem mantido o controle de sua performance no trabalho ao longo do tempo, bem como o quão bom ele estava se
#  sentindo naquele dia, e se ele tomava uma xícara de café pela manhã.
# Faça um gráfico que incorpore todos os quatro recursos deste DataFrame. (Obs: O gráfico não precisa ser bonito, não estamos avaliando data visualisation.)

df = pd.DataFrame({
 "produtividade":[5,2,3,1,4,5,6,7,8,3,4,8,9],
 "horas"        :[1,9,6,5,3,9,2,9,1,7,4,2,2],
 "satisfacao"   :[2,1,3,2,3,1,2,3,1,2,2,1,3],
 "cafe"         :[0,0,1,1,0,0,0,0,1,1,0,1,0]
})

x = np.arange(13)
fig = plt.figure()
ax = plt.subplot(111)
ax.plot(x, df['produtividade'],'d',linewidth=2.0, label='produtividade')
ax.plot(x, df['horas'],"ro",linewidth=2.0, label='Horas')
ax.plot(x, df['satisfacao'],"g^", label='satisfacao',linewidth=2.0, )
ax.plot(x, df['cafe'],"bs", label='cafe',linewidth=2.0,)
plt.title('Dados')
ax.legend()
plt.show()

# C. Modelagem de problemas

# Questão 9
# Considere um DataFrame df o qual possui uma coluna 'X' com inteiros:

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

# Para cada valor, conte a diferença da sua posição para o zero anterior
# (ou para o início da série, o que estiver mais próximo). Estes valores, portanto, devem ser:
# [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]
# Escreva os em uma nova coluna 'Y'.

Y = []
c = 0
for variavel in df['X']:
     if variavel == 0:
         c = 0
         Y.append(c)
     else:
         c = c + 1
         Y.append(c)

df2 = pd.DataFrame(Y, columns=list('Y'))
df = df.join(df2)
 print(df)

