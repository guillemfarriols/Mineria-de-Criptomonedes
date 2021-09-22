import hashlib 
import time as t
comensament=t.time()

NONCE_LIMIT = 10000000000

zeros = 4

def mina(numero_de_bloc, transaccions, hash_anterior):
	for nonce in range(NONCE_LIMIT):
		text_base = str(numero_de_bloc) + transaccions + hash_anterior + str(nonce)
		hash_try = hashlib.sha256(text_base.encode()).hexdigest()
		if hash_try.startswith('0' * zeros):
			print(f"Hash trobat amb Nonce: {nonce}")
			return hash_try

	return -1

numero_de_bloc = 24
transaccions = "76123fcc2141"
hash_anterior = "876de875b967c87"

text_combinat = str(numero_de_bloc) + transaccions + hash_anterior + str(26977)
print(hashlib.sha256(text_combinat.encode()).hexdigest())
