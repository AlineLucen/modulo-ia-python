import random
import string

def gerar_senha(tamanho):
    # Conjunto de caracteres: letras maiúsculas, minúsculas, dígitos e símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Gera a senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Seguras ===")
    
    # Pede ao usuário o tamanho da senha
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha: "))
            if tamanho <= 0:
                print("Por favor, insira um número maior que 0.")
            else:
                break
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
    
    senha = gerar_senha(tamanho)
    print(f"\nSua senha gerada é: {senha}")

if __name__ == "__main__":
    main()
