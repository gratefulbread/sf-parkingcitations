import csv
import sys
import geocoder
file = sys.argv[1]
completeset = []
addresslist = []
justlats = []
with open(sys.argv[1], 'r') as f:
    #permit = file.replace("citationaddresses.csv", "")
    reader = csv.reader(f)
    for row in reader:
        line = [0,0,0,0]
        line[0] = row [0]
        line[1] = row [1]
        line[2] = row [3]
        address = row[4]
        straddress = row[4]
        address = address.replace("02ND","2ND")
        address = address.replace("03RD","3RD")
        address = address.replace("04TH","4TH")
        address = address.replace("05TH","5TH")
        address = address.replace("06TH","6TH")
        address = address.replace("07TH","7TH")
        address = address.replace("08TH","8TH")
        address = address.replace("09TH","9TH")
        address = address.replace("EMBARCADERO NORTH","EMBARCADERO")
        address = address.replace("EMBARCADERO SOUTH","EMBARCADERO")
        address = address + " San Francisco CA"
        line[3] = address
        if straddress != "":
            addresslist.append(address)
            completeset.append(line)
    latlnglist = geocoder.uscensus(addresslist, method='batch')
    for row in latlnglist:
        justlats.append(str(row.wkt))
    for i in range(len(completeset)):
        completeset[i].append(justlats[i])
    for row in completeset:
        if "POINT" not in row[4]:
            test = geocoder.arcgis(row[3])
            row[4] = str(test.wkt)
            if "POINT" not in row[4]:
                print((row[0]) + "|" + (row[1]) + "|" + (row[2]) + "|" + (row[3])+ "|" + (row[4]))
    