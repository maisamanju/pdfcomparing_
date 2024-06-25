import fitz
import difflib
pdf1_path="/Users/maisasaleem/Desktop/ComparePDF.py/comentext1.pdf"
pdf2_path="/Users/maisasaleem/Desktop/ComparePDF.py/comentext2.pdf"
def pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        text += doc[page_num].get_text()
    return text

def pdf_diff(pdf1_path, pdf2_path):
    text1 = pdf_text(pdf1_path)
    text2 = pdf_text(pdf2_path)
    differences = difflib.ndiff(text1.splitlines(), text2.splitlines())
    return '\n'.join(differences)

# Example usage:
differences = pdf_diff('comentext1.pdf', 'comentext2.pdf')
print(differences)
text_file1 = open("finaldifferance.txt", "w") 
text_file1.write(differences)
text_file1.close()
