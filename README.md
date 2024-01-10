# PDFAnswerBot

## About:

- Description: AI-powered question answering for PDFs with user feedback.
- Tech stack: ChatGPT, LangChain, Python, Flask, JavaScript, HTML
- Overview:
  - App workflow:
    ![app workflow](images/PDFAnswerBot_workflow.png)

## Setup:

1. (For project isolation) create & activate a virtual environment (dependencies are installed within the virtual environment other than system-wide & all subsequent steps will be performed within the virtual environment):
   ```
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade the pip package manager to the latest version within the current Python environment: `python -m pip install --upgrade pip`
3. Install libraries/packages/dependencies: `pip install -r requirements.txt`
4. Initialize the database (if ever need to clear out all the data from this application, just run this command again): `flask --app app.web init-db`
5. Start the server with `python app.py`

## Running the app

There are 3 separate processes that need to be running for the app to work:

- invoke the Python server (in development mode): `inv dev`
- invoke the worker: `inv devworker`
- run Redis: `redis-server`

If you stop any of these processes, you will need to start them back up!

If you need to stop them, select the terminal window the process is running in and press ctrl+C to quit.

To reset the database: `flask --app app.web init-db`

I've created an account using the email `user@test.com` and the password `abc123`.

## Resources:

1. [.gitignore File – How to Ignore Files and Folders in Git](https://www.freecodecamp.org/news/gitignore-file-how-to-ignore-files-and-folders-in-git/)
2. [Keyword Argument & Positional Argument in Python](https://www.geeksforgeeks.org/keyword-and-positional-argument-in-python/)
