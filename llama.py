import json
import requests
import argparse

PORT = 11434
MODEL = 'llama3'

"""
llamaccli --generate "<prompt>"

def funciton generate
 - build the request 
    - method
    - route

 - handle the request 
 -> get request with ceratin body info like 
 '{
  "model": "llama2",
  "prompt": "What color is the sky at different times of the day? Respond using JSON",
  "format": "json",
  "stream": false
}'

- note model here will be llama3 
- prompt is what changes as userinput
- format should always be json
- stream false will respond one json response but may be slower (in most cases on test) , stream: true is faster but requires more parsing

- def use the requests library and json library to work with the response 

"""


# a single response handler
def response(): 
    pass

def streamResponse(): 
    pass

def main():
    pass

if __name__ == '__main__': 
    main()