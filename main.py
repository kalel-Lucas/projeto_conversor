import requests 
def main(): 
    menu = ''' 
        ___COTAÇÃO - DÓLAR/REAL___


        1. Ver cotação atual 
        2. Sair 
    '''
    rodando = True 
    while rodando: 
        print(menu)
        opcao = input("Digite a opção desejada:").strip()
        if opcao not in ["1", "2"]: 
            print("\n\nPor favor, inserir uma opção válida!\n\n")
        elif opcao == "1": 
            url = "https://economia.awesomeapi.com.br/last/USD-BRL"
            resposta = requests.get(url)
            dados = resposta.json()
            dolar_atual = dados["USDBRL"]["bid"]
            print(f"Cotação atual do Dólar->Real brasileiro: R$ {dolar_atual}")
        elif opcao == "2":
            print("Até mais :)")
            break; 

if __name__ == "__main__":
     main()
