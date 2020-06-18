from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from .models import MyTask

@require_http_methods(["GET"])
def upload(request):
    return render(request, 'upload.html')

@require_http_methods(["POST"])
def do_upload(request):
    uploadedFile = request.FILES['myfile'] if 'myfile' in request.FILES else False
    if uploadedFile:
        fss = FileSystemStorage()
        filename = fss.save(uploadedFile.name, uploadedFile)
        
        status = 0
        task = MyTask(filename = filename, status = status)
        task.save()
        
        return JsonResponse({'filename': filename, 'status': status})
    else:
        return JsonResponse({'filename': None, 'status': None }, status=400)

@require_http_methods(["GET"])
def get_status(request):
    return JsonResponse(list(MyTask.objects.all().order_by('id').values()), safe=False)

