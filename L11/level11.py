#!/usr/bin/python

import base64

def xor_encrypt(data):
    key = 'MYKEY';
    result = ''
    for i in range(0, len(data)):
        result += chr(ord(data[i]) ^ ord(key[i % len(key)]))

    return result


initial_str = "{\"showpassword\":\"no\",\"bgcolor\":\"#ffffff\"}"
print "Initial string: ", initial_str

# encoded cookie data is "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxZZaAw%3D"
# %3D is '=', URL-encoded
encoded = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxZZaAw=";
decoded = base64.b64decode(encoded);

chars = [ord(c) for c in decoded]
print chars

print "=== test enc/dec/ ==="
print xor_encrypt(initial_str)
print [ord(c) for c in xor_encrypt(initial_str)]
print xor_encrypt(xor_encrypt(initial_str))
print "======"

# A XOR K = B ==> B XOR A = K
key = [ chr(ord(initial_str[i]) ^ ord(decoded[i])) for i in range(0, len(initial_str))]
print key 

# Found key: qw8J
