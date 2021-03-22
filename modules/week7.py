
import urllib.request
from selenium import webdriver
import bs4
import re
import matplotlib.pyplot as plt
import pandas as pd

edc_url = 'https://www.edc.dk'


def edc_interaction(municipal):
    browser = webdriver.Chrome()
    browser.get(edc_url)
    browser.implicitly_wait(5)

    # Accepts cookies:
    button_cookies = browser.find_element_by_xpath(
        "//div[@id='coiPage-1']/div[2]/div/button[3]").click()

    # Inputs municipal in search field:
    input_area = browser.find_element_by_id(
        'TextBoxSearch').send_keys(municipal)

    # Clicks dropdown for house type:
    dropdown_type = browser.find_element_by_xpath(
        '//*[@id="form1"]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/a').click()

    # Selects house type:
    checkbox_type = browser.find_element_by_xpath(
        '//*[@id="form1"]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/span[1]').click()

    # Clicks search button:
    button_search = browser.find_element_by_id(
        'ContentContentPlaceHolder_MainContentPlaceHolder_ContentAreaNewFrontpage_ctl00_ctl02_ctl00_ctl00_ctl00_ctl01_ctl00_buttonSearch').click()

    # Clicks drop-down to select number of results:
    browser.find_element_by_xpath(
        '//*[@id="ContentContentPlaceHolder_MainContentPlaceHolder_ResultSortingAndItemsPerPage_DropDownListItemsPerPage_chosen"]').click()

    # Selects drop-down item to show all results:
    browser.find_element_by_xpath(
        '//*[@id="ContentContentPlaceHolder_MainContentPlaceHolder_ResultSortingAndItemsPerPage_DropDownListItemsPerPage_chosen"]/div/ul/li[4]').click()

    browser.implicitly_wait(5)
    this_url = browser.current_url

    return this_url


def create_df(element_url):
    sauce = urllib.request.urlopen(element_url).read()
    soup = bs4.BeautifulSoup(sauce, 'lxml')

    prices = soup.select('div[class=propertyitem__price] > strong')
    pxs = []

    for node in prices:
        px = re.sub(r'\D', '', node.text)
        pxs.append(int(px))

    house_data = soup.find_all('div', {'class': 'propertyitem__wrapper'})
    result = []

    def conv_str(s):
        num_one = filter(str.isdigit, s)
        num_two = "".join(num_one)
        return int(num_two)

    for h in house_data:
        sample = h.find_all("th")
        sample = [ele.text.strip() for ele in sample]
        sample2 = h.find_all("td")
        sample2 = [ele.text.strip() for ele in sample2]
        vals = [conv_str(s) for s in sample2]
        res = {sample[i]: vals[i] for i in range(len(sample))}
        result.append(res)

    df = pd.DataFrame(result)
    df['Pris'] = pxs

    return df


def show_plot(dataframe, municipal):
    low = dataframe.loc[dataframe['Pris'] < 2000001]['Pris']
    mid = dataframe.loc[dataframe["Pris"].between(
        2000001, 5000000, inclusive=True)]['Pris']
    high = dataframe.loc[(dataframe["Pris"] > 5000000)]['Pris']

    low_count = len(low.index)
    mid_count = len(mid.index)
    high_count = len(high.index)

    d = {"> 2 mio.": low_count, "2-5 mio.": mid_count, "< 5 mio.": high_count}

    plt.bar(range(len(d)), list(d.values()), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.ylabel('Count')
    plt.xlabel('Price range')
    plt.suptitle(municipal)
    plt.show()


def calculate(dataframe, municipal):
    print("Average sales price in " + municipal + ": ")
    print(dataframe["Pris"].mean())

    print("Average sales period in " + municipal + ": ")
    print(dataframe["Liggetid"].mean())


municipal_list = ["Næstved", "Gentofte"]

for m in municipal_list:
    link = edc_interaction(m)
    df = create_df(link)
    show_plot(df, m)
    calculate(df, m)
