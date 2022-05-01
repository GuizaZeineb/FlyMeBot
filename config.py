#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv

class DefaultConfig:
    """ Bot Configuration """
        def __init__(self):
            load_dotenv()
            self.PORT = 8000#3978
            #_____Soit Cela
            self.APP_ID = os.environ.get("MicrosoftAppId", "3c699fe5-4776-47a0-93ca-baa0258c7958") #"this one"
            self.APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sjD8Q~pzxGQ3FQHil2TLW9Fg6Gsg.zRW2vA.Ydqs")
            #_____Soit Cela
    #        self.CHATBOT_BOT_ID = os.environ.get("CHATBOT_BOT_ID", "3c699fe5-4776-47a0-93ca-baa0258c7958")
    #        self.CHATBOT_BOT_PASSWORD = os.environ.get("CHATBOT_BOT_PASSWORD", "sjD8Q~pzxGQ3FQHil2TLW9Fg6Gsg.zRW2vA.Ydqs") #"This one"
    #        self.APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
