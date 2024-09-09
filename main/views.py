from django.shortcuts import render
from django.http import HttpResponse

def show_info(request):
    return HttpResponse("Aplikasi: CutesyBoutique<br>Nama: Nisrina Kamilya<br>Kelas: PBP A")
