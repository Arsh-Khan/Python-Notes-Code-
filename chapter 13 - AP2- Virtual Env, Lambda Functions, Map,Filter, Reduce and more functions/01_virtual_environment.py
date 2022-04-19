# for MacOS/linux users: source myprojectenv/bin/activate
# for windows powershell users : .\myprojectenv\Scripts\activate.ps1
# if virtual environment not running then --> write this command on powershell running as administrator--> Set-ExecutionPolicy Unrestricted -Force 

import flask # flask --0.5.2 
import pandas as pd
import pygame

# if you want to delete the virtual environment simply delete the folder
# as it occupies huge memory 117 mb and above (143mb on our device)

#pip freeze is used to print the packages availables in any environment (can also be used to see which package are there in virtualenv)

# pip freeze > \requirements.txt   or pip freeze > requirements.txt
#above code returns all the packages in requirements .txt file along with versions

#for autofilling command you can write first letter and then press tab

# pip install -r.\requirements.txt
#this code is used to install all the packages present in the text file in another environment
#in this example i made an another virtualenv as harryenv and then downloaded all the files using the above code
