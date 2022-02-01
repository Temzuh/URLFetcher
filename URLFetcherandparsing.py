import re
from urllib.error import HTTPError
from urllib.request import urlopen
import urllib.request



page = input("Give url: ")
try:
    with urlopen(page) as f:
        data = f.read()
        s = data.decode("utf-8")
        y = len(re.findall(r"\b(bomb|murder|kill|terrorism|terror|terrorists|terrorist)\b", s))
        print("The number of bad words: ", str(y))

        x = input("give name for the file: ")
        if x:
            print(x)
        else:
            print("Saving failed.")
        urllib.request.urlretrieve(page, x)

        
except ValueError:
    print("", page)

except HTTPError:
    print("HTTP ERROR", page)

except OSError:
    print("Error opening URL!", page)

except TypeError:
    print("Saving failed", page)

#JPG https://upload.wikimedia.org/wikipedia/commons/0/07/Bomban_talo_1.jpg
#http://brokenurl.doesntexist.com/
#https://fi.wikipedia.org/wiki/Bomban_talo
#https://en.wikipedia.org/wiki/Terrorism