from quiz import *

if __name__ == "__main__":
    q1 = Quiz(10, 2)
    print(q1)
    print(f'Erros {q1.get_erros()}\n')
    print(f'Acertos {q1.get_acertos()}')

    q2 = Quiz2A(10, 2)
    print(q2)
    q3 = Quiz3A(10, 2)
    print(q3)

    List_quiz = [q1, q2, q3]

    aluno1 = Aluno(1, "Ana", List_quiz)
    print(aluno1)
    aluno2 = Aluno(2, "Rafael", List_quiz)
    print(aluno2)

    poo = Disciplina("Poo", "Ferauch", 2024, 2)
    poo.add_aluno(aluno1)
    poo.add_aluno(aluno2)


    print(poo)
