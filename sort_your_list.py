#!/usr/bin/env python
# coding: utf-8

# In[47]:


import sys
import os
try:
    from pytube import Playlist
    import re
    import requests as req
except:
        print("Oops!", sys.exc_info()[1], "occurred.")
        print("error, importing moduls")
    







# In[48]:


def getPlaylistTitles(PlaylistLink):
    playlist = Playlist(PlaylistLink)

    videosTitle = []
    for viedeo in playlist.videos:
        videosTitle.append(viedeo.title)

    return videosTitle


# In[67]:


def handleYoutubeDlPath(title):
    # youtube-dl add the id of the video in the playlist so we delete it
    newtitle = title
    extension = re.search(r'\..*$', title).group()
    newtitle = title[:-(12+len(extension))] + extension
    return newtitle


# In[70]:


def handleYoutubeDlLink(youtubeList):
    # handle the path it replaces every / with _ 
    # and delete every ?
    # replace : with -
    for i in range(len(youtubeList)):
        youtubeList[i] = youtubeList[i].replace('/','_')
        youtubeList[i] = youtubeList[i].replace('?','')
        youtubeList[i] = youtubeList[i].replace(':',' -')
    


# In[76]:


def sortTheList(OSList, youtubeList, path,isDL):
    postion = str()
    newTitle = str()
    for title in OSList:
        newTitle = title
        if isDL.lower()[0] == 'y':
            newTitle = handleYoutubeDlPath(title)
            
        extension = re.search(r'\..*$', newTitle).group()
        if newTitle[:-len(extension)] in youtubeList:
            postion = str(youtubeList.index(newTitle[:-len(extension)]) + 1)
            os.rename(path  + title, path + '#' + postion + " " + newTitle)
        else:
            print(newTitle + 'is not in the youtube list ')
            print('ensure that special character are handled!!')


# In[72]:


def testOSPath(OSPath):
    
    while not (os.path.exists(OSPath)):
        print('this path is incorrect \n try entring another one')
        print('Or enter 0 to exit')
        OSPath = str(input('please enter your path that have the playlist'))
        if OSPath[0] == '0':
            return False

    return True
       


# In[73]:


def testYoutubeLink(youtubeLink):

    response = req.get(youtubeLink).status_code
    while req.get(youtubeLink).status_code != 200:
        print('this link is incorrect \n try entring another one')
        print('Or enter 0 to exit')
        youtubeLink = str(input('please enter your link that have the playlist'))
        if youtubeLink[0] == '0':
            return False
    
    return True


# In[75]:



def main():
    youtubeLink = str(input('please enter link to the youtube list : '))
    if not (testYoutubeLink(youtubeLink)):
        return
    
    OSPath = str(input('please enter your dirctory path that have the playlist : ') + "/")
    if not (testOSPath(OSPath)):
        return
    
    isDL = str(input('is it downloaded using youtube-dl (y/n)? : '))

    print('loading files name...')
    OSlist = os.listdir(OSPath)
    print('finshed')
    
    print('loading youtube list...')
    youtubeTitlesList = getPlaylistTitles(youtubeLink)
    print('finshed')

    if isDL[0].lower() == 'y':
        handleYoutubeDlLink(youtubeTitlesList)
        

    sortTheList(OSlist,youtubeTitlesList,OSPath, isDL)




if __name__ == '__main__':
    main()
    
    


# In[ ]:





# In[ ]:




