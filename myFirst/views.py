from tkinter import Y
from django.http import HttpResponse

def Vision(request):
    return HttpResponse("<h3>The College of Computer Studies shall be a Center of Excellence in Information Technology education<h3/>")

def Mission(request):
    return HttpResponse("<h3>The College of Computer Studies shall produce technically competent Information Technology professionals adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence.<h3/>")

def Objective(request):
    return HttpResponse("<h3>After Graduation, alumni of MSEUF-CCS program shall: 1. Be employed and demontrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions; 2. Embark in lifelong learning or research  to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market;and 3. Exibit leadership and teamwork, and commitment to their respective local or global organization.<h3>")
