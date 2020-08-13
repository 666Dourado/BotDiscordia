import os
import time
import re
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ControllerWhatsApp:

    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def inicia(self,nome_contato):

        self.driver.get('https://web.whatsapp.com/')
        self.driver.implicitly_wait(15)


        self.caixa_de_pesquisa = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        #self.caixa_de_pesquisa = self.driver.find_element_by_class_name('_3FRCZ')

        self.caixa_de_pesquisa.send_keys(nome_contato)

        time.sleep(2)
        print(nome_contato)
        self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
        self.contato.click()
        time.sleep(2)

    def saudacao(self,frase_inicial):
        #self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2FbwG')
        self.caixa_de_mensagem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')

        if type(frase_inicial) == list:
            for frase in frase_inicial:
                self.caixa_de_mensagem.send_keys(frase)
                time.sleep(1)
                self.botao_enviar = self.driver.find_element_by_class_name('_1U1xa')
                self.botao_enviar.click()
                time.sleep(1)
        else:
            return False

    def escuta(self):
        post = self.driver.find_elements_by_class_name('_2hqOq')
        ultimo = len(post) - 1
        try:
            pass
            texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
        except:
            pass
            texto = post[ultimo].text
        return texto
    

    def responde(self,texto, timer):
        response = str(texto)
        response = '::RafaBot: ' + response
        #self.caixa_de_mensagem = self.driver.find_element_by_class_name('_3u328')
        self.caixa_de_mensagem = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        self.caixa_de_mensagem.send_keys(response)
        time.sleep(timer)
        #self.botao_enviar = self.driver.find_element_by_class_name('_3M-N-')
        self.botao_enviar = self.driver.find_element_by_class_name('_1U1xa')
        self.botao_enviar.click()



