from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def seller(name):
    return name[-1]=='y'

def search(name):
    search_queue=deque()
    search_queue+=[name]

    searched_list=set()
    while search_queue:
        person=search_queue.popleft()
        if(person in searched_list):
            continue
        if(seller(person)):
            print(person+': seller found')
            return True
        else:
            searched_list.add(person)
        search_queue+=graph[person]
    return False

print(search("you"))