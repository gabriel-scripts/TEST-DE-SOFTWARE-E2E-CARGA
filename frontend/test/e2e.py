import platform
import os

def config_selenium():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.firefox.service import Service as FirefoxService

    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager

    try:
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        firefox_options = webdriver.FirefoxOptions()
        #firefox_options.add_argument("--headless") 
    except Exception as e: 
        print("error: on configurations of selenium:", e)

    system = platform.system()
    print(system)
    try:
        if system == "Windows":
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif system == "Linux":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        else:
            raise Exception("Error: OS not suported")
    except Exception as e:
        print("Error: ", e)
        print("Please install the required drivers for your OS.")
        return None
    
    return driver

def TestForm(driver):
    NOME_CLIENT_INPUT = '//*[@id="name"]'
    LIMETE_RESTANTE_INPUT = '//*[@id="balance"]'   
    QUANTIDADE_EM_COMPRAS_INPUT = '//*[@id="purchases"]'
    SAQUES_INPUT = '//*[@id="cash_advance"]'
    LIMETE_DE_CREDITO_INPUT = '//*[@id="credit_limit"]'
    PAGAMENTOS_INPUT = '//*[@id="payments"]'

    ENVIAR_ANALISE_BUTTON = '/html/body/div/form/button'
    try:    
        index_path = os.path.abspath("frontend/app/index.html")
        driver.get(f"file://{index_path}")

        driver.find_element("xpath", NOME_CLIENT_INPUT).send_keys("Gabriel")
        driver.find_element("xpath", LIMETE_RESTANTE_INPUT).send_keys("1000")
        driver.find_element("xpath", QUANTIDADE_EM_COMPRAS_INPUT).send_keys("5")
        driver.find_element("xpath", SAQUES_INPUT).send_keys("200")
        driver.find_element("xpath", LIMETE_DE_CREDITO_INPUT).send_keys("1500")
        driver.find_element("xpath", PAGAMENTOS_INPUT).send_keys("500")

        driver.find_element("xpath", ENVIAR_ANALISE_BUTTON).click()
    except Exception as e:
        driver.quit()
        print("error on TestForm:", e)
    
def e2e():
    driver = config_selenium()
    TestForm(driver)

e2e()