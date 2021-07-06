import pyttsx3
import pdfplumber
import PyPDF2

# Gets the files name and the location of the file
file = 'Example.pdf'

# Creates pdf file object
pdf = open(file, 'rb')

# create a pdf file reader object
pdfReader = PyPDF2.PdfFileReader(pdf)

# Get number of pages of the pdf file
pages = pdfReader.numPages

# Create a pdfplumber object and loop through the number of pages in the pdf file
with pdfplumber.open(file) as pdf:
    # loops through number of pages
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()
