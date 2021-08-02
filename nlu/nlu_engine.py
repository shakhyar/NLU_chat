#from taskmanager import TaskManager
from etc.model import config # hprams


class Brain(TaskManager):
	
	def __init__(self, arg):
		super().__init__()


	def chat(self, text):
		self.inferred = []
		self.text = text.lower()

		result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
	                                             truncating='post', maxlen=max_len))
		tag = lbl_encoder.inverse_transform([np.argmax(result)])

		for i in data['intents']:
			if i['tag'] == tag:
				self.inferred.append(np.random.choice(i['responses']))
				self.inferred.append(i['context_set'])
		
		self.intent_understanding(self.text, self.inferred)

	
	def intent_understanding(text, inference_list):
		
		if '--news' == inference_list[1]:
			return self.news(config.headlines)

		elif '--note' == inference_list[1]:
		# for such commands where we need 2 inputs from the user, we will use 2 GET requests
		# first we will need a client handler script on the client
		# then on server this function will return another flag, that will let the
		# user to pause for a second and give the second input, lets say what to write
		# then the text will be notted and stored inside the client.	
			return 'c$get_note'

		elif '--info' == inference_list[1]:
			if 'who' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('who')+4:]
			elif 'whom' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('whom')+4:]
			elif 'what' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('what')+4:]
			elif 'which' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('which')+4:]
			elif 'how' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('how')+4:]
			elif 'where' in inference_list[0]:
				gr = inference_list[0][inference_list[0].index('where')+4:]

			try:
				g_output = self.google(gr)
				if not g_output:
					return self.wiki(gr)
				else:
					return g_output
			# actual server output that the client will get:
			#return 'c$get_info'

		elif '--youtube' == inference_list[1]:
			# if client site download, uncomment following line:
			#return f'c$get_youtube%{text}'
			# and play it on a different thread or multiprocess the audio playback in client
			self.parse_youtube_query(text)

		elif '--memorize' == inference_list[1]:
			pass # need to work more on this


		elif '--weather' == inference_list[1]:
			# note for sample we are using new york as city, this will be more dynamic in future versions
			weather_description, current_temperature, current_humidity = self.weather(config.weather_api_key, 'new york')
			
			if 'humidity' in text or if 'humid' in text:
				return current_humidity

			elif 'weather' in text or if 'cloud' in text or if 'rain' in text or if 'windy' in text or if 'sunnny' text:
				return weather_description

			elif 'temperature' in text:
				return current_temperature

		elif '--joke' == inference_list[1]:
			return self.joke()

		elif '--unsure' == inference_list[1]:
			return inference_list[0]

"""
recent logs:

Start messaging with the bot (type quit to stop)!

User: 
please update me with recent news
ChatBot:Do you want to listen to some recent news?
intent asked for:  --news 

User: 
it seems rainy can you tell me the weather
ChatBot:
intent asked for:  --weather 

User: 
can you write this down
ChatBot:
intent asked for:  --note 

User: 
i am bored can you tell me a joke
ChatBot:
intent asked for:  --joke 

User: 
do you know who is donald trump
ChatBot:
intent asked for:  --info 

User: 
did you know that you dont have a gender
ChatBot:You can call me Walle.
intent asked for:   

User: 
great
ChatBot:super
intent asked for:   

User: 
lol
ChatBot:That's great!
intent asked for:   

User: 
anyways see you again
ChatBot:Goodbye!
intent asked for:   

User: 
quit
"""

#print(config.max_headlines)
