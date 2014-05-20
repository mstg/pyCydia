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
  client = pycydia.cydia("udid", "package", "vendor", "api key")
  
  # Check purchase against cydia servers
  client.checkCydiaPurchase()
  
  # Purchased state
  print client.purchaseCompleted()
  
  # Gift or purchased
  print client.getStatus()
  
  # Payment type
  print client.getProvider()
```
