Hi!

Something about the application. 

The entire application is written in Flask, HTML and CSS. 
All of this is combined in a single package. 

This follows an MVC architecture. 

The thing missing from the application is Long Polling or the Auto refresh of the index page. 

The directory 
structure is as follows: 

    root 
        d- src
            d- controllers - Contains all the controllers and routes and automatically imported when app is started
            d- models
            d- static - Static fles like css
            d- templates - HTML Files
            d- utils - Functions and unitilies
            f- __init__.py 
            f- config.py - Contains application constants ussualy stored in .evn
            f- crawler.db - Auto created DB
        f- gitignore
        f- README.md
        f- requirements.txt
        f- run.py - Runs the server

To start the application (Change the config.py to change the default config like redis/application host and port)

* You will need 3 terminal windows to run the application
* Start the redis server in the first t-window
* On the second t-window
  * Locate the project
  * Create a venv
  * Install the requirements using requirements.txt
  * Activate the venv
  * Use the command: OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES rq worker --with-scheduler to start a worker/redis-client to communicate between application and redis server
* On the third t-window
  * Activate the venv
  * Use the command: python run.py


And that is it :)

FYI: I am using a MAC and the above-mentioned steps may not work 
with windows or linux.
