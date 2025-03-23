DefualtConfigString = """: PROXY FILTER SETTINGS :

ExcludeAnonymitys: False
ExcludedProxyAnonymitys: []

IncludeAnonymitys: False
IncludedProxyAnonymity: []

ExcludeProxyCountrys: False
ExcludedProxyCountrys: []

IncludeProxyCountrys: False
IncludedProxyCountrys: []

ExcludeSites: False
ExcludedSite: []

IncludeSites: False
IncludedSites: []

: EXTRA :
Debug: True"""

def LoadConfig():
    JsonTranslation = {}
    try:
        File = open("FilterSettings.config", "r")
    except FileNotFoundError:
        print("[!] No config file found")
        print("[+] Creating config file")

        with open("FilterSettings.config", "w") as file:
            file.write(DefualtConfigString)

    with open("FilterSettings.config", "r") as file:
        for line in file.readlines():
            line = line.strip()

            if not line or line.startswith(":"):
                continue

            FliteredLine = line.replace("\n", "").replace(" ", "")
            SplitLine = FliteredLine.split(":")
            
            JsonTranslation[SplitLine[0]] = SplitLine[1]

    def Translate(key, value):
        if value.isnumeric():
            return int(value)
        elif value.lower() == "true":
            return True
        elif value.lower() == "false":
            return False
        
    for key in JsonTranslation:
        if JsonTranslation[key].startswith("[") and JsonTranslation[key].endswith("]"):
            JsonTranslation[key] = JsonTranslation[key][1:-1].split(",")

            for i in range(len(JsonTranslation[key])):
                JsonTranslation[key][i] = Translate(key, JsonTranslation[key][i])
        else:
            JsonTranslation[key] = Translate(key, JsonTranslation[key])


    return JsonTranslation

