import pytest
from config import DefaultConfig


from dialogs import BookingDialog, MainDialog


Config = DefaultConfig()
#mainDialog = MainDialog()

#__________Test de fichiers de  configuration____

def test_luis_authoring_key():
    assert Config.LUIS_API_KEY != ""


def test_appInsights():
    assert Config.APPINSIGHTS_INSTRUMENTATION_KEY != ""



# def test_dialogs():
#     assert mainDialog.initial_dialog_id !="WFDialog"
