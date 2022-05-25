import requests
from lxml import html

username = ""
password = ""

payload = {
    'frmLogin$UserName': username,
    'frmLogin$Password': password,
    'PGTokenLogin': 'CrQ23gKfRVR6zNo88HpKsermuGuNzFMJ8XtZuWydRI1ocZbUB4gA'
}
url = 'https://ccsf.instructure.com/courses/48566/pages/m1-dot-1-lesson-online-resources?module_item_id=2642369'

session_requests = requests.session()

login_url = "https://ramid.ccsf.edu"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
# authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

print(result.content)

# open web page
# page = urllib3.request.urlopen(url)

#html of page
html = result.content.decode("utf-8")
f = open("test.html", "w")
f.write(html)
f.close()