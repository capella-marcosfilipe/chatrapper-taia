BOT_NAME = "rap_nacional"

SPIDER_MODULES = ["rap_nacional.spiders"]
NEWSPIDER_MODULE = "rap_nacional.spiders"

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1.5
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_DOMAIN = 2

USER_AGENT = "Mozilla/5.0 (compatible; RapResearchBot/1.0; academic project)"

FEEDS = {
    "../data/letras_raw.json": {
        "format": "json",
        "encoding": "utf8",
        "indent": 2,
        "overwrite": True,
    }
}

LOG_LEVEL = "INFO"