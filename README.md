


This application is deployed using Render's free tier, inline with the cost saving aspect of the project.

### Deployment to Render:
1) Ensure code is in a Github Repo.

2) Create an account on Render: https://render.com/

3) To make a Webservice, in Render's dashboard, click New > Web Service 

4) Connect to the relevant Github Repo

5) Choose the relevant language (Python 3)

6) Select a region nearby

7) For the Build command use: "pip install poetry && poetry install --no-root"

8) For the Start command use: "poetry run gunicorn generator:app"

9) Select Free as the Instance Type

10) Add your OpenAI API key as an environment variable at the bottom, set the Key as "OPENAI_API_KEY". Make another environment variable "PYTHON_VERSION" to specify the version to use (e.g 3.11.11)

11) Click Deploy Web Service

12) Render will then navigate to a deployment page. Wait for deployment to complete

13) Once deployment is successful, you can access the deployed application via the URL provided (likely ending in .onrender.com)

14) If you want to set a specific Python version, naviate to 'Environment' In the Left tool bar, and add an environment 

14) To stop the deployment, navigate to 'Settings' in the Left tool bar, select the relevant Webservice and click 'Suspend Web Service' at the bottom of the page.
