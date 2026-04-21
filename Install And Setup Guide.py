#Install and Setup guide

#Prerequisites:
  #Python 3.6 or higher (Python 3.8.2+ recommended)
  #pip3 package manager

#Check Python Version
  #copy and paste into terminal:
  python3 --version

#Create virtual environment:
  #copy and paste into terminal:
  python3 -m venv fastapi_env 
  #fastapi_venv is just the name of the virutal environment so it can be anything
  #for every metion of the name during this process you replace with the name of the virtual environment you have created if you decided to change 
  #the name of the vritual environment to a name different from what it is here.

#To Activate Virtual Environment:
  #if on MacOS/Linux:
      #copy and paste into terminal:
      source fastapi_env/bin/activate
  #if on windows:
      #copy and paste into terminal:
      fastapi_env\Scripts\activate

#To Install FastAPI:
  #copy and paste into terminal:
  pip3 install fastapi

#To Install Uvicorn (ASGI Server)
  #copy and paste into terminal:
  pip3 install uvicorn[standard]

#To Start Development Server:
  #copy and paste into terminal:
  uvicorn main:app --reload

#To see your API running click on the localhost link which will be outputted on the terminal whenever u start the development server
#to be able to interact with your code visually:
  #go on ur server and then type /docs



