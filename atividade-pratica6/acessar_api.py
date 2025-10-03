import requests

def obter_usuarios(quantidade):
    url = f"https://randomuser.me/api/?results={quantidade}"
    
    try:
        # Fazendo a requisição para a API
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança erro se não for 200 (OK)
        
        # Converte a resposta em JSON
        dados = resposta.json()
        usuarios = dados['results']
        
        print(f"=== {quantidade} Usuários Fictícios Aleatórios ===\n")
        
        # Exibindo as informações de cada usuário
        for i, usuario in enumerate(usuarios, start=1):
            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            print(f"Usuário {i}:")
            print(f"  Nome : {nome}")
            print(f"  E-mail: {email}")
            print(f"  País  : {pais}")
            print("-" * 40)
    
    except requests.exceptions.RequestException:
        print("❌ Falha na conexão com a API. Tente novamente mais tarde.")

def main():
    print("=== Gerador de Usuários Fictícios ===")
    
    # Pergunta ao usuário quantos perfis deseja buscar
    while True:
        try:
            quantidade = int(input("Quantos usuários deseja gerar? "))
            if quantidade <= 0:
                print("Digite um número maior que 0.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    obter_usuarios(quantidade)

if __name__ == "__main__":
    main()

