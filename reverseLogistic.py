# Julio Meza
# This program returns the manufacturer policy based on the NDC
# The program converts UPC to NDC before return the policy
# There is an option to enter the NDC instead of UPC

# data base file
name_file = 'C:/Users/Julio/Dropbox/Woodfield/Promed/Data_Base.txt'

# open file (data base)
data = open(name_file, 'r')
lines = data.readlines()

# UPC input (scan bar code)
def scan():
    upc = raw_input('UPC: ')
    if len(upc) == 12:
        ndc = convert(upc)
        for i in range(len(lines)):
            line = lines[i].split()
            if ndc == line[0]:
                print 'Policy:                  ' + line[1]
                print 'Minimun percentage:      ' + line[2]
                print 'Minimun money:           ' + line[3]
                print 'Expiration in (months):  ' + line[4]
                print 'Expiration out (months): ' + line[5]
                break
    if upc.lower() == 'exit':
        return 'exit'
    if upc.lower() == 'ndc':
        enterNDC()

# convert UPC to NDC
def convert(upc):
    ndc = ''
    if upc[1] != '0':
        ndc = upc[1:6] + '-0' + upc[6:9] + '-' + upc[9:11]
    else:
        ndc = '0' + upc[1:5] + '-' + upc[5:9] + '-' + upc[9:11]
    return ndc 

# NDC input
def enterNDC():
    ndc = raw_input('NDC: ')
    for i in range(len(lines)):
            line = lines[i].split()
            if ndc == line[0]:
                print 'Policy:                  ' + line[1]
                print 'Minimun percentage:      ' + line[2]
                print 'Minimun money:           ' + line[3]
                print 'Expiration in (months):  ' + line[4]
                print 'Expiration out (months): ' + line[5]
                break

# program
s = ''
print 'Scan "UPC" or write "NDC" to enter a NDC or write "EXIT"'
while s != 'exit':
    s = scan()

data.close()
