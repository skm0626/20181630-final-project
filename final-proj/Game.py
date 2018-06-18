from picknumber import Number

skm = Number()


def guess(d):
	try:
		guess = int(d.get('guess', [''])[0])
	except:
		return {'code': 'error', 'msg': 'Wrong Guess'}

	answer = skm.guess(guess)
	trials = skm.getGuessCount()

	return {'code':'success','guess':guess,'answer':answer,'trials':trials}

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'Count Not Given'}

	skm.newGame(count)
	return {'code': 'success'}
