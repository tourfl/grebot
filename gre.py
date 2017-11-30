import json


def process(in_message, str_id):
    out_message = in_message

    with open('static/users.json', 'r') as fu:
        users = json.load(fu)
    try:  # if a conversation already exists
        conversation = users[str_id]
    except KeyError:  # starting a new conversation
        conversation = []
        users[str_id] = conversation

    with open('static/data.json', 'r') as fd:
        answers = json.load(fd)  # load data file into a dic

    for key in conversation:
        answers = answers[key]  # go through the tree

    try:
        out_message = json.dumps(list(answers[in_message].keys()))
        conversation.append(in_message)
        users[str_id] = conversation
    except KeyError:
        out_message = "this is not a good answer"
    except AttributeError:
        out_message = answers[in_message]
        users.pop(str_id)

    with open('static/users.json', 'w') as fu:
        json.dump(users, fu)

    return out_message


def test():
    input = "midi"
    id = "18"

    output = process(input, id)

    print(output)


if __name__ == '__main__':
    test()
