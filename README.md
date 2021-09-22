# AvgCalculatorUPM

This repo calculates the ponderated average of each course. There're two options, using a pdf or a csv.

# Using a csv
 
To create a csv with your grades copy your grades from PV to an excel an export it as a csv. Name the csv 'notas.csv' and run:

### `python meansCSV.py`

The format of your csv should be identical to the one uploaded. Notice you must manually include 3 rows containing seven "SEGUNDO", seven "TERCERO", and seven "CUARTO" preceding each course respectively.


# Using a pdf

Export the last situation pdf from PV, rename it as 'a.pdf' and run:

### `pip install PyPDF2`
### `python meansPDF.py` 
