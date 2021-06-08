
import json

from requests.auth import HTTPBasicAuth
import base64
def test_index(app, client):
    del app
    res = client.get('/')
    assert res.status_code == 404

def test_Users(app, client):
    del app
    valid_credentials = base64.b64encode(b"Yassa Taiseer:yassa123").decode("utf-8")
    res = client.get('/Users/mk_user/Fake_name/fake_password',headers={"Authorization": "Basic " + valid_credentials})
    print(res)
    assert res.status_code == 200
    expected = { "Status": True }
    assert expected == json.loads(res.get_data(as_text=True))