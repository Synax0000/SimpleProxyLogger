import Modules.Config as Config
import argparse

import Scrapers.FreeProxyList as FreeProxyList
import Scrapers.GeoncodeList as GeoncodeList
import Scrapers.ProxyScrape as ProxyScrape

ConfigJson = Config.LoadConfig()

Parser = argparse.ArgumentParser()
Parser.add_argument("-ps", "--printsites", help="Prints all the sites SPL will scrape for proxies", action="store_true")
Parser.add_argument("-s", "--scrape", help="Scrapes the sites for proxies", action="store_true")

Args = Parser.parse_args()

Sites = [
    {
        "LINK": "https://free-proxy-list.net/",
        "FUNCTION": FreeProxyList.Scrape
    },
    {
        "LINK": "https://geoncode.com/",
        "FUNCTION": GeoncodeList.Scrape
    },
    {
        "LINK": "https://proxyscrape.com/",
        "FUNCTION": ProxyScrape.Scrape
    }
]

if Args.printsites:
    for Site in Sites:
        print("[i] " + Site["LINK"])

elif Args.scrape:
    ScrapedProxies = []

    for Site in Sites:
        if ConfigJson["ExcludeSites"] == True:
            for ExcludedSite in ConfigJson["ExcludedSites"]:
                if Site["LINK"] == ExcludedSite:
                    continue

        if ConfigJson["IncludeSites"] == True:
            for IncludedSite in ConfigJson["IncludedSites"]:
                if not Site["LINK"] == IncludedSite:
                    continue

        ScrapedProxies = Site["FUNCTION"](ScrapedProxies, ConfigJson)

    with open("PROXIES.txt", "w") as file:
        for Proxy in ScrapedProxies:
            file.write(f"{Proxy['IP']}:{Proxy['Port']} {Proxy['Anonymity']} {Proxy['Country']} {Proxy['Site']}\n")

    print("[i] Scraped A Total Of " + str(len(ScrapedProxies)) + " Proxies")
    print("[i] Saved to PROXIES.txt")

    input("Press anything to exit this script...")
