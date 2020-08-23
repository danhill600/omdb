#!/usr/bin/env python3
import requests
import json


def get_apikey():
    f = open("omdb_api_key.txt",'r')
    lines = f.read().splitlines()
    apikey = lines[0]
    f.close()
    return apikey


def dict_by_title(apikey, title):
    """gets a NeonCRM session ID for an instance."""
    url = "http://www.omdbapi.com/?t=" + title + "&apikey=" + apikey
    ret = requests.get(url)
    moviedict = json.loads(ret.text)
    return moviedict

apikey = get_apikey()

title = input("Enter movie title: ")

moviedict = dict_by_title(apikey, title)



if moviedict["Response"] == "True":
    print("----------------------------")

    print(moviedict["Title"] + "-(" + moviedict["Year"] + ")")
    print(moviedict["Runtime"] + " Language: " + moviedict["Language"])
    print("Dir. " + moviedict["Director"])

    print("----------------------------")

    print(moviedict["Plot"])

    print("----------------------------")

    print("Actors: " + moviedict["Actors"])
else:
    print("no such movie, there isn't any such movie.")
