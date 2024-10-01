import os
import math

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def avaliar_expressao(expr, x):
    expr = expr.replace('^', '**')  
    expr = expr.replace('e', 'math.e')  
    expr = expr.replace('cos', 'math.cos')  
    expr = expr.replace('sin', 'math.sin')  
    expr = expr.replace('tan', 'math.tan')  
    expr = expr.replace('log', 'math.log')  
    expr = expr.replace('exp', 'math.exp')  
    expr = expr.replace('sqrt', 'math.sqrt')  
    expr = expr.replace('sec', '(1/math.cos)')  
    expr = expr.replace('csc', '(1/math.sin)')  
    expr = expr.replace('cot', '(1/math.tan)')
    expr = expr.replace('asin', 'math.asin')  
    expr = expr.replace('acos', 'math.acos')  
    expr = expr.replace('atan', 'math.atan')  
    expr = expr.replace('asec', '(1/math.acos)')  
    expr = expr.replace('acsc', '(1/math.asin)')  
    expr = expr.replace('acot', '(1/math.atan)')

    return eval(expr) #eval interpreta e avalia essa string como uma expressão

def bissecao(funcao, a, b, precisao, n):
    k = 0
    if funcao(a) * funcao(b) >= 0:
        print("O método de bissecção falhou.")
        return
    
    if abs(b - a) < precisao:  
        raiz = (a + b) / 2  # Escolhe qualquer ponto no intervalo
        print(f"A raiz é: {raiz}")
        print(f"Número de iterações: {k}")  
        return

    while abs(b - a) > precisao and k < n:
        k += 1  
        meio = (a + b) / 2
        f_meio = funcao(meio)

        if funcao(a) * f_meio < 0:
            b = meio
        else:
            a = meio

    raiz = (a + b) / 2  
    print(f"Raiz aproximada: {raiz} após {k} iterações")

def regula_falsi(funcao, a, b, n, precisao):
    if funcao(a) * funcao(b) >= 0:
        print("O método de Regula Falsi falhou.")
        return

    k = 0
    while k < n:
        # Passo 4: M ← f(a)
        M = funcao(a)

        x = a - (funcao(a) * (b - a)) / (funcao(b) - funcao(a))

        # condições de parada
        if abs(funcao(x)) < precisao or abs(b - a) < precisao:
            print(f"A raiz é: {x} após {k + 1} iterações")
            return

        # Atualizar intervalo [a, b]
        if M * funcao(x) > 0:
            a = x  
        else:
            b = x  

        k += 1  

    print(f"Raiz aproximada: {x} após {k} iterações")

def newton(funcao, derivada, x0, precisao, n):
    for k in range(n):
        fx = funcao(x0)
        fxlinha = derivada(x0)
        
        if fxlinha == 0:
            print("Derivada zero, não pode continuar.")
            return
        
        x1 = x0 - fx / fxlinha
        
        if abs(funcao(x1)) < precisao:  # Critério de parada 
            print(f"A raiz é: {x1}")
            print(f"Iterações realizadas: {k + 1}")  
            return
        
        x0 = x1
        
    print(f"Raiz aproximada: {x1} após {n} iterações")

def secante(funcao, x0, x1, precisao, max_iter):
    k = 0  

    while True:
        f0 = funcao(x0)  
        f1 = funcao(x1)  

        # Passo 2
        if abs(f0) < precisao:
            print(f"A raiz é: {x0}")
            print(f"Número de iterações: {k}")
            return x0

        # Passo 3
        if abs(f1) < precisao or abs(x1 - x0) < precisao:
            print(f"A raiz é: {x1}")
            print(f"Número de iterações: {k}")
            return x1

        # Passo 5
        if f1 - f0 == 0:  
            print("Divisão por zero, não pode continuar.")
            return None
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)  

        # Passo 6
        f2 = funcao(x2)
        if abs(f2) < precisao or abs(x2 - x1) < precisao or k >= max_iter:
            print(f"A raiz é: {x2}")
            print(f"Número de iterações: {k}")
            return x2

        # Atualizar os pontos para a próxima iteração
        x0, x1 = x1, x2  
        k += 1  

def mil(funcao, phi, x0, precisao, it):
    k = 0
    while k < it:
        x1 = phi(x0)

        if abs(funcao(x1)) < precisao:  # Critério de parada 
            print(f"A raiz é: {x1}")
            print(f"Iterações realizadas: {k + 1}")  
            return x1
        
        x0 = x1
        k += 1  

    print(f"Raiz aproximada: {x0} após {k} iterações")
    return x0

def main():
    while True:
        clear_terminal()
        print("Escolha o método:")
        print("1. Bissecção")
        print("2. Regula Falsi")
        print("3. Newton")
        print("4. Secante")
        print("5. Mil")
        print("6. Sair")
        
        escolha = input("Digite o número do método desejado: ")
        
        if escolha == '1':
            funcao_str = input("Digite a expressão da função (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            funcao = lambda x: avaliar_expressao(funcao_str, x)
#lamda x: define uma função anônima que aceita x como argumento e usa a função avaliar_expressao para calcular o valor da função para aquele x.
            a = float(input("Digite o limite inferior (a): "))
            b = float(input("Digite o limite superior (b): "))
            precisao = float(input("Digite a precisão (δ): "))
            n = int(input("Digite o número máximo de iterações: "))
            bissecao(funcao, a, b, precisao, n)
        
        elif escolha == '2':
            funcao_str = input("Digite a expressão da função (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            funcao = lambda x: avaliar_expressao(funcao_str, x)
            a = float(input("Digite o limite inferior (a): "))
            b = float(input("Digite o limite superior (b): "))
            n = int(input("Digite o número máximo de iterações: "))
            precisao = float(input("Digite a precisão (δ): "))
            regula_falsi(funcao, a, b, n, precisao)
        
        elif escolha == '3':
            funcao_str = input("Digite a expressão da função (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            funcao = lambda x: avaliar_expressao(funcao_str, x)
            derivada_str = input("Digite a expressão da derivada (use 'x' como variável,  e: +,-,*,/,(),sin,cos,e,^): ")
            derivada = lambda x: avaliar_expressao(derivada_str, x)
            x0 = float(input("Digite o valor inicial (x0): "))
            precisao = float(input("Digite a precisão (δ): "))
            it = int(input("Digite o número máximo de iterações: "))
            newton(funcao, derivada, x0, precisao, it)
        
        elif escolha == '4':
            funcao_str = input("Digite a expressão da função (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            funcao = lambda x: avaliar_expressao(funcao_str, x)
            x0 = float(input("Digite o valor inicial (x0): "))
            x1 = float(input("Digite o segundo valor inicial (x1): "))
            precisao = float(input("Digite a precisão (δ): "))
            max_iter = int(input("Digite o número máximo de iterações: "))  
            secante(funcao, x0, x1, precisao, max_iter)
        
        elif escolha == '5':
            funcao_str = input("Digite a expressão da função (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            funcao = lambda x: avaliar_expressao(funcao_str, x)
            phi_str = input("Digite a função de iteração (use 'x' como variável, e: +,-,*,/,(),sin,cos,e,^): ")
            phi = lambda x: avaliar_expressao(phi_str, x)
            x0 = float(input("Digite o valor inicial (x0): "))
            precisao = float(input("Digite a precisão (δ): "))
            it = int(input("Digite o número máximo de iterações: "))
            mil(funcao, phi, x0, precisao, it)
        
        elif escolha == '6':
            print("Saindo do programa...")
            break
        
        else:
            print("Escolha inválida. Tente novamente.")
        
        input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
