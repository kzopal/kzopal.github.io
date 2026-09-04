#!/usr/bin/python3

from livereload import Server

server = Server()
server.watch('.')
server.serve(port=8000)