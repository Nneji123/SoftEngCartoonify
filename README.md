# Cartoonify Web Application 
[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Flask-darkgreen.svg?style=flat&logo=flask&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
![hosted](https://img.shields.io/badge/Railway-430098?style=flat&logo=railway&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
[![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)](https://gitpod.io/#https://github.com/Nneji123/SoftEngCartoonify)
![reposize](https://img.shields.io/github/repo-size/Nneji123/SoftEngCartoonify)
[![tests](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/test.yml/badge.svg)](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/test.yml)
[![CodeQL](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/codeql.yml/badge.svg)](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/codeql.yml)



## About :speech_balloon:
>A Web application deployed using `Railway` that uses Python, Flask, SQLAlchemy, SQLite or Postgres Database to handle user authentication and manage a database of uploaded images. The application features a login and registration page, and allows users to upload and cartoonify images. The use of Python and relevant libraries enables efficient and secure handling of user authentication and image management.

Link: https://softengcartoonify-production.up.railway.app/login




## Contents :page_with_curl:
- [Cartoonify Web Application](#cartoonify-web-application)
  - [About :speech\_balloon:](#about-speech_balloon)
  - [Contents :page\_with\_curl:](#contents-page_with_curl)
  - [Features :star2:](#features-star2)
  - [Repository File Structure :file\_folder:](#repository-file-structure-file_folder)
  - [Pre-requisites :boom:](#pre-requisites-boom)
  - [How to run the Application :question:](#how-to-run-the-application-question)
  - [Tests :keyboard:](#tests-keyboard)
  - [Deployment :computer:](#deployment-computer)
- [Todo :bookmark\_tabs:](#todo-bookmark_tabs)
- [License :page\_with\_curl:](#license-page_with_curl)
- [Todo :bookmark_tabs:](#todo--bookmark-tabs-)
- [License :page_with_curl:](#license--page-with-curl-)



## Features :star2:
Here are the features of the web application described in the flowchart:
- Registration of users to a database (either SQLite or PostgreSQL)
- Login for authenticated users
- Validation of user details
- Image upload for logged-in users
- Cartoonify process of uploaded image
- Display uploaded image and cartoonified image to logged in user
- Creation of a user folder for storing uploaded images
- Deletion of the user folder upon logout to free up space

## Tools Used :tool:
- Python
- Flask
- SQLAlchemy
- HTML
- CSS
- Javascript
- Postgres
- SQLite
- Docker



## Flowchart :chart:
```mermaid
graph TD
A[Start] --> B[Register User]
B --> C[Login]
C --> D{Successful Login?}
D -- Yes --> E[Check User Details]
E --> F{Valid Details?}
F -- Yes --> G[Home]
F -- No --> C
G --> H[Create User Folder]
H --> I[Upload Image]
I --> J[Cartoonify Image]
J --> K[Display Images]
G --> L[Logout]
L --> M[Delete User Folder]
M --> A
D -- No --> C
```

### Diagram
[![](https://mermaid.ink/img/pako:eNplkctuwjAQRX_F8hp-IItWEPMIhS5KqVTZLEbxECwcO7KdBYr49zoDfUjdee6Zx53xwGuvkRe8CdCd2btQbib3CUI6sun0ic3lGzYmJgzsEDEclZuTXsqtb4zLcUmxGPZ9XWOMp94yQs835URm7BMjpSxkecb6Qn2YwATGxly_ILgcPsAa_a2Pxcu_xSu59i0eH-qrv5tQbkWPtSwDQsJ776W3mqyuCVby0FkPmlUtNGOLiuSNLPOW3jtzuv6gDaEXKUzsLDz00eV9znbc2vcpC1sSdlKgxX-DdwRnjwP8uuUT3mJoweh88UE5xhRPZ2xR8SI_NYSL4srdch70ye-vruZFCj1OeN_pvKAwkD-q5cUJbMTbF6wujiM?type=png)](https://mermaid.live/edit#pako:eNplkctuwjAQRX_F8hp-IItWEPMIhS5KqVTZLEbxECwcO7KdBYr49zoDfUjdee6Zx53xwGuvkRe8CdCd2btQbib3CUI6sun0ic3lGzYmJgzsEDEclZuTXsqtb4zLcUmxGPZ9XWOMp94yQs835URm7BMjpSxkecb6Qn2YwATGxly_ILgcPsAa_a2Pxcu_xSu59i0eH-qrv5tQbkWPtSwDQsJ776W3mqyuCVby0FkPmlUtNGOLiuSNLPOW3jtzuv6gDaEXKUzsLDz00eV9znbc2vcpC1sSdlKgxX-DdwRnjwP8uuUT3mJoweh88UE5xhRPZ2xR8SI_NYSL4srdch70ye-vruZFCj1OeN_pvKAwkD-q5cUJbMTbF6wujiM)



Explanation:
- The flowchart starts at the "Start" node (A).
- The next node is the "Register User" operation (B).
- After the user is registered, the "Login" operation (C) is performed.
- A condition is checked to see if the login was successful (D).
  - If the login was successful, the "Check User Details" operation (E) is performed.
  - If the login was not successful, the flowchart goes back to the "Login" operation (C).
- The user's details are checked to see if they are valid (F).
  - If the details are valid, the flowchart goes to the "Home" end node (G).
  - If the details are not valid, the flowchart goes back to the "Login" operation (C).
- From the "Home" node (G), the user can either upload an image or log out of the application.
  - If the user chooses to upload an image, the "Create User Folder" operation (H) is performed, followed by the "Upload Image" operation (I). The "Cartoonify Image" operation (J) is then performed, followed by the "Display Images" operation (K) to show the uploaded and cartoonified images to the user.
  - If the user chooses to log out, the "Logout" operation (L) is performed and the "Delete User Folder" operation (M) is performed. The flowchart then goes back to the "Start" node (A).




## Repository File Structure :file_folder:
```bash
├───.github # Github Workflows
│   └───workflows
├── app.json # For Deploying to Heroku
├── data
│   └── Rap_lyrics.txt # lyrics file
├── docker-compose.yml # For Containerization with Docker
├── Dockerfile
├── LICENSE 
├── README.md
├── Procfile # For deploying to Heroku and Railway
├── requirements.txt
├── src
│   ├── bot.py # Tweet bot
│   ├── __init__.py
│   ├── server.py # flask server
├── tests # Tests folder
    ├── __init__.py
    └── test_bot.py

```


 
## Application Demo :film_strip:


https://user-images.githubusercontent.com/101701760/210450784-01c707cc-b5e5-4b12-97c5-bc7ca9ba7dc2.mp4



## How to run the Application :question:
<details>
    <summary><b>How to Run the application locally.<b></summary>


To run the application locally do the following:

1. Clone this repository to your local machine
2. Make sure you have python installed. Visit this [link](https://www.python.org/downloads/) for more information on how to install python to your system.
3. Install the required libraries using pip: `pip install -r requirements.txt`
4. Create a file called `.env` in the root directory of your project. Put the necessary environment variables in this file
    * THIS IS JUST FOR TESTING. Once everything is tested and ready to deploy, you'll move these to environment variables.
    * ADD THIS FILE(`.env`) TO THE .gitignore so you're not putting your environment keys publicly on github!

**The environment variables needed are listed below**
```
POSTGRES=
SQLITE="sqlite:///../database.db"
SECRET_KEY
DATABASE_MODE
```

`Note: If **DATABASE_MODE** is set to **postgres**, a postgres database will be used else an sqlite database will be used.`

1. If you choose to use a local `sqlite` database make sure to initialize the database first by doing the following from your terminal
- Change the directory
```bash
cd src
```

- Run python
```bash
python3
from app import db
db.create_all()
```

- A local sqlite database named database.db will be created.

2. Test your changes locally by running `python app.pu` from the src folder of this project.

</details>


<details> 
  <summary><b>Running on Local Machine with Docker Compose</b></summary>

**You can also run the application in a docker container using docker compose(if you have it installed)**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/SoftEngCartoonify.git
```

2. Change the directory:
```
cd SoftEngCartoonify
cd src
```

3. Edit and rename the `.envexample` file to `.env` and store your keys there.


4. Run the docker compose command
```docker
docker compose up -d --build 
```
And then the application should be running on `127.0.0.1:5000`
</details>


<details> 
  <summary><b>Running in a Gitpod Cloud Environment</b></summary>


**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Nneji123/SoftEngCartoonify)
</details>

## Tests :keyboard:
<details> 
  <summary><b>Test Bot</b></summary>

To test the API functions do the following:
1. Clone the repository:
```
git clone https://github.com/Nneji123/SoftEngCartoonify.git
```
2. Change the working directory and install the requirements and pytest:
```
cd SoftEngCartoonify
cd src
pip install -r requirements.txt
```
3. Move to the tests folder and run the tests
```
pip install pytest
pytest tests
```
</details>

## Deployment :computer:

<details>
    <summary><b>Deploy the Bot to Railway<b></summary>
Click the button below to deploy the bot to railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/k_WXDI?referralCode=ZYOf2M)

</details>


# Todo :bookmark_tabs:
- [x] Handle Error Popups
- [x] Update Documentation
- [x] Add support with Docker
- [x] Update Readme.
- [x] Update tests.
- [x] Deploy application to the web.


# License :page_with_curl:
[MIT](https://github.com/Nneji123/SoftEngCartoonify/LICENSE)
