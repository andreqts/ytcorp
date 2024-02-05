from sqlalchemy.orm import sessionmaker
import models as dbm


# insert SETORES

listSetores = [
    'GD',
    'AGÊNCIA REGULADORA', 
    'UNIVERSIDADES E INSTITUTOS DE PESQUISA',
    'JORNALISTAS',
    'POLÍTICOS PROFISSIONAIS',
    'GERAÇÃO',
    'TRANSMISSÃO',
    'DISTRIBUIDORAS',
    'COMERCIALIZAÇÃO'
]

if __name__ == '__main__':
    session = dbm.makeSession()

    # remover todos os arquivos previamente existentes
    try:
        num_deleted = session.query(dbm.Setor).delete()
        session.commit()
    except:
        session.rollback()

    if (num_deleted):
        print('{} preexisting rows deleted...'.format(num_deleted))

    for nomeSetor in listSetores:
        recsetor = dbm.Setor(nome=nomeSetor)
        print('--> inserting setor "{}"'.format(nomeSetor))
        recsetor.insert(session)

    print('Now commiting insertions to table SETOR...')
    recsetor.update(session)




