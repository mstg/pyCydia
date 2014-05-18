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
from pycydia import pycydia
if __name__ == "__main__":
    client = pycydia.cydia("udid", "package_id", "vendor", "api_key")

    # Check purchase against cydia servers
    cydiaPurchase = client.checkCydiaPurchase()

    # Check if the api check was successful
    if cydiaPurchase != False:
        # Purchased?
        print client.purchaseCompleted()

        # Gift or purchased?
        print client.getStatus()

        # Payment type
        print client.getProvider()
    else:
        # Not successful
        print client.ERROR
