from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback,Batch,Organization
from django.forms.models import model_to_dict


@csrf_exempt
def feedback_form(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            batch=Batch.objects.get(id=data['batch'])
            feedback=Feedback.objects.create(
                kbefore=data['kbefore'],
                kafter=data['kafter'],
                communication=data['communication'],
                content=data['content'],
                handson=data['handson'],
                interaction=data['interaction'],
                speed=data['speed'],
                rating=data['rating'],
                feedback=data['feedback'],
                suggestions=data['suggestions'],
                batch=batch,
            )
            feedback.save()
            return JsonResponse({'msg':"submitted"},status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error':"Invalid json"},status=400)
    return JsonResponse({'error':'Invalid Verb'},status=400)

def check_form_status(request,batch_id):
    try:
        batch=Batch.objects.get(id=batch_id)
        if batch.active:
            return JsonResponse({'active':True})
        return JsonResponse({'active':False})
    except Batch.DoesNotExist:
        return JsonResponse({'active':False})


def get_dashboard(request):
    if request.method!="GET":
        return JsonResponse({'error':"Invalid verb"},status=400)
    bactch_id=request.GET.get('batch')
    if bactch_id is None:
        return JsonResponse({'error':"Batch number is required"},status=400)  

    try:
        bactch_id=int(bactch_id)
        batch=Batch.objects.get(id=bactch_id)
    except Batch.DoesNotExist:
        return JsonResponse({'error':"Batch id not found"},status=400)
    except Exception:
        return JsonResponse({'error':"Invalid data provided"},status=400)
    oraganization=Organization.objects.get(id=batch.organization.id)
    feedbacks=Feedback.objects.filter(batch=batch)

    res={
        'organization_name':oraganization.name,
        'batch_name':batch.name,
        'batch_id':batch.id,
        'total_students':batch.total_students,
        'form_active':batch.active,
        'feedbacks':[]
    }

    for feedback in feedbacks:
        res['feedbacks'].append(model_to_dict(feedback))
    

    return JsonResponse(res)