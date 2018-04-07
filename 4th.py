import csv
n=5
sniffer = csv.Sniffer()
with open('/Users/saransh/Downloads/stdout', 'a') as stdout:
    with open('/Users/saransh/Downloads/file_1.csv', 'a') as new_file:
        file = open('/Users/saransh/Downloads/file.csv')
        for i in range(n):
            line = file.next()
            dialect = sniffer.sniff(line)
            deli = dialect.delimiter
            print deli
            print line + 'has total columns: ' + str(len(line.split(deli)))
            new_file.write(line.replace(deli, ' '))

# Didn't Understand when to write ERROR and SUCCESS


