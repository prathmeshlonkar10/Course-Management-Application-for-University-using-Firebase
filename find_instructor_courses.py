# ========== File7 ==========

# Importing the permitted libraries.
import requests
import json

def fetch(instructor_id):
  # Load the Firebase Realtime DB URL stored in the config file.
  with open("config.json") as cfr:
      config_data = json.load(cfr)
  url = config_data["url"]

  # Appending additional strings to the main URL to point towards the data.
  url_split = url.split('.json')
  url = url_split[0] + "course_management_app/relationships/instructors/{}.json".format(instructor_id)

  # Capture the response from Firebase.
  response = requests.get(url)

  # Error Handling for data retreival.
  if response.status_code == 200:
    # The request was successful, hence converting to json format.
    data = response.json()
    if data == None:       
      print("\n========== ERROR ==========\nProvided Instructor ID {} has no associated course data. Please associate this Instructor ID with available Courses and try again.".format(instructor_id))
      return False
  else:
    # The request failed, hence quiting the script.
    print("\n========== ERROR ==========\nUnable to fetch data from Firebase: {}".format(response.status_code))
    return False

  # Print the data if successfully captured.
  print("\n========== SUCCESS ==========\nData Successully fetched for instructor ID {0}, the instructor name and the list of courses taught by the instructor is as follows:\n".format(instructor_id), json.dumps(data, indent=2))
  return True