# ASTG(Another Security Token Generator)

A **Experimental** Security Token generator and verifying library for `python` that uses [FNNH] and `NUMPY` to generate and verify security tokens based on the private key which could be modified easily to create multi level security tokens.

### Requirements

* make sure you have `NUMPY` (Thise was made on version `1.19.2`)
* make sure you have the `FNNH.py` file in the same directory (get it from [FNNH])
* or just download this repo as it has FNNH already with it.

### HOW TO USE

```python
import ASTG
from ASTG import generate_token,verify_token

temp = generate_token()
print(temp)
#Qcd0BrUzu1uyc1w7_J8mDE_7wOzjavBIFEqLvqq3PoppLUG0xfP5dtDUqRrI3jS1 
# - a security token generated as per the private key

status = verify_token(temp)
print(status)
#True - when you verify a token
```

[FNNH]:https://github.com/ApratimR/FNN-Hash