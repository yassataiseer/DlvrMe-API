import json

from requests.auth import HTTPBasicAuth
import base64


## Will grab all data from Order's table
## Check to see if it returns 200 error code
def test_order(app, client):
    del app
    valid_credentials = base64.b64encode(b"Yassa Taiseer:yassa123").decode("utf-8")
    res = client.get('/Orders/all_order',headers={"Authorization": "Basic " + valid_credentials})
    assert res.status_code == 200
    #expected = { "Status": True }
    #assert expected == json.loads(res.get_data(as_text=True))