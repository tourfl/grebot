users = {"18": "test"}


def process(in_message, user_id):
    out_message = in_message

    try:
        out_message = users[str(user_id)]
    except KeyError:
        out_message = "not started any discussion"

    return out_message


def test():
    input = "RU"
    id = 46

    output = process(input, id)

    print(output)

if __name__ == '__main__':
    test()
