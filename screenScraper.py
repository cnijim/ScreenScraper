import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.tascaparts.com/auto-parts/2016/ford/mustang/shelby-gt350r-trim/5-2l-v8-gas-engine/body-cat/bumper-and-components-front-scat")

soup = BeautifulSoup(r.content)
#print soup.prettify()

pageLinks = soup.find_all("a")

for link in pageLinks:
    href = link.get("href")

#tableData = soup.find_all("table", {"class": "all-component-parts"})

allTableData = soup.find("table", {"class": "all-component-parts"})  #includes table head and table body
tableBodyData = allTableData.find("tbody") #includes table body only
tableRowsData = (tableBodyData.find_all("tr")) #includes all table rows within the table body

print "PARSING THROUGH tableRowsData NOW"
for tableRow in tableRowsData:
    print "PRINTING INDIVIDUAL Row on Table!"
    tempDict = {}
    #print table

    ### Finding the list price
    ourPriceData = tableRow.find("td", {"class":"our-price"})
    ourPrice = ourPriceData.text
    tempDict ['ourPrice'] = ourPrice
    print "Our Price: {0}".format(ourPrice)

    descriptionData = tableRow.find("td", {"class":"description"})
    # print tableRows

    # for row in tableRows:
        ### Finding the description
    contextualDescription = descriptionData.find("p", {"class":"contextual_description"})
    if not contextualDescription:
        partDesc = "N/A"
    else:
        partDesc = contextualDescription.text
    tempDict ['partDesc'] = partDesc
    print "Part Description: {0}".format(partDesc)



    ### Finding the Part Name
    ### I need to find the anchor href first
    partNameAnchor = descriptionData.find_all("a")
    partNameUrl = partNameAnchor[0].get("href")
    ### Using the url, make a new soup requests
    ### Parse the new page and find the part name
    partNameResp = requests.get(partNameUrl)
    partNameSoup = BeautifulSoup(partNameResp.content)
    partNotes = partNameSoup.find_all("li", {"class":"part-notes"})
    partNameSpan = partNotes[0].find_all("span", {"class":"list_value"})
    partName = partNameSpan[0].text
    tempDict ['partName'] = partName
    print "Part Name: {0}".format(partName)

    ### Find the part number from this page also
    partNumberListItem = partNameSoup.find_all("li", {"class":"part_number"})
    partNumberSpan = partNumberListItem[0].find_all("span", {"class":"list_value"})
    partNumber = partNumberSpan[0].text
    tempDict ['partNumber'] = partNumber
    print "Part Number: {0}".format(partNumber)
    print ""

    # for row in tableRows:
    #     print row
    #     description = row.get("class")
    #     print description
    # for item in tableRows:
    #     print item.get("class")
    #     print ""
