import tkinter as tk
import math as m
import numpy as np
import sympy as sym
import statistics as st
from functools import reduce


'''
Esta é uma calculadora científica construída usando bibliotecas python -n-built- Tkinter, 
math and statistics- e bibliotecas externas
a saber: numpy e sympy. Os vários botões são as funcionalidades da calculadora. 

'''
btn_paremeters = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': 'grey',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}

btn_paremeters_2 = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': 'powder blue',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}
btn_paremeters_3 = {
    'padx': 1,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': 'pink',
    'font': ('arial', 10),
    'width': 6,
    'height': 2,
    'relief': 'ridge',
    'activebackground': "#666666"
}
global const
const = 180
pi = 22 / 7


def Sin(x):
    return m.sin(x * (const / 180))


def Cos(x):
    return m.cos(x * const)


def Tan(x):
    return m.tan(x)


def Floor(x):
    return m.floor(x)


def Ceil(x):
    return m.ceil(x)


def ArcSin(x):
    return m.acos(x)


def ArcCos(x):
    return m.acos(x)


def ArcTan(x):
    return m.atan(x)


def GCD(x, y):
    if x > y:
        return m.gcd(x, y)
    else:
        return m.gcd(y, x)


def fmod(x, y):
    return m.fmod(x, y)


def Factorial(x):
    return m.factorial(x)


def Sqrt(x):
    return m.sqrt(x)


def Log(x):
    return m.log(x)


def perm(x, y):
    if x >= y:
        return Factorial(x) / Factorial(x - y)
    else:
        return 'Entrada incorreta!'


def comb(x, y):
    if x >= y:
        return Factorial(x) / (Factorial(x - y) * Factorial(y))
    else:
        return 'Entrada errada'


def angle_conversion(x):
    pass


