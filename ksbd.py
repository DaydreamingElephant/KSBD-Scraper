from bs4 import BeautifulSoup
import requests
import pdb
#initiating all libraries, works in google collab
#specify the start point and arrays to store collected data
url = "https://killsixbilliondemons.com/comic/kill-six-billion-demons-chapter-1/"
liturgyarray = []
alttextarray = [] 
#we use array because opening and closing files every cycle feels unoptimal
lc = 0 #counter for monitoring progress

while True:
    lc += 1
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser") #load the page
    altext = soup.find('a', alt=True)
    liturgy = soup.find('div', {'class':'entry'}).text #we have two strings
    next_button = soup.find('a', {'class': 'navi comic-nav-next navi-next'}) 
    #and the link to the next page


    if (altext): #check presence of content then store
         alttextarray.extend([soup.title.text, altext['alt']]) 
    #or it throws syntax error at 40 instances of erratic website formatting
    else:
         i = soup.find('img', title=True)
         alttextarray.extend([soup.title.text, i['alt']]) 
    if (liturgy.rstrip()):
         liturgyarray.extend([soup.title.text, liturgy])         
            
    print(lc, soup.title.text) #monitor progress
    if (next_button == None):
        break #we've reached the last comic
    else:
        url = next_button['href'] #we iterate to the end of comic
        
#write to .txt files
with open('liturgy.txt', 'w') as f:
    for line in liturgyarray:
        f.write(f"{line}\n")    
with open('alt_text.txt', 'w') as f:
    for line in alttextarray:
        f.write(f"{line}\n")  
