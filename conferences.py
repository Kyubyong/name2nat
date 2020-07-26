from urllib.request import urlopen
import re
import os
import sys
from name2nat import Name2nat
from bs4 import BeautifulSoup
from tqdm import tqdm

my_name2nat = Name2nat()

def get_first_author(authors: str) -> str:
    return re.split(",|&| and ", authors)[0].strip()


def lrec2020():
    collection = []
    url = "https://lrec2020.lrec-conf.org/en/conference-programme/accepted-papers/"
    html = urlopen(url).read().decode("utf8")
    soup = BeautifulSoup(html, 'html.parser')
    entries = soup.find_all("tr")
    for entry in tqdm(entries[1:]):
        items = entry.find_all("td")
        if len(items) == 3:
            title, authors = items[1:]
            title = title.text
            authors = authors.text

            first_author = get_first_author(authors)
            results = my_name2nat(first_author, top_n=3)[0][1]
            collection.append((title, authors, results))

    os.makedirs("conferences", exist_ok=True)
    with open('conferences/lrec2020.md', "w", encoding="utf8") as fout:
        fout.write("|Title|Authors|Pred1|Pred2|Pred3|\n")
        fout.write("|--|--|--|--|--|\n")
        for each in collection:
            title, authors, results = each
            results = "|".join(f"{nat} ({round(prob, 2)})" for nat, prob in results)
            fout.write(f"|{title}|{authors}|{results}\n")


if __name__ == "__main__":
    conf = sys.argv[1]
    if conf == "lrec2020":
        lrec2020()
    else:
        print("Sorry. Check the name of the conference again.")