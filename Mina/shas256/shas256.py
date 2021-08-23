# En "ABC" pots canviar de paraula en comptes d'ABC pots introduir Hola entre les comes "".
from hashlib import sha256
print(sha256("ABC".encode("ascii")).hexdigest())
