# Used by all tests
BASE_URL = r"https://api.sunrise-sunset.org/json?"

# Used by test_return_sunset_sunrise_times and test_default_date
PARAMS_NOT_FORMATTED = {"lat": 40.779659, "lng": -73.968995, "formatted": 0}

# Used by test_sunrise_sunset_with_date and test_un_formatted_response
PARAMS_WITH_DATE = {"lat": 40.779659, "lng": -73.968995, "date": "2019-11-27", "formatted": 0}

# Used by test_invalid_date
PARAMS_WITH_INVALID_DATE = {"lat": 40.779659, "lng": -73.968995, "date": "201&-51-2sd"}
PARAMS_WITH_EMPTY_DATE = {"lat": 40.779659, "lng": -73.968995, "date": "null"}

# Used by test_day_length
PARAMS_DAY_LENGTH = {"lat": 40.779659, "lng": -73.968995, "date": "2020-11-01", "formatted": 0}
