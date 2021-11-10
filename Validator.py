import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init(True)
def Validator(mail):
    try:
        session = requests.Session()
        res = session.get("https://login.yahoo.com/?display=narrow&aembed=1&intl=us&lang=en-US&src=iosasdk&dnp=1&appsrc=ymobilemail&.done=https%3A%2F%2Fmobileexchange.yahoo.com%3Fslcc%3D0&appsrcv=42719&srcv=10.3.2&.asdk_embedded=1", timeout=8)
        soup = BeautifulSoup(res.text, "html.parser")
        crumb = soup.find("input", attrs={"name":"crumb"})['value']
        acrumb = soup.find("input", attrs={"name":"acrumb"})['value']
        postdata = """crumb=<crumb>&acrumb=<acrumb>&sessionIndex=QQ--&displayName=&deviceCapability={"pa":{"status":false}}&username=<mail>&passwd=&signin=Next"""
        postdata = postdata.replace('<crumb>', crumb)
        postdata = postdata.replace('<acrumb>', acrumb)
        postdata = postdata.replace('<mail>', mail)
        headers = {"Accept": "*/*","X-Requested-With": "XMLHttpRequest","Accept-Language": "en-us","Origin":"https://login.yahoo.com","Connection": "close","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148","Referer": "https://login.yahoo.com/","Content-Type": "application/x-www-form-urlencoded"}
        req = session.post("https://login.yahoo.com/?display=narrow&aembed=1&intl=us&lang=en-US&src=iosasdk&dnp=1&appsrc=ymobilemail&.done=https%3A%2F%2Fmobileexchange.yahoo.com%3Fslcc%3D0&appsrcv=42719&srcv=10.3.2&.asdk_embedded=1", data=postdata, headers=headers)
        source = req.text
        if source.__contains__("INVALID_USERNAME") or source.__contains__("INVALID_IDENTIFIER"):
            print(f"{Fore.RED}[-]{mail}")
        elif source.__contains__("location"):
            print(f"{Fore.LIGHTGREEN_EX}[+]{mail}")
    except Exception as e:
        Validator(mail)
