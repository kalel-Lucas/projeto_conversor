import requests 

def converter_moeda (): 
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    