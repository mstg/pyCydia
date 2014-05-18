"""
    PyCydia
    by switchpwn

    Copyright (c) 2014 Mustafa Gezen

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from hashlib import sha1
import time, base64, requests, hmac, cgi

class cydia:
    STATE = None
    PROVIDER = None
    STATUS = None
    UDID = None
    PACKAGE_ID = None
    ERROR = None
    VENDOR = None
    APIKEY = None

    def __init__(self, udid, package_id, vendor, apikey):
        self.UDID = udid
        self.PACKAGE_ID = package_id
        self.VENDOR = vendor
        self.APIKEY = apikey

    # encoding stuff
    def safe_b64enc(self, b64):
        tmp = b64.replace("=", "", -1)
        tmp = tmp.replace("/", "_", -1)
        tmp = tmp.replace("+", "-", -1)

        return tmp

    def get_hmac(self, query, key):
        tmphmac = hmac.new(key, query, sha1).digest()

        signature = self.safe_b64enc(base64.b64encode(tmphmac))

        return signature

    # api stuff
    def apiQuery(self, udid, package_id, vendor, apiKey):
        tmpQuery = "api=store-0.9&device=%s&mode=local&nonce=%d&package=%s&timestamp=%d&vendor=%s" % (udid, time.time(), package_id, time.time(), vendor)

        query = "%s&signature=%s" % (tmpQuery, self.get_hmac(tmpQuery, apiKey))

        return query

    def checkCydiaPurchase(self):
        query = self.apiQuery(self.UDID, self.PACKAGE_ID, self.VENDOR, self.APIKEY)

        request = requests.get('http://cydia.saurik.com/api/check?%s' % query)

        if request == None:
            self.ERROR = "Failed to open request to Cydia"
            return False

        if request.content == None:
            self.ERROR = "API request failed"
            return False

        qs = cgi.parse_qs(request.content)

        if qs == None:
            self.ERROR = "No request content"
            return False

        try:
            self.STATE = qs["state"][0]
        except KeyError:
            self.STATE = "uncompleted"
            return False

        try:
            self.PROVIDER = qs["provider"][0]
        except KeyError:
            self.PROVIDER = None
            return False

        try:
            self.STATUS = qs["status"][0]
        except KeyError:
            self.STATUS = None
            return False

        return True


    def purchaseCompleted(self):
        if self.STATE == "completed":
            return True
        else:
            return False

    def getProvider(self):
        if self.PROVIDER != None:
            return self.PROVIDER
        else:
            return False

    def getStatus(self):
        if self.STATUS != None:
            return self.STATUS
        else:
            return False
