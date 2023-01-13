# Cartoonify
[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Flask-darkgreen.svg?style=flat&logo=flask&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
[![HTML](https://img.shields.io/badge/HTML-black.svg?style=flat&logo=html5&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
[![CSS](https://img.shields.io/badge/CSS-blue.svg?style=flat&logo=css3&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
[![Javascript](https://img.shields.io/badge/Javascript-yellow.svg?style=flat&logo=javascript&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
[![Postgres](https://img.shields.io/badge/Postgres-darkblue.svg?style=flat&logo=postgres&logoColor=white)](https://github.com/Nneji123/SoftEngCartoonify)
![hosted](https://img.shields.io/badge/Railway-430098?style=flat&logo=railway&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
[![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)](https://gitpod.io/#https://github.com/Nneji123/SoftEngCartoonify)
![reposize](https://img.shields.io/github/repo-size/Nneji123/SoftEngCartoonify)
[![Python Tests](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/tests.yml/badge.svg)](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/tests.yml)
[![CodeQL](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/codeql.yml/badge.svg)](https://github.com/Nneji123/SoftEngCartoonify/actions/workflows/codeql.yml)



## About :speech_balloon:
>A Web application deployed using `Railway` that uses Python, Flask, SQLAlchemy, SQLite or Postgres Database to handle user authentication and manage a database of uploaded images. The application features a login and registration page, and allows users to upload and cartoonify images. The use of Python and relevant libraries enables efficient and secure handling of user authentication and image management.



### Link: https://softengcartoonify-production.up.railway.app/login




## Contents :page_with_curl:
- [Cartoonify](#cartoonify)
  - [About :speech\_balloon:](#about-speech_balloon)
    - [Link: https://softengcartoonify-production.up.railway.app/login](#link-httpssoftengcartoonify-productionuprailwayapplogin)
  - [Contents :page\_with\_curl:](#contents-page_with_curl)
  - [Features :star2:](#features-star2)
  - [Tools Used :wrench:](#tools-used-wrench)
  - [Repository File Structure :file\_folder:](#repository-file-structure-file_folder)
  - [Flowchart :chart:](#flowchart-chart)
  - [Use Case Diagram :chart\_with\_upwards\_trend:](#use-case-diagram-chart_with_upwards_trend)
  - [Database Schema](#database-schema)
  - [Application Demo :film\_strip:](#application-demo-film_strip)
  - [How to run the Application :question:](#how-to-run-the-application-question)
  - [Tests :keyboard:](#tests-keyboard)
  - [Deployment :computer:](#deployment-computer)
- [Todo :bookmark\_tabs:](#todo-bookmark_tabs)
- [License :page\_with\_curl:](#license-page_with_curl)




## Features :star2:
- Frontend UI with HTML, CSS and Javascript
- Backend with Python and Flask
- Registration of users to a database (either SQLite or PostgreSQL).
- Login for authenticated users.
- Validation of user details.
- Image upload for logged-in users.
- Cartoonify process of uploaded image.
- Display uploaded image and cartoonified image to logged in user.
- Creation of a user folder for storing uploaded images.
- Deletion of the user folder upon logout to free up space.

## Tools Used :wrench:
- Python
- Flask
- SQLAlchemy
- HTML
- CSS
- Oauth
- Javascript
- Postgres
- SQLite
- Docker

## Repository File Structure :file_folder:
```bash
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── app.py # Main application module
    ├── docker-compose.yml
    ├── Dockerfile
    ├── frontend # Frontend files
    │   ├── display_image.html
    │   ├── error.html
    │   ├── home.html
    │   ├── register_and_login.html
    │   └── static # Folder for static files
    │       ├── logo.png
    │       ├── script.js
    │       └── style.css
    ├── home.py # Module for handling homepage
    ├── index.py # For indexing
    ├── login.py # Module for handling user login
    ├── logout.py # Module for handling user logout
    ├── model.onnx # Model responsible for cartoonifying the image
    ├── models.py # Module for handling user models
    ├── register.py # Module for handling user registration
    ├── requirements.txt # Requirements file
    ├── static # Folder for storing uploaded user images
    │   └── placeholder
    └── utils.py # Utility functions for cartoonifying images

```


## Flowchart :chart:

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


## Use Case Diagram :chart_with_upwards_trend:
<details><summary><b>Packages and Model Schema</b></summary>


![packages](https://user-images.githubusercontent.com/101701760/210594020-037a160c-8666-43f2-87fd-66e41ce36984.png)



![classes](https://user-images.githubusercontent.com/101701760/210594036-d97167d5-b894-42b7-86a9-735a238f4de4.png)

</details>

## Database Schema
<details>
<summary><b>Database Example Image</b></summary>

![Screenshot (293)](https://user-images.githubusercontent.com/101701760/210609974-0a843780-55b8-47c6-a992-77a798c46ab2.png)

</details>

 
## Application Demo :film_strip:



https://user-images.githubusercontent.com/101701760/212251021-6747cb11-8434-4eb3-a7b2-3ffe43a3e586.mp4





## How to run the Application :question:
<details>
    <summary><b>How to Run the application locally.</b></summary>


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
SQLITE=
SECRET_KEY=
DATABASE_MODE=
PORT=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_DISCOVERY_URL=https://accounts.google.com/.well-known/openid-configuration
DEBUG=True
```

`Note: If **DATABASE_MODE** is set to **postgres**, a postgres database will be used else an sqlite database will be used.`

1. If you choose to use a local `sqlite` database make sure to initialize the database first by doing the following from your terminal
- Change the directory
```bash
cd src
```

- Run python
```bash
python init_db.py
```

- A local sqlite database named database.db will be created.

2. Test your changes locally by running `python app.py` from the src folder of this project. Once this is done you can go to `127.0.0.1:5000` to see the application running.

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

3. Edit the `Dockerfile` file and add the keys directly instead of running from the environment

Example:
```docker
ENV POSTGRES postgresql://postgres:password@url:port/railway
ENV SQLITE sqlite:///../database.db
ENV SECRET_KEY secret_key 
ENV DATABASE_MODE sqlite
ENV PORT 5000

```

The above is just an example.

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
  <summary><b>Test Application</b></summary>

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

<details> 
  <summary><b>Performing Load Tests with Locust</b></summary>

1. Make sure the application is running already from the above steps.
2. Install locust:

```bash
pip install locust
```

3. Run locust tests

```bash
  cd tests
  locust -f load_test.py
```

4. Set the number of IP's and address and then run the load tests
<details>
    <summary><b>Locust Test Images<b></summary>
      
      
  ![Screenshot (290)](https://user-images.githubusercontent.com/101701760/210607893-15572ca7-4dcc-45fb-8944-c4e6e082b1cf.png)
  ![Screenshot (291)](https://user-images.githubusercontent.com/101701760/210607904-9ce90c2f-ea74-402d-9465-21ae578b4fbb.png)
  ![Screenshot (287)](https://user-images.githubusercontent.com/101701760/210607907-67c5b8cd-d68e-44e0-a79f-679b890f4a71.png)
  ![Screenshot (288)](https://user-images.githubusercontent.com/101701760/210607913-03e628b0-a203-4352-b0c5-1899dce230a8.png)
  ![Screenshot (289)](https://user-images.githubusercontent.com/101701760/210607915-f5f60610-c69d-4ab3-b7c4-cc442829ecbe.png)


</details>


 </details> 

## Deployment :computer:

<summary><b>Deploy the Application to Railway<b></summary>


Click the button below to deploy the application to railway
  
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/Fr7c3B?referralCode=ZYOf2M)

If deploy fails, change the root directory to `src` in the railway application settings page as shown in the image below:


![Screenshot (294)](https://user-images.githubusercontent.com/101701760/210624138-bfa0ed48-9d0b-4676-a04c-8badcb173926.png)



# Todo :bookmark_tabs:
- [x] Handle Error Popups
- [x] Update Documentation
- [x] Add support with Docker
- [x] Update Readme.
- [x] Update tests.
- [x] Deploy application to the web.
- [x] Added support for Google Email Authentication


# License :page_with_curl:
[MIT](https://github.com/Nneji123/SoftEngCartoonify/LICENSE)
