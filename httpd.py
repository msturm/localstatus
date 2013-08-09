#!/usr/bin/env python

import cherrypy, status, os

class LocalStatus(object):
    def index(self):
        return """<html>
                <head>
                    <title>Aurora local status</title>
                    <link href="static/status.css" rel="stylesheet" type="text/css" />
                </head>
                <html>
                <body>
                    <h1>Status of Aurora on your local machine</h1> 
                    <form><input type="checkbox" name="show-notifications" id="show-notifications"><label for="show-notifications">Show notifications</label></form>
                    <div id="counter">&nbsp;</div>
                    <div id="log">&nbsp;</div>
                    <script src="static/jquery-2.0.3.js"></script>
                    <script src="static/status.js"></script>
                </body>
                </html>"""
    
    def status(self):
        cherrypy.response.headers['Content-Type']= 'application/json'
        return status.getServicesStatus() 

    index.exposed = True
    status.exposed = True

class LocalStatusHttpd:
    def __init__(self):
        staticdir = os.path.abspath(os.path.dirname(__file__)) + '/static'
        cherrypy.tree.mount(LocalStatus(), '/static', config={
            '/': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': staticdir,
                    'tools.staticdir.index': 'index.html',
                },
        })
        cherrypy.config.update({'server.socket_port': 5747})
        cherrypy.quickstart(LocalStatus())
