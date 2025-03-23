from bs4 import BeautifulSoup
import requests

def Scrape(ScrapedProxies, ConfigJson):
    URL = "https://free-proxy-list.net/"

    print("[i] Scraping: " + URL)
    
    Soup = BeautifulSoup(requests.get(URL).text, "html.parser")
    TableElement = Soup.find("table", class_="table table-striped table-bordered")
    TBody = TableElement.find("tbody")
    Items = TBody.find_all("tr")

    for Item in Items:
        Tds = Item.find_all("td")
        Ip = Tds[0].text
        Port = Tds[1].text
        Country = Tds[3].text
        Anonymity = Tds[4].text

        if ConfigJson["ExcludeAnonymitys"] == True:
            if Anonymity in ConfigJson["ExcludedProxyAnonymitys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + Ip + ":" + Port + " - " + Country + " - " + Anonymity)
                continue

        if ConfigJson["IncludeAnonymitys"] == True:
            if Anonymity not in ConfigJson["IncludedProxyAnonymity"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + Ip + ":" + Port + " - " + Country + " - " + Anonymity)
                continue

        if ConfigJson["ExcludeProxyCountrys"] == True:
            if Country in ConfigJson["ExcludedProxyCountrys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + Ip + ":" + Port + " - " + Country + " - " + Anonymity)
                continue

        if ConfigJson["IncludeProxyCountrys"] == True:
            if Country not in ConfigJson["IncludedProxyCountrys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + Ip + ":" + Port + " - " + Country + " - " + Anonymity)
                continue

        if ConfigJson["Debug"] == True:
            print("[i] Scraped Proxy: " + Ip + ":" + Port + " - " + Country + " - " + Anonymity)
            print("[+] Adding Proxy To List")

        ScrapedProxies.append({
            "IP": Ip,
            "Port": Port,
            "Country": Country,
            "Anonymity": Anonymity,
            "Site": URL
        })

    print("[i] Finished Scraping: " + URL)
    print("[i] Found " + str(len(ScrapedProxies)) + " Proxies")
        
    return ScrapedProxies
    
