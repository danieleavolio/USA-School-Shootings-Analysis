#scrape instagram profile creating a folder of the username and saving the images in it
#use scrape_instagram library

from scrape_instagram import *
import os

def scrape_insta(username):
    #create a folder of the username
    os.mkdir(username)
    #change the directory to the folder
    os.chdir(username)
    #scrape the profile
    scrape_instagram(username)
    #change the directory to the parent directory
    os.chdir('..')

if __name__ == '__main__':

    #username of the profile to scrape
    username = 'oh_dagne'
    scrape_insta(username)

# Path: scrape_instagram.py
