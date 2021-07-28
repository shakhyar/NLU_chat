from taskmanager import TaskManager
#from playsound import playsound

t = TaskManager()

# youtube : Passed
"""
t.get_youtube_audio("https://www.youtube.com/watch?v=svT7uKdNphU")
t.play("play")"""



# google/wikipedia api : Passed
"""
query = "donald trump"
gr = t.google(query)
if gr == None:
    print(t.wiki(query))
else:
    print(gr)
    """


#joke: Passed
#print(t.joke())



#print(t.memorise("what is my favourite colour", "my favourite colour is lime"))

"""
desc, temp, humid = t.weather('f317f1f507f2d9f0a8aa1316d86507b8', 'delhi')
print(f"Desc: {desc}, temp: {temp}, humid: {humid}")
"""


#print(t.parse_youtube_query('Unstopable tony junior'))
#playsound('music/Tony Junior NIGHT  MOVES ft  Lasse Meling - Unstoppable (Lyric Video).mp4')

print(t.news(2))