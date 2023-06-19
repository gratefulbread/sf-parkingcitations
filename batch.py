import csv
import sys
import geocoder
file = sys.argv[1]
with open(sys.argv[1], 'r') as f:
    #permit = file.replace("citationaddresses.csv", "")
    reader = csv.reader(f)
    adlist = []
    for row in reader:
        address = row[4] + " San Francisco CA"
        address = address.replace("02ND","2ND")
        address = address.replace("03RD","3RD")
        address = address.replace("04TH","4TH")
        address = address.replace("05TH","5TH")
        address = address.replace("06TH","6TH")
        address = address.replace("07TH","7TH")
        address = address.replace("08TH","8TH")
        address = address.replace("09TH","9TH")
        adlist.append(address)
    glist = geocoder.uscensus(adlist, method='batch')
    for result in glist:
        print(result.latlng)
    