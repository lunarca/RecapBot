import argparse
import requests
import os
import struct


def parse_args():
    parser = argparse.ArgumentParser(description='Choose who to give the recap')
    parser.add_argument('--webhook', help='Discord webhook to send the results to')
    parser.add_argument("users", nargs="+", help="Users to choose from")

    return parser.parse_args()

def choose_recap_user(users):
    # Generate random index
    # Use os.urandom for true random values
    random_byte = os.urandom(1)

    # Use struct to decode the value into an int
    byte_as_int = struct.unpack('B', random_byte)[0]
    index = byte_as_int % len(users)
    return users[index]


def main():
    args = parse_args()

    webhook = args.webhook
    users = args.users

    requests.post(webhook, data={"content": "Choosing who to do the recap"})

    user_to_recap = choose_recap_user(users)

    recap_message = "Looks like " + user_to_recap + " is doing the recap this week!"
    requests.post(webhook, data={"content": recap_message})

    


if __name__ == "__main__":
    main()