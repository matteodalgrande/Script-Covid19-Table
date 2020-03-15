
import csv #comma separeted value
from datetime import  datetime
import requests

time = datetime.today()

###########################################################################
# ---> selezionare il range temporale da scaricare e anche la zona
###########################################################################
#dati da cambiare per i download
startIndexDAY = int(input('Inserisci il giorno di inizio[1-31]:'))
finishIndexDAY = int(input('Inserisci il giorno di fine[1-31]:'))
indexMONTH = int(input('Inserisci il mese [1-12]:'))
#selezionare: nazione, regione, provincia
zona = input('Scegliere:[nazionale][regionale][provinciale]')
finishIndexDAY += 1#necessario per il range successivo, sennò ne fa uno in meno
###########################################################################

def downloadPage(month,day,zona):

    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)



    if(zona=='nazionale' or zona=='n'):

        def dataRowTable(daStampare):
            return '<td style="padding:8px; border:1px solid #ddd;">' + daStampare + '</td>'

        def rowTable(daStampare):
            filehtml.write('<tr>')
            filehtml.write(daStampare)
            filehtml.write('</tr>')

        def stampaData(daStampare):
            dati = daStampare[8:10] + '/' + daStampare[5:7] + '/' + daStampare[0:4] #+ ' ' + daStampare[11:16]
            return dati
            
        #request per nazione
        res = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')

        #dato xml dove salvo i file temporaneamente
        filecsv = open("./datoTEMPORANEO.csv","w")
        filecsv.write(res.text.replace('ì','i')) #salvo nel file i dati csv e sostituisco la i accentata di forli
        filecsv.close()

        #gestisco il file html NAZIONALE
        filehtml = open("covid_nazionale.html","w+")

        #HTML
        filehtml.write('<!doctype html><html lang="it"><head><link href="../css/covid2.css" rel="stylesheet" type="text/css"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0"><title>EscapeIT &ndash; COVID-19</title></head>')

        with open("./datoTEMPORANEO.csv", newline="", encoding="UTF-8") as filecsv:
            lettore = csv.reader(filecsv, delimiter=",")
            for index, row in enumerate(lettore):
                if row:
                    if(index == 0):
                        filehtml.write('<table style="border-collapse:collapse;">')
                        rowTable(dataRowTable('COVID-ITALIA') + dataRowTable('Dati del: ' + str(day)+'/'+str(month)+'/'+ str(time.year)))
                        rowTable(dataRowTable('DATA') + dataRowTable('RICOVERATI CON SINTOMI') + dataRowTable('TERAPIA INTENSIVA') + dataRowTable('TOT. OSPEDALIZZATI') + dataRowTable('ISOLAMENTO DOMICILIARE') + dataRowTable('TOT. ATTUALMENTE POSITIVI') + dataRowTable('NUOVI ATTUALMENTE POSITIVI') + dataRowTable('DIMESSI GUARITI') + dataRowTable('DECEDUTI') + dataRowTable('TOT. CASI') + dataRowTable('TAMPONI'))
                #stampo le righe
                    if(index > 0):
                        rowTable(dataRowTable(stampaData(row[0])) + dataRowTable(row[2]) + dataRowTable(row[3]) + dataRowTable(row[4]) + dataRowTable(row[5]) + dataRowTable(row[6]) + dataRowTable(row[7]) + dataRowTable(row[8]) + dataRowTable(row[9]) + dataRowTable(row[10]) + dataRowTable(row[11]))
        
        #HTML DI CHIUSURA
        filehtml.write('</table>')
        filehtml.write('</html>')



    if(zona=='regionale' or zona=='r'):

        def dataRowTable(daStampare):
            return '<td style="padding:8px; border:1px solid #ddd;">' + daStampare + '</td>'

        def rowTable(daStampare):
            filehtml.write('<tr>')
            filehtml.write(daStampare)
            filehtml.write('</tr>')

        #request per regioni
        res = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-' + str(time.year) + str(month) + str(day) + '.csv')

        #dato xml dove salvo i file temporaneamente
        filecsv = open("./datoTEMPORANEO.csv","w")
        filecsv.write(res.text.replace('ì','i')) #salvo nel file i dati csv e sostituisco la i accentata di forli
        filecsv.close()

        #gestisco il file delle REGIONI
