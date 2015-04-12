from bs4 import BeautifulSoup
import re
import sys
import json

def parse_classes(dict, course_el):
    class_el_ls = course_el.find_all("div", id=re.compile("divNYU_CLS_DERIVED_HTMLAREA"))
    class_data_ls = []
    for i in range(1, len(class_el_ls)):
        tmp_dict = parse_classes_text(class_el_ls[i].text)
        class_data_ls.append(tmp_dict)
    dict["classes"] = class_data_ls

def parse_base_course_info(course_dict, course_el):
    course_dict["description"] = course_el.find("div", id=re.compile("divNYU_CLS_DERIVED_HTMLAREA")).text.strip()
    course_id_search = re.search(r"{major_id} +\d+".format(major_id=dict["major_id"]), course_dict["description"])
    whites = re.search(" +", course_id_search.group()).group()
    course_dict["course_id"] = course_id_search.group().replace(whites, u' ')
    course_dict["course_name"] = re.search(".*", course_dict["description"][course_id_search.end():]).group().strip()

def parse_classes_text(text):
    text = text.strip()
    text = text.replace("\n", " ")
    if "Notes: " in text:
        text = text[:text.index("Notes")].strip()
    dict = {}
    try:
        if " at " in text and " with " in text:
            search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+) ([MTWFS]{1}.{15,40}M) at (.*) with (.*)", text)
            parts = search.groups()
        elif " at " in text and " with " not in text:
            if re.search("2015 +at", text):
                search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+) at (.*)", text)
                parts = list(search.groups())
                parts.insert(4, None)
                parts.insert(5, None) #Location is None
            else:
                search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+) ([MTWFS]{1}.{15,40}M) at (.*)", text)
                parts = list(search.groups())
                parts.insert(5, None) #Location is None
        elif " at " not in text and " with " in text:
            # print("### Has only with ###")
            if re.search("2015 +with", text):
                search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+) with (.*)", text)
                parts = list(search.groups())
                parts.insert(4, None)
                parts.append(None) #Professor is None
            else:
                search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+) ([MTWFS]{1}.{15,40}M) with (.*)", text)
                parts = list(search.groups())
                parts.append(None) #Professor is None
        elif " at " not in text and " with " not in text:
            # print("### Has neither ###")
            search = re.search("Class#: (\d+).*Section: (\d+).*Component: ([\w| ]+) ([\d|/| |-]+)", text)
            parts = list(search.groups())
            parts.extend([None, None, None])
        else:
            import ipdb; ipdb.set_trace()

        dict["class_id"], dict["section"], dict["format"], dict["period"], dict["time"], dict["location"], dict["professor"] = parts
        dict["format"] = dict["format"].strip()
        dict["open"] = True if "Open" in text else False
    except:
        import traceback; traceback.print_exc();
        sys.exit()
        # import ipdb; ipdb.set_trace()
    return dict



if __name__ == "__main__":
    dict = {}
    file_name = sys.argv[1] if len(sys.argv) == 2 else "./2015-2016/Economics_(ECON-UA).html"
    print("\n###\n{0}".format(file_name))
    with open(file_name, "r") as f:
        soup = BeautifulSoup(f.read())
        dict["major_id"]=re.search("\(.*\)", file_name).group().replace("(", "").replace(")", "")
        dict["file"]=file_name

    course_ls = soup.find_all("table", id=re.compile("ACE_NYU_CLS_SBDTLVW_CRSE_ID")) #find all courses
    course_data = []
    for course_el in course_ls:
        course_dict = {}
        if "No Classes Scheduled for the Terms Offered" in str(course_el.find("span", "SSSTEXTBLUE")):
            course_dict["offering"]=False
            parse_base_course_info(course_dict, course_el)
        else:
            course_dict["offering"] = True
            parse_base_course_info(course_dict, course_el)
            parse_classes(course_dict, course_el)
        course_data.append(course_dict)
    dict["courses"] = course_data
    json_file_name = file_name.replace("2015-2016/", "json/").replace("html", "json")
    with open(json_file_name, 'w') as f:
        f.write(json.dumps(dict, indent=4, separators=(',', ': ')))
