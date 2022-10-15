from typing import Optional
import requests
import json

class clReq():
    def request(
        type:str=None,
        url:str=None,
        headers:str=None,
        payload:Optional[str]=None,
    ):
        """
        type: str
            Description: Request Type
            onstraints:
                Valid Values: GET, POST, PUT, DELETE
        url: str
            Description: Request URL
        headers: dict(json)
            Description: Request header
        payload: dict(json)
            Description: Request content
        """
        
        if not type:
            raise AttributeError("Http Type is none")
        elif not url:
            raise AttributeError("url is none")
        elif not headers:
            raise AttributeError("headers is none")
        elif not payload and payload != {}:
            if type == 'GET':
                res = requests.get(url, headers=headers).json()
            elif type == 'POST':
                res = requests.post(url, headers=headers).json()
            elif type == 'PUT':
                res = requests.put(url, headers=headers).json()
            elif type == 'DELETE':
                res = requests.delete(url, headers=headers).json()
            elif type == 'PATCH':
                res = requests.patch(url, headers=headers).json()
            else:
                raise AttributeError("The Type is none")

            return res
        else:
            if type == 'GET':
                res = requests.get(url, headers=headers, params=payload).json()
            elif type == 'POST':
                res = requests.post(url, data=json.dumps(payload), headers=headers).json()
            elif type == 'PUT':
                res = requests.put(url, data=json.dumps(payload), headers=headers).json()
            elif type == 'DELETE':
                res = requests.delete(url, data=json.dumps(payload), headers=headers).json()
            elif type == 'PATCH':
                res = requests.patch(url, data=json.dumps(payload), headers=headers).json()
            else:
                raise AttributeError("The Type is none")
                
            return res