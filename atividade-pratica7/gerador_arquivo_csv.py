import csv

def criar_csv(caminho_arquivo):
    # Lista de pessoas (nome, idade, cidade)
    pessoas = [
        {"nome": "Ana",     "idade": 25, "cidade": "São Paulo"},
        {"nome": "Bruno",   "idade": 32, "cidade": "Rio de Janeiro"},
        {"nome": "Carla",   "idade": 28, "cidade": "Belo Horizonte"},
        {"nome": "Diego",   "idade": 40, "cidade": "Curitiba"},
        {"nome": "Fernanda","idade": 22, "cidade": "Recife"}
    ]
    
    try:
        # Abre o arquivo para escrita
        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=["nome", "idade", "cidade"])
            
            # Escreve o cabeçalho
            escritor.writeheader()
            
            # Escreve cada linha de dados
            for pessoa in pessoas:
                escritor.writerow(pessoa)
        
        print(f"✅ Arquivo '{caminho_arquivo}' criado e salvo com sucesso!")
    
    except Exception as e:
        print(f"❌ Falha ao salvar o arquivo: {e}")

def main():
    print("=== Criador de Arquivo CSV ===")
    caminho_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ").strip()
    
    if not caminho_arquivo.endswith(".csv"):
        caminho_arquivo += ".csv"
    
    criar_csv(caminho_arquivo)

if __name__ == "__main__":
    main()
