# -*- coding: utf-8 -*-

class Ibovespa:

    def __init__(self, dt, historico ,fechamento, variancia_dia, abertura, vlr_min, med, 
        vlr_max, volume, negocios):
        self.dt = dt
        self.historico = historico
        self.fechamento = fechamento
        self.variancia_dia = variancia_dia
        self.abertura = abertura
        self.vlr_min = vlr_min
        self.med = med
        self.vlr_max = vlr_max
        self.volume = volume
        self.negocios = negocios
        self.mms = None
        self.mme = None
        self.d1  = None
        self.tendencia = "sem tendencia"

    def getDt(self):
        return self.dt

    def setDt(self, dt):
        self.dt = dt

    def getHistorico(self):
        return self.historico

    def setHistorico(self, historico):
        self.historico = historico

    def getFechamento(self):
        return self.fechamento

    def setFechamento(self, fechamento):
        self.fechamento = fechamento

    def getVariancia_dia(self):
        return self.variancia_dia

    def setVariancia_dia(self, variancia_dia):
        self.variancia_dia = variancia_dia

    def getAbertura(self):
        return self.abertura

    def setAbertura(self, abertura):
        self.abertura = abertura
    
    def getVlr_min(self):
        return self.vlr_min

    def setVlr_min(self, vlr_min):
        self.vlr_min = vlr_min
    
    def getMed(self):
        return self.med

    def setMed(self, med):
        self.med = med

    def getVlr_max(self):
        return self.vlr_max

    def setVlr_max(self, vlr_max):
        self.vlr_max = vlr_max

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getNegocios(self):
        return self.negocios

    def setNegocios(self, negocios):
        self.negocios = negocios

    def getMme(self):
        return self.mme

    def setMme(self, mme):
        self.mme = mme

    def getMms(self):
        return self.mms

    def setMms(self, mms):
        self.mms = mms

    
    def getD1(self):
        return self.d1

    def setD1(self, d1):
        self.d1 = d1

    def getTendencia(self):
        return self.tendencia

    def setTendencia(self, tendencia):
        self.tendencia = tendencia
    
   