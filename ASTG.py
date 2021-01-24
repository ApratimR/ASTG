"""
ASTG
====

Another Security Token Generator
"""
from FNNH import FNNH
import secrets as rn


# edit the private key to use some other private key
private_key = "this is a private key or it vould be a random string like -x5asChj7lyPkt4m6_"


def generaterng():
	strset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
	rng = [rn.choice(strset) for temp in range(32)]
	empstr = ""
	for temp in range(32):
		empstr+=rng[temp]
	return empstr

tokensize = 32

def generate_token():
	"""
	returns a unique token based on the private key
	"""
	thesr = generaterng()

	thekey = FNNH(data=private_key+thesr,hash_size=tokensize,rounds=32)
	thekey = thekey + thesr
	return thekey

def verify_token(token):
	"""
	verify the token string provided against the Private key

	provides output as a bool
	"""
	if token == None:
		raise Exception("No Token string provided")
	elif len(token) !=64:
		raise Exception("invalid size of token entered")

	hash1,thesr2 = token[0:32],token[32:64]

	calchash = FNNH(data=private_key+thesr2,hash_size=tokensize,rounds=32)

	if hash1 == calchash:
		verify = True
	else:
		verify = False
		
	return verify
	

def custom_verify_token(token,c_primary_key):
	"""
	verify the token string provided against the custom Private key

	provides output as a bool
	"""
	if token == None:
		raise Exception("No Token string provided")
	elif len(token) !=64:
		raise Exception("invalid size of token entered")

	hash1,thesr2 = token[0:32],token[32:64]

	calchash = FNNH(data=c_primary_key+thesr2,hash_size=tokensize,rounds=32)

	if hash1 == calchash:
		verify = True
	else:
		verify = False
		
	return verify

def custom_generate_token(c_private_key):
	"""
	returns a unique token based on the custom private key
	"""
	thesr = generaterng()

	thekey = FNNH(data=c_private_key+thesr,hash_size=tokensize,rounds=32)
	thekey = thekey + thesr
	return thekey
