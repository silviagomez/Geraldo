phone = pyb.Pin('X6', pyb.Pin.OUT_PP)

from pyb import udelay
import ure
import ujson

musicTab = {
'Cz' : 0,
'C#' : 1,
'Db' : 1,
'Dz' : 2,
'D#' : 3,
'Eb' : 3,
'Ez' : 4,
'Fz' : 5,
'F#' : 6,
'Gb' : 6,
'Gz' : 7,
'G#' : 8,
'Ab' : 8,
'Az' : 9,
'A#' : 10,
'Bb' : 10,
'Bz' : 11,
'Cb' :11,
}

sharpFlatOrder = 'BEADGCF'

scaleListing = {
'C' : ['z', sharpFlatOrder[:]],
'G' : ['#', sharpFlatOrder[-1]],
'D' : ['#', sharpFlatOrder[-2:]],
'A' : ['#', sharpFlatOrder[-3:]],
'E' : ['#', sharpFlatOrder[-4:]],
'B' : ['#', sharpFlatOrder[-5:]],
'F#' : ['#', sharpFlatOrder[-6:]],
'C#' : ['#', sharpFlatOrder[:]],
'F' : ['b', sharpFlatOrder[0]],
'Bb' : ['b', sharpFlatOrder[0:2]],
'Eb' : ['b', sharpFlatOrder[0:3]],
'Ab' : ['b', sharpFlatOrder[0:4]],
'Db' : ['b', sharpFlatOrder[0:5]],
'Gb' : ['b', sharpFlatOrder[0:6]],
'Cb' : ['b', sharpFlatOrder[:]],
}

styleTab = {
'~' : 'slurred',
'!' : 'accented',
'.' : 'staccato',
}

def playSlurred(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	for duration in range(0, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/Hz))
		phone.low()
		udelay(int(1000000/Hz))
	print('Done')


def playNormal(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	starter = int((Hz + 2 ** 1/12) * length/3)
	for duration in range(0, starter, 2):
		#print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
		phone.low()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
	for duration in range(starter, int(Hz * length), 2):
		#print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/Hz))
		phone.low()
		udelay(int(1000000/Hz))
	print('Finished playing Normal:',starter, int(Hz * length), Hz, int(1000000/Hz))
	print('Done')


def playStaccato(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	starter = int((Hz + 2 ** 1/12) * length/4)
	for duration in range(0, starter, 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
		phone.low()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
	for duration in range(starter, int(Hz * length/2), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/Hz))
		phone.low()
		udelay(int(1000000/Hz))
	udelay(int(length/2 * 1000000))
	print('Done')


def playAccent(note, Hz, length):
	print(note, Hz, int(Hz * length))
	starter = int((Hz + 2 ** 1/12) * length/.5,  .125/2.5)
	for duration in range(0, starter, 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
		phone.low()
		udelay(int(1000000/(Hz + 2 ** 1/12)))
	for duration in range(starter, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1000000/Hz))
		phone.low()
		udelay(int(1000000/Hz))
	print('Done')

playNoteStyle = {
'slurred' : playSlurred,
'normal'  : playNormal,
'staccato'  : playStaccato,
'accented' : playAccent
}


def splitString(pattern, string):
	match = ure.search(pattern, string)
	match = match.group(0) if match else ['']
	counterStr = ''
	returnList = []
	counter, matching = 0, False
	print(pattern, string, match)
	for charStr in string:
		if charStr == match[0] and not matching:
			matching = True
			returnList.insert(len(returnList), counterStr)
			counterStr = charStr
			counter = 1
			if counter == len(match):
				counter = 0
				returnList.insert(len(returnList), counterStr)
				counterStr = ''
				matching = False
		elif charStr == match[counter] and matching:
			counterStr += charStr
			counter += 1
			if counter == len(match):
				counter = 0
				returnList.insert(len(returnList), counterStr)
				counterStr = ''
				matching = False
		else:
			matching = False
			counter = 0
			counterStr += charStr
	returnList.insert(len(returnList), counterStr)
	print('Finished splitString:', match, returnList, counterStr)
	return returnList


def playNote(note, octave, length, style):
	noteVal = musicTab[note]
	Hz = 440 * 2 ** ((-9 + noteVal)/12 - (-octave + 4))
	playNoteStyle[style](note, Hz, length)
	

def handleNoteKey(note, key):
	getList = scaleListing[key]
	print(note, getList)
	return note + getList[0] if note in getList[1] else note + 'z'


def handleSuffix(note, key, suffix, bpm, timesig):
	tonal, length = handleNoteKey(note, key), 60/bpm
	if suffix:
		if suffix[0] in 'zb#':
			tonal = note + suffix[0]
			if len(suffix) > 1:
				length = 60 * (timesig / int(suffix[1:])) / bpm
		else:
			length = 60 * (timesig / int(suffix[:])) / bpm
	return tonal, length


def handlePrefix(prefixStr, baseOctave):
	prefixPattern = '[-0-9]+'
	prefix = splitString(prefixPattern, prefixStr)
	if len(prefix) > 1:
		return styleTab[prefix[0]] if prefix[0] else 'normal', int(prefix[1])
	else:
		return styleTab[prefix[0]] if prefix[0] else 'normal', baseOctave


def handleSplitCharSet(listset, key, baseOctave, bpm, timesig):
	print(listset)
	prefix, note, suffix = listset[0], listset[1], listset[2]
	style, octave = handlePrefix(prefix, baseOctave)
	note, length = handleSuffix(note, key, suffix, bpm, timesig)
	print(note, octave, length, style)
	if note == 'Rz':
		udelay(int(length * 1000000))
	else:
		playNote(note, octave, length, style)
	print('Terminating...')


def splitCharSet(string, key, baseOctave, bpm, timesig):
	print(string)
	pattern = '[A-GR]'
	listset = splitString(pattern, string)
	handleSplitCharSet(listset, key, baseOctave, bpm, timesig)


def removeWhiteSpace(s):
	newstr = ''
	for charStr in s:
		if not ure.search('\s', charStr):
			newstr += charStr
	return newstr

def startUp(text):
	text = removeWhiteSpace(text)
	pattern = chr(123) + '.*?' + chr(125)
	splitTab = splitString(pattern, text)
	print(splitTab)
	tab = ujson.loads(splitTab[1])
	baseOctave, key, bpm, timesig = tab.get('base_octave') if tab.get('base_octave') else 4, tab.get('key') or 'C', tab.get('bpm') or 120, tab.get('time_signature') or 4  
	groupStr = ''
	for charStr in splitTab[2]:
#		print('Going through:', charStr)
		if charStr == '/':
			if groupStr:
				print('Starting up:', groupStr, baseOctave, key, bpm, timesig)
				splitCharSet(groupStr, key, baseOctave, bpm, timesig)
			groupStr = ''
		else:
			groupStr += charStr

def playFormat(name):
	with open(name + '.pyMusic', 'r') as text:
		startUp(text.read())


playFormat('Test')