class Sci_Calculator:
    def __init__(self, master):

        self.master = master
        master.title('Calculadora cientifica ')
        # auto-equação para armazenar valores
        self.expression = ""

        self.result = ""
        self.input_txt = tk.StringVar()
        self.recall = ''
        self.sum_up = ''

        # Mainframe
        MainFrame = tk.Frame(self.master, bg='gray')
        MainFrame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        # moldura para exibição
        top_frame = tk.Frame(MainFrame, height=50, width=100, bg='yellow', relief='groove', bd=4)
        top_frame.pack(side=tk.TOP)

        # a moldura para os botões
        bottom_frame = tk.Frame(MainFrame, height=700, width=100, bg='grey')
        bottom_frame.pack(side=tk.TOP)

        # exibir na tela
        self.screen = tk.Entry(top_frame, width=60, background="grey", foreground="white", textvariable=self.input_txt,
                               bd=5, justify='right', cursor='tcross')
        self.screen.pack()

        # Row 3
        # botão fatorial
        self.mod = tk.Button(bottom_frame, text='n!', **btn_paremeters, command=lambda: self.btn_click('Factorial('))
        self.mod.grid(row=3, column=0)

        #botão raiz cúbica
        self.cube_root = tk.Button(bottom_frame, text='₃√', **btn_paremeters, command=lambda: self.btn_click('**(1/3)'))
        self.cube_root.grid(row=3, column=1)

        # botão de cubo
        self.cube = tk.Button(bottom_frame, text='x^3', **btn_paremeters, command=lambda: self.btn_click('**3'))
        self.cube.grid(row=3, column=2)

        # Autora
        self.ntn = tk.Button(bottom_frame, text='Author', **btn_paremeters,
                             command=lambda: self.btn_click('Thatiane Deboleto'))
        self.ntn.grid(row=3, column=3)

        # botão antilog
        self.pwr10 = tk.Button(bottom_frame, text='10^x', **btn_paremeters, command=lambda: self.btn_click('10**'))
        self.pwr10.grid(row=3, column=4)

        # botão exponencial
        self.exp = tk.Button(bottom_frame, text='e^x', **btn_paremeters, command=lambda: self.btn_click('m.exp('))
        self.exp.grid(row=3, column=5)

        # Row  4
        # fração
        self.frac = tk.Button(bottom_frame, **btn_paremeters, text='x/y', command='', )
        self.frac.grid(row=4, column=0)

        # botão raiz quadrada
        self.rootx = tk.Button(bottom_frame, **btn_paremeters, text='√x', command=lambda: self.btn_click('Sqrt('))
        self.rootx.grid(row=4, column=1)

        # botão quadrado
        self.xsquared = tk.Button(bottom_frame, **btn_paremeters, text='x^2', command=lambda: self.btn_click('**2'), )
        self.xsquared.grid(row=4, column=2)

        # botão de energia
        self.xpwr = tk.Button(bottom_frame, **btn_paremeters, text='x^n', command=lambda: self.btn_click('**'))
        self.xpwr.grid(row=4, column=3)
        # botão de registro de base 10
        self.log = tk.Button(bottom_frame, **btn_paremeters, text='log', command=lambda: self.btn_click('Log('), )
        self.log.grid(row=4, column=4)

        # botão de log natural
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text='ln', command=lambda: self.btn_click('ln('))
        self.btn_ln.grid(row=4, column=5)

        # Row 5
        # x botão
        self.alpah_a = tk.Button(bottom_frame, text='x', **btn_paremeters, command=lambda: self.btn_click('x'))
        self.alpah_a.grid(row=5, column=0)

        # y botão
        self.fact_b = tk.Button(bottom_frame, text='y', **btn_paremeters, command=lambda: self.btn_click('y'))
        self.fact_b.grid(row=5, column=1)

        # ajuda botão
        self.help_btn = tk.Button(bottom_frame, text='HELP', **btn_paremeters,
                                  command=lambda: self.btn_click('visit www.mathsgem.wordpress.com for help'))
        self.help_btn.grid(row=5, column=2)

        # botão seno inverso
        self.sin_inv_btn = tk.Button(bottom_frame, text='Sin^-1', **btn_paremeters,
                                     command=lambda: self.btn_click('Arcsin('))
        self.sin_inv_btn.grid(row=5, column=3)

        # botão cosseno inverso
        self.cos_inv_btn = tk.Button(bottom_frame, text='Cos^-1', **btn_paremeters,
                                     command=lambda: self.btn_click('Arcos('))
        self.cos_inv_btn.grid(row=5, column=4)

        # botão tangente inverso
        self.tan_inv_btn = tk.Button(bottom_frame, text='Tan^-1', **btn_paremeters,
                                     command=lambda: self.btn_click('Arctan('))
        self.tan_inv_btn.grid(row=5, column=5)

        # Row  6
        # botão menos fechado
        self.enclosed_minus_btn = tk.Button(bottom_frame, **btn_paremeters, text='( - )',
                                            command=lambda: self.btn_click('(-'), )
        self.enclosed_minus_btn.grid(row=6, column=0)

        # botão de conversão de grau
        self.angles_btn = tk.Button(bottom_frame, **btn_paremeters, text='o \' \"', command='')
        self.angles_btn.grid(row=6, column=1)

        # botão de função hiperbólica
        self.hyp_btn = tk.Button(bottom_frame, **btn_paremeters_3, text='hyp', command=self.hyp, )
        self.hyp_btn.grid(row=6, column=2)

        # seno
        self.Sin_btn = tk.Button(bottom_frame, **btn_paremeters, text='Sin', command=lambda: self.btn_click('Sin('))
        self.Sin_btn.grid(row=6, column=3)

        # cosseno
        self.cos_btn = tk.Button(bottom_frame, **btn_paremeters, text='Cos', command=lambda: self.btn_click('cos('))
        self.cos_btn.grid(row=6, column=4)

        # tangente
        self.btn_tan = tk.Button(bottom_frame, **btn_paremeters, text='Tan', command=lambda: self.btn_click('Tan('))
        self.btn_tan.grid(row=6, column=5)

        # Row  8
        # função de solução de equações
        self.eqn = tk.Button(bottom_frame, **btn_paremeters_3, text='EQN', command=self.equation_solver, )
        self.eqn.grid(row=8, column=0)

        # algebra função botão
        self.eng_btn = tk.Button(bottom_frame, **btn_paremeters_3, text='Alg', command=self.Alg)
        self.eng_btn.grid(row=8, column=1)

        # colchete esquerdo
        self.left_brac = tk.Button(bottom_frame, **btn_paremeters, text='(', command=lambda: self.btn_click('('))
        self.left_brac.grid(row=8, column=2)

        # colchete direito
        self.right_brac = tk.Button(bottom_frame, **btn_paremeters, text=')', command=lambda: self.btn_click(')'))
        self.right_brac.grid(row=8, column=3)

        # botão de formulário padrão
        self.sd = tk.Button(bottom_frame, **btn_paremeters, text='sd', command='', )
        self.sd.grid(row=8, column=4)


        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text='M+', command='')
        self.btn_ln.grid(row=8, column=5)

        # Row 9
        # botão de função de estatísticas
        self.stat = tk.Button(bottom_frame, text='STAT', **btn_paremeters_3, command=self.Stat)
        self.stat.grid(row=9, column=0)

        # Botão de função de raízes
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters_3, text='Roots', command=self.Roots)
        self.btn_ln.grid(row=9, column=1)

        # Botão de função MMC
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters_3, text='LCM', command=self.LCM)
        self.btn_ln.grid(row=9, column=2)

        # ppolinomial
        self.polyn = tk.Button(bottom_frame, text='Pol  ', **btn_paremeters)
        self.polyn.grid(row=9, column=3)

        # botão de função do teto
        self.floor = tk.Button(bottom_frame, text='Ceil', **btn_paremeters, command=lambda: self.btn_click('Ceil('))
        self.floor.grid(row=9, column=4)

        # botão de função de piso
        self.floor = tk.Button(bottom_frame, text='Floor', **btn_paremeters, command=lambda: self.btn_click('Floor('))
        self.floor.grid(row=9, column=5)

        # Row  10
        # botão de função de matriz
        self.matrix_btn = tk.Button(bottom_frame, text='MATRIX', **btn_paremeters_3, command=self.matrix)
        self.matrix_btn.grid(row=10, column=0)

        # botão de função vetorial
        self.vec_btn = tk.Button(bottom_frame, text='VECTOR', **btn_paremeters_3)
        self.vec_btn.grid(row=10, column=1)

        # função de cálculo
        self.cube = tk.Button(bottom_frame, text='Calc', **btn_paremeters_3, command=self.Calc)
        self.cube.grid(row=10, column=2)

        # permutação
        self.perm_btn = tk.Button(bottom_frame, text='nPr', **btn_paremeters, command=lambda: self.btn_click('perm('))
        self.perm_btn.grid(row=10, column=3)

        # combinação
        self.comb_btn = tk.Button(bottom_frame, text='nCr', **btn_paremeters, command=lambda: self.btn_click('comb('))
        self.comb_btn.grid(row=10, column=4)

        # exponencial
        self.exp = tk.Button(bottom_frame, text='e^x', **btn_paremeters, command=self.btn_click('m.exp('))
        self.exp.grid(row=10, column=5)

        # Row 11
        # botão 7
        self.seven_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='7', command=lambda: self.btn_click('7'), )
        self.seven_btn.grid(row=11, column=0)

        # botão 8
        self.eight_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='8', command=lambda: self.btn_click('8'))
        self.eight_btn.grid(row=11, column=1)

        # botão 9
        self.nine_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='9', command=lambda: self.btn_click('9'), )
        self.nine_btn.grid(row=11, column=2)

        # ddeletar função
        self.Del_btn = tk.Button(bottom_frame, **btn_paremeters, text='DEL', command=self.btn_clear)
        self.Del_btn.grid(row=11, column=3)

        # limpar
        self.Ac_btn = tk.Button(bottom_frame, **btn_paremeters, text='AC', command=self.btn_clearAll, )
        self.Ac_btn.grid(row=11, column=4)

        # Botão de função MDC
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text='GCD', command=lambda: self.btn_click('GCD('))
        self.btn_ln.grid(row=11, column=5)

        # Row  12
        # botão 4
        self.four_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='4', command=lambda: self.btn_click('4'), )
        self.four_btn.grid(row=12, column=0)

        # botão 5
        self.five_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='5', command=lambda: self.btn_click('5'))
        self.five_btn.grid(row=12, column=1)

        # botão 6
        self.six_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='6', command=lambda: self.btn_click('6'), )
        self.six_btn.grid(row=12, column=2)

        # multiplicação
        self.times_btn = tk.Button(bottom_frame, **btn_paremeters, text='x', command=lambda: self.btn_click('*'))
        self.times_btn.grid(row=12, column=3)

        # divisão
        self.div_btn = tk.Button(bottom_frame, **btn_paremeters, text='/', command=lambda: self.btn_click('/'), )
        self.div_btn.grid(row=12, column=4)

        # botão de função complexa
        self.complx = tk.Button(bottom_frame, text='CMPLX', **btn_paremeters, command='')
        self.complx.grid(row=12, column=5)
        # Row 13

        # Row  14
        # botão 1
        self.one_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='1', command=lambda: self.btn_click('1'), )
        self.one_btn.grid(row=14, column=0)

        # botão 2
        self.two_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='2', command=lambda: self.btn_click('2'))
        self.two_btn.grid(row=14, column=1)

        # botão 3
        self.three_btn = tk.Button(bottom_frame, **btn_paremeters_2, text='3', command=lambda: self.btn_click('3'), )
        self.three_btn.grid(row=14, column=2)

        # botão de adição
        self.plus_btn = tk.Button(bottom_frame, **btn_paremeters, text='+', command=lambda: self.btn_click('+'))
        self.plus_btn.grid(row=14, column=3)

        # botão menos
        self.minus_btn = tk.Button(bottom_frame, **btn_paremeters, text='-', command=lambda: self.btn_click('-'), )
        self.minus_btn.grid(row=14, column=4)

        # Botão de distribuição
        self.distr = tk.Button(bottom_frame, text='DISTR', **btn_paremeters)
        self.distr.grid(row=14, column=5)

        # Row  16
        # botão 0
        self.zero_btn = tk.Button(bottom_frame, **btn_paremeters, text='0', command=lambda: self.btn_click('0'), )
        self.zero_btn.grid(row=15, column=0)

        # botão de ponto
        self.dot_btn = tk.Button(bottom_frame, **btn_paremeters, text='.', command=lambda: self.btn_click('.'))
        self.dot_btn.grid(row=15, column=1)

        # botão de vírgula
        self.exp_btn = tk.Button(bottom_frame, **btn_paremeters, text=',', command=lambda: self.btn_click(','), )
        self.exp_btn.grid(row=15, column=2)

        # Botão de resposta
        self.ans_btn = tk.Button(bottom_frame, **btn_paremeters, text='Ans', command=self.Answer)
        self.ans_btn.grid(row=15, column=3)

        # botão igual
        self.equal_btn = tk.Button(bottom_frame, **btn_paremeters, text='=', command=self.btn_equal, )
        self.equal_btn.grid(row=15, column=4)

        # botão mod n
        self.btn_ln = tk.Button(bottom_frame, **btn_paremeters, text='mod n', command=lambda: self.btn_click('fmod('))
        self.btn_ln.grid(row=15, column=5)

        # função para estatísticas

    def Stat(self):
        print('Escolha a tarefa a ser executada:\n1. Média \n2. Modo\n3. Mediana\n4. Desvio Padrão\n5. Variação')
        choice = float(input('Digite o número apropriado:'))
        if choice == 1:
            list_1 = []
            list_2 = []
            x = input('Insira os pontos de dados separados por um espaço: ')
            list_1 = x.split()
            for i in list_1:
                list_2.append(float(i))
            print('A média é', sum(list_2) / len(list_2))

        elif choice == 2:
            list_1 = []
            list_2 = []
            x = input('Insira os pontos de dados separados por um espaço: ')
            list_1 = x.split()
            for i in list_1:
                list_2.append(float(i))
            print('O modo é/são', st.mode(list_2))
        elif choice == 3:
            list_1 = []
            list_2 = []
            x = input('Insira os pontos de dados separados por um espaço: ')
            list_1 = x.split()
            for i in list_1:
                list_2.append(float(i))
            print('A mediana é', st.median_grouped(list_2))
        elif choice == 4:
            list_1 = []
            list_2 = []
            list_3 = []
            list_4 = []
            a = input('É a frequência? s/n: ')
            if a == 's' or a == 'S':
                x = input('Insira os pontos de dados separados por um espaço: ')
                list_1 = x.split()
                for i in list_1:
                    list_2.append(int(i))
                y = input('Insira a frequência de cada ponto de dados de acordo com a separação por espaço:')
                list_3 = y.split()
                for j in list_3:  # converte numero flutuantes
                    list_4.append(int(j))  # lista frequencias
                c = [(x * y) for x, y in zip(list_2, list_4)]
                d = sum(c) / sum(list_4)
                e = [(k - d) ** 2 for k in list_2]
                f = [(m * n) for m, n in zip(list_4, e)]
                print('The standard deviation is', m.sqrt(sum(f) / sum(list_4)))

            elif a == 'N' or a == 'n':
                list_1 = []
                list_2 = []
                x = input('Insira os pontos de dados separados por um espaço: ')
                list_1 = x.split()
                for i in list_1:
                    list_2.append(int(i))
                d = sum(list_2) / len(list_2)
                list_3 = [(k - d) ** 2 for k in list_2]
                print('O desvio padrão é ', m.sqrt(sum(list_3) / len(list_2)))
        elif choice == 5:  # calcular variaveis
            list_1 = []
            list_2 = []
            list_3 = []
            list_4 = []
            a = input('É a frequência? s/n: ')
            if a == 's' or a == 'S':
                x = input('Insira os pontos de dados separados por um espaço: ')
                list_1 = x.split()
                for i in list_1:
                    list_2.append(int(i))
                y = input('Insira a frequência de cada ponto de dados de acordo com a separação por espaço:')
                list_3 = y.split()
                for j in list_3:
                    list_4.append(int(j))
                c = [(x * y) for x, y in zip(list_2, list_4)]
                d = sum(c) / sum(list_4)
                e = [(k - d) ** 2 for k in list_2]
                f = [(m * n) for m, n in zip(list_4, e)]
                print('A variação é', sum(f) / sum(list_4))
            elif a == 'N' or a == 'n':
                list_1 = []
                list_2 = []
                x = input('Insira os pontos de dados separados por um espaço: ')
                list_1 = x.split()
                for i in list_1:
                    list_2.append(int(i))
                d = sum(list_2) / len(list_2)
                list_3 = [(k - d) ** 2 for k in list_2]
                print('A variação é', sum(list_3) / len(list_2))
        else:
            print('Entrada errada!')

        # função para expandir e simplificar expressões algébricas

    def Alg(self):
        # declarar variaveis
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sym.symbols(
            'a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
        print('Escolha a tarefa a ser executada:\n1. Espandir \n2. Simplificar')
        self.choice = float(input('Digite a tarefa a ser executada entre parênteses pares:'))
        # espande expressões algébricas, por exemplo (x + y)**5
        if self.choice == 1:
            expression = input('Insira a expressão para expandir: ')
            print(sym.expand(expression))
        # expressões algébricas simplificadas
        elif self.choice == 2:
            expression = input('Enter the expression to expand: ')
            print(sym.simplify(expression))
        else:
            print('Wrong Input!')

        # função para encontrar os limites, derivada e integral de funções de variável única

    def Calc(self):
        # declaração de todas as variáveis possiveis
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sym.symbols(
            'a, b, c ,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
        print('Escolha a tarefa a ser executada:\n1.Derivativo \n2. Limites \n3. Integral imprópria \n4. Integral definida')
        self.choice = float(input('Digite o número aqui: '))  # user's task to perform

        # derivada de função
        if self.choice == 1:
            expression = input('Digite a função para diferenciar:')
            var_of_func = input('Insira a variável, por exemplo, x, y ou z: ')
            order_of_dydx = input('Digite a ordem da derivada eig 1, 2 ou 3:')
            print(sym.diff(sym.simplify(expression), var_of_func, order_of_dydx))

        # limite de função
        elif self.choice == 2:

            expression = input('Digite a expressão do limite: ')
            var_of_func = input('Insira a variável, por exemplo, x, y ou z: ')
            pt_of_limit = input('Insira o ponto de limite. Se o ponto limite for infinito, digite d: ')

            print(sym.limit(sym.simplify(expression), var_of_func, pt_of_limit))

        # integral de função
        elif self.choice == 3:
            expression = input(
                'Insira a expressão para integrar funções especiais iniciais com sym. por exemplo, sin(x) as sym.sin(x): ')
            var_of_func = input('Enter the variable e.g x, y or z: ')
            print(sym.integrate(sym.simplify(expression)))

        # definite integral
        elif self.choice == 4:
            expression = input(
                'Insira a expressão para integrar funções especiais iniciais com sym. e.g sin(x) as sym.sin(x)')
            lower_limit = input('Insira o valor do limite inferior:')
            var_of_func = input('Enter the variable e.g x, y or z: ')
            upper_limit = input('Insira o valor do limite superior:')
            print(sym.integrate(sym.simplify(expression), (var_of_func, lower_limit, upper_limit)))
        else:
            print('Entrada errada')

        # função para encontrar as raízes de equações polinomiais

    def Roots(self):
        a = []
        b = []
        c = input('Insira os coeficientes do polinômio em potências crescentes da variável separados por espaço: ')
        a = c.split()
        for i in a:
            b.append(float(i))
        v = np.polynomial.Polynomial(b)
        print(v.roots())

    # função para encontrar o mmc do denominador
    def LCM(self):

        a = []
        b = []
        c = input('Digite os números (máximo de 7 números) separados por um espaço: ')
        a = c.split()
        for i in a:
            b.append(int(i))
        arr = np.array(b)
        print(np.lcm.reduce(arr))  # prints the lcm

    # Matrizes
    def matrix(self):
        ''' Esta função avalia o produto, inverso e determinante de matrizes
                 '''

        print('Escolha a tarefa a ser executada:\n1. Multiplicação de Matriz\n2. Determinante da Matriz\n3. Inverso da Matriz')
        self.choice = int(input('Digite a tarefa a ser executada, por exemplo, 1,2 3'))
        if self.choice == 1:
            print('Quantas matrizes para multiplicação (min de 2 e max de 4)?')
            choice = int(input('Digite o número de matrizes aqui:'))
            if choice == 2:
                R_1 = int(input(
                    'Digite o número de linhas para a primeira matriz: '))
                C_1 = int(input('Digite o número de colunas para a primeira matriz: '))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_1 = list(map(float, input().split()))

                R_2 = int(input('Digite o número de linhas para a 2ª matriz: '))
                C_2 = int(input('Digite o número de colunas para a 2ª matriz:'))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_2 = list(map(float, input().split()))

                matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                print(sym.Matrix(matrix_1) * sym.Matrix(matrix_2))

            elif choice == 3:
                R_1 = int(input('Digite o número de linhas para a primeira matriz: '))
                C_1 = int(input('Digite o número de colunas para a primeira matriz: '))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_1 = list(map(float, input().split()))

                R_2 = int(input('Digite o número de linhas para a 2ª matriz: '))
                C_2 = int(input('Digite o número de colunas para a 2ª matriz:'))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_2 = list(map(float, input().split()))

                R_3 = int(input('Digite o número de linhas para a 3ª matriz: '))
                C_3 = int(input('Digite o número de colunas para a 3ª matriz:'))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_3 = list(map(float, input().split()))

                matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                matrix_3 = np.array(entries_3).reshape(R_3, C_3)
                print(sym.Matrix(matrix_1) * sym.Matrix(matrix_2) * sym.Matrix(matrix_3))

            elif choice == 4:
                R_1 = int(input('Digite o número de linhas para a primeira matriz: '))
                C_1 = int(input('Digite o número de colunas para a primeira matriz: '))
                print('Insira todas as entradas (linhas) em uma única linha separada por espaço:')
                entries_1 = list(map(float, input().split()))

                R_2 = int(input('Digite o número de linhas para a 2ª matriz: '))
                C_2 = int(input('Digite o número de colunas para a 2ª matriz: '))
                print('Digite todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_2 = list(map(float, input().split()))

                R_3 = int(input('Digite o número de linhas para a 3ª matriz: '))
                C_3 = int(input('Digite o número de colunas para a 3ª matriz: '))
                print('Digite todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_3 = list(map(float, input().split()))

                R_4 = int(input('Digite o número de linhas para a 3ª matriz: '))
                C_4 = int(input('Digite o número de colunas para a 3ª matriz: '))
                print('Digite todas as entradas (linhas) em uma única linha separada por espaço: ')
                entries_4 = list(map(float, input().split()))

                matrix_1 = np.array(entries_1).reshape(R_1, C_1)
                matrix_2 = np.array(entries_2).reshape(R_2, C_2)
                matrix_3 = np.array(entries_3).reshape(R_3, C_3)
                matrix_4 = np.array(entries_4).reshape(R_4, C_4)

                print(sym.Matrix(matrix_1) * sym.Matrix(matrix_2) * sym.Matrix(matrix_3) * sym.Matrix(matrix_4))

        elif self.choice == 2:
            R_1 = int(input('Digite o número de linhas para a primeira matriz: '))
            C_1 = int(input('Digite o número de colunas para a primeira matriz: '))
            print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
            entries = list(map(float, input().split()))
            matrix_1 = np.array(entries).reshape(R_1, C_1)
            print(round(np.linalg.det(matrix_1), 2))

        elif self.choice == 3:
            R_1 = int(input('Digite o número de linhas para a primeira matriz: '))
            C_1 = int(input('Digite o número de colunas para a primeira matriz: '))
            print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
            entries = list(map(float, input().split()))
            matrix_1 = np.array(entries).reshape(R_1, C_1)
            print(np.linalg.inv(matrix_1))

    def equation_solver(self):
        '''This function solves linear system of equations  '''

        R_1 = int(input('Digite o número de equações: '))
        C_1 = int(input('Digite o número de incógnitas: '))
        print('Insira todas as entradas (linhas) em uma única linha separada por espaço: ')
        entries_1 = list(map(float, input().split()))  #
        R_2 = R_1
        C_2 = int(input('Digite 1: '))
        print('Digite todas as constantes das equações de acordo: ')
        entries_2 = list(map(float, input().split()))
        matrix_1 = np.array(entries_1).reshape(R_1, C_1)
        matrix_2 = np.array(entries_2).reshape(R_2, C_2)
        print(np.linalg.inv(matrix_1) * sym.Matrix(matrix_2))

        # para exibir itens na tela

    def btn_click(self, x):
        if len(self.expression) >= 100:
            self.expression = self.expression
            self.input_txt.set(self.expression)
        else:
            self.expression = self.expression + str(x)
            self.input_txt.set(self.expression)

        # para retrocesso

    def btn_clear(self):
        self.expression = self.expression[:-1]
        self.input_txt.set(self.expression)

        # avaliar expressões na tela

    def btn_equal(self):
        self.result = str(eval(self.expression))
        self.expression = self.result
        self.input_txt.set(self.expression)

        # limpa a tela de todas as expressões

    def btn_clearAll(self):
        self.expression = ""
        self.input_txt.set(self.expression)

    def hyp(self):
        choice = int(input('1.seno\n2.cosseno\n3.tangente'))
        if choice == 1:
            user_entry = float(input('Insira numeros: '))
            print(m.sinh(user_entry))
        elif choice == 2:
            user_entry = float(input('Insira numeros '))
            print(m.cosh(user_entry))
        elif choice == 3:
            user_entry = float(input('Insira numeros '))
            print(m.sinh(user_entry))
        else:
            print('Entrada errada!')

    def Answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.input_txt.set(self.expression)

    # # usa o que está armazenado na recuperação da memória

    def memory_recall(self):
        if self.expression == "":
            self.input_txt.set('0' + self.expression + self.recall)
        else:
            self.input_txt.set(self.expression + self.recall)


root = tk.Tk()
first_gui = Sci_Calculator(root)
root.geometry('')
root.mainloop()
