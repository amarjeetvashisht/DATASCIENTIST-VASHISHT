#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# # a python program to display all the header tags from wikipedia.org and make data frame.
# 

# In[3]:


page=requests.get("https://en.wikipedia.org/wiki/Main_Page")
page


# In[4]:


soup=BeautifulSoup(page.content)

print(soup.prettify())


# In[5]:


headings=soup.find_all('div',class_="vector-header-container")
headings


# In[6]:


titles=[]

for title in headings:
    title=title.get_text().replace('\n', "")
    title=title.strip(" ")
    titles.append(title)
    
titles


# In[7]:


import pandas as pd


# In[8]:


data=pd.DataFrame()
data['Heading name']=titles
data


# # top 50 IMDB movies 

# In[9]:


page=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_50")
page


# In[10]:


soup=BeautifulSoup(page.content)
soup


# In[11]:


movie=soup.find_all('td',class_="titleColumn")
movie


# In[12]:


names = []
for name in movie:
    name=name.get_text().replace('\n', "")
    name=name.strip(" ")
    names.append(name)
names


# In[13]:


rate=soup.find_all('td',class_="ratingColumn imdbRating")
rate


# In[14]:


ratings = []
for rating in rate:
    rating=rating.get_text().replace('\n', "")
    rating=rating.strip(" ")
    ratings.append(rating)
ratings


# In[15]:


import pandas as pd


# In[16]:


data=pd.DataFrame()
data['movies name']=names
data['ratings']=ratings
data.head(50)


# # 50 indian movies 

# In[17]:


page=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
page


# In[18]:


soup=BeautifulSoup(page.content)
soup


# In[19]:


indmovie=soup.find_all('td',class_="titleColumn")
indmovie


# In[20]:


names = []
for name in indmovie:
    name=name.get_text().replace('\n', "")
    name=name.strip(" ")
    names.append(name)
names


# In[21]:


rate=soup.find_all('td',class_="ratingColumn imdbRating")
rate


# In[22]:


ratings = []
for rating in rate:
    rating=rating.get_text().replace('\n', "")
    rating=rating.strip(" ")
    ratings.append(rating)
ratings


# In[23]:


data=pd.DataFrame()
data['movies name']=names
data['ratings']=ratings
data.head(50)


# # python program to display list of respected former presidents of India

# In[24]:


page=requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page


# In[25]:


soup=BeautifulSoup(page.content)
soup


# In[26]:


indpresident=soup.find_all('div', class_="presidentListing")
indpresident


# In[27]:


names = []
for name in indpresident:
    name=name.get_text().replace('\n', "")
    name=name.strip(" ")
    names.append(name)
names


# In[28]:


presiname=soup.find_all('h3')
presiname


# In[29]:


presiterms=soup.find_all('p')[0:14]
presiterms


# In[30]:


names = []
for name in presiname:
    name=name.get_text().replace('\n', "")
    name=name.strip(" ")
    names.append(name)
names


# In[31]:


terms = []
for term in presiterms:
    term=term.get_text().replace('\n',"")
    term=term.strip(" ")
    terms.append(term)
terms


# In[32]:


data=pd.DataFrame()
data['president names']=names
data['terms of office']=terms
data


# # a python program to scrape cricket rankings

# In[33]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[34]:


soup=BeautifulSoup(page.content)
soup


# In[35]:


team=soup.find_all('span',class_="u-hide-phablet")
team


# In[36]:


teams = []
for oditeam in team:
    oditeam=oditeam.get_text().replace('\n',"")
    oditean=oditeam.strip(" ")
    teams.append(oditeam)
teams


# In[37]:


ausmatch=soup.find_all('td',class_="rankings-block__banner--matches")
ausmatch


# In[38]:


aumatches = []
for auodimatch in ausmatch:
    auodimatch=auodimatch.get_text().replace('\n',"")
    auodimatch=auodimatch.strip(" ")
    aumatches.append(auodimatch)
aumatches


# In[39]:


auspoint=soup.find_all('td',class_="rankings-block__banner--points")
auspoint


# In[40]:


ratpoints = []
for point in auspoint:
    point=point.get_text().replace('\n',"")
    point=point.strip(" ")
    ratpoints.append(point)
ratpoints


# In[41]:


ausrating=soup.find_all('td',class_="rankings-block__banner--rating u-text-right")
ausrating


# In[42]:


rataus = []
for rat in ausrating:
    rat=rat.get_text().replace('\n',"")
    rat=rat.strip(" ")
    rataus.append(rat)
rataus


# In[43]:


match_p=soup.find_all('td',class_="table-body__cell u-center-text")
match_p


# In[44]:


matches = []
for odimatch in match_p:
    odimatch=odimatch.get_text().replace('\n',"")
    odimatch=odimatch.strip(" ")
    matches.append(odimatch)
matches


# In[45]:


matrating=soup.find_all('td',class_="table-body__cell u-text-right rating")
matrating


# In[46]:


ratings = []
for mrating in matrating:
    mrating=mrating.get_text().replace('\n',"")
    mrating=mrating.strip(" ")
    ratings.append(mrating)
ratings


# In[47]:


