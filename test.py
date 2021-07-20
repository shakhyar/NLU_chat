from taskmanager import TaskManager


t = TaskManager()

# youtube
"""
t.get_youtube_audio("https://www.youtube.com/watch?v=svT7uKdNphU")
t.play("play")"""

# google/wikipedia api

query = "donald trump"
gr = t.google(query)
if gr == None:
    print(t.wiki(query))
else:
    print(gr)

#joke
#print(t.joke())



#print(t.memorise("what is my favourite colour", "my favourite colour is lime"))
