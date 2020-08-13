from webservice.pocket import Pocket                                                                    

class ControllerPocket:
    def __init__(self):
        self.error = None

    def postPocket(self, url, tag):
        pocket = Pocket()
        retorno = pocket.postPocket(url, tag)
        return retorno

