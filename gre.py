
def process(in_message, user_id):
    out_message = user_id

    return out_message


def test():
    input = "RU"
    id = "1A"

    output = process(input, id)

    print(output)

if __name__ == '__main__':
    test()
