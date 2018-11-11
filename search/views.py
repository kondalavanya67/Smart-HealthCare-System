from django.shortcuts import render, get_object_or_404

from doctor.models import Doctor

# Create your views here.



def doctor_search_view(request):
	method_dict=request.GET
	query=method_dict.get('q','kalpa')
	queryset=Doctor.objects.filter(username__icontains=query)
	context={
	   'object_list':queryset
	}
   	
	return render(request, "search.html", context=context)

