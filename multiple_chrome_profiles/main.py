#
# * https://www.youtube.com/watch?v=dzQVbezoTv4

import threading
import time

import config as cf
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def start(index):
    options = webdriver.ChromeOptions()
    profile_path = f"user-data-dir={cf.local['userDataDir']}{index}"
    options.add_argument(profile_path)

    print(f"Thread {index} - {profile_path}")

    service = Service(cf.local["executable_path"])
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.google.com")
    time.sleep(10)


def main():
    profiles = []
    for i in range(cf.AMOUNT_THREADS):
        profiles += [threading.Thread(target=start, args=[i])]

    for i in profiles:
        i.start()

    for i in profiles:
        i.join()


if __name__ == "__main__":
    main()
