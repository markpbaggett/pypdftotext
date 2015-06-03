import PyPDF2
pdfFileOBJ = open('testing.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileOBJ)
numPages = pdfReader.numPages
print numPages
f = open('test.txt', 'w')
i = 0
while i < numPages:
	pageObj = pdfReader.getPage(i)
	pageNumber = i + 1
	f.write('Page %d \n' % pageNumber)
	f.write(pageObj.extractText().encode('utf8') + '\n\n')
	i += 1
f.close()
print 'Done'