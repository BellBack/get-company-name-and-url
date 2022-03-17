import undetected_chromedriver
from bs4 import BeautifulSoup
import csv


def get_html():
    try:
        driver = undetected_chromedriver.Chrome()
        driver.get("https://walletconnect.com/registry/wallets?page=1")
        html = driver.page_source
        with open("index.html", "w", encoding="utf-8") as file:
            file.write(html)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_data():
    with open(file='index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    links = soup.find_all("a", class_="chakra-link css-14e2i6a")[40:]

    for x in links:
        name = x.find("h6").get_text()
        site = x.get("href")
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow(
                [name, site]
                        )


def main():
    get_html()
    get_data()


if __name__ == '__main__':
    main()
