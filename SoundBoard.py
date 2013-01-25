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
    soundPlayer = "playwav" # Update "microwav" if you want to use a different audio player. 
    #soundPlayer = "playwav2.exe" # Update "microwav" if you want to use a different audio player. 
else:
    soundPlayer = "play"     # Update "play" if you want to use a different audio player. 

soundEffectsDirectory = 'sounds'    
cmdLinePlaySoundCommand = os.path.join(localPath, soundPlayer) 
osSpeakCommand = "say"
## ------------SETTINGS----------------------


class playLocalSound:
    def playSound(self, sndName):
        print sndName
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
                f = open(os.path.join(localPath, soundEffectsDirectory, sndName), 'r')
                return f.read()
        except:
            return '' # you can send an 404 error here if you want        

class getSoundList:
    def GET(self):
        responseObject = {}
        soundArray = os.listdir(soundEffectsDirectory)
        cleanSounds = []
        for s in soundArray:
            if not s.startswith("."):
                soundObj = []
                soundObj.append(s)
                soundObj.append(s[:-4].replace("_", " ").title())
                cleanSounds.append(soundObj)
        responseObject["sounds"] = cleanSounds
        return json.dumps(responseObject)

class speak:
    def GET(self, words):
    	if words:
    		os.popen(osSpeakCommand + " " + words)
        return "said"

class index:
    def GET(self):
        raise web.seeother('/static/index.html')

class Upload:
    def POST(self):
        x = web.input(myfile={})
        f = open(os.path.join(localPath, soundEffectsDirectory, x['myfile'].filename), 'w')
        f.write(x['myfile'].value , "wb")
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