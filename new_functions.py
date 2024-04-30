from ast import Try
from urllib.request import urlopen
import urllib.error
import re

def createBackloggdLink(game):
    game = re.sub(r'\W+', ' ', game)
    game = game.replace(" ", "-")
    game = game.lower()
    game = "https://backloggd.com/games/" + game + "/"
    return game

def getGameScore(link):
    # Score
    try: 
        url = urlopen(link)
        data = url.read()
        html_content = data.decode('utf-8')
    except(urllib.error.HTTPError):
        return "error"
    
    index = html_content.find('<h1 class="text-center">')
    score = html_content[index+24:index+27]
    
    return score

def getFormattedTitle(link):
    try: 
        url = urlopen(link)
        data = url.read()
        html_content = data.decode('utf-8')
    except (urllib.error.HTTPError):
        return "error"
    
    index_start = html_content.find('<h1 class="mb-0">')
    index_end = html_content[index_start:].find("</h1>") + index_start
    title = html_content[index_start+17:index_end]
    
    return title

def getPlays(link):
    link = link.replace("games", "logs")
    link += "plays" # Creates new link to access play count

    try: 
        url = urlopen(link)
        data = url.read()
        html_content  = data.decode('utf-8')
    except (urllib.error.HTTPError):
        return "error"
    
    index_start = html_content.find('<p class="my-auto subtitle-text sort-heading mr-1">')
    index_end = html_content[index_start:].find('</p>') + index_start
    plays = html_content[index_start+51:index_end]
    
    return plays

createBackloggdLink("Disgaea 7: Vows of the Virtueless")
print(getGameScore(createBackloggdLink("Disgaea 7: Vows of the Virtueless")))



# To do list:
# - User input: Search for specific games, convert games into links then search using that link
# - More info: Maybe release date & developers/publishers?
# - Series/multiple games & averages
# - Create an actual UI lol, this'll take a bit so be ready