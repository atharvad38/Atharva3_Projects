from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request,'home.html')

# def analyze(request):
#     djtext = request.POST.get('text','default')
#     removepunc = request.POST.get('removepunc','off')
#     count = request.POST.get('count','off')
#     upper = request.POST.get('upper','off')
#     spaces = request.POST.get('extraspaces','off')
#     capital = request.POST.get('capital','off')
#     word = request.POST.get('wordcount','off')
#
#     if removepunc == "on":
#             analyzedtext=""
#             punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#             for i in djtext:
#                 if i not in punctuations:
#                     analyzedtext= analyzedtext+i
#             params = {'purpose':'Removed Punctuations','analyzed_text':analyzedtext}
#             djtext=analyzedtext
#             #return render(request,'analyze.html',params)
#
#     if count=="on":
#
#         count=0
#         for i in djtext:
#             if i!=" ":
#                 count+=1
#         params = {'purpose':'counting characters','analyzed_text':'No of characters:'+str(count)}
#         return render(request,'analyze.html',params)
#
#     elif upper=="on":
#         analyzedtext=""
#         for i in djtext:
#             analyzedtext = analyzedtext + i.upper()
#         params = {'purpose':'Converted to UpperCase','analyzed_text':analyzedtext}
#         return render(request,'analyze.html',params)
#
#     elif spaces=='on':
#         analyzedtext=""
#         for index,char in enumerate(djtext):
#             if not (djtext[index] == " " and djtext[index+1] == " "):
#                 analyzedtext = analyzedtext+char
#         params = {'purpose':'Removed Extra Spaces','analyzed_text':analyzedtext}
#         return render(request,'analyze.html',params)
#
#     elif capital=="on":
#
#
#         params = {'purpose':'Text Capitalized','analyzed_text':djtext.capitalize()}
#         return render(request,'analyze.html',params)
#
#     elif word=='on':
#
#         words = djtext.split(" ")
#         wcount = len(words)
#         params = {'purpose':'Number of Words','analyzed_text':'No of words '+str(wcount)}
#         return render(request,'analyze.html',params)
#



def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    count = request.POST.get('count', 'off')
    upper = request.POST.get('upper', 'off')
    spaces = request.POST.get('extraspaces', 'off')
    capital = request.POST.get('capital', 'off')
    word = request.POST.get('wordcount', 'off')

    analyzed_text = djtext  # Initialize analyzed text with original text
    results = {}  # Initialize dictionary to store analysis results

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed_text = ''.join(char for char in analyzed_text if char not in punctuations)
        results['Removed Punctuations'] = analyzed_text

    if count == "on":
        count_result = len(analyzed_text)
        results['Count of Characters'] = count_result

    if upper == "on":
        analyzed_text_upper = analyzed_text.upper()
        results['Converted to Uppercase'] = analyzed_text_upper

    if spaces == 'on':
        analyzed_text_spaces = ' '.join(analyzed_text.split())
        results['Removed Extra Spaces'] = analyzed_text_spaces

    if capital == "on":
        analyzed_text_capital = analyzed_text.capitalize()
        results['Text Capitalized'] = analyzed_text_capital

    if word == 'on':
        words = analyzed_text.split()
        word_count = len(words)
        results['Number of Words'] = word_count

    params = {'purpose': 'Text Analysis', 'results': results, 'original_text': djtext}
    return render(request, 'analyze.html', params)





