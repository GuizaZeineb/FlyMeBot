#import pytest
from config import DefaultConfig
from dialogs import BookingDialog, MainDialog

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

# Source : https://github.com/microsoft/botbuilder-python/blob/main/libraries/botbuilder-testing/tests/test_dialog_test_client.py

import logging

from aiounittest import AsyncTestCase
from botbuilder.core import MessageFactory
from botbuilder.dialogs import (
    ComponentDialog,
    DialogContext,
    DialogTurnResult,
    DialogTurnStatus,
    PromptOptions,
    TextPrompt,
    WaterfallDialog,
    WaterfallStepContext,
)
from botbuilder.schema import Activity
from botbuilder.testing import DialogTestClient, DialogTestLogger

from dialogs import BookingDialog, MainDialog

#Config = DefaultConfig()
#mainDialog = MainDialog()

 ################################################
#       Test de fichiers de  configuration      #
################################################

def test_luis_authoring_key():
    assert Config.LUIS_API_KEY != ""


def test_appInsights():
    assert Config.APPINSIGHTS_INSTRUMENTATION_KEY != ""


#############################################################
#       Bot Builder Testing : test_dialog_test_client.py    #
#############################################################


class DialogTestClientTest(AsyncTestCase):
    """Tests for dialog test client."""

    def __init__(self, *args, **kwargs):
        super(DialogTestClientTest, self).__init__(*args, **kwargs)
        logging.basicConfig(format="", level=logging.INFO)

    def test_init(self):
        client = DialogTestClient(channel_or_adapter="test", target_dialog=None)
        self.assertIsInstance(client, DialogTestClient)

    def test_init_with_custom_channel_id(self):
        client = DialogTestClient(channel_or_adapter="custom", target_dialog=None)
        self.assertEqual("custom", client.test_adapter.template.channel_id)



    async def test_single_turn_waterfall_dialog(self):
        async def step1(step: DialogContext) -> DialogTurnResult:
            await step.context.send_activity("hello")
            return await step.end_dialog()

        dialog = WaterfallDialog("waterfall", [step1])
        client = DialogTestClient("test", dialog)

        reply = await client.send_activity("hello")

        self.assertEqual("hello", reply.text)
        self.assertEqual("test", reply.channel_id)
        self.assertEqual(DialogTurnStatus.Complete, client.dialog_turn_result.status)
        
        
        
    # async def test_component_dialog(self):
    #         BOOKING_DIALOG = BookingDialog()
    #         DIALOG = MainDialog(None, BOOKING_DIALOG)
    #         client = DialogTestClient(
    #         "test",
    #         DIALOG,
    #         initial_dialog_options=None,
    #         middlewares=[DialogTestLogger()],
    #         )
    #         reply = await client.send_activity("Hello")    
