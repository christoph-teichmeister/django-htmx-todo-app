def convert_byte_body_to_dict(request_body_as_byte) -> dict:
    decoded_body = request_body_as_byte.decode('utf-8')
    decoded_body_list = decoded_body.replace('=', '&').split('&')

    body = {}
    while len(decoded_body_list) != 0:
        val = decoded_body_list.pop()
        key = decoded_body_list.pop()
        body[key] = val

    return body
