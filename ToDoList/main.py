import tkinter as tk
from tkinter import messagebox

# Ana uygulama penceresi oluşturma
root = tk.Tk()
root.title("To-Do List")
root.geometry("1080x480")
root.config(bg="#092835",borderwidth=10)


# To-Do List için bir liste oluşturma
tasks = []


# Görev ekleme fonksiyonu
def add_task():
    task = gorev_entry.get()
    if task:  # Eğer görev boş değilse
        tasks.append({"task": task, "priority": oncelikli_val.get()})
        update_listbox()
        gorev_entry.delete(0, tk.END)  # Girdi kutusunu temizle
        save_tasks_to_file()  # Görevleri dosyaya kaydet
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin!")


# Görev düzenleme fonksiyonu
def edit_task():
    try:
        index = gorevler_listbox.curselection()[0]
        new_task = edit_entry.get()
        tasks[index]["task"] = new_task
        update_listbox()
        edit_window.destroy()
        save_tasks_to_file()  # Görevleri dosyaya kaydet
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")


# Görev silme fonksiyonu
def delete_task():
    try:
        index = gorevler_listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks_to_file()  # Görevleri dosyaya kaydet
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")


# Görev tamamlama fonksiyonu
def complete_task():
    try:
        index = gorevler_listbox.curselection()[0]
        tasks[index]["task"] = f"{tasks[index]['task']} - Tamamlandı"
        update_listbox()
        save_tasks_to_file()  # Görevleri dosyaya kaydet
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")


# Listbox'ı güncelleme fonksiyonu
def update_listbox():
    gorevler_listbox.delete(0, tk.END)
    for task in tasks:
        gorevler_listbox.insert(tk.END, f"{task['task']} - Öncelik: {task['priority']}")


# Görevleri dosyaya kaydetme fonksiyonu
def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['priority']}\n")


# Dosyadan görevleri yükleme fonksiyonu
def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, priority = line.strip().split("|")
                tasks.append({"task": task, "priority": priority})
        update_listbox()
    except FileNotFoundError:
        pass


# Yeni pencere oluşturma fonksiyonu (Görev düzenleme için)
def create_edit_window():
    global edit_entry, edit_window
    try:
        index = gorevler_listbox.curselection()[0]
        edit_window = tk.Toplevel(root,background="#092835")
        edit_window.title("Görev Düzenle")
        edit_window.geometry("500x300")

        edit_label = tk.Label(edit_window,
                              text="Yeni Görev:",
                              font=("Consolas", 15),
                              background="#092835",
                              foreground="white")
        edit_label.place(x=10, y=30)

        edit_entry = tk.Entry(edit_window,
                              width=35,
                              font=("Consolas",15))
        edit_entry.place(x=10, y=60)

        edit_entry.insert(tk.END, tasks[index]["task"])

        edit_button = tk.Button(edit_window,
                                text="Kaydet",
                                command=edit_task,
                                font=("Consolas", 15),
                                background="#7A9419",
                                foreground="white")
        edit_button.place(x=30, y=120)
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçin!")



# Arayüz öğeleri oluşturma
gorev_label = tk.Label(root,
                       text="Görevinizi Giriniz:",
                       font=("Consolas", 15),
                       background="#092835",
                       foreground="white")
gorev_label.place(x=50, y=6)

gorev_entry = tk.Entry(root,
                       font=("Consolas",15),
                       width=30)
gorev_entry.place(x=50, y=30)

oncelikli_val = tk.StringVar()
oncelikli_val.set("Normal")

oncelikli_frame = tk.Frame(root)
oncelikli_frame.place(x=30,y=80)

dusuk_radiobutton = tk.Radiobutton(oncelikli_frame,
                                   text="Düşük",
                                   variable=oncelikli_val,
                                   value="Düşük",
                                   font=("Consolas",15),
                                   background="#092835",
                                   foreground="white")
dusuk_radiobutton.pack(side=tk.LEFT)

normal_radiobutton = tk.Radiobutton(oncelikli_frame,
                                    text="Normal",
                                    variable=oncelikli_val,
                                    value="Normal",
                                    font=("Consolas", 15),
                                    background="#092835",
                                    foreground="white")
normal_radiobutton.pack(side=tk.LEFT)

yuksek_radiobutton = tk.Radiobutton(oncelikli_frame,
                                    text="Yüksek",
                                    variable=oncelikli_val,
                                    value="Yüksek",
                                    font=("Consolas", 15),
                                    background="#092835",
                                    foreground="white")
yuksek_radiobutton.pack(side=tk.LEFT)

ekle_button = tk.Button(root,
                        text="Görev Ekle",
                        command=add_task,
                        font=("Consolas", 15),
                        background="#7A9419",
                        foreground="white")
ekle_button.place(x=50, y=150)

gorevler_listbox = tk.Listbox(root, width=60,
                              font=("Consolas", 15),
                              height=15,
                              highlightcolor="#0099cc")

gorevler_listbox.place(x=400, y=30)

sil_button = tk.Button(root,
                       text="Görev Sil",
                       command=delete_task,
                       font=("Consolas", 15),
                       background="#7A9419",
                       foreground="white")
sil_button.place(x=0, y=400)

tamamla_button = tk.Button(root,
                           text="Görev Tamamla",
                           command=complete_task,
                           font=("Consolas", 15),
                           background="#7A9419",
                           foreground="white")
tamamla_button.place(x=130, y=400)

duzenle_button = tk.Button(root,
                           text="Görev Düzenle",
                           command=create_edit_window,
                           font=("Consolas", 15),
                           background="#7A9419",
                           foreground="white")
duzenle_button.place(x=300, y=400)

# Kayıtlı görevleri dosyadan yükle
load_tasks_from_file()

# Ana döngüyü başlatma
root.mainloop()
