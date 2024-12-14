from django.shortcuts import render, redirect
from .forms import ProfesorForm
from django.contrib import messages

def registrar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            profesor = form.save(commit=False)
            profesor.contraseña = form.cleaned_data['contraseña']  # Aquí puedes aplicar encriptación si es necesario
            profesor.save()
            messages.success(request, '¡Registro exitoso!')
            return redirect('registro_exitoso')  # Redirige a una página de éxito
    else:
        form = ProfesorForm()
    return render(request, 'registro/registro_profesor.html', {'form': form})
