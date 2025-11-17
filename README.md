# 📐 Calculadora de Determinante 3x3 por Triangularização

Este é um programa simples em Python que calcula o determinante de uma matriz 3x3. O programa pede ao utilizador que insira os 9 elementos da matriz através do teclado e, em seguida, utiliza o método de **Triangularização (Eliminação Gaussiana)** para encontrar o determinante.

## Como Funciona o Programa

O algoritmo segue estes passos:

1.  **Entrada de Dados:** O programa pede ao utilizador para digitar, um por um, os 9 valores da matriz.
2.  **Cópia Segura:** É criada uma cópia da matriz para que a original não seja alterada.
3.  **Triangularização:** O código aplica operações elementares nas linhas para transformar a matriz numa **matriz triangular superior** (onde todos os elementos abaixo da diagonal principal são zero).
      * **Pivotação:** Se um elemento da diagonal (pivô) for zero, o programa procura uma linha abaixo e troca-as. Cada troca inverte o sinal do determinante final.
      * **Eliminação:** O programa "zera" os elementos abaixo de cada pivô.
4.  **Cálculo Final:** O determinante de uma matriz triangular é simplesmente o **produto dos elementos da sua diagonal principal** (multiplicado pelo fator de sinal das trocas de linha).
5.  **Resultado:** O programa imprime a matriz original e o determinante calculado.

## Requisitos

  * Python 3.x

(Não são necessárias bibliotecas externas como NumPy ou Pandas; o programa usa apenas módulos nativos do Python).

## Como Rodar o Programa

1.  Abre o teu terminal (PowerShell, CMD, Terminal, etc.).

2.  Navega até à pasta onde salvaste o ficheiro `main.py`.

3.  Executa o seguinte comando:

    ```bash
    python main.py
    ```

4.  O programa irá pedir-te para inserires os 9 elementos da matriz, um de cada vez:

    ```
    --- Cálculo de Determinante 3x3 por Triangularização ---
    Por favor, insira os 9 elementos da matriz.
    Use ponto (.) como separador decimal (ex: 3.14).
    Elemento [Linha 1, Coluna 1]: 1
    Elemento [Linha 1, Coluna 2]: 2
    Elemento [Linha 1, Coluna 3]: 3
    ...
    ```

-----

## Exemplos de Teste

Podes verificar se o programa está a funcionar corretamente usando estes exemplos:

### Teste 1: Matriz Singular (Determinante = 0)

  * **Entrada:**
      * Linha 1: `1`, `2`, `3`
      * Linha 2: `4`, `5`, `6`
      * Linha 3: `7`, `8`, `9`
  * **Resultado Esperado:**
    ```
    O determinante da matriz é: 0.0
    ```

### Teste 2: Matriz Identidade (Determinante = 1)

  * **Entrada:**
      * Linha 1: `1`, `0`, `0`
      * Linha 2: `0`, `1`, `0`
      * Linha 3: `0`, `0`, `1`
  * **Resultado Esperado:**
    ```
    O determinante da matriz é: 1.0
    ```

### Teste 3: Matriz Aleatória (Com Pivotação)

  * **Entrada:**
      * Linha 1: `0`, `1`, `5`
      * Linha 2: `2`, `1`, `1`
      * Linha 3: `3`, `4`, `0`
  * **Resultado Esperado:**
    ```
    O determinante da matriz é: 37.0
    ```