filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames:
    f = open(file, "w")
    f.write("hello")
    f.close()
