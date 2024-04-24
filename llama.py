#!/usr/bin/env python3
import json
import requests as request
import argparse
from dotenv import load_dotenv, set_key, dotenv_values
import os

load_dotenv()


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








// command line tool name will be names: 








"""


# Attempt at OOPing this 

class user(): 
    def __init__(self,inputPrompt=""):
        user.prompt=inputPrompt
        user.model= os.getenv("MODEL")
        print(user.model)
       ## Load existing environment variables from the .env file
       #env_vars = dotenv_values(".env")

       ## Change the value of the "MODEL" variable to "Gemma"
       #env_vars["MODEL"] = "Gemma"

       ## Update the .env file with the new value
       #set_key(".env", "MODEL", env_vars["MODEL"])
       #os.environ["MODEL"] = env_vars["MODEL"]

       #user.model= os.getenv("MODEL")
       #print(user.model)


    def getModelData(self):
        with open('models.json','r') as file: 
            models = json.load(file)
        return models["models"]

    def changeModel(self,newModel):
        """
        - code to list models
        - code to change model
        - continously running or change some variable in the .env
        # Access environment variables
        variable_value = os.getenv("VARIABLE_NAME")

        # Modify environment variables
        os.environ["VARIABLE_NAME"] = "new_value"
        """
        models = self.getModelData()
        print(models)
        if newModel not in models: 
            print(models.items())
            print("\033[31mModel Not Found\033[0m")
            return None
        if newModel == os.environ["MODEL"]: 
            print("\033[31mMODEL ALREADY IN USE\033[0m")
            return None
            

    def listModels(self):
        """
        - should list models avialable from a list? 
        - put in env varaibles for now ? 
        - using the api to get this list && updating the json wit it 

        API: 
            GET /api/tags

            json response like: 
            {
            "models": [
                {
                "name": "codellama:13b",
                "modified_at": "2023-11-04T14:56:49.277302595-07:00",
                "size": 7365960935,
                "digest": "9f438cb9cd581fc025612d27f7c1a6669ff83a8bb0ed86c94fcf4c5440555697",
                "details": {
                    "format": "gguf",
                    "family": "llama",
                    "families": null,
                    "parameter_size": "13B",
                    "quantization_level": "Q4_0"
                }
                },
                    {
                "name": "llama2:latest",
                "modified_at": "2023-12-07T09:32:18.757212583-08:00",
                "size": 3825819519,
                "digest": "fe938a131f40e6f6d40083c9f0f430a515233eb2edaa6d72eb85c50d64f2300e",
                "details": {
                    "format": "gguf",
                    "family": "llama",
                    "families": null,
                    "parameter_size": "7B",
                    "quantization_level": "Q4_0"
                    }
                    }
                ]
            }
        """
        pass
    def updateModelList(self): 
        """
        - updates the json if a new model is installed? 
        - for now user input on models
        """
        pass
    def requestBuilder(self): 
        pass
    def response(self,prompt=""): 
        request.post()
    def streamResponse(self): 
        pass

# a single response handler



def main():

    olamCCLi=user("sup")
    olamCCLi.changeModel("llama3")
    

if __name__ == '__main__': 
    main()