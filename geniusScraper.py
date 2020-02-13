import requests
from bs4 import BeautifulSoup
import os

# https://towardsdatascience.com/generating-text-using-a-recurrent-neural-network-1c3bfee27a5e - site for creating the neural network. 
GENIUS_API_KEY = 'y_ffeHQMG4swK_vGBokmlwDGXDz6uYi4wB_-ECBK0lj7AdJoQGkB3LgSE5foHy35'

base_url = 'http://api.genius.com'
headers = {
    'Authorization': 'Bearer ' + GENIUS_API_KEY
}

# list of artists to scrape from
artists = [
            'Travis Scott'
        ]

def get_lyrics(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)
    json = response.json()
    path = json['response']['song']['path']
    #print 'path %s' % path
    page_url = 'http://genius.com' + path
    page = requests.get(page_url)

    print ('Page %s' % page)

    html = BeautifulSoup(page.text, 'html.parser')

    print ('HTML %s' % html)

    [h.extract() for h in html('script')]
    lyrics = html.find('div', { 'class': 'lyrics'}).get_text()

    # print out the lyrics
    print ('Lyrics %s' % lyrics)
    with open('input.txt', 'a') as f:
        f.write(lyrics.encode('utf-8'))
        f.close()

if __name__ == "__main__":
    for artist_name in artists:
        search_url = base_url + '/search?q=%s' % artist_name
        print ('Base URL: %s' % (search_url))
        print ('headers %s' % (headers))

         #send the request
        response = requests.get(search_url, headers=headers)
        json = response.json()

        #print "JSON %s" % (json)

        song_info = None

        for hit in json['response']['hits']:
            print(hit['result']['api_path'])
            get_lyrics(hit['result']['api_path'])
