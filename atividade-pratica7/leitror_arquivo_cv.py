import pandas as pd

def analisar_logs(caminho_arquivo):
    try:
        # Lendo o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        
        # Verifica se a coluna existe
        if 'tempo_execucao' not in df.columns:
            print("❌ A coluna 'tempo_execucao' não foi encontrada no arquivo CSV.")
            return
        
        # Calculando média e desvio padrão
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()
        
        print("\n=== Análise dos Logs de Treinamento ===")
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
    
    except FileNotFoundError:
        print(f"❌ Arquivo '{caminho_arquivo}' não encontrado.")
    except pd.errors.EmptyDataError:
        print("❌ O arquivo está vazio ou corrompido.")
    except Exception as e:
        print(f"❌ Erro inesperado ao ler o arquivo: {e}")

def main():
    print("=== Analisador de Logs de Treinamento ===")
    caminho_arquivo = input("Digite o caminho do arquivo CSV: ").strip()
    
    analisar_logs(caminho_arquivo)

if __name__ == "__main__":
    main()
