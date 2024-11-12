How to run the bot in local machine?
1. Create a Virtual environment in local

    Step 1: Open Command Prompt or PowerShell
    To start, open Command Prompt or PowerShell on Windows.

    Step 2: Navigate to Your Project Directory
    Use the cd command to navigate to the directory where you want to create your virtual environment.
    ```cd path\to\your\project```
    Replace path\to\your\project with the actual path to your project folder.

    Step 3: Create the Virtual Environment
    Use the following command to create a virtual environment:
    ```python -m venv venv```
    Here, venv is the name of the virtual environment folder. You can name it something else if you prefer (like myenv), but venv is commonly used.

    Step 4: Activate the Virtual Environment
    Once created, activate the virtual environment with:
    In Command Prompt:
    ```venv\Scripts\activate```
    In PowerShell:
    ```.\venv\Scripts\Activate```
    After activating, you should see (venv) at the beginning of the command line, indicating that your virtual environment is active.

    Step 5: Deactivate the Virtual Environment
    When you’re done working, you can deactivate the virtual environment with:
    ```deactivate```
    This will return you to the global Python environment.
2. Pull the code to your folder which contains the virtual environment folder.
3. Install the necessary libraries using the below command
   ```pip install -r requirements.txt```
4. Start the bot using the below command
   ```python /folder/containing/main.py```






