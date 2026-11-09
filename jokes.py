import requests

API_URL='https://api.api-ninjas.com/v1/dadjokes'

def generate_joke(api_key):
    headers={'X-Api-Key':api_key}
    response=requests.get(API_URL,headers=headers,verify=False )
    if response.status_code==requests.codes.ok:
        joke_obj=response.json()
        return joke_obj['joke']
    #fall back to a default joke if the API fails
    return f'time flies like an arrow.  fruit flies like a banana'