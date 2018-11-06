# -*- coding : utf-8 -*-
from ibovespa import Ibovespa
import csv

bov_hist = open('Historico_IBOVESPA.csv', 'r')
ibov_arff = open('hist-ibov-2016-2018.arff', 'w')


### Lambda para conversão de data ###
formDt = lambda d: "{}-{}-{}".format(d[0:2], d[3:5], d[6:10])
i = 0

arff = "@RELATION historico_ibov_cot_dia\n\n"

fechamento_ant = 0
ibov_old = None
ibov = None
mult = 2 / (2 +1)
mme = 0
lines = bov_hist.readlines()

for line in lines:

    if(i == 0):
        col = line.split(';')
        arff += "@ATTRIBUTE " + col[0] + " date \"dd-MM-yyyy\"\n"
        arff += "@ATTRIBUTE " + col[1] + " numeric\n"
        arff += "@ATTRIBUTE " + col[2] + " numeric\n"
        arff += "@ATTRIBUTE " + col[3] + " real\n"
        arff += "@ATTRIBUTE " + col[4] + " real\n"
        arff += "@ATTRIBUTE " + col[5] + " numeric\n"
        arff += "@ATTRIBUTE " + col[6] + " numeric\n"
        arff += "@ATTRIBUTE " + col[7] + " numeric\n"
        arff += "@ATTRIBUTE " + col[8] + " numeric\n"
        arff += "@ATTRIBUTE " + col[9].strip() + " numeric\n"
        arff += "@ATTRIBUTE mms real\n"
        arff += "@ATTRIBUTE mme real\n"
        arff += "@ATTRIBUTE d1 real\n"
        arff += "@ATTRIBUTE tendencia {'baixa', 'sem tendencia', 'alta'}\n"
        arff += "@DATA\n\n"

    if(i > 0):
        col = line.split(';')

        if(col):
            ibov = Ibovespa(formDt(col[0]), col[1], col[2], col[3], col[4], col[5], col[6], col[7], col[8], col[9])
         
    if(i > 2):
        col2 = lines[i -1].split(';')

        if(col2):
            ibov_old = Ibovespa(formDt(col2[0]), col2[1], col2[2], col2[3], col2[4], col2[5], col2[6], col2[7], col2[8], col2[9])

    if(ibov_old):
        #print(ibov.fechamento, ibov_old.fechamento)
        mms = (int(ibov_old.fechamento) + int(ibov.fechamento)) / 2
        if (mme == 0):
            mme = mms
        else:
            mme = ((int(ibov_old.fechamento) - mme) * mult) + mme
        ibov.mme = mme
        ibov.mms = mms
        ibov.d1 = '0'
        ibov.tendencia = "sem tendencia"
        if(ibov_old.fechamento < ibov.fechamento):
            ibov.tendencia = "alta"
        elif(ibov_old.fechamento > ibov.fechamento):
            ibov.tendencia = "baixa"

    
        arff += ibov.dt.strip()  + "," \
                + ibov.historico.strip() + "," \
                + ibov.fechamento.strip() + "," \
                + ibov.variancia_dia.strip()  + "," \
                + ibov.abertura.strip()  + "," \
                + ibov.vlr_min.strip()  + "," \
                + ibov.med.strip()  + "," \
                + ibov.vlr_max.strip()  + "," \
                + ibov.volume.strip()  + "," \
                + ibov.negocios.strip()  + "," \
                + str(ibov.mms) + "," \
                + str(ibov.mme) + "," \
                + str(ibov.d1) + "," \
                + "'" + ibov.tendencia + "'\n"
    i += 1

ibov_arff.write(arff)