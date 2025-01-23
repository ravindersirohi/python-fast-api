# python-fast-api
Python Fast API

## About
Python Fast API running on [Google Cloud Run ](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service) container app, and secured via Google Platform Identity.

## How to setup ?

Please refer below steps to setup the Python Fast API.

1. First clone [gh repo clone ravindersirohi/python-fast-api] the python-fast-api repository.
2. Go to the gcp-fast-api folder.
3. Run - [pip install -r requirements.txt] from command prompt.
4. Now create the virtual environment [python -m venv env] and activate (Windows [.\env\Scripts\activate], macOS/Linux [source env/bin/activate]) the virtual environment.
5. [uvicorn main:app --reload] to start the app, once api is up should see http://127.0.0.1:8000
6. http://127.0.0.1:8000/docs to see the Open API/Swagger documentation.

## Deployment

Source and infrastructre deployed via the Github workflow, please refer [.github/workflow/deploy](https://github.com/ravindersirohi/python-fast-api/blob/main/.github/workflows/deploy.yml) yaml file.

## Security
1. Enable [Identity-Aware Proxy API](https://cloud.google.com/security/products/iap?hl=en_US&_gl=1*1enm781*_ga*NzczNDcyLjE3Mzc1NDA5MTE.*_ga_WH2QY8WWF5*MTczNzU1MTg4OS4zLjEuMTczNzU1MjE0Ny4zLjAuMA..) in GCP.
2. Create oAuth2.0 Client Id in [GPC](https://support.google.com/cloud/answer/6158849?hl=en).
3. REDIRECT_URI to be your cloud run base url https://..../callback
4. Populate GCP_CLIENT_ID, GCP_CLIENT_SECRET and REDIRECT_URI values (from step 2) in GitHub secrets (Repository settings->Secrets and Variables).

## Infrastrue setup
API infrastructe is setup on Google Cloud Platform via Terraform, please refer [gcp-terraform-infra](https://github.com/ravindersirohi/gcp-terraform-infra) and extend for below resources.

```
Service Account:

resource "google_service_account" "service_account" {
  account_id   = "service-account-id"
  display_name = "Service Account"
}

oAuth Client App:

resource "google_identity_platform_oauth_idp_config" "oauth_idp_config" {
  name          = "oidc.oauth-idp-config"
  display_name  = "Display Name"
  client_id     = "client-id"
  issuer        = "issuer"
  enabled       = true
  client_secret = "secret"
}

Artifact Registry:

resource "google_artifact_registry_repository" "my-repo" {
  location      = "europ-west2"
  repository_id = "my-repository"
  description   = "example docker repository"
  format        = "DOCKER"
}

```

### How to access API once hosted on Google Cloud ?

Once the source code gets deployed via the Github trigger, should be able to see container access point (for example - https://cloud-run-fast-api-123456789.europe-west2.run.app).
Please follow below to access secured API.

1. .../docs - Swagger UI endpoint.
2. .../login - Login endpoint, authencticate yourself, once authencticated will get the token back.
3. .../protected endpoint - Call this endpoint with the Access_Token receieved post login.

## Additional references

- [Fast API](https://fastapi.tiangolo.com/)
- [oAuth2 in Google](https://developers.google.com/identity/protocols/oauth2)
- [OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server)
- [Google Identity Platform Config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/identity_platform_config)