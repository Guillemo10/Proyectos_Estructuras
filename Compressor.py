import heapq
import pickle
from bitarray import bitarray
from PIL import Image
import librosa
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

class Node:
    def __init__(self, simbolo = None, frecuencia = 0, hijo_izq = None, hijo_der = None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.hijo_izq = hijo_izq
        self.hijo_der = hijo_der
    
    def __lt__(self, otro): #Esto se usa para que al momento de utilizar la funcion "heapify" compare de acuerdo con la frecuencia
        return self.frecuencia < otro.frecuencia

class Text:
    def obtener_texto(self, direccion):
        with open(direccion,'r') as file:
            text = file.read() 
        return text

    def frecuencia_simbolos(self, direccion):
        frecuencia_letras = {}
        with open(direccion,'r') as file:
            text = file.read()
        for caracter in text:
            frecuencia_letras[caracter] = frecuencia_letras.get(caracter, 0) + 1
        return frecuencia_letras
    
    def codificar_texto(self, texto, diccionario):
        texto_codificado = ''.join(diccionario[caracter] for caracter in texto)
        """print(texto_codificado)"""
        return texto_codificado
    
    def comprimir(self, diccionario, texto, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, texto)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol, archivo_descomprimido):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_texto(comprimido, arbol, archivo_descomprimido)
    
    def decodificar_texto(self, bits, arbol_huffman, archivo_descomprimido):
        texto_recuperado = ""
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                texto_recuperado += nodo_actual.simbolo
                nodo_actual = arbol_huffman

        with open(archivo_descomprimido, 'w') as file:
            file.write(texto_recuperado)

        return texto_recuperado


class Imagen:
    def obtener_imagen(self, direccion):
        with open(direccion,'rb') as file:
            imagen = file.read() 
        return imagen

    def frecuencia_simbolos(self, direccion):
        frecuencia_bytes = {}
        with open(direccion,'rb') as file:
            imagen = file.read()
        for byte in imagen:
            frecuencia_bytes[byte] = frecuencia_bytes.get(byte, 0) + 1
        return frecuencia_bytes
    
    def codificar_imagen(self, imagen, diccionario):
        imagen_codificado = ''.join(diccionario[byte] for byte in imagen)
        return imagen_codificado
    
    def comprimir(self, diccionario, imagen, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, imagen)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol, archivo_descomprimido):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_imagen(comprimido, arbol, archivo_descomprimido)
    
    def decodificar_imagen(self, bits, arbol_huffman, archivo_descomprimido):
        imagen_recuperado = bytearray()
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                imagen_recuperado.append(nodo_actual.simbolo)  # convert to string before concatenating
                nodo_actual = arbol_huffman

        with open(archivo_descomprimido, 'wb') as file:
            file.write(imagen_recuperado)

        return imagen_recuperado
    
    
class Audio:
    def obtener_audio(self, direccion):
        with open(direccion,'rb') as file:
            audio = file.read() 
        return audio

    def frecuencia_simbolos(self, direccion):
        frecuencia_bytes = {}
        with open(direccion,'rb') as file:
            audio = file.read()
        for byte in audio:
            frecuencia_bytes[byte] = frecuencia_bytes.get(byte, 0) + 1
        return frecuencia_bytes
    
    def codificar_audio(self, audio, diccionario):
        audio_codificado = ''.join(diccionario[byte] for byte in audio)
        """print(texto_codificado)"""
        return audio_codificado
    
    def comprimir(self, diccionario, audio, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, audio)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol, archivo_descomprimido):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_audio(comprimido, arbol, archivo_descomprimido)
    
    def decodificar_audio(self, bits, arbol_huffman, archivo_descomprimido):
        audio_recuperado = bytearray()
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                audio_recuperado.append(nodo_actual.simbolo)  # convert to string before concatenating
                nodo_actual = arbol_huffman

        with open(archivo_descomprimido, 'wb') as file:
            file.write(audio_recuperado)

        return audio_recuperado
    
