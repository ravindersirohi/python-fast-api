# python-fast-api
Python Fast API

## About
Python Fast API to perform async CRUD operations on GCP SQL.

## How to setup ?

Please follow the listed below steps.

1. First clone [gh repo clone ravindersirohi/python-fast-api] the python-fast-api repository.
2. Go to the gcp-fast-api folder.
3. Run - [pip install -r requirements.txt] from command prompt.
4. Now create the virtual environment [python -m venv env] and activate (Windows [.\env\Scripts\activate], macOS/Linux [source env/bin/activate]) the virtual environment.
5. [uvicorn main:app --reload] to start the app, once api is up should see http://127.0.0.1:8000
6. http://127.0.0.1:8000/docs to see the Open API/Swagger documentation.

## Infrastructure
API infrastructe is setup on Google Cloud Platform via Terraform, find below the list of components.
TODO

## Security
1. Enable [Identity-Aware Proxy API](https://cloud.google.com/security/products/iap?hl=en_US&_gl=1*1enm781*_ga*NzczNDcyLjE3Mzc1NDA5MTE.*_ga_WH2QY8WWF5*MTczNzU1MTg4OS4zLjEuMTczNzU1MjE0Ny4zLjAuMA..) in GCP.
2. 

## Additional contents

- [Fast API](https://fastapi.tiangolo.com/)
- [oAuth2 in Google](https://developers.google.com/identity/protocols/oauth2)
- [OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server)