from sqlalchemy.orm import sessionmaker
import models as dbm
from sqlalchemy import inspect #TODOAQ:
from enum import IntEnum, auto
from datetime import date

# insert SETORES

listSetores = [
    'GD',
    'AGÊNCIA REGULADORA', 
    'UNIVERSIDADES, CONSULTORIAS E INSTITUTOS DE PESQUISA',
    'JORNALISTAS',
    'POLÍTICOS PROFISSIONAIS',
    'GERAÇÃO',
    'TRANSMISSÃO',
    'DISTRIBUIDORAS',
    'COMERCIALIZAÇÃO',
    'CONSUMIDORES',
    'CONSULTORES JURÍDICOS',
    'GESTÃO E INVESTIMENTOS'
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
    CONSUMIDORES = auto()
    ADVOGADOS = auto()
    INVESTIMENTOS = auto()

listCatVideos = [
    'ENTREVISTA ONLINE',
    'ENTREVISTA PRESENCIAL',    
    'DEBATES ONLINE',
    'DEBATES PRESENCIAIS',
    'VIDEOS DIDÁTICOS',
    'APRESENTAÇÕES EM EVENTOS PRESENCIAIS',
    'APRESENTAÇÃO EM EVENTOS ONLINES',
]

class Ct(IntEnum):
    ENTR_ON = 0
    ENTR_PR = auto()
    DBT_ON = auto()
    DBT_PR = auto()
    VD_DID = auto()
    APR_EV_PR = auto()
    APR_EV_ON = auto()
    
listPalestrantes = [
    #NOME, SETORES (indices), AFILIACAO, EXPERIENCIA (na ind. de energia)   
    ('AGNES MARIA DE ARAGÃO DA COSTA', [St.AGENCIA], 'ANEEL', 9),
    ('ALEX CHERMUCSNIS VIEIRA', [St.INVESTIMENTOS], 'COPPERLEAF STRATEGIC MANAGEMENT', 20),
    ('ALEXANDRE UHLIG', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 18),
    ('ANDRE RUELLI', [St.AGENCIA], 'ANEEL', 23),
    ('ANGELA SARAIVA', [St.COMERCIALIZACAO], 'ELECTRA ENERGY', 23),
    ('ARNALDO CALIL PEREIRA JARDIM', [St.POLITICOS], 'DEPUTADO FEDERAL - CIDADANIA', 0),
    ('BÁRBARA RUBIM', [St.GD, St.ADVOGADOS], 'ABSOLAR', 7),
    ('BENTO COSTA LIMA LEITE DE ALBUQUERQUE JUNIOR', [St.POLITICOS], 'Ex-ministro', 8),
    ('CARLOS ALBERTO CALIXTO MATTAR', [St.INSTITUTOS], 'ANEEL', 40),
    ('CLAUDIO FABIANO ALVES', [St.COMERCIALIZACAO], 'ELECTRA ENERGY', 11),
    ('CLAUDIO J. D. SALES', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 30),
    ('DANILO FORTE', [St.POLITICOS], 'DEPUTADO FEDERAL UNIÃO-CE', 0),
    ('EDUARDO MUELLER MONTEIRO', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 21),
    ('EDVALDO SANTANA', [St.INSTITUTOS, St.AGENCIA, St.CONSUMIDORES], 'INSTITUTO ACENDE BRASIL', 30),
    ('EFRAIN PEREIRA DA CRUZ', [St.AGENCIA, St.POLITICOS], 'Ex-Diretor da ANEEL', 9),
    ('EMANUEL SIMON', [St.INSTITUTOS], 'LATIN AMERICA POWER & RENEWABLES', 14),
    ('FERNANDO BALDOTTO', [St.DISTRIBUIDORAS], 'EDP BRASIL', 19),
    ('FERNANDO MOSNA', [St.AGENCIA, St.ADVOGADOS], 'ANEEL', 14),
    ('GREG GUTHRIDGE', [St.INSTITUTOS], 'Ernst & Young', 34),
    ('GUILHERME CHRISPIM', [St.GD], 'ABGD', 9),
    ('GUILHERME SUSTERAS', [St.GD], 'ABSOLAR', 7),
    ('HÉLVIO NEVES GUERRA', [St.AGENCIA], 'ANEEL', 43),
    ('JERSON KELMAN', [St.AGENCIA, St.INSTITUTOS], 'UFRJ', 51),
    ('JESSIANE PEREIRA', [St.AGENCIA], 'ANEEL', 7),
    ('JOSÉ MÁRIO ABDO', [St.INSTITUTOS, St.AGENCIA], 'ABDO, ELLERY & ASSOCIADOS', 51),
    ('LAVINIA HOLLANDA', [St.INSTITUTOS], 'ESCOPO ENERGIA', 10),
    ('LEANDRO CAIXETA MOREIRA', [St.POLITICOS, St.AGENCIA], 'ANEEL', 20),
    ('LUIZ AUGUSTO NOBREGA BARROSO', [St.INSTITUTOS], 'PSR', 26),
    ('MARCIA MASSOTTI', [St.DISTRIBUIDORAS], 'ENEL', 18),
    ('MARCOS AURÉLIO MADUREIRA DA SILVA', [St.DISTRIBUIDORAS], 'ABRADEE', 48),
    ('MAURICIO ALVARES DA SILVA VELLOSO FERREIRA', [St.DISTRIBUIDORAS], 'EQUATORIAL', 9),
    ('NARA RÚBIA DE SOUZA', [St.AGENCIA], 'ANEEL', 28),
    ('NICOLÒ ROSSETTO', [St.INSTITUTOS], 'FLORENCE SCHOOL OF REGULATION', 15),
    ('PEDRO MELLO LOMBARDI', [St.AGENCIA], 'ANEEL', 19),
    ('RAPHAEL GOMES', [St.ADVOGADOS], 'LEFOSSE ADVOGADOS', 23),
    ('RENATO POVIA', [St.GERACAO, St.TRANSMISSAO, St.DISTRIBUIDORAS, St.COMERCIALIZACAO], 'CPFL ENERGIA', 12),
    ('RICARDO BRANDAO SILVA', [St.DISTRIBUIDORAS], 'ABRADEE', 20),
    ('RICARDO FERNANDEZ', [St.INSTITUTOS], 'Ernst & Young', 26),
    ('RICARDO LAVORATO TILI', [St.AGENCIA], 'ANEEL', 17),
    ('RICARDO PEREZ BOTELHO', [St.GERACAO, St.TRANSMISSAO, St.DISTRIBUIDORAS, St.COMERCIALIZACAO], 'ENERGISA', 23),
    ('RICHARD LEE HOCHSTETLER', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 21),
    ('RODRIGO FERREIRA', [St.COMERCIALIZACAO, St.JORNALISTAS], 'ABRACEEL', 24),
    ('RODRIGO LOPES SAUAIA', [St.INSTITUTOS], 'ABSOLAR', 16),
    ('RODRIGO MORISHITA WADA', [St.ADVOGADOS], 'UniCEUB', 0),
    ('RODRIGO ROLLEMBERG', [St.POLITICOS], 'SECRETARIO - PSB', 0),
    ('SANDOVAL DE ARAUJO FEITOSA NETO', [St.AGENCIA], 'ANEEL', 21),
    ('SOLANGE RIBEIRO', [St.DISTRIBUIDORAS, St.INSTITUTOS], 'NEOENERGIA', 20),
    ('STEFANIA RELVA', [St.INSTITUTOS], 'USP', 12),
    ('TIAGO LEITE FERREIRA', [St.INSTITUTOS], 'UNIVERSIDADE DE COMILLAS, ESPANHA', 19),
    ('VLADIMIRO HENRIQUE BARROSA PINTO DE MIRANDA', [St.INSTITUTOS], 'UNIVERSIDADE DO PORTO', 41),
    ('WALMIR DE FREITAS FILHO', [St.INSTITUTOS], 'UNICAMP', 23),
]


class Pltr(IntEnum):
    AGNES = 0
    VIEIRA = auto()
    UHLIG = auto()
    RUELLI = auto()
    ANGELA = auto()
    JARDIM = auto()
    BARBARA = auto()
    BENTO = auto()
    MATTAR = auto()
    CLAUDIO = auto()
    SALES = auto()
    DANILO = auto()
    MONTEIRO = auto()
    EDVALDO = auto()
    EFRAIN = auto()
    SIMON = auto()
    BALDOTTO = auto()
    MOSNA = auto()
    GREG = auto()
    CHRISPIM = auto()
    SUSTERAS = auto()
    HELVIO = auto()
    KELMAN = auto()
    JESSIANE = auto()
    ABDO = auto()
    LAVINIA = auto()
    CAIXETA = auto()
    BARROSO = auto()
    MASSOTTI = auto()
    MADUREIRA = auto()
    VELLOSO = auto()
    NARA = auto()
    ROSSETTO = auto()
    LOMBARDI = auto()
    RAPHAEL = auto() 
    POVIA = auto()
    BRANDAO = auto()
    FERNANDEZ = auto()
    TILI = auto()
    BOTELHO = auto()
    HOCHSTETLER = auto()
    FERREIRA = auto()
    SAUAIA = auto()
    MORISHITA = auto()
    ROLLEMBERG = auto()
    SANDOVAL = auto()
    SOLANGE = auto()
    RELVA = auto()
    TIAGO = auto()
    VLADIMIRO = auto()
    WALMIR = auto()

listVideos = [
    # TITLE, ID, CATEGORIA (indice), PALESTRANTES (indices), DATA (formato ISO)
    ('Seminário “O Futuro do Consumidor de Energia Elétrica” – 5/5/2022 – Parte 1', 'UntRu_fFeLU', Ct.APR_EV_PR,
        [Pltr.SANDOVAL, Pltr.DANILO, Pltr.JARDIM, Pltr.BENTO, Pltr.GREG, Pltr.FERNANDEZ, Pltr.EFRAIN, Pltr.MORISHITA,
         Pltr.AGNES, Pltr.FERREIRA, Pltr.LAVINIA], "03:36:07", "2022-05-05"),
    ('Seminário “O Futuro do Consumidor de Energia Elétrica” – 5/5/2022 – Parte 2', 'LivoOrKfi1Y', Ct.APR_EV_PR,
        [Pltr.SANDOVAL, Pltr.BARROSO, Pltr.TIAGO, Pltr.VLADIMIRO, Pltr.ROSSETTO, Pltr.HELVIO, Pltr.WALMIR, Pltr.BOTELHO,
         Pltr.VELLOSO, Pltr.POVIA], "03:36:08", "2022-05-05"),
    ('CanalEnergia Debate os caminhos da Geração Distribuída no Brasil', '9iwHMbiA7mA', Ct.DBT_ON, 
        [Pltr.MADUREIRA, Pltr.NARA, Pltr.RAPHAEL, Pltr.CHRISPIM], "01:30:55", "2023-04-27"),
    ('ENERGY Tech TALKS | Temporada 4, Episódio 1', 'XFIplF43xbo', Ct.DBT_ON, 
        [Pltr.EDVALDO, Pltr.ANGELA, Pltr.CLAUDIO], "01:10:38", "2023-08-24"),
    ('ENERGY Tech TALKS | Temporada 4, Episódio 2', 'misg_b6ut0s', Ct.ENTR_ON, 
        [Pltr.BALDOTTO, Pltr.VIEIRA], "01:00:14", "2023-10-06"),
    ('Brazil Energy Frontiers 2023 - Parte 01', 'rVQRj8MCQFk', Ct.APR_EV_PR, 
        [Pltr.UHLIG, Pltr.SIMON], "01:36:34", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 02', 'Bl4UnXyjjB0', Ct.APR_EV_PR, 
        [Pltr.JARDIM, Pltr.MASSOTTI, Pltr.ROLLEMBERG, Pltr.RELVA, Pltr.MONTEIRO], "01:17:31", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 03', '6hwMm02R944', Ct.APR_EV_PR, 
        [Pltr.KELMAN, Pltr.HOCHSTETLER], "01:40:42", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 04', '7xnTO0g0D7s', Ct.APR_EV_PR, 
        [Pltr.ABDO, Pltr.CAIXETA, Pltr.SOLANGE, Pltr.BRANDAO, Pltr.SALES], "01:18:37", "2023-10-25"),    
    ('Mesa Redonda – Desafios da Micro e Minigeração Distribuída', 'JovmyoI0Wxs', Ct.APR_EV_PR, 
        [Pltr.MOSNA, Pltr.TILI, Pltr.HELVIO, Pltr.SAUAIA, Pltr.LOMBARDI, Pltr.BARBARA, 
         Pltr.JESSIANE], "03:43:21", "2023-11-23"),
    ('SETOR ELÉTRICO PASSADO, PRESENTE, FUTURO', 'zVlDMCxat_c', Ct.ENTR_PR, 
        [Pltr.EDVALDO], "01:17:29", "2024-10-24"),
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

            vduracao = videoData[4]

            vdata = date.fromisoformat(videoData[5])

            print(f'Inserting video "{vtitle}"...')
            video = dbm.Videos(title=vtitle, yt_id=vid, categoria=categoria, palestrantes=palestrantes,
                                duracao=vduracao, data=vdata)
            video.insert(session)
        
        session.commit()
    except:
        print('Exception inserting Videos!')
        session.rollback()
        raise




    print('Done!')

    




