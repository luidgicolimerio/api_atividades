from models import Pessoas, Usuarios

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

def insere_usuario():
    usuario = Usuarios(login='Colimerio', senha='321')
    usuario.save()
    print(usuario)

def consulta_usuarios():
    usuarios= Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoas()
    # consulta_pessoas()
    # exclui_pessoa()
    # consulta_pessoas()
    insere_usuario()
    consulta_usuarios()