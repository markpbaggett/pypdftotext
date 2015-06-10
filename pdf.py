import PyPDF2
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="fileName", help="specify PDF to extract from")
parser.add_option("-o", "--output", dest="outputName", help="specify output filename to write text to")

(options, args) = parser.parse_args()
if options.fileName is None or options.outputName is None:
        parser.print_help()
        parser.error("a PDF name and an extract name are required!!!")

if options:
	fileName = outputName = ''
	if options.fileName:
		fileName = options.fileName
	if options.outputName:
		outputName = options.outputName

pdfFileOBJ = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileOBJ)
numPages = pdfReader.numPages
print 'Extracting %d pages.' % numPages
f = open(outputName, 'w')
i = 0
while i < numPages:
	pageObj = pdfReader.getPage(i)
	pageNumber = i + 1
	f.write('Page %d \n' % pageNumber)
	f.write(pageObj.extractText().encode('utf8') + '\n\n')
	i += 1
f.close()
print 'Done'