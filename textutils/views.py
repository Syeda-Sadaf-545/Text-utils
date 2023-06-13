# I have created this file.

from django.http import HttpResponse
from django.shortcuts import render
#
# def index(request):
#     return HttpResponse("<h1>Hello World From Sadaf Using Python</h1>")


# Textfile read code
# def about(request):
#     return HttpResponse("About Page From Sadaf Using Python")
#
# def index(request):
#     a= open("textutils/1.txt")
#     return HttpResponse(a.read())
#-------------------------------------------------------------------
#Trying here template html file for prctc
def index(request):
    return render(request,"index.html")

#---------------------------------------------------------------------
def index0(request):

    return render(request,"index.html")


#-________________________________________________________________
def about(request):
    return render(request,"About.html")
#-________________________________________________________________
#-________________________________________________________________
def contactus(request):
    return render(request,"ContactUs.html")
#-________________________________________________________________

# def index1(request):
#     all='''
#         <h2>All pages Home<br></h2>
#         <button><a href="http://127.0.0.1:8000/rp">Remove Punctuation</a></button><br><br>
#         <button><a href="http://127.0.0.1:8000/cp">Capatilize First</a></button><br><br>
#         <button><a href="http://127.0.0.1:8000/nlr">New-line Remover</a></button><br><br>
#         <button><a href="http://127.0.0.1:8000/sr">Space-Remover</a></button><br><br>
#         <button><a href="http://127.0.0.1:8000/cc">Character-Count</a></button><br><br>
#     '''
#     return HttpResponse(all)




def analyze(request):
        dtext = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', 'off')
        fullcap = request.POST.get('fullcap', 'off')
        nlr = request.POST.get('nlr', 'off')
        ers = request.POST.get('ers', 'off')
        cc = request.POST.get('cc', 'off')
        print(dtext)
        print(removepunc)

        #Removing Punctuations
        if removepunc == 'on':
            punctuations = '''! " # $ % & ' ( ) * + , - . / : ; ? @ [ \ ] ^ _ ` { | } ~ <>'''
            analyzed = ''
            for char in dtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed }
            return render(request, 'analyze.html', params)

        #Full capatilize
        elif (fullcap=='on'):
            analyzed = ''
            for char in dtext:
                analyzed = analyzed + char.upper()
            params = {'purpose': 'Change to upper', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)

        #New Line Remover
        elif(nlr == 'on'):
            analyzed = ''
            for char in dtext:
                if char != '\n':
                    analyzed = analyzed + char
            params = {'purpose':'New-Line Remover','analyzed_text': analyzed}
            return render(request,'analyze.html', params)

        #Extra-Space-Remover
          # AND OPERATOR: True only if both exp1 and exp2 are true; otherwise, false.
        elif (ers == 'on'):
            analyzed = ''
            for index , char in enumerate(dtext):
                if not(dtext[index] == " " and dtext[index+1] == " "):

                    analyzed = analyzed + char
            params = {'purpose': 'Extra-Space-Remover', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)

        # CHARACTER-COUNTER
        elif (cc=='on'):
            analyzed = ''
            for char in dtext:
                 analyzed = "The Number of characters in your text is: " + str(len(dtext))
            params = {'purpose': 'Character-Counter', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)


#COMBINING ALL OF THEM :


# def cp(request):
#     b = '''
#     <h2>CP1 <br></h2
#      <button><a href="http://127.0.0.1:8000/">Back To Home</a></button><br><br>
#
#     '''
#     return HttpResponse(b)
#
# #GET THE TEXT
# #ANALYZ THE TEXT
#
# def nlr(request):
#     # c = '''
#     # <h2>NLR1 <br></h2
#     #  <button><a href="http://127.0.0.1:8000/">Back To Home</a></button><br><br>
#     #
#     # '''
#     # return HttpResponse(c)
#     # GET THE TEXT
#     t= request.GET.get('text','default')
#     print(t)
#     # ANALYZ THE TEXT
#     return HttpResponse('nlr')
#
#
# def sr(request):
#     d = '''
#     <h2>SR1 <br></h2
#      <button><a href="http://127.0.0.1:8000/">Back To Home</a></button><br><br>
#
#     '''
#     return HttpResponse(d)
#
# def cc(request):
#     e = '''
#     <h2>CC1 <br></h2
#      <button><a href="http://127.0.0.1:8000/">Back To Home</a></button><br><br>
#
#     '''
#     return HttpResponse(e)