# Importamos o módulo 'copy'
# Usamo-lo para fazer uma cópia exata da matriz, 
# para que a matriz original não seja destruída durante os cálculos.
import copy

def calcular_determinante_3x3(matriz):
    """
    Calcula o determinante de uma matriz 3x3 fornecida.
    O método usado é a triangularização (Eliminação Gaussiana).
    """
    
    # --- Preparação ---
    
    # 1. Cópia da Matriz
    # Criamos uma cópia 'profunda' (deepcopy) da matriz original.
    # 'm' será a nossa matriz de trabalho que vamos modificar.
    m = copy.deepcopy(matriz)
    
    # 2. Variável de Sinal
    # Quando trocamos duas linhas, o sinal do determinante inverte.
    # Esta variável (sinal) começa em 1 e será multiplicada por -1 a cada troca.
    sinal = 1.0
    
    # 3. Tamanho da Matriz
    # Embora saibamos que é 3x3, usar 'n' torna o código mais legível.
    n = 3

    # --- Início da Triangularização (Eliminação Gaussiana) ---
    
    # O objetivo é zerar os elementos abaixo da diagonal principal.
    # A diagonal é m[0][0], m[1][1], m[2][2].
    
    # Iteramos por cada coluna 'j' que servirá como pivô.
    # Para uma matriz 3x3, só precisamos de fazer isto para a coluna 0 e 1.
    for j in range(n - 1): # j vai ser 0, depois 1
        
        # --- 1. Pivotação (Garantir que o pivô m[j][j] não é zero) ---
        
        # Se o nosso pivô (o elemento da diagonal) for zero...
        if m[j][j] == 0:
            # ...precisamos de encontrar uma linha abaixo dela (linha 'i')
            # que tenha um número diferente de zero nessa mesma coluna 'j'.
            
            linha_para_trocar = -1 # Começa como -1 (não encontrada)
            
            # Itera pelas linhas 'i' abaixo da linha 'j'
            for i in range(j + 1, n):
                if m[i][j] != 0: # Se encontrarmos um elemento não-zero
                    linha_para_trocar = i # Guardamos o índice dessa linha
                    break # Paramos a procura
            
            # Se encontrámos uma linha válida para trocar...
            if linha_para_trocar != -1:
                # Trocamos a linha 'j' inteira pela 'linha_para_trocar'
                m[j], m[linha_para_trocar] = m[linha_para_trocar], m[j]
                
                # IMPORTANTE: Cada troca de linhas inverte o sinal do determinante
                sinal = sinal * -1
            else:
                # Se não encontrámos nenhuma linha para trocar (toda a coluna abaixo é zero),
                # a matriz é singular (não tem inversa) e o seu determinante é 0.
                return 0.0 # Retorna 0 e termina a função.

        # --- 2. Eliminação (Zerar elementos abaixo do pivô) ---
        
        # Agora que temos a certeza que m[j][j] (o pivô) não é zero,
        # vamos usá-lo para zerar todos os elementos abaixo dele (na coluna 'j').
        
        # Itera por todas as linhas 'i' que estão ABAIXO da linha do pivô 'j'
        for i in range(j + 1, n):
            
            # Pega no valor que queremos zerar (ex: m[1][0] ou m[2][0])
            valor_a_zerar = m[i][j]
            
            # Se o valor já é zero, não precisamos de fazer nada
            if valor_a_zerar == 0:
                continue # Pula para a próxima linha 'i'
                
            # Pega no valor do pivô (ex: m[0][0])
            pivo_valor = m[j][j]
            
            # Calcula o multiplicador necessário para a eliminação.
            # (Ex: se o pivô é 2 e o valor a zerar é 6, o multiplicador é 6/2 = 3)
            multiplicador = valor_a_zerar / pivo_valor
            
            # Agora, aplica a operação: Linha[i] = Linha[i] - multiplicador * Linha[j]
            # Isto tem de ser feito para todos os elementos da linha 'i'
            for k in range(j, n): # Itera por cada coluna 'k' na linha 'i'
                # Pega no elemento da linha do pivô (m[j][k])
                # Multiplica-o pelo multiplicador
                # Subtrai esse resultado do elemento da linha atual (m[i][k])
                m[i][k] = m[i][k] - multiplicador * m[j][k]
    
    # --- Fim da Triangularização ---
    
    # Neste ponto, a matriz 'm' é uma Matriz Triangular Superior.
    # Ex: [[a, b, c], [0, d, e], [0, 0, f]]
    
    # O determinante de uma matriz triangular é o produto da sua diagonal principal.
    
    # Começamos o determinante com o nosso fator de sinal (1 ou -1)
    determinante_final = sinal
    
    # Iteramos pela diagonal principal (m[0][0], m[1][1], m[2][2])
    for i in range(n):
        # Multiplicamos o resultado pelo elemento da diagonal
        determinante_final = determinante_final * m[i][i]
        
    # Retorna o valor calculado
    return determinante_final

