import os

class Action(object):
    """
    All action scripts are in the format of a dictionary with the key "action" 
    point to a list of tuples. Each tuple describe a action for the webdriver,
    or an element, or a group of elements. 
    ("actor", "action", "attribute", "next")

    For example:
    ("driver", "get", "http://google.com", None) command the driver to go to 
    google.com and go to the next action

    next can also be another Action dictionary
    ("elements", "click", None, Action.COURSE_CATA_SCRAP) click all the elements
    and recursively run commands from Action.COURSE_CATA_SCRAP
    """

    nyu_id = os.getenv("NYU_ID")
    nyu_pass = os.getenv("NYU_PASS")

    if nyu_id is None: 
        nyu_id = raw_input("your NetID: ")
    if nyu_pass is None:
        nyu_pass = raw_input("your password: ")

    LOGIN = {
        "action": [
            ("driver", "get", "http://home.nyu.edu", None),
            ("driver", "find_element_by_id", "netid", None),
            ("element", "send_keys", nyu_id, None),
            ("driver", "find_element_by_id", "password", None),
            ("element", "send_keys", nyu_pass, None),
            ("element", "submit", None, None),
        ]
    }

    ALBERT_TO_MAJOR_CATA = {
        "action": [
            ("driver", "get", "http://albert.nyu.edu/", None),
            ("driver", "get", "https://sis.nyu.edu/psc/csprod/EMPLOYEE/CSSS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.NYU_STUDENT_CTR&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder&PortalActualURL=https%3a%2f%2fsis.nyu.edu%2fpsc%2fcsprod%2fEMPLOYEE%2fCSSS%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&PortalContentURL=https%3a%2f%2fsis.nyu.edu%2fpsc%2fcsprod%2fEMPLOYEE%2fCSSS%2fc%2fSA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL&PortalContentProvider=CSSS&PortalCRefLabel=Student%20Center&PortalRegistryName=EMPLOYEE&PortalServletURI=https%3a%2f%2fadmin.portal.nyu.edu%2fpsp%2fpaprod%2f&PortalURI=https%3a%2f%2fadmin.portal.nyu.edu%2fpsc%2fpaprod%2f&PortalHostNode=EMPL&NoCrumbs=yes", None),
            ("driver", "find_element_by_link_text", "Search For Classes", None),
            ("element", "click", None, None),
            # ("driver", find_element_by_name)
        ]
    }

    MAJOR_CATA_TO_COURSE_CATA = {
        "action": [
            ("driver", "find_elements_by_css_selector", "table.PSLEVEL3GRIDNBO a.SSSAZLINK", None), #find all major 
        ]
    }

    #MORE?