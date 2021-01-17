"""
This script runs the regrr application using a development server.
"""

from os import environ
from regrr import app

if __name__ == '__main__':
    app.run()
	#OST = environ.get('SERVER_HOST', 'localhost')
#	HOST = '0.0.0.0'
	#try:
	#	PORT = int(environ.get('SERVER_PORT', '5555'))
	#except ValueError:
#		PORT = 8080
#	app.run(HOST, PORT)
