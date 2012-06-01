NetworkSoundBoard
=================
A fun tool that serves up a web soundboard **with a twist**, when a client clicks on a sound it plays on the serving computer **not** the client. 

This is perfect for open plan offices/schools, anywhere you have a bunch of people listening to a common audio system from computer.

Also extra fun points for recording co-workers and playing their voices back for everyone. 

Instructions
------------
	OS's
		This should work out of the box on an OSX machine. 
		Linux, Windows and anything that can run Python will also work if 
		you have a command line audio player and update the path in SoundBoard.py. 
    The ability to speak words is also run from the command line. 
		
	Run this from the terminal like so:
		python SoundBoard.py
		
	Access it from a browser as http://{machinename}:8080
		Then click any of the sounds and they should play on the server machine. 
		To preview the sounds on your client computer, click the little Music note next to the sound button. 
		
	To add more sounds just add them to the soundEffects folder and refresh the browser. 
	
	Have fun.



History 
--------
Originally created 01-24-09 as an Adobe Flex page. 
Converted in 2012 to an HTML5 kind of deal. 


Contributing
------------

If you're having fun with it, let me know and if you come up with enhancements publish em.


Authors
-------

**Joshua Bloom**

+ http://twitter.com/joshbloom
+ http://github.com/code128


License
---------------------

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: 

Libraries & Applications Used
-----------------------------

* [web.py] (http://webpy.org/)
* [play] (http://www.hieper.nl/)
* [ZURB Foundation] (http://foundation.zurb.com/)
* [jQuery] (http://jquery.com/)

Example sounds are from [simplythebest.net](http://simplythebest.net/sounds/WAV/WAV_sounds.html)