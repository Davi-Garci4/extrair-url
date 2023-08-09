url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"  #Nessa url temos o nome do site/pagina acessada ? e os parâmetros.
print(url)

indice_interrogacao = url.find("?")

base_url = url[:indice_interrogacao]
print(base_url)
parametro_url = url[indice_interrogacao+1:]
print(parametro_url)