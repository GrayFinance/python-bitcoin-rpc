import urllib.parse as urlparse
import requests

class BitcoinRPC:

    def __init__(self, url: str) -> None:
        self.url = url
    
    def call(self, method: str, *params: tuple) -> dict:
        data = {"method": method, "params": list(params)}
        resp = requests.post(self.url, headers={"Content-type": "application/json"}, json=data).json()
        if resp.get("error"):
            raise Exception(resp.get("error"))
        else:
            return resp.get("result")
    
    def getnewaddress(self) -> str:
        return self.call("getnewaddress")
    
    def decoderawtransaction(self, rawtx: str) -> dict:
        return self.call("decoderawtransaction", rawtx)
    
    def getaddressinfo(self, address: str) -> dict:
        return self.call("getaddressinfo", address)
    
    def getblockcount(self) -> int:
        return int(self.call("getblockcount"))
    
    def importdescriptors(self, descriptors: tuple) -> dict:
        return self.call("importdescriptors", *list(descriptors))