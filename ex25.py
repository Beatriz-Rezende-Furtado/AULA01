#  Crie um programa que permita ao usuário cadastrar nomes de alunos em uma lista.
# Depois, exiba todos os alunos cadastrados. Pergunte ao usuário se deseja remover 
# um aluno específico. Exiba a lista atualizada após a remoção.

def alunos(): 
    aluno = input("Digite o nome dos estudantes cadastrar separados por um espaço: ").split()
    print(f"{alunos}")
    
    if alunos: 
        opcao = input("Deseja remover um aluno [1] sim ou [2] nao?: ")
        if opcao == 'sim' or '1':
            excluir_aluno = input("Digite o nome do aluno que deseja remover: ")
            if excluir_aluno in alunos:
                alunos.remove(excluir_aluno)
                print(f"{alunos}")
            else:
                print("Esse aluno não existe.")
    else:
        print("Não há alunos")


