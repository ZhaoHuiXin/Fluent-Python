
from unicodedata import name
latin_set = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(latin_set)