from config import getApi
import os

api = getApi()

def postStatus(update):
    status = api.PostUpdate(update)
    print(status)

postStatus("Test 1!")
