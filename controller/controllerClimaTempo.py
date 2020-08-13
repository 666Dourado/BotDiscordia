from webservice.climatempo import ClimaTempo                                                                    

class ControllerClimaTempo:
    def __init__(self):
        self.error = None

    def recebeTemperatura(self):
        clima = ClimaTempo()
        dadosClimaTempo = clima.getClimaTempo()
        return dadosClimaTempo