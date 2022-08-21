import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv


# loading environment variables for .env file
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#creating instance of ibm watson language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2020-08-21',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#list of al languages
#print(json.dumps(languages, indent=2))

#translate the given text in english to french
def translateEnglishToFrench(englishText):
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

#translate the given text in french to english
def translateFrenchToEnglish(frenchText):
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText








