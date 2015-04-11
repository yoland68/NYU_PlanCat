from selenium import webdriver
from command import Command
from customized_action import run_customized_action
from action import Action

class Session(object):
    def __init__(self, name="Session 1"):
        self.name = name
        self.driver = self.get_driver()
        #TBI

    def get_driver(self):
        try:
            return webdriver.Chrome()
        except WebDriverException:
            return webdriver.Firefox()

    def run_scrap(self):
        comm = Command(self.driver)
        comm.run_action(Action.LOGIN)
        comm.run_action(Action.ALBERT_TO_MAJOR_CATA)
        # import ipdb; ipdb.set_trace()

        #customized actions:
        run_customized_action(self.driver)



if __name__ == "__main__":
    try:
        s = Session()
        s.run_scrap()
    except:
        import traceback; traceback.print_exc();
        import ipdb; ipdb.set_trace()
        traceback.print_exc();
    # s.driver.quit()
    
