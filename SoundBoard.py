##
# Joshua Bloom
# SoundBoard runs on an OSX machine and plays sounds from the command line
# when told to by HTTP requests. Multiple clients can control it and 
# play sound effects from the included Flash interface. 
# V 1.0
##  

import json
import web
import os 

localPath = os.path.dirname( os.path.realpath( __file__ ) )

## ------------SETTINGS----------------------
soundEffectsDirectory = 'soundEffects'		 
cmdLinePlaySoundCommand = os.path.join(localPath, "play") # Update "play" if you want to use a different audio player. 
osSpeakCommand = "say"
## ------------SETTINGS----------------------


class playLocalSound:
    def playSound(self, sndName):
        print sndName
        if (os.path.exists((os.path.join(localPath, soundEffectsDirectory, sndName )))):
            os.popen(cmdLinePlaySoundCommand + " '" + os.path.join(localPath, soundEffectsDirectory, sndName) + "'")

    def GET(self, name):
        if not name:
            return "Missing Sound Name"
        self.playSound(name)
        return "Sound played."     

class getSoundList:
    def GET(self):
        responseObject = {}
        soundArray = os.listdir(soundEffectsDirectory)
        cleanSounds = []
        for s in soundArray:
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
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" value="Upload New Sound"  />
</form>
</body></html>"""

    def POST(self):
        x = web.input(myfile={})
        f = open(os.path.join(localPath, soundEffectsDirectory, x['myfile'].filename), 'w')
        f.write(x['myfile'].value)
        f.close()
        raise web.seeother('/static/index.html')

urls = (
    '/getSounds/', 'getSoundList',
    '/speak/(.*)', 'speak',
    '/upload/', 'Upload', 
    '/play/(.*)', 'playLocalSound',
    '/','index'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
