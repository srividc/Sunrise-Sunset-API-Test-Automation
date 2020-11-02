import datetime
import json
import re

import requests
from behave import given, when, then
from pytest import fail

import constants


@given('I want to test the sunrise and sunset times returned')
@when('I input  valid latitude and longitude in the get request')
@then('I get a successful response including sunset and sunrise times for the specified area')
def test_return_sunset_sunrise_times():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_NOT_FORMATTED)
    assert (get_response.status_code == 200), "Status code is not 200. Rather found : " + str(get_response.status_code)
    data = json.loads(get_response.text)
    response = data["results"]
    date_format = re.compile('\\d{4}-\\d{2}-\\d{2}')
    if response["sunrise"] is not None and date_format.match(response["sunrise"]):
        print ("\n")
        print ("Sunrise time is:", response["sunrise"])
    else:
        fail("Sunrise time is incorrect")
    if response["sunset"] is not None and date_format.match(response["sunset"]):
        print ("Sunset time is:", response["sunset"])
    else:
        fail("Sunset time is incorrect")
    if response["day_length"] is not None and str(response["day_length"]).isdigit():
        print ("Day length  is:", response["day_length"])
    else:
        fail("Day length is incorrect")


@given('The sunset and sunrise API is available I want to test default date')
@when('I do not specify date but specify a valid latitude and longitude in the get request')
@then('I get a successful response for today\'s date by default')
def test_default_date():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_NOT_FORMATTED)
    load_response = json.loads(get_response.text)
    data = load_response["results"]
    sunrise_time = data["sunrise"]
    match = re.search('\\d{4}-\\d{2}-\\d{2}', sunrise_time)
    extract_date = str(datetime.datetime.strptime(match.group(), '%Y-%m-%d').date())
    today = str(datetime.date.today().strftime('%Y-%m-%d'))
    if extract_date == today:
        print ("By default the get request returns today's date when un-formatted")
    else:
        print ("date returned is not today : " + str(extract_date))


@given('The sunset and sunrise API is available and I want to test response for a specific date')
@when('I input valid latitude and longitude query parameters in the get request')
@then('I get a successful response including valid sunset and sunrise times for the specified area')
def test_sunrise_sunset_with_date():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_WITH_DATE)
    assert (get_response.status_code == 200), "Status code is not 200. Rather found : " + str(get_response.status_code)
    load_response = json.loads(get_response.text)
    data = load_response["results"]
    date_time_sunrise = data["sunrise"]
    date_time_sunset = data["sunset"]
    match_sunrise = re.search('\\d{4}-\\d{2}-\\d{2}', date_time_sunrise)
    match_sunset = re.search('\\d{4}-\\d{2}-\\d{2}', date_time_sunset)
    date_str_sunrise = str(datetime.datetime.strptime(match_sunrise.group(), '%Y-%m-%d').date())
    date_str_sunset = str(datetime.datetime.strptime(match_sunset.group(), '%Y-%m-%d').date())
    date_requested_in_api_request = str(constants.PARAMS_WITH_DATE.get("date"))
    if date_str_sunrise == date_requested_in_api_request and date_str_sunset == date_requested_in_api_request:
        print ("Specifying a valid latitude and longitude returns sunrise and sunset times as expected")
    else:
        fail("sunrise and sunset times are not returned correctly")


@given('The sunset and sunrise API is available and I want to test un-formatted response')
@when('I input "formatted =0" query parameter in the get request')
@then('I get un-formatted response for all fields in the response')
def test_un_formatted_response():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_WITH_DATE)
    assert (get_response.status_code == 200), "Status code is not 200. Rather found : " + str(get_response.status_code)
    load_response = json.loads(get_response.text)
    date_requested = str(constants.PARAMS_WITH_DATE.get("date"))
    # creating a new dictionary
    results_dict = load_response["results"]
    print ("\n")
    for key, value in results_dict.items():
        if not (key.startswith("day_length")):
            if value.startswith(date_requested):
                print("Response is not formatted as expected for the key: " + key)
            else:
                fail("Expected Response to be formatted but failed for key " + key)


@given('The sunset and sunrise API is available and I want to test INVALID Date')
@when('I input wrong date and null date as query parameters in the get request')
@then('I get a 400 status code with "INVALID DATE"')
def test_invalid_date():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_WITH_INVALID_DATE)
    load_response = json.loads(get_response.text)
    data = load_response["status"]
    assert (get_response.status_code == 400 and data == "INVALID_DATE"), \
        "Status code is not 200. Rather found " ": " + str(data.status_code)
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_WITH_EMPTY_DATE)
    assert (get_response.status_code == 400 and data == "INVALID_DATE"), \
        "Status code is not 200. Rather found : " + str(get_response.status_code)
    print ("Invalid and null date tested")


@given('I want to verify if time between sunrise and sunset is accurately represented by day length')
@when('I input valid latitude and longitude query parameters in the  request')
@then('I get a response where the time between sunrise and sunset is represented by day length')
def test_day_length():
    get_response = requests.get(constants.BASE_URL, constants.PARAMS_DAY_LENGTH)
    assert (get_response.status_code == 200), "Status code is not 200. Rather found : " + str(get_response.status_code)
    load_response = json.loads(get_response.text)
    data = load_response["results"]
    day_length = data["day_length"]
    date_time_format = '%Y-%m-%dT%H:%M:%S+%f:00'
    date1 = data["sunrise"]
    date2 = data["sunset"]
    diff = datetime.datetime.strptime(date2, date_time_format) - datetime.datetime.strptime(date1, date_time_format)
    time_diff = diff.seconds
    print ("\n")
    if day_length == time_diff:
        print ("Time between sunrise and sunset:" + str(time_diff) +
               " is accurately represented by day length:" + str(day_length))
    else:
        fail(" day length is not correct")
