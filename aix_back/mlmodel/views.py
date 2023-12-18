from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .forms import PredictionForm
from .modelmanager import ModelManager
# Create your views here.

weights_filename='mlmodel/Resources/salary_predictor.pkl'
trained_model=ModelManager(weights_filename)
trained_model.load()

def index(request):
    if request.method=='POST':
        form=PredictionForm(request.POST)

        if form.is_valid():
            input_array=[]

            for data in form.base_fields.keys(): input_array.append(form.cleaned_data[data])

            if (trained_model.isActive()):
                if request.headers.get('x-requested-with')=='XMLHttpRequest':
                    prediction=int(trained_model.predict(input_array))
                    return JsonResponse({'prediction':prediction})
                else:
                    return render(request, 'ml.html')
            else: prediction=None

            return render(request, 'ml.html', context={'prediction':prediction, 'form':form})
        
    else: form=PredictionForm()
    return render(request, 'ml.html', context={'form':form})