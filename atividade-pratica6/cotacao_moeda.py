import requests
from datetime import datetime

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        # Faz a requisição para a API
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança erro se a resposta não for 200 (OK)

        dados = resposta.json()

        # O nome da chave na resposta vem no formato "USDBRL", "EURBRL", etc.
        chave = f"{moeda.upper()}BRL"

        if chave not in dados:
            print("❌ Moeda não encontrada. Verifique o código digitado.")
            return

        cotacao = dados[chave]

        # Extrai as informações
        valor_atual = float(cotacao["bid"])
        valor_maximo = float(cotacao["high"])
        valor_minimo = float(cotacao["low"])
        timestamp = int(cotacao["timestamp"])
        data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        # Exibe os resultados
        print(f"\n=== Cotação {moeda.upper()} -> BRL ===")
        print(f"Valor atual : R$ {valor_atual:.2f}")
        print(f"Máxima do dia: R$ {valor_maximo:.2f}")
        print(f"Mínima do dia: R$ {valor_minimo:.2f}")
        print(f"Última atualização: {data_hora}")

    except requests.exceptions.RequestException:
        print("❌ Erro na conexão com a API. Tente novamente mais tarde.")
    except (KeyError, ValueError):
        print("❌ Não foi possível processar os dados da cotação.")

def main():
    print("=== Consulta de Cotações de Moedas ===")
    print("Exemplos de códigos: USD (Dólar), EUR (Euro), BTC (Bitcoin), ARS (Peso Argentino)")
    
    moeda = input("Digite o código da moeda que deseja consultar: ").strip().upper()
    
    if not moeda.isalpha() or len(moeda) < 3:
        print("❌ Código de moeda inválido!")
        return
    
    consultar_cotacao(moeda)

if __name__ == "__main__":
    main()
