from urllib.request import urlopen

def getGameInfo(link):
    # Score
    url_score = urlopen(link)
    data_score = url_score.read()
    html_content_score = data_score.decode('utf-8')

    index = html_content_score.find('<h1 class="text-center">')
    score = float(html_content_score[index+24:index+27])

    index_start = html_content_score.find('<h1 class="mb-0">')
    index_end = html_content_score[index_start:].find("</h1>") + index_start
    title = html_content_score[index_start+17:index_end]

    # Plays
    link_logs = link.replace("games", "logs")
    link_logs += "plays"

    url_logs = urlopen(link_logs)
    data_logs = url_logs.read()
    html_content_logs  = data_logs.decode('utf-8')
    
    index_start = html_content_logs.find('<p class="my-auto subtitle-text sort-heading mr-1">')
    index_end = html_content_logs[index_start:].find('</p>') + index_start
    plays = html_content_logs[index_start+51:index_end]

    print(title + ": " + str(score) + "/5.\nPlays: " + str(plays))

getGameInfo("https://backloggd.com/games/disgaea-6-defiance-of-destiny/")
getGameInfo("https://backloggd.com/games/celeste/")