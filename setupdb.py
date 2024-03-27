from sqlalchemy.orm import sessionmaker
import models as dbm
from sqlalchemy import inspect #TODOAQ:
from enum import IntEnum, auto
from datetime import date

# insert SETORES

listSetores = [
    'GD',
    'AGÊNCIA REGULADORA E ÓRGÃOS DE GOVERNO', #ANEEL, EPE, ONS, etc...
    'UNIVERSIDADES, CONSULTORIAS E INSTITUTOS DE PESQUISA',
    'JORNALISTAS',
    'POLÍTICOS PROFISSIONAIS',
    'GERAÇÃO',
    'TRANSMISSÃO',
    'DISTRIBUIDORAS',
    'COMERCIALIZAÇÃO',
    'CONSUMIDORES',
    'CONSULTORES JURÍDICOS',
    'GESTÃO E INVESTIMENTOS',
    'FABRICANTES DE EQUIPAMENTOS E TECNOLOGIA'
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
    FABRICANTES = auto()

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
    ('ALDO DE JESUS PESSANHA', [St.DISTRIBUIDORAS], 'ENEL', 17),    
    ('ALEX CHERMUCSNIS VIEIRA', [St.INVESTIMENTOS], 'COPPERLEAF STRATEGIC MANAGEMENT', 20),
    ('ALEXANDRE UHLIG', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 18),
    ('ALTINO VENTURA FILHO', [St.INSTITUTOS], 'ACADEMIA NACIONAL DE ENGENHARIA', 52),
    ('AMANDA LACERDA PRADO', [St.DISTRIBUIDORAS], 'ENERGISA', 9),
    ('ANDRE RUELLI', [St.AGENCIA], 'ANEEL', 23),
    ('ÂNGELA GOMES', [St.INSTITUTOS], 'PSR', 25),
    ('ÂNGELA SARAIVA', [St.COMERCIALIZACAO], 'ELECTRA ENERGY', 23),
    ('ARNALDO CALIL PEREIRA JARDIM', [St.POLITICOS], 'DEPUTADO FEDERAL - CIDADANIA', 0),
    ('BÁRBARA RUBIM', [St.GD, St.ADVOGADOS], 'ABSOLAR', 7),
    ('BENTO COSTA LIMA LEITE DE ALBUQUERQUE JUNIOR', [St.POLITICOS], 'Ex-ministro', 8),
    ('BERNARDO MARANGON', [St.COMERCIALIZACAO, St.FABRICANTES], 'EXATA ENERGIA', 14),
    ('BRUNO HENRIQUE KIKUMOTO DE PAULA', [St.GD, St.INSTITUTOS], 'CANAL SOLAR', 7),
    ('CAMILA FIQUEIREDO BOMFIM LOPES', [St.AGENCIA], 'ANEEL', 24),
    ('CARLOS ALBERTO CALIXTO MATTAR', [St.INSTITUTOS], 'ANEEL', 40),
    ('CARLOS AUGUSTO LEITE BRANDÃO', [St.INSTITUTOS], 'CAE / ABAQUE', 40),
    ('CLAUDIO ELIAS CARVALHO', [St.FABRICANTES], 'VOLT ROBOTICS', 24),
    ('CLAUDIO FABIANO ALVES', [St.COMERCIALIZACAO], 'ELECTRA ENERGY', 11),
    ('CLAUDIO J. D. SALES', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 30),
    ('CRISTIANO VIEIRA DA SILVA', [St.AGENCIA], 'ONS / ANEEL', 21),    
    ('DANILO FORTE', [St.POLITICOS], 'DEPUTADO FEDERAL UNIÃO-CE', 0),
    ('DIEGO LUÍS BRANCHER', [St.AGENCIA], 'ANEEL', 18),
    ('DJALMA MOSQUEIRA FALCÃO', [St.INSTITUTOS], 'UFRJ', 50),
    ('DONATO DA SILVA FILHO', [St.FABRICANTES], 'VOLT ROBOTICS', 20),
    ('EDUARDO MUELLER MONTEIRO', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 21),
    ('EDVALDO SANTANA', [St.INSTITUTOS, St.AGENCIA, St.CONSUMIDORES], 'UFSC', 30),
    ('EFRAIN PEREIRA DA CRUZ', [St.AGENCIA, St.POLITICOS], 'Ex-Diretor da ANEEL', 9),
    ('EMANUEL SIMON', [St.INSTITUTOS], 'LATIN AMERICA POWER & RENEWABLES', 14),
    ('ERIK REGO', [St.INSTITUTOS], 'PSR', 21),
    ('EWERTON GUARNIER', [St.FABRICANTES], 'VOLT ROBOTICS', 16),
    ('FELIPE GONÇALVES', [St.INSTITUTOS], 'FGV ENERGIA RESEARCH', 20),
    ('FERNANDO BALDOTTO', [St.DISTRIBUIDORAS], 'EDP BRASIL', 19),
    ('FERNANDO MOSNA', [St.AGENCIA, St.ADVOGADOS], 'ANEEL', 14),
    ('GREG GUTHRIDGE', [St.INSTITUTOS], 'Ernst & Young', 34),
    ('GUILHERME CHRISPIM', [St.GD], 'ABGD', 9),
    ('GUILHERME GOLDBACH', [St.INSTITUTOS], 'MITSIDI', 7),
    ('GUILHERME SUSTERAS', [St.GD], 'ABSOLAR', 7),
    ('HÉLVIO NEVES GUERRA', [St.AGENCIA], 'ANEEL', 43),
    ('IONY PATRIOTA DE SIQUEIRA', [St.AGENCIA, St.INSTITUTOS], 'CIGRE/ACADEMIA NACIONAL DE ENGENHARIA', 23),
    ('IURI DE OLIVEIRA BAROUCHE', [St.DISTRIBUIDORAS], 'ENEL', 16),
    ('JAN KNAACK', [St.INSTITUTOS], 'GIZ', 15),
    ('JERSON KELMAN', [St.AGENCIA, St.INSTITUTOS], 'UFRJ', 51),
    ('JESSIANE PEREIRA', [St.AGENCIA], 'ANEEL', 7),
    ('JERZY ZBIGNIEW LEOPOLD LEPECKI', [St.INSTITUTOS], 'ACADEMIA NACIONAL DE ENGENHARIA / CIGRE', 71),
    ('JOSÉ MÁRIO ABDO', [St.INSTITUTOS, St.AGENCIA], 'ABDO, ELLERY & ASSOCIADOS', 51),
    ('LAVINIA HOLLANDA', [St.INSTITUTOS], 'ESCOPO ENERGIA', 10),
    ('LEANDRO CAIXETA MOREIRA', [St.POLITICOS, St.AGENCIA], 'ANEEL', 20),
    ('LINDEMBERG REIS', [St.DISTRIBUIDORAS], 'ABRADEE', 18),
    ('LUCAS NOURA GUIMARÃES', [St.DISTRIBUIDORAS], 'EDP', 7),
    ('LUIZ AUGUSTO NOBREGA BARROSO', [St.INSTITUTOS], 'PSR', 26),
    ('MARCIA MASSOTTI', [St.DISTRIBUIDORAS], 'ENEL', 18),
    ('MARCOS AURÉLIO MADUREIRA DA SILVA', [St.DISTRIBUIDORAS], 'ABRADEE', 48),
    ('MARCOS VASCONCELOS', [St.AGENCIA], 'ANEEL', 14),
    ('MÁRIO LUIZ MENEL DA CUNHA', [St.INSTITUTOS, St.GERACAO, St.COMERCIALIZACAO], 'ACADEMIA NACIONAL DE ENGENHARIA / ABIAPE', 56),
    ('MARKUS VLASITS', [St.INSTITUTOS], 'NEWCHARGE ENERGY', 11),
    ('MAURICIO ALVARES DA SILVA VELLOSO FERREIRA', [St.DISTRIBUIDORAS], 'EQUATORIAL', 9),
    ('NARA RÚBIA DE SOUZA', [St.AGENCIA], 'ANEEL', 28),
    ('NELSON JOSE HUBNER MOREIRA', [St.AGENCIA, St.INSTITUTOS], 'GESEL E EX-ANEEL', 30),
    ('NELSON FONTES SIFFERT FILHO', [St.INSTITUTOS], 'ICT RESEL', 2),
    ('NELSON MARTINS', [St.INSTITUTOS], 'CIGRE', 46),
    ('NICOLÒ ROSSETTO', [St.INSTITUTOS], 'FLORENCE SCHOOL OF REGULATION', 15),
    ('PAULO ANDRÉ SEHN DA SILVA', [St.INSTITUTOS], 'ABIAPE', 15),
    ('PAULO GOMES', [St.INSTITUTOS], 'ACAMEDIA NACIONAL DE ENGENHARIA', 52),
    ('PAULO LUCIANO DE CARVALHO', [St.AGENCIA], 'ANEEL', 30),
    ('PEDRO MELLO LOMBARDI', [St.AGENCIA], 'ANEEL', 19),
    ('PIETRO ERBER', [St.INSTITUTOS], 'INSTITUTO NACIONAL DE EFICIÊNCIA ENERGÉTICA', 20),
    ('RAPHAEL GOMES', [St.ADVOGADOS], 'LEFOSSE ADVOGADOS', 23),
    ('RENATA DE OLIVEIRA E SILVA', [St.DISTRIBUIDORAS], 'EQUATORIAL', 14),
    ('RENATO HADDAD SIMÕES MACHADO', [St.AGENCIA], 'EPE', 15),
    ('RENATO POVIA', [St.GERACAO, St.TRANSMISSAO, St.DISTRIBUIDORAS, St.COMERCIALIZACAO], 'CPFL ENERGIA', 12),
    ('RICARDO BRANDAO SILVA', [St.DISTRIBUIDORAS], 'ABRADEE', 20),
    ('RICARDO FERNANDEZ', [St.INSTITUTOS], 'Ernst & Young', 26),
    ('RICARDO LAVORATO TILI', [St.AGENCIA], 'ANEEL', 17),
    ('RICARDO PEREZ BOTELHO', [St.GERACAO, St.TRANSMISSAO, St.DISTRIBUIDORAS, St.COMERCIALIZACAO], 'ENERGISA', 23),
    ('RICHARD LEE HOCHSTETLER', [St.INSTITUTOS], 'INSTITUTO ACENDE BRASIL', 21),
    ('ROBERTO DE CARVALHO BRANDAO', [St.INSTITUTOS], 'GESEL', 14),
    ('ROBERTO VALER', [St.FABRICANTES], 'HUAWEI', 19),
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
    ALDO = auto()
    VIEIRA = auto()
    UHLIG = auto()
    ALTINO = auto()
    AMANDA = auto()
    RUELLI = auto()
    AGOMES = auto()
    ANGELA = auto()
    JARDIM = auto()
    BARBARA = auto()
    BENTO = auto()
    BERNARDO = auto()
    BRUNO = auto()
    CAMILA = auto()
    MATTAR = auto()
    CARLOS = auto()
    CARVALHO = auto()
    CLAUDIO = auto()
    SALES = auto()
    CRISTIANO = auto()
    DANILO = auto()
    BRANCHER = auto()
    FALCAO = auto()
    DONATO = auto()
    MONTEIRO = auto()
    EDVALDO = auto()
    EFRAIN = auto()
    SIMON = auto()
    ERIK = auto()
    EWERTON = auto()
    FELIPE = auto()
    BALDOTTO = auto()
    MOSNA = auto()
    GREG = auto()
    CHRISPIM = auto()
    GOLDBACH = auto()
    SUSTERAS = auto()
    HELVIO = auto()
    IONY = auto()
    BAROUCHE = auto
    JAN = auto()
    KELMAN = auto()
    JESSIANE = auto()
    LEPECKI = auto()
    ABDO = auto()
    LAVINIA = auto()
    CAIXETA = auto()
    LINDEMBERG = auto()
    LUCAS = auto()
    BARROSO = auto()
    MASSOTTI = auto()
    MADUREIRA = auto()
    VASCONCELOS = auto()
    MENEL = auto()
    VLASITS = auto()
    VELLOSO = auto()
    NARA = auto()
    HUBNER = auto()
    SIFFERT = auto()
    MARTINS = auto()
    ROSSETTO = auto()
    SEHN = auto()
    GOMES = auto()
    PAULO = auto()
    LOMBARDI = auto()
    ERBER = auto()
    RAPHAEL = auto()
    RENATA = auto()
    RENATO = auto()
    POVIA = auto()
    BRANDAO = auto()
    FERNANDEZ = auto()
    TILI = auto()
    BOTELHO = auto()
    HOCHSTETLER = auto()
    ROBERTO = auto()
    VALER = auto()
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
         Pltr.AGNES, Pltr.FERREIRA, Pltr.LAVINIA], "ANEEL", "03:36:07", "2022-05-05"),
    ('Seminário “O Futuro do Consumidor de Energia Elétrica” – 5/5/2022 – Parte 2', 'LivoOrKfi1Y', Ct.APR_EV_PR,
        [Pltr.SANDOVAL, Pltr.BARROSO, Pltr.TIAGO, Pltr.VLADIMIRO, Pltr.ROSSETTO, Pltr.HELVIO, Pltr.WALMIR, Pltr.BOTELHO,
         Pltr.VELLOSO, Pltr.POVIA], "ANEEL", "03:36:08", "2022-05-05"),
    ('CanalEnergia Debate os caminhos da Geração Distribuída no Brasil', '9iwHMbiA7mA', Ct.DBT_ON, 
        [Pltr.MADUREIRA, Pltr.NARA, Pltr.RAPHAEL, Pltr.CHRISPIM], "CANAL ENERGIA", "01:30:55", "2023-04-27"),
    ('Webinar Gesel Armazenamento de energia - 23/05/2023', 'FIzEezK5Mz8', Ct.APR_EV_ON,
        [Pltr.JAN, Pltr.SIFFERT, Pltr.VLASITS, Pltr.GOLDBACH, Pltr.ROBERTO], "GESEL",  "01:46:47", "2023-05-23"),
    ('Webinar sobre Armazenamento de Energia Elétrica - 14/06/2023', 'UHO6jxA3H2c', Ct.DBT_ON,
        [Pltr.HELVIO, Pltr.CRISTIANO, Pltr.RENATO], "ANEEL",  "02:30:12", "2023-06-14"),
    ('Armazenamento e Serviços Ancilares no Sistema Elétrico Brasileiro', 'hNwKPm2l93s', Ct.DBT_ON, 
        [Pltr.CARLOS, Pltr.KELMAN, Pltr.IONY, Pltr.MENEL, Pltr.SANDOVAL, Pltr.SEHN, Pltr.MARTINS, Pltr.GOMES, Pltr.ALTINO, Pltr.ERBER, Pltr.LEPECKI],
         "ACADEMIA NACIONAL DE ENGENHARIA", "02:14:03", "2023-06-20"),
    ('ENERGY Tech TALKS | Temporada 4, Episódio 1', 'XFIplF43xbo', Ct.DBT_ON, 
        [Pltr.EDVALDO, Pltr.ANGELA, Pltr.CLAUDIO], "CANAL ENERGIA", "01:10:38", "2023-08-24", True),
    ('Geração Distribuída', 'sXGz5zH5rxQ', Ct.DBT_ON, [Pltr.CHRISPIM, Pltr.KELMAN, Pltr.MENEL, Pltr.WALMIR,
                                                       Pltr.IONY, Pltr.GOMES, Pltr.ALTINO, Pltr.FALCAO],
     "ACADEMIA NACIONAL DE ENGENHERIA", "01:51:03", "2023-09-14"),
    ('ENERGY Tech TALKS | Temporada 4, Episódio 2', 'misg_b6ut0s', Ct.ENTR_ON, 
        [Pltr.BALDOTTO, Pltr.VIEIRA], "CANAL ENERGIA", "01:00:14", "2023-10-06"),
    ('Webinar | Medidores inteligentes e a modernização do SEB', 'fvNDHoamaTg', Ct.APR_EV_PR, 
        [Pltr.LINDEMBERG, Pltr.KELMAN, Pltr.HUBNER, Pltr.VASCONCELOS, Pltr.ALDO], "FGV",
         "01:37:37", "2023-10-09"),
    ('Energy Summit 2023 - Morning', 'V6yXS0v6ARQ', Ct.APR_EV_PR, [Pltr.VALER], "UFPB CEAR", 
     "03:07:38", "2023-10-20"),
    ('Brazil Energy Frontiers 2023 - Parte 01', 'rVQRj8MCQFk', Ct.APR_EV_PR, 
        [Pltr.UHLIG, Pltr.SIMON], "INSTITUTO ACENDE BRASIL", "01:36:34", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 02', 'Bl4UnXyjjB0', Ct.APR_EV_PR, 
        [Pltr.JARDIM, Pltr.MASSOTTI, Pltr.ROLLEMBERG, Pltr.RELVA, Pltr.MONTEIRO], "INSTITUTO ACENDE BRASIL", 
        "01:17:31", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 03', '6hwMm02R944', Ct.APR_EV_PR, 
        [Pltr.KELMAN, Pltr.HOCHSTETLER], "INSTITUTO ACENDE BRASIL", "01:40:42", "2023-10-25"),
    ('Brazil Energy Frontiers 2023 - Parte 04', '7xnTO0g0D7s', Ct.APR_EV_PR, 
        [Pltr.ABDO, Pltr.CAIXETA, Pltr.SOLANGE, Pltr.BRANDAO, Pltr.SALES], "INSTITUTO ACENDE BRASIL", 
        "01:18:37", "2023-10-25"),    
    ('Mesa Redonda – Desafios da Micro e Minigeração Distribuída', 'JovmyoI0Wxs', Ct.APR_EV_PR, 
        [Pltr.MOSNA, Pltr.TILI, Pltr.HELVIO, Pltr.SAUAIA, Pltr.LOMBARDI, Pltr.BARBARA, 
         Pltr.JESSIANE, Pltr.MATTAR], "ANEEL", "03:43:21", "2023-11-23"),
    ('Processos Tarifários de 2024: O que esperar? | Live Canal Solar', 'sd6VqMoKXDA', Ct.DBT_ON, 
        [Pltr.DONATO, Pltr.CARVALHO, Pltr.EWERTON, Pltr.BRUNO], "CANAL SOLAR", "01:19:16", "2024-01-24"),
    ('SETOR ELÉTRICO PASSADO, PRESENTE, FUTURO', 'zVlDMCxat_c', Ct.ENTR_PR, 
        [Pltr.EDVALDO], "CANAL SOLAR", "01:17:29", "2024-01-24"),
    ('COMO PROJETAR SISTEMAS DE ENERGIA SOLAR COM BATERIA? Aula Magna', '_owDcOMaCZE', Ct.APR_EV_ON, 
        [Pltr.BRUNO, Pltr.BERNARDO], "CANAL SOLAR", "02:29:20", "2024-02-08"),
    #TODOAQ: revisar duração e participantes após final do evento
    ('Workshop da 1ª Chamada de Sandboxes Tarifários', 'X0Z_TObjwfw', Ct.DBT_PR, 
        [Pltr.SANDOVAL, Pltr.CAMILA, Pltr.BRANDAO, Pltr.PAULO, Pltr.BRANCHER, Pltr.LINDEMBERG, Pltr.BAROUCHE,
         Pltr.LUCAS, Pltr.RENATA, Pltr.AMANDA], "ANEEL", "09:00:00", "2024-02-21"), 
    ('Renovações de concessões, leilões e desafios de 2024', 'TjDI-koDfk4', Ct.DBT_ON, 
        [Pltr.AGOMES, Pltr.ERIK], "MegaWhat", "01:00:00", "2024-02-27"),
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

            vorganizador = videoData[4]

            vduracao = videoData[5]

            vdata = date.fromisoformat(videoData[6])

            vtransc = False
            INDEX_TRANSCRIBED = 7
            if (len(videoData) > INDEX_TRANSCRIBED):
                vtransc = videoData[INDEX_TRANSCRIBED]

            print(f'Inserting video "{vtitle}"...')
            video = dbm.Videos(title=vtitle, yt_id=vid, categoria=categoria, transcrito=vtransc, palestrantes=palestrantes,
                                organizador=vorganizador, duracao=vduracao, data=vdata)
            video.insert(session)
        
        session.commit()
    except:
        print('Exception inserting Videos!')
        session.rollback()
        raise




    print('Done!')

    




