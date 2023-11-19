import base64

# # Base64 encoded string
# encoded_str = "QWxhZGRpbjpvcGVuIHNlc2FtZQ=="

# # Decoding the Base64 string
# decoded_str = base64.b64decode(encoded_str).decode('utf-8')
# decoded_str
#
# # Original string
# original_str = "Aladdin:open sesame"
#
# # Encoding the string to Base64
# encoded_str = base64.b64encode(original_str.encode('utf-8')).decode('utf-8')
# encoded_str

def encode_to_basic(username, password):
    unencoded_string = f"{username}:{password}"
    return base64.b64encode(unencoded_string.encode('utf-8')).decode('utf-8')

def decode_basic_auth(encoded_string):
    return base64.b64decode(encoded_string).decode('utf-8')

b64 = encode_to_basic("Aladdin", "open sesame")
print(b64)

decoded = decode_basic_auth(b64)
print(decoded)