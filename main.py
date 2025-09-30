"""
main.py: třetí projekt od Engeto Online Python Akademie

author: Martina Tarabová
email: martinapetrikova39@gmail.com
"""

from requests import get
from bs4 import BeautifulSoup as bs
import argparse
import csv

def valid_url(value: str) -> str:
    """Checks if the first entered argument is valid."""
    if value.startswith("http://") or value.startswith("https://"):
        return value
    else:
        raise argparse.ArgumentTypeError(
            "Your input is not a URL that starts with 'http://' or 'https://'."
        )

def valid_file_name(name: str) -> str:
    """Checks if the second entered argument is a valid CSV filename."""
    if name.lower().endswith(".csv"):
        return name
    else:
        raise argparse.ArgumentTypeError(
            "The filename must end with '.csv'"
        )

def main():
    """Parses and validates command-line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url",
        type=valid_url,
        help="URL of the territorial unit page."
    )
    parser.add_argument(
        "file_name",
        type=valid_file_name,
        help="Name of the output .csv file."
    )
    args = parser.parse_args()
    print(
        "Thank you! Your arguments are valid.\n"
        "Please, wait a moment while the data is being downloaded."
    )
    return args

def link_scraper(url: str) -> list[dict]:
    """Scrapes the city codes, names, and URLs from the given page."""
    link = get(url)
    new_html = bs(link.text, features="html.parser")
    code_scraper = new_html.find_all("td", {"class": "cislo"})
    name_scraper = new_html.find_all("td", {"class": "overflow_name"})

    every_city = []
    for code, name in zip(code_scraper, name_scraper):
        a = code.find("a")
        a_1 = a.text.strip()
        href = a["href"]
        name = name.text.strip()
        full_url = "https://www.volby.cz/pls/ps2017nss/" + href
        every_city.append({"code": a_1, "city": name, "url": full_url})
    return every_city

def one_city_scraper(url: str) -> dict:
    """Scrapes election data for one city."""
    link2 = get(url)
    link2 = bs(link2.text, features="html.parser")

    registered_votes = link2.find("td", headers="sa2").text.strip()
    envelopes = link2.find("td", headers="sa3").text.strip()
    valid_votes = link2.find("td", headers="sa6").text.strip()
    parties = link2.find_all("td", {"class": "overflow_name"})
    votes = link2.find_all("td", headers=lambda v: v and "t1sb3" in v)

    result_city = {
        "registerd": registered_votes,
        "envelopes": envelopes,
        "valid votes": valid_votes
    }

    for party, vote in zip(parties, votes):
        result_city[party.text.strip()] = vote.text.strip()
    return result_city

def results_for_every_city(url: str) -> list[dict]:
    """Scraps all cities in the given URL and returns their results."""
    all_results = []
    for city in link_scraper(url):
        city_res = one_city_scraper(city["url"])
        city_res["code"] = city["code"]
        city_res["city"] = city["city"]
        all_results.append(city_res)
    return all_results

def write_csv(file_name: str, url: str) -> None:
    """Creates a .csv file with election results for all cities."""
    all_results = results_for_every_city(url)
    keys = set()

    for result in all_results:
        keys.update(result.keys())

    basic = ["code", "city", "registerd", "envelopes", "valid votes"]
    parties = [k for k in keys if k not in basic]
    head = basic + sorted(parties)

    with open(file_name, mode="w", encoding="utf-8") as file_csv:
        writer_csv = csv.DictWriter(file_csv, fieldnames=head, dialect="excel-tab")
        writer_csv.writeheader()
        writer_csv.writerows(all_results)

    print(f"All done! Your results have been saved in '{file_name}'.")

if __name__ == "__main__":
    args = main()
    print("Data downloaded succesfully. Creating the .csv file...")
    write_csv(args.file_name, args.url)