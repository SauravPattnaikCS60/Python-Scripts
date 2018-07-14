import json
import difflib

"""A simple to use dictionary application"""


access_dict = json.load(open('data.json', 'r'))


def return_meaning(w):
    w = w.lower()
    if w in access_dict:
        print("Meaning :")
        return access_dict[w]
    else:
        sol = difflib.get_close_matches(w, access_dict.keys(), 3)
        if len(sol) != 0:
            print('Sorry exact word not found!. Choose from the list below or enter -1 to exit')
            print(sol)
            index = int(input())
            if index == -1:
                store(w)
            else:
                print("Meaning :")
                return access_dict[sol[index]]
        else:
            return 'Word does not exist!'


def store(new_word):
    print('Sorry that word was not found.Could you provide us with a rough meaning of it')
    print('Enter Y to provide meaning or any other key to exit setup')
    choice = input()
    if choice == 'Y':
        meaning = input()
        access_dict[new_word] = meaning
        file = open('data.json', 'w')
        json.dump(access_dict, file)
        file.close()
    else:
        exit()


print("Dictionary....")
word = input("Input the word you want to know the meaning of : ")
print(return_meaning(word))