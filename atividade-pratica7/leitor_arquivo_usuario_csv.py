import csv

def ler_csv(caminho_arquivo):
    try:
        # Abre o arquivo CSV para leitura
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            
            print("\n=== Conteúdo do Arquivo CSV ===\n")
            
            # Percorre cada linha do arquivo e exibe
            for linha in leitor:
                print(linha)
    
    except FileNotFoundError:
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

def main():
    print("=== Leitor de Arquivo CSV ===")
    caminho_arquivo = input("Digite o caminho do arquivo CSV: ").strip()
    
    ler_csv(caminho_arquivo)

if __name__ == "__main__":
    main()