def obter_matriz_do_utilizador():
    """
    Pede ao utilizador para digitar os 9 valores da matriz 3x3, via teclado.
    Valida a entrada para garantir que são números.
    Retorna a matriz como uma lista de listas (ex: [[1,2,3], [4,5,6], [7,8,9]]).
    """
    
    # Cria uma lista vazia que vai guardar as 3 linhas da matriz
    matriz_criada = []
    
    print("--- Cálculo de Determinante 3x3 por Triangularização ---")
    print("Por favor, insira os 9 elementos da matriz.")
    print("Use ponto (.) como separador decimal (ex: 3.14).")
    
    # Itera de 0 a 2 (para criar 3 linhas)
    for i in range(3):
        
        # Cria uma lista vazia para guardar os 3 números da linha atual
        linha_atual = []
        
        # Itera de 0 a 2 (para pedir 3 colunas)
        for j in range(3):
            
            # Este loop 'while True' serve para validar a entrada.
            # Ele só para (break) quando o utilizador digita um número válido.
            while True:
                try:
                    # Pede o valor para o elemento [i+1, j+1] (para ficar fácil de ler)
                    valor_texto = input(f"Elemento [Linha {i+1}, Coluna {j+1}]: ")
                    
                    # Tenta converter o texto digitado para um número 'float' (decimal)
                    valor_numero = float(valor_texto)
                    
                    # Se deu certo, adiciona o número à lista da linha atual
                    linha_atual.append(valor_numero)
                    
                    # Sai do loop 'while' e passa para o próximo elemento
                    break
                    
                except ValueError:
                    # Se a conversão 'float()' falhou (ex: utilizador digitou "abc"),
                    # imprime um erro e o loop 'while' repete-se, pedindo o mesmo valor novamente.
                    print(f"Erro: '{valor_texto}' não é um número válido. Tente novamente.")
                    
        # Fim do loop das colunas. Adiciona a linha completa (com 3 números) à matriz.
        matriz_criada.append(linha_atual)
        
    # Fim do loop das linhas. Retorna a matriz 3x3 completa.
    return matriz_criada

# --- Ponto de Entrada Principal do Programa ---
def main():
    """
    Função principal que orquestra todo o programa.
    """
    
    # 1. Chama a função que pede a matriz ao utilizador
    matriz_original = obter_matriz_do_utilizador()
    
    # 2. Chama a função que calcula o determinante
    resultado_determinante = calcular_determinante_3x3(matriz_original)

    if resultado_determinante == -0.0:
        resultado_determinante = 0.0
    
    # 3. Imprime os resultados na tela
    
    print("\n--- Resultado ---")
    
    # Imprime a matriz que o utilizador inseriu, para conferência
    print("Matriz Original Inserida:")
    for linha in matriz_original:
        print(f"  {linha}") # Imprime cada linha formatada
        
    # Imprime o resultado final do determinante
    print(f"\nO determinante da matriz é: {resultado_determinante}")

# Esta é uma convenção padrão em Python.
# O código dentro deste 'if' só é executado quando o ficheiro 'main.py'
# é corrido diretamente (e não quando é importado por outro ficheiro).
if __name__ == "__main__":
    # Chama a função 'main()' para iniciar o programa.
    main()