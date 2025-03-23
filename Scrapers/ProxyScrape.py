from bs4 import BeautifulSoup
import requests
import json

def Scrape(ScrapedProxies, ConfigJson):
    URL = "https://proxyscrape.com"

    print("[i] Scraping: " + URL)

    JsonData = json.loads(requests.get("https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json").text)
    ScrapedCount = 0

    for Proxy in JsonData["proxies"]:
        try:
            ip = Proxy["ip"]
            port = Proxy["port"]
            country = Proxy["ip_data"]["country"]
            anonymity = Proxy["anonymity"]

            if ConfigJson["ExcludeAnonymitys"] == True:
                if anonymity in ConfigJson["ExcludedProxyAnonymitys"]:
                    if ConfigJson["Debug"] == True:
                        print("[i] Excluded Proxy: " + ip + ":" + str(port) + " - " + country + " - " + anonymity)
                    continue

            if ConfigJson["IncludeAnonymitys"] == True:
                if anonymity not in ConfigJson["IncludedProxyAnonymity"]:
                    if ConfigJson["Debug"] == True:
                        print("[i] Excluded Proxy: " + ip + ":" + str(port) + " - " + country + " - " + anonymity)
                    continue

            if ConfigJson["ExcludeProxyCountrys"] == True:
                if country in ConfigJson["ExcludedProxyCountrys"]:
                    if ConfigJson["Debug"] == True:
                        print("[i] Excluded Proxy: " + ip + ":" + str(port) + " - " + country + " - " + anonymity)
                    continue

            if ConfigJson["IncludeProxyCountrys"] == True:
                if country not in ConfigJson["IncludedProxyCountrys"]:
                    if ConfigJson["Debug"] == True:
                        print("[i] Excluded Proxy: " + ip + ":" + str(port) + " - " + country + " - " + anonymity)
                    continue

            if ConfigJson["Debug"] == True:
                print("[i] Scraped Proxy: " + ip + ":" + str(port) + " - " + country + " - " + anonymity)
                print("[+] Adding Proxy To List")

            ScrapedCount += 1

            ScrapedProxies.append({
                "IP": ip,
                "Port": port,
                "Anonymity": anonymity,
                "Country": country,
                "Site": URL
            })
        except:
            pass

    print("[i] Finished Scraping: " + URL)
    print("[i] Found: " + str(ScrapedCount) + " Proxies")

    return ScrapedProxies