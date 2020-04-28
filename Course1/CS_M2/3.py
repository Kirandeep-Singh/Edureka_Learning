import base64

A="Kd123"

B=base64.b64encode(A.encode())

print (base64.b64decode(B))