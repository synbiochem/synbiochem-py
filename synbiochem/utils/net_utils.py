'''
synbiochem (c) University of Manchester 2015

synbiochem is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import requests


def get(url, headers, verify=False):
    '''GETs url.'''
    return __process_resp(requests.get(url, headers=headers,
                                       verify=verify))


def put(url, data, headers, verify=False):
    '''POSTs data to url.'''
    return __process_resp(requests.put(url, data=data,
                                       headers=headers, verify=verify))


def post(url, data, headers, verify=False):
    '''POSTs data to url.'''
    return __process_resp(requests.post(url, data=data, headers=headers,
                                        verify=verify))


def post_file(url, files, headers, verify=False):
    '''POSTs a file to url.'''
    new_headers = {}

    for header in headers:
        new_headers[header] = headers[header]

    new_headers['Accept'] = 'application/json'
    new_headers['Content-Type'] = 'multipart/form-data'

    return __process_resp(requests.post(url, files=files, headers=new_headers,
                                        verify=verify))


def __process_resp(response):
    '''Processes a HTTP response.'''
    if response.status_code == 200:
        return response.text

    raise NetworkError(response.status_code, response.text)


class NetworkError(RuntimeError):
    '''Class to represent a network error.'''

    def __init__(self, status, text):
        super(NetworkError, self).__init__(NetworkError)
        self.__status = status
        self.__text = text

    def get_status(self):
        '''Gets the status.'''
        return self.__status

    def get_text(self):
        '''Gets the text.'''
        return self.__text

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str({'status': self.__status, 'text': self.__text})
