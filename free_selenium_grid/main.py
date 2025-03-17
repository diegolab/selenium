#
# * https://www.youtube.com/watch?v=GRu117xiusQ
import concurrent.futures

from selectolax.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

urls = [
    "https://www.amazon.co.uk/dp/B0002E4Z8M",
    "https://www.amazon.co.uk/dp/B004MQSVQ4",
    "https://www.amazon.co.uk/dp/B002YUAK54",
    "https://www.amazon.co.uk/dp/B0006H92QK",
    "https://www.amazon.co.uk/dp/B009MCU0KI",
    "https://www.amazon.co.uk/dp/B07QR6Z1JB",
    "https://www.amazon.co.uk/dp/B08Q1NJSBQ",
    "https://www.amazon.co.uk/dp/B07MSCRVK",
]

# Função para aceitar cookies
def accept_cookies(driver):
    try:
        # Aguarda o botão "Accept Cookies" aparecer (ajuste o seletor conforme necessário)
        accept_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#sp-cc-accept")
            )  # Exemplo de seletor
        )
        accept_button.click()  # Clica no botão
        print("Cookies aceitos com sucesso!")
    except Exception:
        print("Banner de cookies não encontrado ou já fechado.")



def get_html(url):
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", options=options
    )
    driver.get(url)
    # accept_cookies(driver)
    driver.maximize_window()

    # Espera explícita para o preço ser carregado
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.a-offscreen"))
        )
    except Exception:
        print(f"Elemento não encontrado na URL: {url}")

    html = driver.page_source
    driver.quit()
    return html


def parse_html(html):
    data = HTMLParser(html)
    price_element = data.css_first("span.a-offscreen")
    return {
        "title": data.css_first("title").text(strip=True),
        "price": price_element.text(strip=True)
        if price_element
        else "Preço não encontrado",
    }


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(get_html, urls))

# results = []
# for url in urls:
#     html = get_html(url)
#     data = parse_html(html)
#     results.append(data)

# for idx, result in enumerate(results):
#     print(f"Product {idx + 1}:")
#     print(f"Title: {result['title']}")
#     print(f"Price: {result['price']}")
#     print("\n")

for res in results:
    print(parse_html(res))


