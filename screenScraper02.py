import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.tascaparts.com/auto-parts/2016/ford/mustang/shelby-gt350r-trim/5-2l-v8-gas-engine/body-cat/bumper-and-components-front-scat")

soup = BeautifulSoup(r.content)
#print soup.prettify()

pageLinks = soup.find_all("a")

for link in pageLinks:
    href = link.get("href")

#tableData = soup.find_all("table", {"class": "all-component-parts"})

divData = soup.find_all("table", {"class": "all-component-parts"})
rowNames = (divData[0].find_all("tr"))

print "GOING TO PRINT CLASS NAMES"
### Preparing the row names below:
rowNamesList = []
for rowName in rowNames:
    row = rowName.get("class")

    concatenatedString = ""
    try:
        for i, string in enumerate(row):
            if i == 0:
                concatenatedString = string
            else:
                concatenatedString = concatenatedString + " " + string
        rowNamesList.append(concatenatedString)
        print "THE FINAL concatenatedString is: %s" % concatenatedString
    except (RuntimeError, TypeError, NameError):
        pass


print "PARSING THROUGH tableData NOW"
for row in rowNamesList:
    print "PRINTING INDIVIDUAL TABLE ITEM!!!"
    #print table
    tableRow = row.get("class": {row)}
    print tableRow
    # for item in tableRows:
    #     print item.get("class")
#     #     print ""
