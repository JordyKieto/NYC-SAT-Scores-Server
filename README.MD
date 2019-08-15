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
    >bash start_server.sh
##### __Testing__
* run 
    >pytest
___
### *Client
* from the NYC-SAT-Scores-Client directory
* run 
    >npm install
* run 
    >bash start_server *host*

### *Database
* Connection String -> Server=localhost;Database=master;Trusted_Connection=True;

## Technologies Used
* Python
* Pandas 
* Flask
* Pytest
* Sqlite3

## Future Updates
* ~~Create a regression model to predict SAT score from demographic makeup, and visualization~~
* ~~Write unit tests for scores route~~
* ~~Replace iterrows with df apply~~
* ~~Remove duplicate data in Filter function~~
* Unit tests for formatScores utility
* Use reduce instead for enumerate for formatScores
* Allow user input of data