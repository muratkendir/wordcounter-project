from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html', {'benkimim': 'Murat Kendir'})
def count(request):
	fulltext = request.GET['fulltext']
	#print(dir(fulltext))
	words = fulltext.split(' ')
	#print(dir(words))
	wordcount = len(words)
	#print(str(wordcount)+' words!!!')
	wordDictionary = {}
	for word in words:
		if word in wordDictionary:
			wordDictionary[word] += 1
		else:
			wordDictionary[word] = 1
	sortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
	print(sortedWords)
	return render(request, 'count.html', {'fulltext': fulltext, 'wordcount':wordcount, 'wordDictionary':sortedWords})

def about(request):
	return render(request, 'about.html')