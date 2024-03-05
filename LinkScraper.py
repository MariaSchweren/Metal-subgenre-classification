import requests
varlist = open("List.csv", "w")
letterlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "NBR", "~"]
for letter in letterlist:

    counter = 200
    response = requests.get(f"https://www.metal-archives.com/browse/ajax-letter/l/{letter}/json/1?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength={counter}&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1709667719115", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    response_json = response.json()
    counter = response_json["iTotalRecords"]
    print (counter, letter)

    response = requests.get(f"https://www.metal-archives.com/browse/ajax-letter/l/{letter}/json/1?sEcho=1&iColumns=4&sColumns=&iDisplayStart=0&iDisplayLength={counter}&mDataProp_0=0&mDataProp_1=1&mDataProp_2=2&mDataProp_3=3&iSortCol_0=0&sSortDir_0=asc&iSortingCols=1&bSortable_0=true&bSortable_1=true&bSortable_2=true&bSortable_3=false&_=1709667719115", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    response_json = response.json()
    links = response_json["aaData"]       
    output_String = letter

    for entry in links:
        output_String += ";" + entry[0].split("'")[1]
    varlist.write(output_String + "\n")
