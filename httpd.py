#!/usr/bin/env python

import cherrypy, status, os

class LocalStatus(object):
    def index(self):
        return """<html>
                <head>
                    <title>Aurora local status</title>
                </head>
                <html>
                <body>
                    <h1>Status of Aurora on your local machine</h1> 
                </body>
                </html>"""
    
    def status(self):
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
