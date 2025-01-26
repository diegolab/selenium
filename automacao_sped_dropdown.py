from time import sleep
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


# Configuração do ChromeDriver
options = Options()
options.add_argument("--start-maximized")
service = Service(ChromeDriverManager().install())

url = "http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal"

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url)

    # Localiza o elemento do dropdown pela primeira vez
    pacote_dropdown = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_ddlPacotes"))
    )
    primeiro_dropdown = Select(pacote_dropdown)

    # Itera por todas as opções dinamicamente, exceto a primeira (índice 0)
    for index in range(1, len(primeiro_dropdown.options)):
        try:
            # Reobter o elemento do dropdown em cada iteração
            pacote_dropdown = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#ctl00_ContentPlaceHolder1_ddlPacotes"))
            )
            primeiro_dropdown = Select(pacote_dropdown)
            
            # Seleciona a opção pelo índice
            opcao_texto = primeiro_dropdown.options[index].text
            print(Fore.LIGHTBLUE_EX + f"Selecionando a opção: {opcao_texto}", Style.RESET_ALL)
            primeiro_dropdown.select_by_index(index)

            # Aguarde até que a próxima ação seja possível (ex.: carregamento de página)
            sleep(2)
            # Tenta lidar com o botão "OK" caso ele apareça
            try:
                botao_ok = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="Button2"]'))
                )
                print(Fore.LIGHTYELLOW_EX + "Botão de confirmação detectado! Clicando em 'OK'...", Style.RESET_ALL)
                botao_ok.click()
                sleep(1)  # Pequeno delay para garantir que o fluxo continue
            except TimeoutException:
                # Se o botão "OK" não aparecer, segue normalmente
                pass
            
        except Exception as e:
            print(Fore.RED + f"Erro ao selecionar a opção de índice {index}: {e}", Style.RESET_ALL)
            continue

    print(Fore.LIGHTGREEN_EX + "Todas as opções foram selecionadas com sucesso!", Style.RESET_ALL)

except Exception as e:
    print(Fore.RED + f"Ocorreu um erro: {e}", Style.RESET_ALL)

finally:
    driver.quit()
