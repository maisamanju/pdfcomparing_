
import fitz
import difflib

pdf1_path = "sample1.pdf"
pdf2_path = "sample2.pdf"

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
    return differences

# Example usage:
differences = pdf_diff(pdf1_path, pdf2_path)
extra_text = [line for line in differences if line.startswith('+ ')]

# Join the filtered lines and write to file
extra_text_str = '\n'.join(extra_text)
print(extra_text_str)
with open("finaldifferance.txt", "w", encoding="utf-8") as text_file1:
    text_file1.write(extra_text_str)
