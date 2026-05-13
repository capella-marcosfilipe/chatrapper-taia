import scrapy
import re


ARTISTAS = [
    {"slug": "sabotage",  "nome": "Sabotage"},
    {"slug": "bk", "nome": "BK"},
    {"slug": "tasha-e-tracie", "nome": "Tasha e Tracie"},
]


class RapSpider(scrapy.Spider):
    name = "rap_nacional"
    allowed_domains = ["vagalume.com.br"]

    def start_requests(self):
        for artista in ARTISTAS:
            url = f"https://www.vagalume.com.br/{artista['slug']}/"
            yield scrapy.Request(
                url,
                callback=self.parse_artista,
                cb_kwargs={"artista": artista},
            )

    def parse_artista(self, response, artista):
        links = response.css("a[href*='/" + artista["slug"] + "/']::attr(href)").getall()

        links_letras = [
            l for l in links  # noqa: E741
            if re.match(r"^/" + artista["slug"] + r"/[^/]+\.html$", l)
            and not any(excluir in l for excluir in [
                "discografia", "fotos", "relacionados",
                "popularidade", "noticias", "cifras"
            ])
        ]

        links_letras = list(dict.fromkeys(links_letras))
        self.logger.info(f"[{artista['nome']}] {len(links_letras)} músicas encontradas.")

        for href in links_letras:
            yield response.follow(
                href,
                callback=self.parse_letra,
                cb_kwargs={"artista": artista},
            )

    def parse_letra(self, response, artista):
        titulo = response.css("div#lyricContent h1::text").get()
        if not titulo:
            titulo = response.css("h1::text").get()
        if not titulo:
            titulo = (
                response.url.split("/")[-1]
                .replace(".html", "")
                .replace("-", " ")
                .title()
            )

        container = response.css("div#lyrics")
        if not container:
            self.logger.warning(f"#lyrics não encontrado: {response.url}")
            return

        textos = container.css("::text").getall()
        linhas = [t.strip() for t in textos if t.strip()]

        if not linhas:
            self.logger.warning(f"Letra vazia: {response.url}")
            return

        yield {
            "artista": artista["nome"],
            "titulo": titulo.strip(),
            "url": response.url,
            "letra": "\n".join(linhas),
        }