from http import client
import json
import pprint
from sre_parse import CATEGORIES

import veryfi

client_id = "vrfvWJ9nitjKT1WFbeBwFKI6b8NJyG47CTJK5Gs"
client_secret = "tlMa59Z3j4oTKVBE47mN3L8hFNxzzV4pcB8DxS9ENFXPyFhwiFDnxFT6JkKD58E6hMCr6PFZPrWVo9FX98vF8cHSWTSlk0lRXhmD9jU6v4zC0hfOHnxcbzAM01VDPm2m"
username = "12412wfwf"
api_key = "bedf3e8a8355b8b93bf27d1c48e37b1"

client = veryfi.Client(client_id, client_secret,username,api_key)

categories = ["travel", "Airfair,lodging","Job Supplies and materials","Grocery" ]
json_result = client.process_document("receipt.jpg", categories)

pprint.pprint(json_result)