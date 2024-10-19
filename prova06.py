loginCorreto = "Luiz"
senhaCorreta = "Voar"

tentativasMaximas = 3

for tentar in range(tentativasMaximas):
    login = input("Digite o nome:")
    senha = input("Digite a senha:")

    if login == loginCorreto and senha == senhaCorreta:
        print("Você está logado!")
        break
    else:
        tentativasSobradas = tentativasMaximas - (tentar + 1)
        
        if tentativasSobradas > 0:
            print(f"Incorreto! Você tem {tentativasSobradas} que restam")
        else:
            for _ in range(3):
                print("Não possui acesso!")
