import requests


class Pocket:

    def __init__(self):
        self.erro = None

    def postPocket(self, url, tag):
        #url = 'https://pypi.org/project/requests-oauth/'
        #tags = 'Teste'
        tweet_id = '666'
        consumer_key = '86477-d5d38533cebfba634f3f5ac4'
        access_token = '808878b4-32b4-2a44-1031-a1a26c'
        retorno = None

        try:

            #url_dev = 'https://getpocket.com/v3/add?' + 'url=' + url + '&tags=' + tag + '&tweet_id=' + tweet_id + '&consumer_key=' + consumer_key + '&access_token=' + access_token

            response = requests.post('https://getpocket.com/v3/add?' + 'url=' + url + '&tags=' + tag + '&tweet_id=' + tweet_id + '&consumer_key=' + consumer_key + '&access_token=' + access_token)
            json_response = response.json()
            retorno = json_response['status']
            if(retorno == 1):
                retorno = 1
            else:
                retorno = 0

        except:
            retorno = 0

        return retorno
 