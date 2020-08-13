from webservice.noticias import Noticias                                                                    

class ControllerNoticias:
    def __init__(self):
        self.error = None

    def recebeNoticiasEsporte(self):
        noticias = Noticias()
        noticia = noticias.getNoticiasEsporte()
        lista = []
        for news in noticia['articles']:
            titulo = news['title']
            link = news['url']
            noticia = [titulo, link]
            lista.append(noticia)   
        return lista

    def recebeNoticiasGoogle(self):
        noticias = Noticias()
        noticia = noticias.getNoticiasGoogle()
        lista = []
        for news in noticia['articles']:
            titulo = news['title']
            link = news['url']
            noticia = [titulo, link]
            lista.append(noticia)   
        return lista
    
    def recebeNoticiasTecnologia(self):
        noticias = Noticias()
        noticia = noticias.getNoticiasTecnologia()
        lista = []
        for news in noticia['articles']:
            titulo = news['title']
            link = news['url']
            noticia = [titulo, link]
            lista.append(noticia)   
        return lista