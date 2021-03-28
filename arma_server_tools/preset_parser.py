import click
from bs4 import BeautifulSoup


class PresetParser(object):

    def __init__(self, html_file):
        self.html_file = html_file

    def parse(self):
        with open(self.html_file, encoding="ISO-8859-1") as fp:
            self.soup = BeautifulSoup(fp, features="html.parser")

        rows = self.soup.findAll("tr", {"data-type": "ModContainer"})

        for r in rows:
            self.parse_row(r)

    def parse_row(self, row):
        display_name = row.find("td", {"data-type": "DisplayName"}).text
        steam_url = row.find("a", {"data-type": "Link"}).get("href")
        steam_id = steam_url.split("id=")[-1]

        print(f'{display_name} : {steam_id}')


@click.command()
@click.argument(
    'html_file',
    required=True,
)
def main(html_file):

    pp = PresetParser(html_file)
    pp.parse()


if __name__ == '__main__':
    main()
