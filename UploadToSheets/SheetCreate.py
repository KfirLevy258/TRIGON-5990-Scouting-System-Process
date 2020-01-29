from pprint import pprint

from googleapiclient import discovery

credentials = None

service = discovery.build('sheets', 'v4', credentials=credentials)

spreadsheet_body = {
    # TODO: Add desired entries to the request body.
}

request = service.spreadsheets().create(body=spreadsheet_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
