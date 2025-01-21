from PyPDF2 import PdfReader
from os import listdir
from os.path import isfile, join

only_files = [f for f in listdir('./input') if isfile(join('./input', f))]
only_pdfs = [x for x in only_files if '.pdf' in x]

print(only_pdfs)
for pdf in only_pdfs:
    reader = PdfReader('./input/'+pdf)
    extracted_text = ''
    for page in reader.pages:
        extracted_text += page.extract_text()
    
    with open('./input/'+pdf.split('.')[0]+'.txt','w',encoding='utf-8') as f:
        f.write(extracted_text)
