class Disciplina:
    __nome: str
    __professor: str
    __ano: int
    __semestre: int
    __alunos: list

    def __init__(self, nome: str, prof: str, ano: int, semestre: int, alunos: list):
        self.__nome = nome
        self.__professor = prof
        self.__ano= ano
        self.__semestre = semestre
        self.__alunos = alunos




