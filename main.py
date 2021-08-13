import datetime #for reading present date
import time
import requests #for web requests
from plyer import notification #for getting notification on your PC


def get_todo_list(name):
    print(f"Hey {name}, Enter each list item and enter done once complete.")
    todo_list = []
    while True:
        todo_input = input("Enter to-do item")
        if todo_input != "done".lower():
            todo_list.append(todo_input)
        else:
            break
    return todo_list


# if we fetched data
def create_notification(todo_list, name):


    # repeating the loop for multiple times
    while (True):
        notification.notify(
            # title of the notification,
            title="Hey {}, here is your to-do list for {} :".format(name, datetime.date.today()),
            # the body of the notification
            message= '\n'.join([str(n) for n in todo_list]),
            # creating icon for the notification
            # we need to download a icon of ico file format
            app_icon="Paomedia-Small-N-Flat-Bell.ico",
            # the notification stays for 50sec
            timeout=50
        )
        # sleep for 4 hrs => 60*60*4 sec
        # notification repeats after every 4hrs
        time.sleep(60 * 60 * 4)

def main():
    name = input("Enter name : ")
    create_notification(todo_list=get_todo_list(name), name=name)
if __name__ == '__main__':
    main()