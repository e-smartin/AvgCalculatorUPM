from subprocess import call
import re
import PyPDF2 as pdf

def main ():
    #decrypt pdf to avoide errors
    call('qpdf --password='' --decrypt a.pdf decrypteda.pdf', shell =True)
    pdfFile = open('decrypteda.pdf', 'rb')
    pdfR = pdf.PdfFileReader(pdfFile)
    ts =[]

    #read each page n clean the data extracting the relevant info 
    for i in range(pdfR.numPages -1):
        page = pdfR.getPage(i)
        s = page.extractText()
        s = s.split("Curso")[1]
        s = re.sub("(\d{4}-\d{2})","a",s)
        s = re.sub("General \d{1}","a",s)
        s = re.sub("Apto","Apto)",s)
        s = re.sub("ReconocimientoCred","ReconocimientoCred)",s)
        s = s.split(")")
        for line in s:
            if "NOTA" in line or "Reconocimiento Cred" in line or "Apto" in line:
                s.remove(line)

        s = "\n".join(s)
        s = re.sub("\("," ",s)
        s = re.sub(",",".",s)
        s = re.findall("\d{1}\.{1}\d{1}|10|\d{1}", s)
        ts+=s

    #calculate the mean for each year
    ts = [float (i) for i in ts]
    ects,tot = [0,0,0,0],[0,0,0,0]
    for i in range(0,len(ts)-2,3):
        ects[int(ts[i])-1] += ts[i+1]
        tot[int(ts[i])-1] += ts[i+1]*ts[i+2]
    
    #print the results
    for i in range(len(ects)):
        print(str(i+1)+"º: "+ '%.2f' % (tot[i]/ects[i]))

    call('rm decrypteda.pdf', shell =True)

if __name__ == "__main__":
    main()
