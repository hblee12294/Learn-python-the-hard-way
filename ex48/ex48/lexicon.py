def convert_number(s):
	try:
		return int(s)
	except:
		return None
		
def scan(sentence):
	words = sentence.split()
	result = []
		
	directions = ['north', 'south', 'west', 'east']
	verbs = ['go', 'kill', 'eat']
	stops = ['the', 'in', 'of']
	nouns = ['bear', 'princess']

		
	for word in words:
		if word in directions:
			result.append(('direction', word))
		elif word in verbs:
			result.append(('verb', word))
		elif word in stops:
			result.append(('stop', word))
		elif word in nouns:
			result.append(('noun', word))
		elif convert_number(word):
			num = int(word)
			result.append(('number', num))
		else:
			result.append(('error', word))
		
	return result