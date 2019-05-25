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
### *Client
* from the NYC-SAT-Scores-Client directory
* run 
    >npm install
* run 
    >REACT_APP_SAT_PROXY=http://localhost:5000/ npm start

## Technologies Used
* Pandas 
* Flask
* React / Redux

## Future Updates
* Detail View should display demographic pie chart initially
* Detail View should show 3 bar charts of a particular schools SAT scores onClick
* Create a regression model to predict SAT score from demographic makeup, and visualization