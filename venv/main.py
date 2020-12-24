import pandas as pd
from selenium import webdriver


def getSubmenus(clicked, products):
    s = d.find_elements_by_css_selector("div.sidebar-nav ul li a")
    for ss in s:
        try:
            clicked.index(ss.text)
            if (products.get(ss.text) == None):
                products[ss.text] = []
                s2 = d.find_elements_by_css_selector(".thumbnail")
                for ss2 in s2:
                    products[ss.text].append({"nombre": ss2.find_element_by_css_selector(".caption h4 a").text,
                                              "precio": ss2.find_element_by_css_selector(".caption .price").text,
                                              "desc": ss2.find_element_by_css_selector(".caption .description").text,
                                              "rev": ss2.find_element_by_css_selector(".ratings .pull-right").text,
                                              "rating": ss2.find_element_by_css_selector(
                                                  ".ratings .pull-right + p").get_attribute("data-rating")})
        except:
            clicked.append(ss.text)
            ss.click()
            clicked = getSubmenus(clicked, products)
            return clicked
    return clicked


try:
    d = webdriver.Chrome(executable_path="webdrivers/chromedriver_linux64/chromedriver")
except:
    try:
        d = webdriver.Chrome(executable_path="webdrivers/chromedriver_win32/chromedriver.exe")
    except:
        try:
            d = webdriver.Chrome(executable_path="webdrivers/chromedriver_mac64/chromedriver")
        except:
            print("No ha sido posible ejecutar chrome")
            exit()

d.get("https://webscraper.io/test-sites/e-commerce/scroll")
clicked = []
products = {}
clicked = getSubmenus(clicked, products)
df = pd.DataFrame(products)
df.to_json("some.json")
d.quit()
