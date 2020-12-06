# Sunrise-Sunset-API-Test-Automation  
# Goal - Write Tests to test Public sunrise API
# Attribution credits to https://api.sunrise-sunset.org/api

**Pre-requisites** 

* Ensure python3 and pip3 are installed
* Run the below command to automatically install needed packages
>pip3 install -r requirements.txt

(OR)

*Install the below manually* 
* Python 3
* pip 3
* pytest 6.1.2
* behave 1.2.6
* pytest-html 2.1.1 
* requests   2.24.0

**Steps to Run Tests** <br/>
*Run the below command in the directory you downloaded the tests into* <br/>
>python -m pytest -v -s  test_sunrise_sunset.py

*To generate results along with log messages*
>python -m pytest -v -s --capture=sys test_sunrise_sunset.py --html=report.html 

**Extra Scenarios:**

*Happy:*

* Scenario 1: Send date parameter in different formats and check if the api response returns a status 200

* Scenario 2: Send a request with the optional callback query parameter and check if a JSONP response is received

* Scenario 3: Check if day_length is received in seconds when request is not formatted and day_length is returned in H:M:S format when request us formatted.

* Scenario 4: check if API documentation is returned at https://api.sunrise-sunset.org/

*Sad/edge cases:*

* Scenario 1: When date parameter is left empty (null is already covered) in 
Environment, the response returned should be a status 200

* Scenario 2: When latitude or longitude is left empty,’invalid request’ should be returned

* Scenario 3: When latitude or longitude is a string instead of float, invalid request should be returned with a 400-bad request status code

* Scenario 4:When date parameter is a string instead of date format, the API seems to return a 200 defaulting to todays date.This result is debatable.
