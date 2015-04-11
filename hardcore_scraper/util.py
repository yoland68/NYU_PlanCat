import time

def send_keys(el, keys):
    return el.send_keys(keys)

def submit(el):
    return el.submit()

def click(el):
    return el.click()

def click_wait(driver, el):
    result = el.click()
    # time.sleep(1)
    tmp = driver.find_element_by_id("WAIT_win0")
    try_counter = 0
    while "display: block" in tmp.get_attribute("style") and try_counter < 20:
        print("page loading...")
        if try_counter == 18:
            import ipdb; ipdb.set_trace()
        try_counter += 1
        time.sleep(0.5)
    return result


