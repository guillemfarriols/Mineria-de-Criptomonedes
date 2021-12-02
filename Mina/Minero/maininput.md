# Minador de Criptomonedes Miner

Importem hashlib, la llibreria on conté l'algoritme criptografic sha256. 

```import hashlib```

Importem time, la  llibreria de python que conta cuan comensa o acaba una funcio del codi, posteriorment la anomenem t per cridar-la mes facilment en el codi.

```import time as t```

Li diem al programa que el limit de numeros que pot probar per desxifrar el minat es 10000000000

```NONCE_LIMIT = 10000000000```

Establim el numero de zeros en aquest cas a 4, segons la dificultat donada.

```zeros = 4```

Definim 3 variable d'execucio amb def(definir) com el numero de bloc el numero de transccio i el hash anterior a la transaccio

```def mina(numero_de_bloc, transaccions, hash_anterior):```

Dintre de la funcio def utilitzarem un bucle 'for' per realitzar el que s'anomena forsa bruta per esbrinar el hash utilitzant el anteriorment establert com a limit en un rang d'intents.

```	for nonce in range(NONCE_LIMIT):```

Dintre del bucle for li direm que junti en text_base les tres variables donades (numero_de_bloc, transaccions, hash_anterior) mes el numero nonce en que sestablira a paritr de diferents intents de l'1 al 10000000000.

```text_base = str(numero_de_bloc) + transaccions + hash_anterior + str(nonce)```

Dintre del bucle for seguit del text_base encriptarem amb l'algoritme sha256 el text_base

```hash_try = hashlib.sha256(text_base.encode()).hexdigest()```

Afegim el condicional if per crear una condicio per quan trobi mitjansant forsa bruta el hash que contingui els 0 x anteriorment establert com a 4

```if hash_try.startswith('0' * zeros):```

Dintre de la condicio fem una impresio a la consola del numero nonce que ha permes trobar el hash amb els x zeros 

```print(f"Hash trobat amb Nonce: {nonce}")```

Dintre de la condicio seguit de l'anterior impressio a consola fem una altre impressio pero aquesta vegada amb el hash trobat utilitzant Formatted string literals print(f" value not formatted {value}") el que ens permet imprimir un text mes el valor de hash_try.

```print(f"El hash es:  {hash_try}")```

Return per acabar el condicional

```return```

En el bucle for si el programa proba els 10000000000 numeros i no troba el hash farem enviar al programa un misatge de error amb return -1

```return -1```

Comencem el instant temps perque comenci a comptar cuan s'executi el miner. Cal remarcar que es anomenat comensament sense c trencada ja que el codi es sol escriure en angles i no un altre idioma ja que si utiltzem caracters que no procesa el llenguatge els podria interpretar erroneament i per tant no fer funcional el programa.

```comensament=t.time()```

Ara hem de cridar a la funcio miner per que executi el que hem definit en el def anteriorment.

```miner(numero_de_bloc, transaccions, hash_anterior)```

Per acabar aturem el temps.

```temps_donat = t.time()- comensament```

I imprimim a consola el temps entre el comensament d'execucio del programa fins al final


















