# SimpleProxyLogger

**SimpleProxyLogger** is a Python script that scrapes free proxy list websites and collects proxies for use. It’s simple, fast, and gives you control over where the proxies come from.

## Features

- Scrapes multiple public proxy list sites
- Allows filtering proxies by country, anonymity, and source site
- Configurable through a simple config file
- Easy-to-use command-line interface
- Optional debug mode for troubleshooting

## Usage

Run the script with one of the following flags:

```
  -h, --help         Show this help message and exit
  -ps, --printsites  Print all the sites SimpleProxyLogger will scrape for proxies
  -s, --scrape       Scrape the sites and output the collected proxies
```

### Example

```bash
python simple_proxy_logger.py --scrape
```

## Configuration

SimpleProxyLogger uses a configuration file to let you customize how proxies are filtered and how the script behaves. The config file supports the following settings:

```
: PROXY FILTER SETTINGS :

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

Debug: True
```

### Notes:
- Set `ExcludeAnonymitys` or `IncludeAnonymitys` to `True` to filter proxies by anonymity levels.
- Use `ExcludedProxyCountrys` or `IncludedProxyCountrys` to filter by country codes.
- `ExcludeSites` or `IncludeSites` lets you control which sources are used for scraping.
- Enable `Debug` for detailed logging while the script runs.

