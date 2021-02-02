import pyttsx3
import PyPDF2
bok = open('java.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(bok)
pages = pdfReader.numPages
fullpage = str(pages)

print('This Book Contataint '+fullpage+ ' Number of Pages')

speaker = pyttsx3.init()
for num in range(21, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    nowpage = str(num)
    print('Now I am Reading '+nowpage+' Page.')
    speaker.say(text)
    speaker.runAndWait()
