import os
from django.http import JsonResponse, FileResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from pytube import YouTube
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def descargarVideo(request):
    try:
        link = request.data.get('link')
        video = YouTube(link)
        video.streams.get_by_resolution("360p").download()
        return JsonResponse({"message": "Video descargado con éxito"}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@api_view(['POST'])
def videoToMp3(request):
    directorio_actual = os.getcwd()
    try:
        
        mp4_file = "Let Me Go.mp4"

        mp3_file = "Let Me Go.mp3"

        videoClip = VideoFileClip(mp4_file)
        audioClip = videoClip.audio
        audioClip.write_audiofile(mp3_file)
        audioClip.close()
        videoClip.close()

        return JsonResponse({"message": f"La conversión de '{mp4_file}' a '{mp3_file}' fue exitosa."}, status=201)
    except Exception as e:
        return JsonResponse({"message": f"Error durante la conversión: {str(e)}"}, status=500)

@api_view(['POST'])
def videoToMp3V2(request):
    directorio_actual = os.getcwd()
    try:
        link = request.data.get('link')
        video = YouTube(link)
        nombre = video.title
        directorio_actual = os.getcwd()
        
        mp4_file = nombre+".mp4"
        mp3_file = nombre+".mp3"

        # Combina la ruta del directorio actual con los nombres de los archivos
        mp4_path = os.path.join(directorio_actual, mp4_file)
        mp3_path = os.path.join(directorio_actual, mp3_file)

        # Cargar el archivo de video
        video_clip = VideoFileClip(mp4_path)

        # Extraer el audio del video
        audio_clip = video_clip.audio

        # Guardar el audio en formato MP3
        audio_clip.write_audiofile(mp3_path)

        # Cierra los clips para liberar recursos
        audio_clip.close()
        video_clip.close()

        # Envia el archivo MP3 como respuesta
        response = FileResponse(open(mp3_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{mp3_file}"'
        return response
    except Exception as e:
        return JsonResponse({"message": f"Error durante la conversión: {str(e)}"}, status=500)


@api_view(['POST'])
def existeVideo(request):
    
    link = request.data.get('link')
    video = YouTube(link)
    nombre = video.title
    directorio_actual = os.getcwd()

    # Combina la ruta del directorio actual con el nombre del archivo
    ruta_archivo = os.path.join(directorio_actual, nombre+".mp4")

    mensaje = ""
    # Verifica si el archivo existe
    if os.path.isfile(ruta_archivo):
        mensaje = (f"El archivo '{nombre}' existe en la carpeta {directorio_actual}.")
    else:
        mensaje = (f"El archivo '{nombre}' no existe en la carpeta actual.")
    return JsonResponse({"message": mensaje}, status=201)