import hashlib

secret = "bgvyzdsv"

for i in range(0, 99999999):
    m = hashlib.md5()

    stuff = secret + str(i)
    m.update(stuff.encode())
    hashed = m.hexdigest()
    #if(hashed[:5] == "00000"):
    #    break
    if(hashed[:6] == "000000"):
        break

print(i)
