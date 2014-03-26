##
# Joshua Bloom
# SoundBoard runs on an OSX machine and plays sounds from the command line
# when told to by HTTP requests. Multiple clients can control it and 
# play sound effects through the included HTML interface. 
# V 2.0
##  


import web
import os 
import sys

if sys.version_info < (2,6):
    import simplejson as json
else:
    import json


localPath = os.path.dirname( os.path.realpath( __file__ ) )

## ------------SETTINGS----------------------
if os.name == 'nt':
    soundPlayer = "playwav" # Update "playwav" if you want to use a different audio player. 
    osSpeakCommand = "SayStatic"
else: #Assuming it's OSX
    soundPlayer = "play"     # Update "play" if you want to use a different audio player. 
    osSpeakCommand = "say"

soundEffectsDirectory = 'sounds'    
cmdLinePlaySoundCommand = os.path.join(localPath, soundPlayer) 

## ------------SETTINGS----------------------

def walkSoundDirectories(soundEffectsDirectory):
    folderArray = []
    for dirName, subdirList, fileList in os.walk(soundEffectsDirectory):
        responseObject = {}
        responseObject["folderName"] = os.path.basename(dirName)
        responseObject["soundFiles"] = []
        for fname in fileList:
            if not fname.startswith("."):
                soundObj = []
                soundObj.append(fname)
                soundObj.append(fname[:-4].replace("_", " ").title())
                responseObject["soundFiles"].append(soundObj)
        folderArray.append(responseObject)
    return folderArray

class playLocalSound:
    def playSound(self, sndName):
        print sndName
        if sndName.startswith(soundEffectsDirectory):
            sndName = sndName[len(soundEffectsDirectory)+1:]
        if (os.path.exists((os.path.join(localPath, soundEffectsDirectory, sndName )))):
            os.popen(cmdLinePlaySoundCommand + ' "' + os.path.join(localPath, soundEffectsDirectory, sndName) + '"')

    def GET(self, name):
        if not name:
            return "Missing Sound Name"
        self.playSound(name)
        return "Sound played."     

class playRemoteSound:
    def GET(self, sndName):
        try:
            if (os.path.exists((os.path.join(localPath, soundEffectsDirectory, sndName )))):
                f = open(os.path.join(localPath, soundEffectsDirectory, sndName), 'rb')
                return f.read()
        except:
            return '' # you can send an 404 error here if you want        

class getSoundList:
    def GET(self):
        return json.dumps(walkSoundDirectories(soundEffectsDirectory))        

class speak:
    def POST(self, words):
        user_data = web.input()
        print user_data.words
    	if user_data.words:
            os.popen(osSpeakCommand + " " + user_data.words)
        raise web.seeother('/static/index.html')

class index:
    def GET(self):
        raise web.seeother('/static/index.html')

class Upload:
    def POST(self):
        x = web.input(myfile={})
        f = open(os.path.join(localPath, soundEffectsDirectory, x['myfile'].filename), 'wb')
        f.write(x['myfile'].value)
        f.close()
        raise web.seeother('/static/index.html')

def notfound():
    raise web.seeother('/static/index.html')

urls = (
    '/getSounds/', 'getSoundList',
    '/speak/(.*)', 'speak',
    '/upload/', 'Upload', 
    '/preview/(.*)', 'playRemoteSound',
    '/play/(.*)', 'playLocalSound',
    '/','index'
)

app = web.application(urls, globals())
app.notfound = notfound

if __name__ == "__main__":
    app.run()