data=pd.DataFrame()
data['team name']=teams
data['matches']=matches
data['ratings']=ratings
data.head(10)


# In[48]:


len(matches)


# In[49]:


len(ratings)


# In[50]:


len(teams)


# In[51]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi")
page


# In[52]:


soup=BeautifulSoup(page.content)
soup


# In[53]:


name=soup.find_all('td', class_="table-body__cell name")
name


# In[54]:


players = []
for players_name in name:
    players_name=players_name.get_text().replace('\n',"")
    players_name=players_name.strip(" ")
    players.append(players_name)
players


# In[55]:


nation=soup.find_all('td', class_="table-body__cell nationality-logo")
nation


# In[56]:


nationality = []
for players_nationality in nation:
    players_nationality=players_nationality.get_text().replace('\n',"")
    players_nationality=players_nationality.strip(" ")
    nationality.append(players_nationality)
nationality


# In[57]:


ratings_play=soup.find_all('td', class_="table-body__cell u-text-right rating")
ratings_play


# In[58]:


ratings_point = []
for players_ratings in ratings_play:
    players_ratings=players_ratings.get_text().replace('\n',"")
    players_ratings=players_ratings.strip(" ")
    ratings_point.append(players_ratings)
ratings_point


# In[59]:


data=pd.DataFrame()
data['players_name']=players
data['nationality']=nationality
data['ratings']=ratings_point
data.head(10)


# In[60]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/all-rounder")
page


# In[61]:


soup=BeautifulSoup(page.content)
soup


# In[62]:


all_name=soup.find_all('td', class_="table-body__cell rankings-table__name name")
all_name


# In[63]:


allrounders = []
for players_all in all_name:
    players_all=players_all.get_text().replace('\n',"")
    players_all=players_all.strip(" ")
    allrounders.append(players_all)
allrounders


# In[64]:


nation=soup.find_all('td', class_="table-body__cell nationality-logo rankings-table__team")
nation


# In[65]:


nationalityy = []
for players_nation in nation:
    players_nation=players_nation.get_text().replace('\n',"")
    players_nation=players_nation.strip(" ")
    nationalityy.append(players_nation)
nationalityy


# In[66]:


ratings=soup.find_all('td', class_="table-body__cell rating")
ratings


# In[67]:


players_rating = []
for all_rating in ratings:
    all_rating=all_rating.get_text().replace('\n',"")
    all_rating=all_rating.strip(" ")
    players_rating.append(all_rating)
players_rating


# In[68]:


data=pd.DataFrame()
data['players_name']=allrounders
data['nationality']=nationalityy
data['ratings']=players_ratings
data.head(10)


# # a python program to scrape cricket rankings for womens

# In[69]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[70]:


soup=BeautifulSoup(page.content)
soup


# In[71]:


teamwood=soup.find_all('span', class_="u-show-phablet")
teamwood


# In[72]:


teams = []
for womens_team in teamwood:
    womens_team=womens_team.get_text().replace('\n',"")
    womens_team=womens_team.strip(" ")
    teams.append(womens_team)
teams


# In[73]:


womenrating=soup.find_all('td', class_="table-body__cell u-text-right rating")
womenrating


# In[74]:


teamsra = []
for womens_teamrat in womenrating:
    womens_teamrat=womens_teamrat.get_text().replace('\n',"")
    womens_teamrat=womens_teamrat.strip(" ")
    teamsra.append(womens_teamrat)
teamsra[0:12]


# In[75]:


womenmatches=soup.find_all('td', class_="rankings-block__banner--matches")
womenmatches


# In[76]:


data=pd.DataFrame()
data['players_name']=teams
data['nationality']=teamsra
data.head(10)


# In[ ]:


len(teams)


# In[ ]:


len(teamsra)


# In[ ]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
page


# In[ ]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:


playerwomen=soup.find_all('td', class_="table-body__cell name")
playerwomen


# In[ ]:


playername = []
for womens_player in playerwomen:
    womens_player=womens_player.get_text().replace('\n',"")
    womens_player=womens_player.strip(" ")
    playername.append(womens_player)
playername[0:28]


# In[ ]:


natwomen=soup.find_all('span', class_="table-body__logo-text")
natwomen


# In[77]:


playernation = []
for womens_nation in natwomen:
    womens_nation=womens_nation.get_text().replace('\n',"")
    womens_nation=womens_nation.strip(" ")
    playernation.append(womens_nation)
playernation


# In[78]:


ratwomen=soup.find_all('td', class_="table-body__cell u-text-right rating")
ratwomen


# In[79]:


playerrating = []
for womens_rating in ratwomen:
    womens_rating=womens_rating.get_text().replace('\n',"")
    womens_rating=womens_rating.strip(" ")
    playerrating.append(womens_rating)
playerrating


# In[80]:


data=pd.DataFrame()
data['players_name']=playername
data['nationality']=playernation
data['ratings']=playerrating
data.head(10)


# In[81]:


len(playername)


# In[82]:


len(playernation)


# In[83]:


len(playerrating)


# In[84]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[85]:


soup=BeautifulSoup(page.content)
soup


# In[90]:


al_women=soup.find_all('td', class_="table-body__cell rankings-table__name name")
al_women


# In[91]:


alplayer = []
for womens_all in al_women:
    womens_all=womens_all.get_text().replace('\n',"")
    womens_all=womens_all.strip(" ")
    alplayer.append(womens_all)
alplayer


# In[93]:


nat_women=soup.find_all('td', class_="table-body__cell nationality-logo rankings-table__team")
nat_women


# In[94]:


natplayer = []
for womens_nat in nat_women:
    womens_nat=womens_nat.get_text().replace('\n',"")
    womens_nat=womens_nat.strip(" ")
    natplayer.append(womens_nat)
natplayer


# In[95]:


rat_women=soup.find_all('td', class_="table-body__cell rating")
rat_women


# In[96]:


ratplayer = []
for womens_rat in rat_women:
    womens_rat=womens_rat.get_text().replace('\n',"")
    womens_rat=womens_rat.strip(" ")
    ratplayer.append(womens_rat)
ratplayer


# In[97]:


data=pd.DataFrame()
data['players_name']=alplayer
data['nationality']=natplayer
data['ratings']=ratplayer
data.head(10)


# # a python program to scrape mentioned news details 

# In[98]:


page=requests.get("https://www.cnbc.com/world/?region=world")
page


# In[99]:


soup=BeautifulSoup(page.content)
soup


# In[104]:


news=soup.find_all('div', class_="LatestNews-headlineWrapper")
news


# In[105]:


news_headings = []
for news_lat in news:
    news_lat=news_lat.get_text().replace('\n',"")
    news_lat=news_lat.strip(" ")
    news_headings.append(news_lat)
news_headings


# In[103]:


news_time=soup.find_all('time', class_="LatestNews-timestamp")
news_time


# In[ ]:


news_headings = []
for news_lat in news:
    news_lat=news_lat.get_text().replace('\n',"")
    news_lat=news_lat.strip(" ")
    news_headings.append(news_lat)
news_headings


# In[107]:


news_link=soup.find_all('div', class_="nav-menu-navLinks")
news_link


# In[108]:


link = []
for latest in news_link:
    latest=latest.get_text().replace('\n',"")
    latest=latest.strip(" ")
    link.append(latest)
link


# In[168]:


data=pd.DataFrame()
data['time & headings']=news_headings
data['link']=link
data


# # a python program to scrape the details of most downloaded articles from AI

# In[111]:


page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[112]:


soup=BeautifulSoup(page.content)
soup


# In[115]:


article=soup.find_all('h2', class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg")
article


# In[116]:


paper_title = []
for title in article:
    title=title.get_text().replace('\n',"")
    title=title.strip(" ")
    paper_title.append(title)
paper_title


# In[117]:


author=soup.find_all('span', class_="sc-1w3fpd7-0 dnCnAO")
author


# In[118]:


author_title = []
for writer in author:
    writer=writer.get_text().replace('\n',"")
    writer=writer.strip(" ")
    author_title.append(writer)
author_title


# In[119]:


date=soup.find_all('span', class_="sc-1thf9ly-2 dvggWt")
date


# In[120]:


published = []
for disclose in date:
    disclose=disclose.get_text().replace('\n',"")
    disclose=disclose.strip(" ")
    published.append(disclose)
published


# In[131]:


data=pd.DataFrame()
data['paper title']=paper_title
data['authors']=author_title
data['published date']=published
data


# # a python program to scrape mentioned details from dineout.co.in 

# In[132]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[133]:


soup=BeautifulSoup(page.content)
soup


# In[145]:


name=soup.find_all('a', class_="restnt-name ellipsis")
name


# In[146]:


ras_name = []
for rastaurant in name:
    rastaurant=rastaurant.get_text().replace('\n',"")
    rastaurant=rastaurant.strip(" ")
    ras_name.append(rastaurant)
ras_name


# In[152]:


cuisine=soup.find_all('span', class_="double-line-ellipsis")
cuisine


# In[153]:


ras_cuisine = []
for type in cuisine:
    type=type.get_text().replace('\n',"")
    type=type.strip(" ")
    ras_cuisine.append(type)
ras_cuisine


# In[154]:


location=soup.find_all('div', class_="restnt-loc ellipsis")
location


# In[155]:


ras_location = []
for place in location:
    place=place.get_text().replace('\n',"")
    place=place.strip(" ")
    ras_location.append(place)
ras_location


# In[156]:


rating=soup.find_all('div', class_="restnt-rating rating-4")
rating


# In[167]:


ras_rating = []
for points in rating:
    points=points.get_text().replace('\n',"")
    ras_rating.append(points)
ras_rating


# In[158]:


image=soup.find_all('img', class_="no-img")
image


# In[162]:


ras_image = []
for photos in image:
    photos=photos.get_text().replace('\n',"")
    photos=photos.strip(" ")
    ras_image.append(photos)
ras_image


# In[163]:


data=pd.DataFrame()
data['rastaurant_name']=ras_name
data['cuisine']=ras_cuisine
data['location']=ras_location
data['ratings']=ras_location
data['image']=ras_image
data


# In[ ]:





# In[ ]:




