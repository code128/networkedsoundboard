##
# Joshua Bloom
# SoundBoard runs on an OSX machine and plays sounds from the command line
# when told to by HTTP requests. Multiple clients can control it and 
# play sound effects from the included Flash interface. 
##  

import web
import os 

localPath = os.path.dirname( os.path.realpath( __file__ ) )

## ------------SETTINGS----------------------
soundEffectsDirectory = 'soundEffects'		 
cmdLinePlaySoundCommand = os.path.join(localPath, "play") # Update "play" if you want to use a different audio player. 
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
        return os.listdir(soundEffectsDirectory).__str__()[1:-1] #Remove the brackets around the list repr with [1:-1]

urls = (
    '/getSounds/', 'getSoundList',
    '/(.*)', 'playLocalSound',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()