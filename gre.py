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

    with open('static/tree.json', 'r') as fd:
        answers = json.load(fd)  # load data file into a dic

    for key in conversation:
        answers = answers[key]  # go through the tree

    if in_message is not "question" and in_message in answers:
        answers = answers[in_message]
        conversation.append(in_message)
        users[str_id] = conversation

        if type(answers) is list or type(answers) is int:
            users.pop(str_id)

            with open('static/users.json', 'w') as fu:
                json.dump(users, fu)

            with open('static/facilities.json', 'r') as ff:
                facilities = json.load(ff)

                if type(answers) is list:
                    return print_facilities("This facilities might be interesting for you:\n", [facilities[i] for i in answers])
                else:
                    return print_facilities("This facility might be interesting for you:\n", facilities[answers], False)

    out_message = answers.pop("question")

    for prop in answers:
        out_message += "\n- " + prop

    with open('static/users.json', 'w') as fu:
        json.dump(users, fu)

    return out_message


def print_facilities(out_message, facilities, many=True):

    if many is False:
        facilities = [facilities]

    for facility in facilities:
        facility.pop("id")
        out_message += "\n"
        for key, value in facility.items():
            out_message += key + ": " + value + "\n"
    return out_message


def test():
    input = "Presqu'ile"
    id = "18"

    output = process(input, id)

    print(output)


if __name__ == '__main__':
    test()
