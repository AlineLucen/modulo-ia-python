import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        # Fazendo a requisição
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança erro se a resposta não for 200 (OK)
        
        dados = resposta.json()  # Converte a resposta em JSON
        
        # Verifica se o CEP existe
        if "erro" in dados:
            print("❌ CEP não encontrado. Verifique o número digitado.")
            return
        
        # Exibindo as informações
        print("\n=== Dados do CEP ===")
        print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
        print(f"Bairro    : {dados.get('bairro', 'Não informado')}")
        print(f"Cidade    : {dados.get('localidade', 'Não informado')}")
        print(f"Estado    : {dados.get('uf', 'Não informado')}")
    
    except requests.exceptions.RequestException:
        print("❌ Falha na conexão com a API. Tente novamente mais tarde.")

def main():
    print("=== Consulta de CEP ===")
    cep = input("Digite o CEP (somente números): ").strip()
    
    # Valida o CEP (precisa ter 8 dígitos numéricos)
    if not cep.isdigit() or len(cep) != 8:
        print("❌ CEP inválido! Digite apenas 8 números.")
        return
    
    consultar_cep(cep)

if __name__ == "__main__":
    main()