#        covid_regioni = str(time.year) + '_' + str(month) + '_' + str(day) + '_covid_regioni.html'
        covid_regioni_nuovo = 'covid_regioni_nuovo.txt'
        filehtml = open(covid_regioni_nuovo,"w+")#apre in lettura e scrittura ma elimina il contenuto del file


        with open("./datoTEMPORANEO.csv", newline="", encoding="UTF-8") as filecsv:
            lettore = csv.reader(filecsv, delimiter=",")
            for index, row in enumerate(lettore):
        #stampo l'INTESTAZIONE
                if(index == 0):
                    filehtml.write('<table style="border-collapse:collapse;">')
                    rowTable(dataRowTable('Dati del: ' + str(day)+'/'+str(month)+'/'+ str(time.year)))
                    rowTable(dataRowTable('REGIONE') + dataRowTable('RICOVERATI CON SINTOMI') + dataRowTable('TERAPIA INTENSIVA') + dataRowTable('TOT. OSPEDALIZZATI') + dataRowTable('ISOLAMENTO DOMICILIARE') + dataRowTable('TOT. ATTUALMENTE POSITIVI') + dataRowTable('NUOVI ATTUALMENTE POSITIVI') + dataRowTable('DIMESSI GUARITI') + dataRowTable('DECEDUTI') + dataRowTable('TOT. CASI') + dataRowTable('TAMPONI'))
                    #print(('REGIONE' + ' '*15)[0:21]+'|' + ' RICOVERATI CON SINTOMI |' + ' TERAPIA INTENSIVA |' + ' TOT. OSPEDALIZZATI |' + ' ISOLAMENTO DOMICILIARE |' + ' TOT. ATTUALMENTE POSITIVI |' + ' NUOVI ATTUALMENTE POSITIVI |' + ' DIMESSI GUARITI |' + ' DECEDUTI |' + ' TOT. CASI |' + ' TAMPONI')
            #stampo le righe
                if(index > 0):
                    # print((row[3] + ' '*15)[0:21]+' |')
                    rowTable(dataRowTable(row[3]) + dataRowTable(row[6]) + dataRowTable(row[7]) + dataRowTable(row[8]) + dataRowTable(row[9]) + dataRowTable(row[10]) + dataRowTable(row[11]) + dataRowTable(row[12]) + dataRowTable(row[13]) + dataRowTable(row[14]) + dataRowTable(row[15]))
            filehtml.write('</table>')

        filehtml.close()
        filehtml2 = open(covid_regioni_nuovo, "r")
        linesTemporaneo = filehtml2.readlines()
        covid_regioni = 'covid_regioni.html'
        fileHTMLregioni = open(covid_regioni,"r+")#apre in lettura e scrittura ma mantiene il contenuto del file
        linesRegioni = fileHTMLregioni.readlines()
        for numeroRiga, line in enumerate(linesRegioni):
            if line.find('</head>') > -1:
                linesRegioni[numeroRiga] = '</head>\n' + linesTemporaneo[0] + '\n<br>\n'

                passaggioHTML = 'filepassaggio.txt'
                filePassaggio = open(passaggioHTML, "w+")
                filePassaggio.writelines(linesRegioni)
                filePassaggio.close()
                filePassaggio2 = open(passaggioHTML, "r")
                fileHTMLregioni.close()

                linesPassaggio = filePassaggio2.readlines()
                fileHTMLregioni2 = open(covid_regioni,"w+")
                fileHTMLregioni2.writelines(linesPassaggio)
                break

    if(zona=='provinciale' or zona=='p'):

        def dataRowTable(daStampare):
            return '<td style="padding:8px; border:1px solid #ddd;">' + daStampare + '</td>'

        def rowTable(daStampare):
            filehtml.write('<tr>')
            filehtml.write(daStampare)
            filehtml.write('</tr>')

        #request per provincia
        res = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province-' + str(time.year) + str(month) + str(day) + '.csv')

        #dato xml dove salvo i file temporaneamente
        filecsv = open("./datoTEMPORANEO.csv","w")
        filecsv.write(res.text.replace('ì','i')) #salvo nel file i dati csv e sostituisco la i accentata di forli
        filecsv.close()

        #gestisco il file PROVINCIALE
        covid_province_nuovo = 'covid_province_nuovo.txt'
        filehtml = open(covid_province_nuovo,"w+")#apre in lettura e scrittura eliminado il contenuto del file

        with open("./datoTEMPORANEO.csv", newline="", encoding="UTF-8") as filecsv:
            lettore = csv.reader(filecsv, delimiter=",")
            for index, row in enumerate(lettore):
                #stampo l'INTESTAZIONE
                if(index == 0):
                    filehtml.write('<table style="border-collapse:collapse;">')
                    rowTable(dataRowTable('COVID-PROVINCE') + dataRowTable('Dati del: ' + str(day)+'/'+str(month)+'/'+ str(time.year)))
                    rowTable(dataRowTable('NOME REGIONE') + dataRowTable('NOME PROVINCIA') + dataRowTable('SIGLA PROVINCIA') + dataRowTable('TOTALE CASI'))
            #stampo le righe
                if(index > 0 and (not('In fase di definizione/aggiornamento' in row[5]))):
                    rowTable(dataRowTable(row[3]) + dataRowTable(row[5]) + dataRowTable(row[6]) + dataRowTable(row[9]))
            filehtml.write('</table>')

        filehtml.close()
        filehtml2 = open(covid_province_nuovo, "r")
        linesTemporaneo = filehtml2.readlines()
        covid_province = 'covid_province.html'
        fileHTMLprovince = open(covid_province,"r+")#apre in lettura e scrittura ma mantiene il contenuto del file
        linesProvince = fileHTMLprovince.readlines()
        for numeroRiga, line in enumerate(linesProvince):
            if line.find('</head>') > -1:
                linesProvince[numeroRiga] = '</head>\n' + linesTemporaneo[0] + '\n<br>\n'

                passaggioHTML = 'filepassaggio.txt'
                filePassaggio = open(passaggioHTML, "w+")
                filePassaggio.writelines(linesProvince)
                filePassaggio.close()
                filePassaggio2 = open(passaggioHTML, "r")
                fileHTMLprovince.close()

                linesPassaggio = filePassaggio2.readlines()
                fileHTMLprovince2 = open(covid_province,"w+")
                fileHTMLprovince2.writelines(linesPassaggio)
                break

    print('[+] ok')

for day in range(startIndexDAY,finishIndexDAY):
    downloadPage(indexMONTH, day, zona)