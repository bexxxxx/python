#!python2
import urllib

def read_text():
    quotes = open("/Users/RebeccaReilly/github/Python/movie_quotes.txt")
    contents = quotes.read()
    #print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    webconnection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = webconnection.read()
    #print(output)
    webconnection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()
