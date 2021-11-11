import os
import requests 
import json
import simplejson
import discord 
from discord.ext import commands
weatherKey = os.environ['weatherkey']

zipcode=input("Enter the zip code of the location: ")
#lockeyR = requests.get( "http://dataservice.accuweather.com/locations/v1/postalcodes/search?apikey="+weatherKey+"&q="+zipcode)
#lockeyRjson= lockeyR.json()
#print(lockeyRjson["key"])
client = commands,Bot(command_prefix = "!")


