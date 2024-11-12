How to deploy the bot in AWS ec2 instance?

1. Launch an EC2 Instance
    Go to the AWS Management Console and open the EC2 Dashboard.
    Click "Launch Instance" and follow these steps:
    a) Name and AMI: Name your instance and choose an Amazon Machine Image (AMI). You might select an Ubuntu AMI if you're comfortable with it.
    b) Instance Type: Choose an instance type (e.g., t2.micro for free tier eligibility).
    c) Key Pair: Select or create a key pair to SSH into the instance.
    d) Network Settings: Ensure the security group allows SSH (port 22) and any other necessary ports (e.g., 80/443 for HTTP/HTTPS).
    e) Storage: Adjust storage as needed.
    f) Launch the instance by clicking "Launch Instance."
    Once the instance is running, note its Public IP Address.
2.  Connect to the EC2 Instance
    Use SSH to connect to the instance:
    ```ssh -i "your-key.pem" ubuntu@<EC2_PUBLIC_IP>```
    Replace "your-key.pem" with your key file and <EC2_PUBLIC_IP> with the actual IP address.
3.  Install Dependencies on EC2
    After connecting to the instance, update the package lists and install Git (if it’s not installed already) and Python:
    ```sudo apt update```
    ```sudo apt install -y git python3-pip```
4. Clone the GitHub Repository
   Replace <github-repo-url> with the actual URL of your GitHub repository:
   ```git clone <github-repo-url>```
   Navigate to the cloned directory:
   ```cd <repo-directory>```
5. Install Python Package Dependencies
   If your repository has a requirements.txt file, install dependencies:
   ```pip3 install -r requirements.txt```
6. Run the Python Script
   Run the desired Python script, for example:
   ```python3 main.py```

Optional: 
Automate with a User Data Script
If you want to automate this, you can pass a User Data script when creating the instance to automate setup.

Here’s an example User Data script:

```
#!/bin/bash
sudo apt update
sudo apt install -y git python3-pip
git clone <github-repo-url>
cd <repo-directory>
pip3 install -r requirements.txt
python3 your_script.py
```

When launching the instance, you can add this script under the Advanced Details > User data section. This will execute the script on startup, cloning the repo, installing requirements, and running the Python script automatically.