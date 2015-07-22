'''
/Intro/

Congratulations! This is George Ung. You are reading the program that tells your PyBoard how to sing (with a passive buzzer)!
This is set up to be on pin X6. On the bottom, you call the function "playFormat" with the name 
of the ".pyMusic" file (but you have to omit the ".pyMusic" part since it automatically
puts is on the end).


/How does the program work/

The program first opens a ".pyMusic" file and remove all the whitespace characters (like tabs, spacebars, line feeds).
It then finds a JSON table using "Regular Expressions" and set defaults for this program to output the score.
After that, it reads through the score and reads each notes in-between two forward slashes.
The note contains information on how to play the note and must be splitted up into individual parts.
Each part tells important information on how to play and then runs the playing function.

The pitches you hear are based off of how frequent you hear 1 pitch. The A440 (4th octave A) is 440 Hz meaning that
the pitch you hear is actually played 440 times a second. Each half-step adds or subtracts 2 ^ (1/12) to a multiplier
(A440 having 2 ^ (0/12) or simply 1) and multiplys it by 440 to get how fast does the buzzer fluctuate.


/How to score/

There are two main parts of the scoring sheet:
	- The JSON table
	- The notes

The JSON table basically indicates the 4 basic settings of PyMusic:
	-	"key" takes a Major scale (indicated in "scaleListing") and defaults to the key of "C". 
	This is used for automatically setting the notes to a flat, natural, or sharp.
	-	"bpm" takes a number (never tested with a float) which stands for the "beats per minute." Defaults to 120 BPM.
	-	"time_signature" takes pref. an int to decide which note is 1 beat (i.e. set it to 4 to make quarter notes equal a beat).
	-	"base_octave" takes an int to automatically set notes to a certain octave. Defaults to 4.

After that comes the actual notes. Notes come in a look like this:
/C/

or this:

/E#/

or even this:

/!6Fz4/


Let's break this down to understand each part of a note.
A note is first seperated into three parts:
-	Prefix
-	Note
-	Suffix

The Prefix contains:
-	How the note is played
-	What octave the note is played in.

Omitting the symbol to how the note is played defaults to playing it normally. You can find a list in "styleTab" in this code.
Omitted the octave defaults to the "base_octave" set earlier in the code.

The Note contains:
-	The literal letter of the note.

This indicates what note should be played. You can replace the note with a "R" to rest instead. "R" supports length of a note.

The Suffix contains:
-	Flat, Natural, Sharp accidentals
-	How long the note is played for

Flat, Natural, Sharps override the default accidental for the note. Flats are indicated as "b", Naturals are indicated as "z", and Sharps are indicated as "#".
How long the note is played is a number (supports float) that defaults to 1 beat. The number corresponds to the name of the note
(i.e. 4 is a quarter note, 1 is a whole note, 2 is a half note, 32 is a thirty-second note, 3 is a dotted quarter note)


(Note: Commenting out code uses parentheses. If I wanted to make a comment in the middle of the score (or even a note), you can simply do:
(This code won't read this. Please don't put parentheses in parentheses)
)

/Outro/

I know this isn't much of a tutorial and it's kinda wordy and probably not the most ideal way to understand how the code works or how to score,
but if you just try working stuff out in your own time, you may suprise yourself with what you could make.
'''


phone = pyb.Pin('X6', pyb.Pin.OUT_PP)

from pyb import udelay
import ure
import ujson
import math

musicTab = {
'B#' : 0,
'Cz' : 0,
'C#' : 1,
'Db' : 1,
'Dz' : 2,
'D#' : 3,
'Eb' : 3,
'Ez' : 4,
'Fb': 4,
'E#' : 5,
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
'w' : 'trill',
'^' : 'tremelo'
}

def playSlurred(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	for duration in range(0, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/Hz))
		phone.low()
		udelay(int(1e6/Hz))
	print('Done')


def playTremelo(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	for duration in range(0, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		if duration % 25:
			phone.high()
			udelay(int(1e6/Hz))
			phone.low()
			udelay(int(1e6/Hz))
		else:
			udelay(int(1e6/Hz * 2))
	print('Done')


def playTrill(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	A = False
	baseLength = int(Hz * length)
	switchAmounts = baseLength // (Hz // 10)
	oddAmounts = math.ceil(switchAmounts / 2)
	evenAmounts = switchAmounts - oddAmounts
	finalLength = baseLength + (2 ** (1/12) * evenAmounts * (Hz//10))
	
	for duration in range(0, int(finalLength), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		A = not A if (duration % (Hz // 10)) == 0 else A
		phone.high()
		udelay(int(1e6/(Hz if A else (Hz + 2 ** (1/12)))))
		phone.low()
		udelay(int(1e6/(Hz if A else (Hz + 2 ** (1/12)))))
	print('Done')


def playNormal(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	highHz = (Hz + 2 ** 1/12)
	starter = int(highHz * length/4)
	for duration in range(0, starter, 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/highHz))
		phone.low()
		udelay(int(1e6/highHz))
	for duration in range(starter, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/Hz))
		phone.low()
		udelay(int(1e6/Hz))
	print('Done')


def playStaccato(note, Hz, length):
#	print(note, Hz, int(Hz * length))
	highHz = (Hz + 2 ** 1/12)
	starter = int(highHz * length/4)
	for duration in range(0, starter, 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/highHz))
		phone.low()
		udelay(int(1e6/highHz))
	for duration in range(starter, int(Hz * length/2), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/Hz))
		phone.low()
		udelay(int(1e6/Hz))
	udelay(int(length/2 * 1e6))
	print('Done')


def playAccent(note, Hz, length):
	print(note, Hz, int(Hz * length))
	highHz = (Hz + 2 ** 6/12)
	starter = int(highHz * length/3)
	for duration in range(0, starter, 2):
		if duration % (Hz // (50/1.25)):
	#		print('Running note:', note + ':', 1/Hz, duration, '/', starter)
			phone.high()
			udelay(int(1e6/highHz))
			phone.low()
			udelay(int(1e6/highHz))
		else:
			udelay(int(1e6/highHz * 2))
#	udelay(int(1e6 * (length/3 - length/1.25)))

	pauseLength = int((length/3 - length/1.25) * Hz)

	for duration in range(starter, int(Hz * length), 2):
#		print('Running note:', note + ':', 1/Hz, duration, '/', int(Hz * length))
		phone.high()
		udelay(int(1e6/Hz))
		phone.low()
		udelay(int(1e6/Hz))
	print('Done')

playNoteStyle = {
'slurred' : playSlurred,
'normal'  : playNormal,
'staccato'  : playStaccato,
'accented' : playAccent,
'trill' : playTrill,
'tremelo' : playTremelo
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
				length = 60 * (timesig / float(suffix[1:])) / bpm
		else:
			length = 60 * (timesig / float(suffix[:])) / bpm
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
		udelay(int(length * 1e6))
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
	ignore = 0
	for charStr in splitTab[2]:
#		print('Going through:', charStr)
		if charStr == '/' and not ignore:
			if groupStr:
				print('Starting up:', groupStr, baseOctave, key, bpm, timesig)
				splitCharSet(groupStr, key, baseOctave, bpm, timesig)
			groupStr = ''
		elif charStr == '(':
			ignore += 1
		elif charStr == ')':
			ignore -= 1
		elif not ignore:
			groupStr += charStr

def playFormat(name):
	with open(name + '.pyMusic', 'r') as text:
		startUp(text.read())


playFormat('Test')