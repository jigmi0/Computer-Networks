Lab 1: Web Server

FILES
- WebServer.py                
- MultiThreadedWebServer.py   
- client.py                   
- HelloWorld.html             
- screenshots              
- report.pdf                  

ENVIRONMENT
- Python 3.8 or newer, no extra packages
- Works on Windows, macOS, or Linux

HOW TO RUN
Run from inside this folder:

    python WebServer.py

Then open in a browser:
- http://localhost:6789/HelloWorld.html   (shows the page)
- http://localhost:6789/missing.html      (shows 404 Not Found)

Optional:

    python MultiThreadedWebServer.py
    python client.py localhost 6789 HelloWorld.html
