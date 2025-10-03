import json

def salvar_json(caminho_arquivo, dados):
    """Salva os dados em um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Dados salvos com sucesso em '{caminho_arquivo}'!")
    except Exception as e:
        print(f"❌ Falha ao salvar o arquivo: {e}")

def ler_json(caminho_arquivo):
    """Lê e exibe os dados de um arquivo JSON."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        print("\n=== Dados Lidos do Arquivo JSON ===")
        print(f"Nome : {dados.get('nome', 'Não informado')}")
        print(f"Idade: {dados.get('idade', 'Não informado')}")
        print(f"Cidade: {dados.get('cidade', 'Não informado')}")
    
    except FileNotFoundError:
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
    except json.JSONDecodeError:
        print("❌ O arquivo existe, mas não contém JSON válido.")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

def main():
    print("=== Programa de Leitura e Escrita JSON ===")
    caminho_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ").strip()
    
    if not caminho_arquivo.endswith(".json"):
        caminho_arquivo += ".json"
    
    # Dados para salvar
    pessoa = {
        "nome": "Aline",
        "idade": 30,
        "cidade": "São Paulo"
    }
    
    # Salvar no arquivo JSON
    salvar_json(caminho_arquivo, pessoa)
    
    # Ler o arquivo JSON
    ler_json(caminho_arquivo)

if __name__ == "__main__":
    main()
