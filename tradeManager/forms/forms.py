from django import forms
from decimal import Decimal

class TaskForm(forms.Form):
    period = forms.DecimalField(label='Perioda [s]', min_value=1)
    symbols = (
        ("btcusd","BTC/USD"),
        )
    symbol = forms.ChoiceField(choices=symbols)
    
    brokers = (
         ("bitfinex","Bitfinex"),
         )                          
    broker = forms.ChoiceField(choices=brokers)