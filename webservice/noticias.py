import requests
import json
import pandas as pd

class Noticias:

    def __init__(self):
        self.erro = None
        self.token = 'f6fdb7cb0f2a497d92dbe719a29b197f'

    def getNoticiasEsporte(self):      
        req = requests.get('https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=' + self.token)
        noticias = json.loads(req.text)

        return noticias

    def getNoticiasGoogle(self):
        req = requests.get('https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey=' + self.token)
        noticias = json.loads(req.text)

        return noticias
    
    def getNoticiasTecnologia(self):
        req = requests.get('https://newsapi.org/v2/top-headlines?country=br&category=technology&apiKey=' + self.token)
        noticias = json.loads(req.text)

        return noticias