class Video:
    def obtener_video(self, direccion):
        with open(direccion,'rb') as file:
            video = file.read() 
        return video

    def frecuencia_simbolos(self, direccion):
        frecuencia_bytes = {}
        with open(direccion,'rb') as file:
            video = file.read()
        for byte in video:
            frecuencia_bytes[byte] = frecuencia_bytes.get(byte, 0) + 1
        return frecuencia_bytes
    
    def codificar_video(self, video, diccionario):
        video_codificado = ''.join(diccionario[byte] for byte in video)
        return video_codificado
    
    def comprimir(self, diccionario, video, archivo_salida, arbol_huffman, archivo_salida_arbol):
        s = bitarray()
        s.encode({simbolo: bitarray(code) for simbolo, code in diccionario.items()}, video)
        with open(archivo_salida, 'wb') as file:
            s.tofile(file)
        with open(archivo_salida_arbol, 'wb') as file:
            pickle.dump(arbol_huffman, file)

    def descomprimir(self, archivo_salida, archivo_salida_arbol, archivo_descomprimido):
        with open(archivo_salida, 'rb')as file:
            comprimido = bitarray()
            comprimido.fromfile(file)
        with open(archivo_salida_arbol, 'rb') as file:
            arbol = pickle.load(file)
        
        self.decodificar_video(comprimido, arbol, archivo_descomprimido)
    
    def decodificar_video(self, bits, arbol_huffman, archivo_descomprimido):
        video_recuperado = bytearray()
        nodo_actual = arbol_huffman

        for bit in bits:
            if str(bit) == '0':
                nodo_actual = nodo_actual.hijo_izq
            else:
                nodo_actual = nodo_actual.hijo_der

            if nodo_actual.simbolo is not None:
                video_recuperado.append(nodo_actual.simbolo)  # convert to string before concatenating
                nodo_actual = arbol_huffman

        with open(archivo_descomprimido, 'wb') as file:
            file.write(video_recuperado)

        return video_recuperado
    


class Huffman:   
    def generar_arbol_huffman(self, frecuencia_letras):
        cola_prioridad = [Node(caracter, frecuencia) for caracter, frecuencia in frecuencia_letras.items()]
        heapq.heapify(cola_prioridad)

        
        while len(cola_prioridad) > 1:
            izq = heapq.heappop(cola_prioridad)
            der = heapq.heappop(cola_prioridad)
            new_node = Node(frecuencia = izq.frecuencia + der.frecuencia, hijo_izq = izq, hijo_der = der)
            heapq.heappush(cola_prioridad, new_node)

        return cola_prioridad[0]
    
    def diccionario_codigos_nuevos(self, arbol_huffman, codigo = '', diccionario = None):
        if diccionario is None:
            diccionario = {}
        if arbol_huffman.simbolo is not None:
            diccionario[arbol_huffman.simbolo] = codigo
        if arbol_huffman.hijo_izq is not None:
           self.diccionario_codigos_nuevos(arbol_huffman.hijo_izq, codigo + '0', diccionario)
        if arbol_huffman.hijo_der is not None:
            self.diccionario_codigos_nuevos(arbol_huffman.hijo_der, codigo + '1', diccionario)
        """print(diccionario)"""
        return diccionario



