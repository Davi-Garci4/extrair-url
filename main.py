#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "
url = url.strip()  # Aqui eu está sendo tirado os espaços vazios

if url == "":
    raise ValueError("A URL esta vazia")   #Aqui está sendo alertado sobre o erro


# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)       #Aqui eu estou pegando o indice inicial do parâmetro a partir da busca do seu nome com o método find.
indice_valor = indice_parametro + len(parametro_busca) + 1    # Aqui eu estou pegando o indice inicial do valor do parâmetro a partir do seu indice inicial mais o seu len e + 1 por conta do sinal de igualdade
indice_e_comercial = url_parametros.find('&', indice_valor)   #Aqui eu estou verificando se existe o "&" que divide os parâmetros a partir do indice do valor
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]                     #Se o find retornar "-1" significa que não existe o divisor de parâmetros e que pode se printado desde o indice inicial do valor até o fim da string
else:
    valor = url_parametros[indice_valor:indice_e_comercial]   #Caso exista o "&" será printado do indice inicial do valor até o "&" que é exclusivo

print(valor)