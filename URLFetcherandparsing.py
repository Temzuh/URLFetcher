import re
from urllib.error import HTTPError
from urllib.request import urlopen
import urllib.request


page = input("Give url: ")
try:
    with urlopen(page) as resp:
        data = resp.read()
        bad_word_count = 0
        try:
            decoded = data.decode('utf-8')
            bad_word_count = len(re.findall(r"\b(bomb|murder|kill|terrorism|terror|terrorists|terrorist)\b", decoded))
            print("The number of bad words: ", bad_word_count)
        except TypeError:
            print("Downloading binary file...")
        except UnicodeDecodeError:
            print("Downloading binary file...")
        finally: 
            x = input("give name for the file: ")
            if x:
                print(x)
                urllib.request.urlretrieve(page, x)
            else:
                print("Saving failed.")
        
except ValueError as e:
    print("error", page, e)

except HTTPError as e:
    print("HTTP ERROR", page, e)

except OSError as e:
    print("Error opening URL!", page, e)

except TypeError as e:
    print("Saving failed", page, e)

#JPG https://upload.wikimedia.org/wikipedia/commons/0/07/Bomban_talo_1.jpg
#http://brokenurl.doesntexist.com/
#https://fi.wikipedia.org/wiki/Bomban_talo
#https://en.wikipedia.org/wiki/Terrorism