class Interface:
    def __init__(self):
        self.file_path_compress = None
        self.file_path_decompress = None
        self.extension = None
        self.extension_des = None
        self.file_arbol = None
        self.file_archivo = None
        self.file_archivo_des = None
        self.Obj = Huffman()
        self.Obj1 = Text()
        self.Obj2 = Imagen()
        self.Obj3 = Audio()
        self.Obj4 = Video()

    def select_file_compress(self):
        self.file_path_compress = filedialog.askopenfilename(title="Seleccionar archivo para comprimir", filetypes=[("Todos los archivos", "*.*")])
        index = self.file_path_compress.find("OneDrive")
        self.file_path_compress = self.file_path_compress[index:]
        if self.file_path_compress:
            entry.delete(0, tk.END) 
            entry.insert(0, self.file_path_compress)
    
    def select_file_decompress(self):
        self.file_path_decompress = filedialog.askopenfilename(title="Seleccionar archivo para comprimir", filetypes=[("Todos los archivos", "*.*")])
        index = self.file_path_decompress.find("OneDrive")
        self.file_path_decompress = self.file_path_decompress[index:]
        if self.file_path_decompress:
            entry2.delete(0, tk.END) 
            entry2.insert(0, self.file_path_decompress)

    def compress_file(self):
        self.extension = os.path.splitext(self.file_path_compress)[1]
        self.file_archivo = os.path.normpath(os.path.join(os.path.dirname(self.file_path_compress), "Comprimido.bin"))
        self.file_arbol = os.path.normpath(os.path.join(os.path.dirname(self.file_path_compress), "Arbol.bin"))

        try:
            if self.extension == ".txt":
                frecuencia_letras = self.Obj1.frecuencia_simbolos(self.file_path_compress)
                arbol_de_huffman = self.Obj.generar_arbol_huffman(frecuencia_letras)
                text = self.Obj1.obtener_texto(self.file_path_compress)
                diccionario_codigos_nuevos = self.Obj.diccionario_codigos_nuevos(arbol_de_huffman)
                self.Obj1.comprimir(diccionario_codigos_nuevos, text, self.file_archivo, arbol_de_huffman , self.file_arbol)
            elif self.extension == ".bmp" or self.extension == ".png" or self.extension == ".jpg":
                frecuencia_bytes = self.Obj2.frecuencia_simbolos(self.file_path_compress)
                arbol_de_huffman = self.Obj.generar_arbol_huffman(frecuencia_bytes) 
                imagen = self.Obj2.obtener_imagen(self.file_path_compress) 
                diccionario_codigos_nuevos = self.Obj.diccionario_codigos_nuevos(arbol_de_huffman)
                self.Obj2.comprimir(diccionario_codigos_nuevos, imagen, self.file_archivo, arbol_de_huffman , self.file_arbol)
            elif self.extension == ".wav" or self.extension == ".mp3":
                frecuencia_bytes = self.Obj3.frecuencia_simbolos(self.file_path_compress)
                arbol_de_huffman = self.Obj.generar_arbol_huffman(frecuencia_bytes)
                audio = self.Obj3.obtener_audio(self.file_path_compress)
                diccionario_codigos_nuevos = self.Obj.diccionario_codigos_nuevos(arbol_de_huffman)
                self.Obj3.comprimir(diccionario_codigos_nuevos, audio, self.file_archivo, arbol_de_huffman , self.file_arbol)
            elif self.extension == ".mov":
                frecuencia_bytes = self.Obj4.frecuencia_simbolos(self.file_path_compress)
                arbol_de_huffman = self.Obj.generar_arbol_huffman(frecuencia_bytes)
                video = self.Obj4.obtener_video(self.file_path_compress)
                diccionario_codigos_nuevos = self.Obj.diccionario_codigos_nuevos(arbol_de_huffman)
                self.Obj4.comprimir(diccionario_codigos_nuevos, video, self.file_archivo, arbol_de_huffman , self.file_arbol)
            else:
                print("No se reconocio la extensión")

        except FileNotFoundError:
            entry.delete(0, tk.END)
            entry.insert(0, "Archivo no encontrado")

    def decompress_file(self):
        self.file_archivo = os.path.normpath(os.path.join(os.path.dirname(self.file_path_decompress), "Comprimido.bin"))
        self.file_arbol = os.path.normpath(os.path.join(os.path.dirname(self.file_path_decompress), "Arbol.bin"))
        try:
            if self.extension_des == ".txt":
                archivo_descomprimido = self.file_path_decompress.replace("Comprimido.bin", "Texto_Descomprimido.txt")
                self.Obj1.descomprimir(self.file_archivo, self.file_arbol, archivo_descomprimido)
            elif self.extension_des == ".bmp" or self.extension_des == ".png" or self.extension_des == ".jpg":
                archivo_descomprimido = self.file_path_decompress.replace("Comprimido.bin", "Imagen_Descomprimido.bmp")
                self.Obj2.descomprimir(self.file_archivo, self.file_arbol, archivo_descomprimido)
            elif self.extension_des == ".wav" or self.extension_des == ".mp3":
                archivo_descomprimido = self.file_path_decompress.replace("Comprimido.bin", "Audio_Descomprimido.wav")
                self.Obj3.descomprimir(self.file_archivo, self.file_arbol, archivo_descomprimido)
            elif self.extension_des == ".mov":
                archivo_descomprimido = self.file_path_decompress.replace("Comprimido.bin", "Video_Descomprimido.mov")
                self.Obj4.descomprimir(self.file_archivo, self.file_arbol, archivo_descomprimido)
            else:
                print("No se reconocio la extensión")

        except FileNotFoundError:
            entry.delete(0, tk.END)
            entry.insert(0, "Archivo no encontrado")

    def text(self):
        self.extension_des = ".txt"
    def image(self):
        self.extension_des = ".bmp"
    def audio(self):
        self.extension_des = ".wav"
    def video(self):
        self.extension_des = ".mov"



interface = Interface()

ventana = tk.Tk()
ventana.title("Compresor")


entry = tk.Entry(ventana)
entry.grid(row=0, column=0, padx=60, pady=20)

button = tk.Button(ventana, text="Selecciona tu archivo", command=interface.select_file_compress)
button.grid(row=1, column=0, padx=28, pady=20)

button2 = tk.Button(ventana, text="Comprimir", command=interface.compress_file)
button2.grid(row=1, column=1, padx=28, pady=20)


entry2 = tk.Entry(ventana)
entry2.grid(row=3, column=0, padx=60, pady=20)


button5 = tk.Button(ventana, text="Texto", command=interface.text)
button5.grid(row=2, column=0, padx=28, pady=20)

button6 = tk.Button(ventana, text="Imagen", command=interface.image)
button6.grid(row=2, column=1, padx=28, pady=20)

button7 = tk.Button(ventana, text="Audio", command=interface.audio)
button7.grid(row=2, column=2, padx=28, pady=20)

button8 = tk.Button(ventana, text="Video", command=interface.video)
button8.grid(row=2, column=3, padx=28, pady=20)



button3 = tk.Button(ventana, text="Selecciona tu archivo", command=interface.select_file_decompress)
button3.grid(row=4, column=0, padx=28, pady=20)

button4 = tk.Button(ventana, text="Descomprimir", command=interface.decompress_file)
button4.grid(row=4, column=1, padx=28, pady=20)

ventana.mainloop()
