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


customkey = "private key that can be used to make tokens for muliple tiers"

temp = ASTG.custom_generate_token(customkey)
print(temp)
#P1eF7ysgX00P4yGcf1xM4fQTQ1m_7obSseePeVfPWd7q8LLxlJ74L6LPqO3I--uv
# - a security token generated as per the custom private key

status = ASTG.custom_verify_token(temp,customkey)
print(status)
#True - when you verify a token against the custom private key
```

[FNNH]:https://github.com/ApratimR/FNN-Hash