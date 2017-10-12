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
tableData = (divData[0].find_all("tr"))

#print tableData
print "\n \n THE tableData VARIABLE TYPE IS:"
print type(tableData)
# print len(tableData)

print "PARSING THROUGH tableData NOW"
for table in tableData:
    print "PRINTING INDIVIDUAL TABLE ITEM!!!"
    #print table
    tableRows = table.find_all("td", {"class":"description"})
    print tableRows
    for row in tableRows:
        ### Finding the description
        contextualDescription = row.find_all("p", {"class":"contextual_description"})
        if not contextualDescription:
            print "There is no Part Description available for this part."
        else:
            partDesc = contextualDescription[0].text
            print "The Part Description is %s: " %partDesc

        ### Finding the Part Name
        partNameAnchor = row.find_all("a")
        partNameUrl = partNameAnchor[0].get("href")
        print partNameUrl

        partNameResp = requests.get(partNameUrl)
        partNameSoup = BeautifulSoup(partNameResp.content)
        partNotes = partNameSoup.find_all("li", {"class":"part-notes"})
        partNameSpan = partNotes[0].find_all("span", {"class":"list_value"})
        partName = partNameSpan[0].text
        print partName
        print ""

    # for row in tableRows:
    #     print row
    #     description = row.get("class")
    #     print description
    # for item in tableRows:
    #     print item.get("class")
    #     print ""
