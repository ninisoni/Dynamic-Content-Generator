from django.shortcuts import render
from django.http import HttpResponse
import random

SENTENCE_TEMPLATES = [
    "The {word} is amazing!",
    "I love {word}.",
    "Have you ever seen such a beautiful {word}?",
    "{word} is essential for life.",
    "I can't imagine living without {word}."
]
def generate_random(word):
    temp = random.choice(SENTENCE_TEMPLATES)
    sentence = temp.format(word=word)
    return sentence

def get_word(request):
    return render(request, 'get_word/word.html')

def generate_content(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        generate_content = generate_random(word)
        return render(request,'get_word/content.html', {'content': generate_content})
    else:
        return {'error' : "something went wrong"}

