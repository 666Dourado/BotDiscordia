import re
import time
import datetime
from random import randint

from controller.controllerWhatsApp import ControllerWhatsApp
from controller.controllerPocket import ControllerPocket
from controller.controllerNoticias import ControllerNoticias
from controller.controllerClimaTempo import ControllerClimaTempo

class Service:

    def __init__(self):
        self.error = None
        self.grupo = 'Discórdia e Agressão'
        #self.grupo = 'Familia_RibGon'
        self.saudacao = (['::RafaBot: Oi, sou o bot da discordia. No momento o Rafael tá sem tempo há perder aqui então estou no seu lugar. Irei de agora em diante interagir com vocês, seus noobs'])
        self.ultimo_texto = ''

    def monitor(self):
        print('Iniciando servico do Bot da ' + self.grupo +  '!')

        #Instancia as classes a serem utilizadas pelo Bot
        zap = ControllerWhatsApp()

        zap.inicia(self.grupo)
        zap.saudacao(self.saudacao)

        while True:
            texto = zap.escuta()

            if texto != self.ultimo_texto and not re.match(r'^::', texto):   
                self.ultimo_texto = texto

                opcao = randint(0,15)

                if(opcao == 0):
                    inicio = 'Ninguem se importa'
                    zap.responde(inicio, 1)

                elif(opcao == 1):
                    inicio = 'Tá sem trabalho ai hoje ?'
                    zap.responde(inicio, 1)
                    
                elif(opcao == 2):
                    inicio = 'Comedor de sopa de Mandragora'
                    zap.responde(inicio, 1)

                elif(opcao == 3):
                    inicio = 'Só tem Noob nesse grupo'
                    zap.responde(inicio, 1)

                elif(opcao == 4):
                    inicio = 'Sem tempo irmão'
                    zap.responde(inicio, 1)

                elif(opcao == 5):
                    inicio = 'Ninguem liga'
                    zap.responde(inicio, 1)
   
                elif(opcao == 6):
                    inicio = 'Hummmm é mesmo ?'
                    zap.responde(inicio, 1)
            
                elif(opcao == 7):
                    inicio = 'Fodas'
                    zap.responde(inicio, 1)

                elif(opcao == 8):
                    inicio = 'Ai ai'
                    zap.responde(inicio, 1)

                elif(opcao == 9):
                    inicio = 'Tá perdendo seu e o meu tempo'
                    zap.responde(inicio, 1)

                elif(opcao == 10):
                    inicio = 'Vou fingir que nem li isso'
                    zap.responde(inicio, 1)

                elif(opcao == 11):
                    inicio = 'É tão absurdo que nem pode ser chamado de burro'
                    zap.responde(inicio, 1)

                elif(opcao == 12):
                    inicio = 'Você leu isso antes de escrever ?'
                    zap.responde(inicio, 1)

                elif(opcao == 13):
                    inicio = 'Serio mesmo ?'
                    zap.responde(inicio, 1)

                elif(opcao == 14):
                    inicio = 'Alguem ai ta precisando mandar uns curriculos'
                    zap.responde(inicio, 1)

                elif(opcao == 15):
                    inicio = 'Eu não pago a internet para ler esse tipo de coisa'
                    zap.responde(inicio, 1)
            
                time.sleep(30)

            else:
                time.sleep(30)
               

    
    def helpSistema(self):
        lista = []
        lista.append('"pocket" = Serviço para salvar links uteis no Pocket')
        lista.append('"noticias-esporte" = Serviço que retorna as noticias de Esporte do Globo.com')
        lista.append('"noticias-google" = Serviço que retorna as noticias de primeira pagina do Google News')
        lista.append('"noticias-tecnologia" = Serviço que retorna as noticias relacionadas a Tecnologia')
        lista.append('"temperatura" = Serviço que retorna a temperatura na data hora atual')
        return lista



