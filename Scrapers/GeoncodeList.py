from bs4 import BeautifulSoup
import requests
import json

def Scrape(ScrapedProxies, ConfigJson):
    JsonData = json.loads(requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc").text)
    ScrapedCount = 0

    URL = "https://proxylist.geonode.com/"

    print("[i] Scraping: " + "https://proxylist.geonode.com/")

    for Proxy in JsonData["data"]:
        ip = Proxy["ip"]
        port = Proxy["port"]
        country = Proxy["country"]
        anonymity = Proxy["anonymityLevel"]

        if ConfigJson["ExcludeAnonymitys"] == True:
            if anonymity in ConfigJson["ExcludedProxyAnonymitys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + ip + ":" + port + " - " + country + " - " + anonymity)
                continue

        if ConfigJson["IncludeAnonymitys"] == True:
            if anonymity not in ConfigJson["IncludedProxyAnonymity"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + ip + ":" + port + " - " + country + " - " + anonymity)
                continue

        if ConfigJson["ExcludeProxyCountrys"] == True:
            if country in ConfigJson["ExcludedProxyCountrys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + ip + ":" + port + " - " + country + " - " + anonymity)
                continue

        if ConfigJson["IncludeProxyCountrys"] == True:
            if country not in ConfigJson["IncludedProxyCountrys"]:
                if ConfigJson["Debug"] == True:
                    print("[i] Excluded Proxy: " + ip + ":" + port + " - " + country + " - " + anonymity)
                continue

        ScrapedCount += 1

        if ConfigJson["Debug"] == True:
            print("[i] Scraped Proxy: " + ip + ":" + port + " - " + country + " - " + anonymity)
            print("[+] Adding Proxy To List")

        ScrapedProxies.append({
            "IP": ip,
            "Port": port,
            "Country": country,
            "Anonymity": anonymity,
            "Site": URL
        })

    print("[i] Finished Scraping: " + "https://proxylist.geonode.com/")
    print("[i] Found: " + str(ScrapedCount) + " Proxies")

    return ScrapedProxies

        