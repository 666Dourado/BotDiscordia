import requests

class ClimaTempo:

    def __init__(self):
        self.erro = None

    def getClimaTempo(self):
        locale = '6879' #Belo Horizonte
        access_token = '6b0a2705d5817605e4aa556c60973d9b'
        retorno = None

        try:
            response = requests.get('http://apiadvisor.climatempo.com.br/api/v1/weather/locale/' + locale + '/current?token=' + access_token)
            json_response = response.json()
            retorno = json_response['data']
        except:
            retorno = 0

        return retorno
 