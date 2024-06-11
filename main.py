from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import clipboard


def undo():
    undo = messagebox.askokcancel("Предупреждение", "Вы то что хотите отменить?")
    if undo:
        text_fild.edit_undo()

def redo():
    text_fild.edit_redo()
    messagebox.askokcancel("Выполнено", "Вернули старое")

def cut():
    text = text_fild.selection_get()
    if text:
        clipboard.copy(text)
        text_fild.delete(SEL_FIRST, SEL_LAST)  # Удаляем выделенный текст
        messagebox.askokcancel("Выполнено","Текст вырезан и помещен в буфер обмена.")
    else:
        messagebox.askokcancel("Выполнено","Выделите текст, прежде чем копировать.")

def copy():
        text = text_fild.get(1.0, END)  # Получаем выделенный текст
        if text:
            clipboard.copy(text)
            messagebox.askokcancel("Выполнено","Текст скопирован в буфер обмена.")
        else:
            messagebox.askokcancel("Выполнено","Выделите текст, прежде чем копировать.")


def paste():
    text = clipboard.paste()
    text_fild.insert(END, text)  # Вставляем текст в текстовое поле
    messagebox.askokcancel("Выполнено","Текст из буфера обмена вставлен.")


def chage_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def chage_fonts(font1):
    text_fild['font'] = fonts[font1]['font']

def exit():
    exits = messagebox.askokcancel("Выход", "Вы точно хотите выйти?")
    if exits:
        root.destroy()

def open_file():
    openFile = filedialog.askopenfilename(title="Выбор файла", filetypes=(("Текставой документ (*.txt)", '*.txt'), ("Все фалы", "*.*")))
    text_fild.delete('1.0', END)
    text_fild.insert('1.0', open(openFile, encoding='utf-8').read())

def saveFile():
    saveFils = filedialog.asksaveasfilename(filetypes=(("Текставой документ (*.txt)", '*.txt'), ("Все фалы", "*.*")))
    f = open(saveFils, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()

root = Tk()
root.title("Блокнот 1.2")
root.geometry('1280x520')
#root.iconbitmap('icoprogram.ico')

menu = Menu(root)
#File
file_menu = Menu(menu, tearoff=0)
unre_menu_sub = Menu(file_menu, tearoff=0)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=saveFile)
file_menu.add_separator()
unre_menu_sub.add_command(label="Отменить", command=undo)
unre_menu_sub.add_command(label="Вернуть", command=redo)
file_menu.add_cascade(label="Допалнительные фукции", menu=unre_menu_sub)
file_menu.add_separator()
file_menu.add_command(label="Закрыть", command=exit)
root.config(menu=file_menu)
#view
view_menu = Menu(menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label="Тёмная", command=lambda: chage_theme('dark'))
view_menu_sub.add_command(label="Светлая", command=lambda: chage_theme('light'))
view_menu_sub.add_command(label="Светлая-Лайм", command=lambda: chage_theme('light-lime'))
view_menu_sub.add_command(label="Тёмная-Лайм", command=lambda: chage_theme('dark-lime'))
view_menu.add_cascade(label="Тема", menu=view_menu_sub)

font_menu_sub.add_command(label="Calibri", command=lambda: chage_fonts('Calibri'))
font_menu_sub.add_command(label="Arial", command=lambda: chage_fonts('Arial'))
font_menu_sub.add_command(label="Alegreya", command=lambda: chage_fonts('Alegreya'))
font_menu_sub.add_command(label="Comic Sans MS", command=lambda: chage_fonts('CSMS'))
font_menu_sub.add_command(label="Mon Amour One", command=lambda: chage_fonts('MAO'))
view_menu.add_cascade(label="Шрифт...", menu=font_menu_sub)
root.config(menu=view_menu)

text_menu = Menu(menu, tearoff=0)
text_menu.add_command(label="Вырезать", command=cut)
text_menu.add_command(label="Копировать", command=copy)
text_menu.add_command(label="Вставить", command=paste)

menu.add_cascade(label="Файл", menu=file_menu)
menu.add_cascade(label="Вид", menu=view_menu)
menu.add_cascade(label="Тест", menu=text_menu)

root.config(menu=menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'white', 'cursor': 'white', 'select_bg':'#292828'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': 'black', 'select_bg':'#8f8e8c'
    },
    'dark-lime':{
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'white', 'select_bg':'#292828'
    },
    'light-lime':{
        'text_bg': 'white', 'text_fg': 'lime', 'cursor': 'black', 'select_bg':'#8f8e8c'
    }
}
fonts = {
    'Calibri':{
        'font': 'Calbri 12 bold'
    },
    'Alegreya':{
        'font': 'Alegreya 12 bold'
    },
    'Arial':{
        'font': 'Arial 12 bold'
    },
    'CSMS':{
        'font': ('Comic Sans MS', 12, 'bold')
    },
    'MAO': {
        'font': ('Mon Amour One', 12, 'bold')
    }
}

text_fild = Text(f_text, bg='black', fg='white', padx=10, pady=10, wrap=WORD, insertbackground='white',
                 selectbackground='#292828', spacing3=10, font='Alegreya 12 bold', undo=True)
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

scroll =Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.bind("<Control-z>", undo)
root.bind("<Control-y>", redo)
root.bind("<Control-c>", copy)
root.bind("<Control-x>", cut)
root.bind("<Control-v>", paste)


root.mainloop()