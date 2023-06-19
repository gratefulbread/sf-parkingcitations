import csv
import sys
import geocoder
file = sys.argv[1]
with open(sys.argv[1], 'r') as f:
    permit = file.replace("citationaddresses.csv", "")
    reader = csv.reader(f)
    i = 0
    addresslist = []
    output = [[] * 9999]
    for row in reader:
        if row[4] != "Citation Location":
            output[i][0] = (row[0])
            output[i][1]=(row[1])
            output[i][2].append(row[3])
            output[i][3].append(row[4])
            address = row[4]
            address = address.replace("02ND","2ND")
            address = address.replace("03RD","3RD")
            address = address.replace("04TH","4TH")
            address = address.replace("05TH","5TH")
            address = address.replace("06TH","6TH")
            address = address.replace("07TH","7TH")
            address = address.replace("08TH","8TH")
            address = address.replace("09TH","9TH")
            address = address + ", San Francisco, CA"
            addresslist.append(address)
            i = i + 1
            

    codedlist = geocoder.uscensus(addresslist, method='batch')
    print(codedlist.latlng)

        
    