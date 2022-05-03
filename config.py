#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

#_________________New Version takes into account the virtual environment  ______________


import os
from dotenv import load_dotenv

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    #    def __init__(self):
    load_dotenv()


        #-------details for github action deployment______
    PORT = 8000
        #_____Soit Cela
    APP_ID = os.environ.get("MicrosoftAppId", "3c699fe5-4776-47a0-93ca-baa0258c7958") #"this one"
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sjD8Q~pzxGQ3FQHil2TLW9Fg6Gsg.zRW2vA.Ydqs")
         #_______________Nouveau Luis____________
    LUIS_APP_ID = os.environ.get("LuisAppId", "fe2ea595-12f7-494c-8737-bc881341be54")# very last one for insights

   # #   Authoring Resource
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "p10luisresource-authoring.cognitiveservices.azure.com/")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "44680094d70f4b22bc6fb194086ee9f8")
    
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
            "AppInsightsInstrumentationKey", "428b9636-5fe0-4eaa-8d34-7a0dec6c8a5e"
        )


    #   Prediction Resource
    #    LUIS_API_KEY = os.environ.get("LuisAPIKey", "5fc4ccbb7dc04aa094934613afb5f55f")
    #    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "p10luisresource.cognitiveservices.azure.com/")


