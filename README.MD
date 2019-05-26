# NYC SAT DATA

## Goal
*  Provide analysis and visualization of SAT scores in New York city dataset

## How to Run Locally
### *Prerequisites
* clone [Client App](https://github.com/JordyKieto/NYC-SAT-Scores-Client)
* clone [Server App](https://github.com/JordyKieto/NYC-SAT-Scores-Server)

### *Server
* from the NYC-SAT-Scores-Server directory
* run 
    >pip install -r requirements.txt
* run 
    >FLASK_APP=app.py flask run
##### __Testing__
* run 
    >pytest
___
### *Client
* from the NYC-SAT-Scores-Client directory
* run 
    >npm install
* run 
    >REACT_APP_SAT_PROXY=http://localhost:5000/ npm start

## Technologies Used
* Python
* Pandas 
* Flask
* Pytest

## Future Updates
* Create a regression model to predict SAT score from demographic makeup, and visualization
* Write unit tests for scores route
* Remove duplicate data in Filter function