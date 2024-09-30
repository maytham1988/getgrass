import subprocess
import os
import requests
from git import Repo
import time

# Path to the Git repository
repo_path = '/data/data/com.termux/files/home/getgrass'

while True:
    # Download the file from the URL
    url = 'https://raw.githubusercontent.com/monosans/p'  # تکمیل آدرس URL در اینجا ضروری است
    response = requests.get(url)
    with open('all.txt', 'wb') as f:
        f.write(response.content)

    # Rename the file
    os.rename('all.txt', 'proxy.txt')

    # Add all files to the Git repository
    repo = Repo(repo_path)
    repo.index.add('*')

    # Commit changes
    repo.index.commit('Automatic commit')
    
    # افزودن یک تایمر به منظور جلوگیری از اجرای مکرر بدون وقفه
    time.sleep(60)  # اجرای حلقه هر 60 ثانیه
