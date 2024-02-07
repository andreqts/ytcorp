from sqlalchemy.orm import sessionmaker
import models as dbm
from sqlalchemy import inspect #TODOAQ:
from enum import IntEnum, auto


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

class St(IntEnum):
    GD = 0
    AGENCIA = auto()
    INSTITUTOS = auto()
    JORNALISTAS = auto()
    POLITICOS = auto()
    GERACAO = auto()
    TRANSMISSAO = auto()
    DISTRIBUIDORAS = auto()
    COMERCIALIZACAO = auto()


listCatVideos = [
    'ENTREVISTAS',
    'DEBATES ONLINE',
    'DEBATES PRESENCIAIS',
    'VIDEOS DIDÁTICOS',
    'APRESENTAÇÕES EM EVENTOS PRESENCIAIS',
    'APRESENTAÇÃO EM EVENTOS ONLINES',
]

class Ct(IntEnum):
    ENTR = 0
    DBT_ON = auto()
    DBT_PR = auto()
    VD_DID = auto()
    APR_EV_PR = auto()
    APR_EV_ON = auto()
    
listPalestrantes = [
    #NOME, SETORES (indices), AFILIACAO, EXPERIENCIA    
    ('JERSON KELMAN', [St.AGENCIA, St.INSTITUTOS], 'UFRJ', 51),
    ('RICHARD LEE HOCHSTETLER', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 21)
]

class Pltr(IntEnum):
    KELMAN = 0
    HOCHSTETLER = auto()

listVideos = [
    # TITLE, ID, CATEGORIA (indice), PALESTRANTES (indices)
    ('Brazil Energy Frontiers 2023 - Parte 03', '6hwMm02R944', Ct.APR_EV_PR, [Pltr.KELMAN, Pltr.HOCHSTETLER])
]

if __name__ == '__main__':
    session = dbm.makeSession()

    # inserção dos setores
    try:
        for nomeSetor in listSetores:
            print(f'Inserting sector "{nomeSetor}"...')
            recsetor = dbm.Setores(nome=nomeSetor)
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

            print(f'Inserting palestrante "{pnome}"...')
            setoresResult = session.query(dbm.Setores).filter(dbm.Setores.nome.in_(psetores))
            setores = setoresResult.all()

            palestrante = dbm.Palestrantes(nome=pnome, experiencia=pexper,
                                    afiliacao=pafil, listSetores=setores)
        
            palestrante.insert(session)
        session.commit()
    except:
        print('Exception inserting Palestrantes!')
        session.rollback()
        raise

    # inserção das categorias de videos
    session = dbm.makeSession()

    try:
        for nomeCat in listCatVideos:
            print(f'Inserting video category "{nomeCat}"...')
            recCat = dbm.CategoriasVideo(nome=nomeCat)
            recCat.insert(session)
        
        session.commit()
    except:
        print('Exception inserting CategoriasVideo!')
        session.rollback()
        raise
    
    # inserção dos videos
    session = dbm.makeSession()

    try:
        for videoData in listVideos:
            vtitle = videoData[0]
            vid = videoData[1]
            vcat = listCatVideos[videoData[2]]

            catResults = session.query(dbm.CategoriasVideo).filter(dbm.CategoriasVideo.nome == vcat)
            categoria = catResults.one()

            vpalestr = [listPalestrantes[i][0] for i in videoData[3]]
            palstrResults = session.query(dbm.Palestrantes).filter(dbm.Palestrantes.nome.in_(vpalestr))
            palestrantes = palstrResults.all()

            print(f'Inserting video "{vtitle}"...')
            video = dbm.Videos(title=vtitle, yt_id=vid, categoria=categoria, palestrantes=palestrantes)
            video.insert(session)
        
        session.commit()
    except:
        print('Exception inserting Videos!')
        session.rollback()
        raise

    print('Done!')

    




