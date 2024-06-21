import PyPDF2
import filecmp
import difflib
from compare1 import compare

input_filepath=('/Users/maisasaleem/Desktop/ComparePDF.py/input/samp1.pdf')
output_filepath=('/Users/maisasaleem/Desktop/ComparePDF.py/output/samp1change.pdf')

def Compare_file():
  
    expected_text=Extect_file(input_filepath)
    actuak_text=Extect_file(output_filepath)
    #print(expected_text)
    #print(actuak_text)
    text_file1 = open("exp/text1.txt", "w")
    text_file1.write(expected_text)
    text_file1.close()
    text_file2= open("exp/text2.txt", "w")
    text_file2.write(actuak_text)
    text_file2.close()
    filepath1="exp/text1.txt"
    filepath2="exp/text2.txt"
    compare(filepath1,filepath2)
         
   
    try:
        assert text_file1 == text_file2
    except AssertionError:
        print("the pdf are not identical")
    else:
        print("pdf are identical")

def Extect_file(file_path):
    Pdf_file= open(file_path,'rb')
    read_pdf=PyPDF2.PdfReader(Pdf_file)
    page = read_pdf.pages[0]
    page_content = page.extract_text()
    #print(page_content)
    return page_content



if __name__ == "__main__":
   Compare_file()