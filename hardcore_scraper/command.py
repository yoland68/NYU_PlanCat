import inspect
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

import util
from util import *


class Command(object):
    def __init__(self, driver):
        self.driver = driver
        self.el = None #current element/elements
        self.element_action_table = dict(inspect.getmembers(util, inspect.isfunction))
        self.driver_action_table = {
            "get": self.driver.get,
            "find_element_by_id": self.driver.find_element_by_id,
            "find_element_by_link_text": self.driver.find_element_by_link_text,
            "find_element_by_css_selector": self.driver.find_element_by_css_selector,
            "find_element_by_class_name": self.driver.find_element_by_class_name,
            "find_elements_by_class_name": self.driver.find_elements_by_class_name,
            "find_elements_by_css_selector": self.driver.find_elements_by_css_selector,
            "switch_to_frame": self.driver.switch_to_frame,
        }


    def run_action(self, action_dict):
        action_list = action_dict.get("action")
        for actor, action, attr, next in action_list:
            if actor == "driver":
                self.driver_action(action, attr)
            elif actor == "element":
                self.element_action(action, attr)
            elif actor == "elements":
                for e in self.el:
                    self.el = e
                    self.element_action(action, attr)
                    if next is not None:
                        self.run_action(next)

            if next is not None:
                run_action(self, next)

    def driver_action(self, action, attr):
        try_counter = 0
        while try_counter < 10:
            try:
                action_function = self.driver_action_table[action]
                if attr is not None:
                    temp = action_function(attr)
                else:
                    temp = action_function()
                if temp is not None:
                    if isinstance(temp, WebElement):
                        self.el = temp
                    elif isinstance(temp[0], WebElement):
                        self.el = temp
                break
            except NoSuchElementException:
                if try_counter == 3:
                    import ipdb; ipdb.set_trace()
                    try_counter += 1
                if try_counter < 10:
                    try_counter += 1
                    time.sleep(1)
                    print("Retry \n\turl: {0}, \n\taction: {1}, \n\tattribute: {2}"
                        .format(self.driver.current_url, action, attr))
                    pass
                else:
                    import traceback; traceback.print_exc();
                    break

    def element_action(self, action, attr):
        try:
            action_function = self.element_action_table[action]
            if attr is not None:
                temp = action_function(self.el, attr)
            else:
                temp = action_function(self.el)

            if temp is not None: #if the action return is not None, it can be an element or a list of element
                if isinstance(temp, WebElement):
                    self.el = temp
                elif isinstance(temp[0], WebElement):
                    self.el = temp
        except NoSuchElementException:
            import ipdb; ipdb.set_trace()


