# %%
import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old websits.")
site =  input("Type a site URL:")
era =  input("Type a year, month, and day, like 20220101:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archvied_snapshots"]["closest"]["url"]
    print("Found this copy:", old_site)
    print("It should appear in your browesr now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)

print("test")


