from collections import deque
graph ={}
graph['Dom'] = ['Aslihan','Marco','Dennis','Qasim']
graph['Qasim'] = ['Skuuu','Ozzy']
graph['Skuuu'] = []
graph['Ozzy'] = []
graph['Aslihan'] = ['Bastet']
graph['Bastet'] = []
graph['Marco'] = ['Dennis','Caren']
graph['Dennis'] = []
graph['Caren']= []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)
    return "No Mango sellers"


def person_is_seller(name):
    return name[-1] == 'm'

print(search("Dom"))