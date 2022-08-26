# Calc-Flask

### Instructions:

#### To run the application there are two ways, it can be executed directly by python or in a container with Docker:

  * Running with Python :snake: 
    * Install [Python](https://www.python.org/downloads/)
      
      * Install [pip](https://pip.pypa.io/en/stable/installation/)
       
        * Install [Flask](https://flask.palletsprojects.com/en/2.2.x/installation/)
        
           * ``` python3 app.py ``` 
  
  * Running with Docker :whale:
    * Install [Docker](https://docs.docker.com/engine/install/)
      
      * ``` docker build -t calcflask:version1.0 . ```
       
        * ``` docker run -d -p 80:80 calcflask:version1.0  ```
