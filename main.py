import pandas as pd
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk


def remover_regex(texto, padroes):
    for padrao in padroes:
        texto = re.sub(padrao, '', texto)
    return texto


def contar_combos(texto, combos, n_combos=10):
    # Remover expressões regulares do texto
    # Substitua 'pattern1', 'pattern2', etc. pelos padrões desejados
    padroes_regex = [r'cláusula', r'quitação',
                     r'acordo', r'anual', r'coletivo']
    texto = remover_regex(texto, padroes_regex)

    # Tokenizar o texto em palavras
    palavras = word_tokenize(texto)

    # Remover stopwords e palavras com menos de 3 caracteres
    stop_words = set(stopwords.words('portuguese'))
    palavras = [palavra.lower() for palavra in palavras if palavra.isalpha(
    ) and len(palavra) > 3 and palavra.lower() not in stop_words]

    # Criar combos de palavras consecutivas
    combos_consecutivos = [' '.join(palavras[i:i+3])
                           for i in range(len(palavras)-1)]

    # Contar a ocorrência de cada combo de palavras
    contagem = Counter(combos_consecutivos)

    # Retornar os combos mais comuns
    return contagem.most_common(n_combos)


arquivo = input("insira o nome da planilha: ")
# Carregar a planilha Excel
planilha = pd.read_excel(arquivo)

coluna = input("insira o nome da coluna de textos: ")
# Definir os combos de palavras que você deseja contar
# Adicione os combos desejados
combos = ['adicional noturno', 'combo2', 'combo3']

# Criar uma lista para armazenar os combos mais comuns de todas as linhas
combos_mais_comuns_total = []

# Iterar sobre cada linha da planilha
for index, linha in planilha.iterrows():
    # Obter o texto da coluna desejada (substitua 'coluna_texto' pelo nome real da sua coluna)
    texto_linha = linha[coluna]
    # Chamar a função para contar os combos da linha atual
    combos_mais_comuns_linha = contar_combos(texto_linha, combos)
    # Adicionar os combos mais comuns da linha à lista total
    combos_mais_comuns_total.extend(combos_mais_comuns_linha)

# Contar a ocorrência total de cada combo em todas as linhas
contagem_total = Counter(dict(combos_mais_comuns_total))

# Exibir os combos mais comuns de todas as linhas
print("Combos mais comuns de todas as linhas:")
# Altere 10 para o número desejado de combos mais comuns
for combo, frequencia in contagem_total.most_common(10):
    print(f"{combo}: {frequencia}")
