from django.shortcuts import render

def main_page(request):
    return render(request, "main.html", {})

def edit_page(request):
    return render(request, "edit.html", {})
