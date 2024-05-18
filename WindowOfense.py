from tkinter import *
import requests
from bs4 import BeautifulSoup

words = ["puto", "bobo", "tonto", "gilipollas", "idiota", "Abrazafarolas", "Barriobajero"]


def get_web(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    page_text = soup.get_text()
    encontradas = []
    for palabra in words:
        if palabra in page_text:
            encontradas.append(palabra)
    return encontradas

def create_file(url):
    new_file = "PalabrasOfensivas.txt"
    words_file = open(new_file, "w")
    ofensive_words = get_web(url)
    for word in ofensive_words:
        words_file.write(word + "\n")


def main():

    window = Tk()
    window.title("Ejemplo de Entry")

    entry = Entry(window, width=50)
    entry.pack(pady=20)

    frame = Frame(window)
    frame.pack()

    entry.insert(0, "Ingrese la URL de la web: ")

    create = Button(frame, text="Crear archivo con las palabras ofensivas", height=2, width=35, font=35, command=lambda:create_file(entry.get()))
    create.grid(row=0, column=0)

    window.mainloop()   

if __name__ == "__main__":
    main()
