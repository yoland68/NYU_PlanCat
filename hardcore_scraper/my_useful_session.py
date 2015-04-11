# coding: utf-8

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://home.nyu.edu")
nid = driver.find_element_by_id("netid")
nid.send_keys("yy808")
pass = driver.find_element_by_id("password")
password = driver.find_element_by_id("password")
password.send_keys("")
password.submit()
driver.find_element_by_link_text("Academics")
ac = driver.find_element_by_link_text("Academics")
ac.click()
ac.id
ac.text
ac = driver.find_element_by_link_text("Albert Login")
ac.text
ac.id
ac.location
ac.parent
ac.rect
ac
ac.size
ac.click()
for handle in driver.window_handles:
    print(handle)
    
driver.current_window_handle
for handle in driver.window_handles:
    print(type(handle))
    
driver.switch_to.window("CDwindow-480AE0A2-250B-4E66-A13C-4EF2EB414FB1")
el = driver.find_element_by_css_selector("#student_center_wsq a img")
el
el.text
el.tag
el.tag_name
el.click()
driver.find_element_by_text("Search for classes").click()
driver.find_element_by_link_text("Search for classes").click()
driver.find_element_by_link_text("search for classes".upper())
el = driver.find_element_by_id("DERIVED_SSS_SCL_SSS_GO_4$205$")
driver.find_elements_by_tag_name("iframe")
driver.find_elements_by_tag_name("frame")
driver.find_elements_by_tag_name("frame")[1].find_elements_by_tag_name("a")
driver.find_elements_by_tag_name("frame")[1].id
driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[1].id)
driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[1].name)
driver.switch_to.frame(driver.find_elements_by_tag_name("frame")[1])
driver.find_element_by_tag_name("a")
driver.find_element_by_link_text("Search for classes")
driver.current_window_handle
driver.page_source
driver.back()
driver
driver.page_source
f = open("/Users/yoland/Desktop/test.html", 'r')
f = open("/Users/yoland/Desktop/test.html", 'w')
f.write(driver.page_source)
f.close()
driver.find_elements_by_tag_name("a")
driver.find_element_by_link_text("Search for Classes")
driver.find_element_by_link_text("Search for Classes")
driver.find_element_by_css_selector("#DERIVED_SSS_SCL_SSS_GO_4$205$")
driver.find_element_by_css_selector(".SSSBUTTON_CONFIRMLINK")
driver.find_element_by_css_selector(".SSSBUTTON_CONFIRMLINK a")
el = driver.find_element_by_css_selector(".SSSBUTTON_CONFIRMLINK a")
el.text
el.click()
driver.page_source()
f = open("/Users/yoland/Desktop/2015-2016.html", 'w')
f.write(driver.page_source)
f.close()
driver.find_element_by_partial_link_text("2014-2015")
el = driver.find_element_by_partial_link_text("2014-2015")
el.text
el.click()
f = open("/Users/yoland/Desktop/2014-2015.html", 'w')
f.write(driver.page_source)
f.close()
driver.find_elements_by_tag_name("a")
len(driver.find_elements_by_tag_name("a"))
get_ipython().magic('save my_useful_session')
get_ipython().magic('save my_useful_session 0-80')
