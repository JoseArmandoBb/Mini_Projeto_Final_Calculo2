# Importa o método
import math

from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
import fractions

def f(x):
    #integral definida
    #return x + 2           # limites a , b = 2 , 4
    #return (x-1)**10       # limites a , b = 0 , 1
    return np.log(1+x)      # limites a, b = 0, 1
    # return -x**2+5*x-9 # 1,4


    #area
    #return x**2
    # return x ** 2



def g(x) :

    return x + 2
    # return x+6


# grafico para area de uma fracao:
'''
x = np.linspace(-1,3,100000)
plt.plot(x, f(x))
plt.ylabel('Eixo y')
plt.xlabel('Eixo x')
plt.title('Grafico da Função Definida')
plt.axis('auto')
plt.show()
funcao = lambda x: f(x)
#integral, limite inferior, limite superior
a, b = 0, 1
valor = integrate.quad(funcao, a, b)
valor_fracao = fractions.Fraction(valor[0])

print("O resultado é  : ",valor_fracao , ' ou aproximadamente: ' , valor[0] )
'''
print()
# juntar as duas equacoes:
a, b = -1 , 2
#a , b = -2,3
x = np.linspace(-1,3,10000)
plt.fill_between(x,f(x), g(x), where= [(x>a) and (x<b) for x in x], color = 'green' , alpha = 0.2)

plt.axhline(color = 'black')
plt.ylabel('Eixo y')
plt.xlabel('Eixo x')
plt.title('Grafico de area')
plt.axis('auto')
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.show()



# Declara a funcao
#LAMBDA consiste em uma função que é atribuida a um objeto o tal se comportará como uma função
funcao = lambda x: f(x) - g(x)

#(integral, limite superior, limite inferior)
#General purpose integration
valor = integrate.quad(funcao, b, a)
valor_fracao = fractions.Fraction(valor[0])

print("A area de integral é : ",valor_fracao , ' ou aproximadamente: ' , valor[0] )


