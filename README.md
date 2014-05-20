pyCydia
=======

Cydia API wrapper in Python

Installation
=======
```
$ git clone https://github.com/switchpwn/pyCydia.git
$ cd pyCydia
$ python setup.py install
```
OR
```
$ pip install pyCydia
```

Example
=======
```python
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
```
