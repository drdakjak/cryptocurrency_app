from django.shortcuts import render


from trader.models import Pubticker

from controllers import PeriodicTask
from controllers import Tasks

from .forms.forms import TaskForm

'''
    Task
'''
def new_task(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            broker_task = PeriodicTask(symbol = form_data['symbol'], period = form_data['period'], broker=form_data['broker'])
            Tasks.tasks[broker_task.task_id] = broker_task
            context = { 
                        'tasks': Tasks.tasks,
                        'form': TaskForm(),
                    }
            return render(request, 'tradeManager/tasks_manager.html', context)

    else:
        context = { 
                    'tasks': Tasks.tasks,
                    'form': TaskForm(),
                }
        return render(request, 'tradeManager/tasks_manager.html', context)


def manager(request):
    context = {
        'tasks': Tasks.tasks,
        'form': TaskForm(),
        }
    return render(request, 'tradeManager/tasks_manager.html', context)

def trade_manager(request,task_id):
    _task = Tasks.tasks[int(task_id)]
    _trader = _task.trader

    context = { 'pubticker': _trader.pubticker,
                'orders' : _trader.orders,
                'period':_task.period,
                'tasks': Tasks.tasks,
                'task_id': task_id,
                'form': TaskForm(),
                
            }
    return render(request, 'tradeManager/manager.html', context)


def stop_threads(request, task_id):
    

    Tasks.tasks[int(task_id)].stop_threads()
    del Tasks.tasks[int(task_id)]
    
    context = {'pubticker': "kill",
                'orders' : "kill",
                'tasks': Tasks.tasks,
                'form': TaskForm(),
            }
    return render(request, 'tradeManager/tasks_manager.html', context)


# from django.core.context_processors import csrf
# from django.views.decorators.csrf import csrf_protect

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
import json
from django.utils import timezone


@csrf_exempt
def pubticker_history(request):
    response_json=serializers.serialize('json',Pubticker.objects.all().order_by('-import_date')[:20])

    if request.method == 'GET':
        if request.is_ajax()== True:
            return HttpResponse(json.dumps(response_json), content_type="application/json")
    
    

''' 
    Trade
'''

from controllers import Tasks

def buy(request,task_id):
    _task = Tasks.tasks[int(task_id)]
    _trader = _task.trader
    _trader.buy()
    context = {
        'pubticker':_trader.pubticker,
        'orders' : _trader.orders,
        'tasks': Tasks.tasks,
        'period':_task.period,
        'task_id': task_id,
        }
    return render(request, 'tradeManager/manager.html',context)
    
def sell(request,task_id):
    _task = Tasks.tasks[int(task_id)]
    _trader = _task.trader
    _trader.sell()
    context = {
        'pubticker':_trader.pubticker,
        'orders' : _trader.orders,
        'tasks': Tasks.tasks,
        'period':_task.period,
        'task_id': task_id,
    }
    
    return render(request, 'tradeManager/manager.html',context)
    
def close(request,task_id,trade_id):
    _task = Tasks.tasks[int(task_id)]
    _trader = _task.trader
    _trader.close(trade_id)
    context = {
        'pubticker':_trader.pubticker,
        'orders' : _trader.orders,
        'period':_task.period,
        'tasks': Tasks.tasks,
        'task_id': task_id,
    }
    return render(request, 'tradeManager/manager.html',context)
    
