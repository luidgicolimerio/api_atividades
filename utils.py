from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Rodrigo', idade=35)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Marcos').first()
    print(pessoa.idade)

def altera_pessoas():
    # pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rodrigo').first()
    pessoa.exclui()

if __name__ == '__main__':
    #insere_pessoas()
    altera_pessoas()
    consulta_pessoas()
    exclui_pessoa()
    consulta_pessoas()