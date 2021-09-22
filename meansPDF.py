import re
import PyPDF2 as pdf

def main ():
    pdfFile = open('a.pdf', 'rb')
    pdfR = pdf.PdfFileReader(pdfFile)
    ts =[]

    #read each page n clean the data extracting the relevant info 
    for i in range(pdfR.numPages -1):
        page = pdfR.getPage(i)
        s = page.extractText()
        s = s.split("Calificación")[1]
        s = re.sub("(\d{4}-\d{2})","a",s)
        s = re.sub("General \d{1}","a",s)
        s = re.sub("Apto","Apto)",s)
        s = re.sub("ReconocimientoCred","ReconocimientoCred)",s)
        s = s.split(")")
        m = s[:]
        for line in s:
            if "NOTA" in line or "ReconocimientoCred" in line or "Apto" in line:
                m.remove(line)

        #join the string without the lines deleted
        s = "\n".join(m)
        s = re.sub(",",".",s)
        s = re.findall("\d{1}\.{1}\d{1}|10|12|\d{1}", s)
        ts+=s

    #convert to float 
    ts = [float (i) for i in ts]
    
    #calculate the mean 4 each year
    ects,tot = [0,0,0,0],[0,0,0,0]
    for i in range(0,len(ts)-2,3):
        ects[int(ts[i])-1] += ts[i+1]
        tot[int(ts[i])-1] += ts[i+1]*ts[i+2]
    
    #print the results
    for i in range(len(ects)):
        pass
        print(str(i+1)+"º: "+ '%.2f' % (tot[i]/ects[i]))
    print("Total: "+ '%.2f' % (sum(tot)/sum(ects)))

if __name__ == "__main__":
    main()
