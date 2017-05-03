"""
this program decrypts messages

ktpxy gmht rdar vmsix jaht yms epfkct
vdar xm yms ctr vdtk yms nsr pmmr lttp fk a qosapt ciaqq?
lttp.
yms apt ak atqrdtrfeaiiy nitaqfkc nmrarm! <3
f rdfkh f dax a epsqd mk yms nm-ra-rm
"""


import cypher
import random

x = 5
key = ""
msg = """
    ktpxy gmht rdar vmsix jaht yms epfkct
    vdar xm yms ctr vdtk yms nsr pmmr lttp fk a qosapt ciaqq?
    lttp.
    yms apt ak atqrdtrfeaiiy nitaqfkc nmrarm! <3
    f rdfkh f dax a epsqd mk yms nm-ra-rm
    """

# for times in range(7893600):
    #for i in range(keylen):
    #    x = random.randrange(97,123)
    #    a = chr(x)
    #    while a in key:
    #        x = random.randrange(97,123)
    #        a = chr(x)
    #    key += chr(x)

key = "alext"

print(cypher.decrypt(msg, key))

# if 'nerdy joke that will make you cringe' in translated:
print(key + "\n")
# key = ""
