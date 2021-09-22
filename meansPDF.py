import re
import pdfplumber
#import PyPDF2 as pdfRA

def main ():
    with pdfplumber.open('a.pdf') as pdf:
        ts = []
        for i in range (len(pdf.pages)-1):
            page = pdf.pages[i]
            s = (page.extract_text())

            s = re.sub("(\d{4}-\d{2})","a",s)
            s = re.sub("General \d{1}","a",s)
            s = re.sub("Apto","Apto)",s)
            s = re.sub("ReconocimientoCred","ReconocimientoCred)",s)
            s = s.split(")")
            for line in s:
                if "Curso" in line or "Página" in line or  "NOTA" in line or "Reconocimiento" in line or "Apto" in line:
                    s.remove(line)

            s = "\n".join(s)
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
            print(str(i+1)+"º: "+ '%.2f' % (*tot[i]/ects[i]))
        bigAv = sum(tot)/sum(ects)*
        print("Total average: %.2f" %bigAv)



if __name__ == "__main__":
    main()
