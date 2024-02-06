from sqlalchemy.orm import sessionmaker
import models as dbm
from sqlalchemy import inspect #TODOAQ:


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

listPalestrantes = [
    #NOME, SETORES (indices), AFILIACAO, EXPERIENCIA    
    ('JERSON KELMAN', [1, 2], 'UFRJ', 51),
    ('RICHARD LEE HOCHSTETLER', [2], 'INSTITUTO ACENDE BRASIL', 21)
]

if __name__ == '__main__':
    session = dbm.makeSession()

    # remover todos os arquivos previamente existentes
    num_deleted = 0
    try:
        num_deleted = session.query(dbm.Setor).delete()
        session.commit()
    except:
        session.rollback()

    if (num_deleted):
        print('{} preexisting rows deleted...'.format(num_deleted))

    session = dbm.makeSession()

    # inserção dos setores
    try:
        for nomeSetor in listSetores:
            recsetor = dbm.Setor(nome=nomeSetor)
            recsetor.insert(session)

        session.commit()
    except:
        print('Exception inserting sectors!')
        session.rollback()
        raise

    # inserção dos palestrantes
    session = dbm.makeSession()

    try:

        for palestrData in listPalestrantes:
            pnome = palestrData[0]
            psetores = [listSetores[i] for i in palestrData[1]]
            pafil = palestrData[2]
            pexper = palestrData[3]

            print(f'Inserting palestrante {pnome}...')
            setoresResult = session.query(dbm.Setor).filter(dbm.Setor.nome.in_(psetores))
            setores = setoresResult.all()
            print('setores results = ', setores)

            palestrante = dbm.Palestrante(nome=pnome, experiencia=pexper,
                                    afiliacao=pafil, listSetores=setores)
        
            palestrante.insert(session)
        session.commit()
    except:
        print('Exception inserting Palestrantes!')
        session.rollback()
        raise

    




