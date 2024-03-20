import pandas as pd
from collections import Counter
import re

def obter_expressoes_tres_palavras(texto):
    # Dividir o texto em tokens considerando apenas palavras alfanuméricas e traços
    tokens = re.findall(r'\b[a-zA-Z0-9-]+\b', texto.lower())
    
    # Criar uma lista de expressões de 3 tokens
    expressoes_tres_tokens = [' '.join(tokens[i:i+3]) for i in range(len(tokens) - 2)]
    
    # Contar a frequência das expressões
    contagem_expressoes = Counter(expressoes_tres_tokens)
    
    # Retornar as 3 expressões mais comuns
    return contagem_expressoes.most_common(20)

# Carregar o arquivo Excel
caminho_arquivo = input("insira o nome do arquivo: ")  # Substitua pelo caminho do seu arquivo
nome_planilha = input("insira o nome da planilha: ")  # Substitua pelo nome da sua planilha
nome_coluna = input("insira o nome da coluna: ")  # Substitua pelo nome da coluna que deseja analisar

# Carregar a coluna do arquivo Excel
dados = pd.read_excel(caminho_arquivo, sheet_name=nome_planilha)
coluna_texto = dados[nome_coluna].dropna().astype(str)

# Concatenar todos os textos da coluna em uma única string
texto_completo = ' '.join(coluna_texto)

# Chamar a função e exibir o resultado
resultado = obter_expressoes_tres_palavras(texto_completo)
print(resultado)