This project is a simple phishing compliance test web server implemented in Python. The server displays a phishing notice to users, informing them that they have clicked on a phishing link during a recent cybersecurity and phishing compliance test. This project is designed to raise awareness and improve security measures and employee training within an organization.

Features:

    Custom web server built using Python's http.server module.
    Displays a phishing notice when the root path / is accessed.
    Logs the IP address of all visitors accessing the phishing notice.
    Easy to configure and deploy.

Dependencies:

    Python 3.6 or higher

Usage:

    Clone the repository or download the files server.py and notice.html.

    Ensure that the notice.html file containing the phishing notice is in the same directory as the server.py script.

    Run the Python script by executing the following command in the terminal:


python3 server.py

This will start the web server on the default port (8081). You can access the phishing notice by navigating to http://localhost:8081 or http://<your-local-ip-address>:8081.

If you'd like to use a different port, you can change the PORT variable in the server.py script.
