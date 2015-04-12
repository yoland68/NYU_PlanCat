import time
import codecs

from util import click_wait as click

def run_customized_action(driver):
    time.sleep(1)
    elems = driver.find_elements_by_css_selector("table.PSLEVEL3GRIDNBO a.SSSAZLINK")
    counter = 648
    for i in range(len(elems)):
        el = elems[counter]
        file_name = el.text.replace("\n", "").strip()
        file_name = file_name.replace("/", "-")
        print("\ncounter: {0}, course: {1}\n================".format(counter, file_name))
        click(driver, el)
        run_page_scrapping(driver, file_name)
        elems = driver.find_elements_by_css_selector("table.PSLEVEL3GRIDNBO a.SSSAZLINK")
        counter += 1


def run_page_scrapping(driver, file_name):
    elems = driver.find_elements_by_tag_name("img")
    for i in range(len(elems)):
        el = driver.find_elements_by_tag_name("img")[i]
        try:
            if el.get_attribute("alt") == "Expand section Click here to learn more:   | Terms Offered: Fall 2015":
                click(driver, el)
            finished = True
        except:
            import traceback; traceback.print_exc();
            import ipdb; ipdb.set_trace()
    with codecs.open("./2015-2016/{0}.html".format(file_name), "w", "utf-8") as f:
        f.write(driver.page_source)

    el = driver.find_element_by_name("NYU_CLS_DERIVED_BACK")
    try_counter = 0
    while try_counter < 10:
        try: 
            click(driver, el)
            break
        except:
            print("Retrying clicking back to subject button...")
            if try_counter == 9:
                import ipdb; ipdb.set_trace()
            try_counter += 1


