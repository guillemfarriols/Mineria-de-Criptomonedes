# Minador de Criptomonedes Miner

Importem hashlib, la llibreria on conté l'algoritme criptografic sha256. 

```import hashlib```

Importem time, la  llibreria de python que conta cuan comensa o acaba una funcio del codi, posteriorment la anomenem t per cridar-la mes facilment en el codi.

```import time as t```

Comencem el instant temps perque comenci a comptar fins que acabi de llegir les properes linies de codi i arribi fins la seva altre variable que aturi aquest. Cal remarcar que es anomenat comensament sense c trencada ja que el codi es sol escriure en angles i no un altre idioma ja que si utiltzem caracters que no procesa el llenguatge els podria interpretar erroneament.

```comensament=t.time()```

Li diem al programa que el limit de numeros que pot probar per desxifrar el minat es 10000000000

```NONCE_LIMIT = 10000000000```

Establim el numero de zeros en aquest cas a 4, segons la dificultat donada.

```zeros = 4```

Definim 3 variable d'execucio amb def(definir) com el numero de bloc el numero de transccio i el hash anterior a la transaccio

```def mina(numero_de_bloc, transaccions, hash_anterior):```

Dintre de la funcio def utilitzarem un bucle 'for' per realitzar el que s'anomena forsa bruta per esbrinar el hash utilitzant el anteriorment establert com a limit en un rang d'intents.

```	for nonce in range(NONCE_LIMIT):```

Dintre del bucle for li direm que junti les tres variables donades (numero_de_bloc, transaccions, hash_anterior) mes el numero nonce que sestablira a paritr de diferents intents de l'1 al 10000000000.

```text_base = str(numero_de_bloc) + transaccions + hash_anterior + str(nonce)```

Dintre del bucle for seguit del text_base encriptarem amb l'algoritme sha256 el text_base

```hash_try = hashlib.sha256(text_base.encode()).hexdigest()```

Afegim el condicional if per crear una condicio per quan trobi mitjansant forsa bruta el hash que contingui els 0 x anteriorment establert com a 4

```hash_try = hashlib.sha256(text_base.encode()).hexdigest()```

Dintre de la condicio fem una impresio a la consola del numero nonce que ha permes trobar el hash amb els x zeros 

```print(f"Hash trobat amb Nonce: {nonce}")```

D











