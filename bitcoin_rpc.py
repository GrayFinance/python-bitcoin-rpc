import urllib.parse as urlparse
import requests

class BitcoinRPC:

    def __init__(self, url: str) -> None:
        self.url = urlparse.urlparse(url)
    
    def call(self, method: str, *params: tuple) -> dict:
        data = {"method": method, "params": list(params)}
        base = self.url.geturl()
        resp = requests.post(base, headers={"Content-type": "application/json"}, json=data).json()
        if resp.get("error"):
            raise Exception(resp.get("error"))
        else:
            return resp.get("result")
    
    def getnewaddress(self) -> str:
        return self.call("getnewaddress")
    
    def decoderawtransaction(self, rawtx: str):
        return self.call("decoderawtransaction", rawtx)