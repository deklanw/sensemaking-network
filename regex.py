from bs4 import BeautifulSoup
import lxml
import re

# pattern = re.compile('(.*)\s&\s(.*)')
# pattern = re.compile('\((.*)\s&\s(.*)\)')
# pattern = re.compile('-\s(.*)')
# pattern = re.compile('\|\s(.*)')
# pattern = re.compile('(.*)\s\|\s(.*)')
# pattern = re.compile('\d+\s(.*)\s(“|\")')
# pattern = re.compile('(.*)\son\s')
# pattern = re.compile('\d+\s-\s(.*)\son\s')
# pattern = re.compile('\d+\s-\s(.*)\s\(')
pattern = re.compile('(.*)\s\|.*')


def run():
    with open("toscrape.html", encoding='utf8') as fp:
        soup = BeautifulSoup(fp, "lxml")
        for tag in soup.find_all('a'):
            name = tag.string
            if name and name != "":
                # print(name)
                m = re.search(pattern, name)
                if m:
                    print(m.group(1), end=", ")


run()
