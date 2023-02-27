import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Add code to create an instance of the IBM Watson Language translator 
authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

""" Add function englishToFrench which takes in the englishText as a string argument
    Use the instance of the Language Translator you created previously, 
    to translate the text input in English to French and return the French text.
"""
def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

""" Add function frenchToEnglish which takes in the frenchText as a string argument
    Use the instance of the Language Translator you created previously, 
    to translate the text input in French to English and return the English text.
"""

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText = translation['translations'][0]['translation']
    return englishText