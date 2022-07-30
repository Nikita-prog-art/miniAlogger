from minialogger import __version__
import requests


def test_version():
    assert __version__ == '0.1.0'

def test_response():
    data = {
        'service': 'test',
        'level': 'info'.capitalize(),
        'msg': 'testing'
    }
    r = requests.post("http://127.0.0.1:5000", data=data)
    print(r.text)
    assert r.status_code == 200
