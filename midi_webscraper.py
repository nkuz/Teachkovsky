from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import wget
import os
cwd = os.getcwd() + '/song.mid'

my_song_name = text = input("Enter song name:")
upated_song_name = my_song_name.replace(' ', '+')

#sets url to the url after you search for a song
my_url = 'http://www.mididb.com/search.asp?q=' + upated_song_name + '&formatID=1'

#opening up the connection and grabbing the page
uClient = uReq(my_url)
first_page_html = uClient.read()
uClient.close()

#html parsing
first_page_soup = soup(first_page_html, "html.parser")


#finds url for download link
song_containers = first_page_soup.findAll("div", {"class":"left song-details"})
download_url = song_containers[0].find('a').get('href')

#opening up the connection and grabbing the page
uClient2 = uReq(download_url)
second_page_html = uClient2.read()
uClient2.close()

#html parsing
second_page_soup = soup(second_page_html, "html.parser")

#gets real download url for song
download_containers = second_page_soup.find("div",{"class":"right"})
real_download_url = download_containers.div.div.div.find('a').get('href')

wget.download(real_download_url, cwd)  

