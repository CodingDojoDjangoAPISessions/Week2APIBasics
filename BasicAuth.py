import base64

# Basic auth concatenates the username and password separated by a colon
# and encodes them with Base64 encoding
# The HTTP header for Basic Auth is Authorization: Basic <credentials>

def encode_to_basic(username, password):
    unencoded_string = f"{username}:{password}"
    return base64.b64encode(unencoded_string.encode('utf-8')).decode('utf-8')

def decode_basic_auth(encoded_string):
    return base64.b64decode(encoded_string).decode('utf-8').split(":")

b64 = encode_to_basic("JoeBiden", "cornpop")
print(b64)

decoded = decode_basic_auth(b64)
print(decoded)