import uuid
import json
import requests

class MoneyGramAPI:


    def quote_transaction(destinationCountry: str, currency: str, amountSend: float, currencyReceive: str):

        # Step 1: Read configuration values with upmost security
        token = "your_access_token_from_oauth_response"
        # For production - api.moneygram.com & For test - sandboxapi.moneygram.com
        host = "api.moneygram.com";
        url = 'https://' + host + '/transfers/v1/transactions/quote';

        # Step 2: Create the POST request headers & body
        headers = {
            'Content-Type': 'application/json',
            'X-MG-ClientRequestId': str(uuid.uuid4()), # New UUID for each request tracing
            'Authorization': 'Bearer ' + token,
        }
        request = {
            'agentPartnerId': 'your_partner_id',
            'targetAudience': 'AGENT_FACING',
            'userLanguage': 'en-US',
            'destinationCountryCode': f'{destinatoinCountry}',
            'destinationCountrySubdivisionCode': 'US-MN',
            'serviceOptionCode': 'WILL_CALL',
            'sendAmount': {
                'currencyCode': f'{curreny}',
                'value': amountSend
            },
            'receiveCurrencyCode': f'{currencyReceive}',
        }

        try:
            # Step 3: Send the request and obtain the response
            response = requests.post(url, json=request, headers=headers)

            # Step 4: Parse the success response and process further
            if response.status_code == 200:
                parsed_response = json.dumps(json.loads(response.text), indent=2)
                print(parsed_response)
            else:
                # Print the error message if request fails
                # TODO: handle exception
                print("Request failed with status code:", response.status_code)
                print(json.loads(json.dumps(response.text, indent=4)))

        except requests.exceptions.RequestException as e:
            # Print any error that occurred during the request
            # TODO: handle exception
            print("An error occurred:", e)
