from asyncore import poll
from django.shortcuts import render
from .models import Agentname, AnnouncedLgaResults,AnnouncedPuResults,AnnouncedStateResults,AnnouncedWardResults, New_Polling_unit
from .forms import AddPolls, NewPollingUnit
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
def polling_results(request, unique_id):
    results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unique_id)
    context = {'results':results}
    return render (request, 'election_results/index.html', context)

   
def add_poll_results(request):
    global poll_score,poll
    poll = ''
    poll_score= ''
    form = AddPolls()
    if request.method == 'POST':
        form = AddPolls(request.POST)
        if form.is_valid():
            polling_unit_uniqueid = form.cleaned_data['polling_unit_uniqueid']
            form.save(commit=False)
            
            poll = AnnouncedPuResults.objects.all().filter(polling_unit_uniqueid=polling_unit_uniqueid)
            poll_score = poll.aggregate(Sum('party_score'))
            print(poll_score)
            poll_score = poll_score.get("party_score__sum")
            print(poll_score)
            
                 
        else:
            form = AddPolls()

        
    return render (request,'election_results/poll.html',{'form':form , 'poll_score':poll_score,'poll':poll})

def new_polling_unit(request):
    form = NewPollingUnit()
    if request.method == 'POST':
        form = NewPollingUnit(request.POST)
        if form.is_valid():
            f= form.save()
            f.Polling_unit = form.cleaned_data['polling_unit']
            f.party = form.cleaned_data['party']
            f.party_score = form.cleaned_data['party_score']
            
            form.save()

            messages.success(request, f'A new polling unit has been !')
            
    else: 
        form = NewPollingUnit()

    return render(request, 'election_results/new_poll.html',{'form':form})
def display(request):
    results =  New_Polling_unit.objects.all()
    context = {'results':results}

    return render (request, 'election_results/display.html',context)
            