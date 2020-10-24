# --importacion de librerias
from tkinter import *
from tkinter import messagebox
import pymysql

def pantalla_principal():
    global root

    root=Tk()
    root.title("VENTANA ADMINISTRATIVA")
    root.iconbitmap("talk.ico")

    raiz=Frame(root)
    raiz.pack()

    fondos=PhotoImage(file="alo.gif")
    fondol=Label(raiz,image=fondos).pack()

    texto=Label(raiz, text="ACCESO AL SISTEMA",fg="black",font=("Calibri,20"),width=34)
    texto.pack()
    texto.place(x=5,y=400)

    buttom=Button(raiz, text="Registrate",width=40,command=Registrar)
    buttom.pack()
    buttom.place(x=20,y=450)

    sed=Button(raiz, text="Iniciar Sesión",width=40,command=Inicio_Sesión)
    sed.pack()
    sed.place(x=20,y=500)

    root.mainloop()

def Inicio_Sesión():
    pantalla=Toplevel(root)
    pantalla.geometry("320x570")
    pantalla.title("Inicio de Sesión")
    pantalla.iconbitmap("talk.ico")

    global fondos
    global usuario
    global contraseña
    global entrada_usuario
    global entrada_contraseña

    usuario=StringVar()
    contraseña=StringVar()

    fondos=PhotoImage(file="alo.gif")
    campo=Label(pantalla,image=fondos)
    campo.pack()

    texto1=Label(pantalla, text="POR FAVOR INGRESE USUARIO Y CONTRASEÑA",font=("Calibri",12))
    texto1.pack()
    texto1.place(x=3,y=280)
    
    texto1=Label(pantalla, text="Usuario",width=40)
    texto1.pack()
    texto1.place(x=20,y=360)

    entrada_usuario=Entry(pantalla,textvariable=usuario,width=40, fg="green")
    entrada_usuario.pack()
    entrada_usuario.config(justify="center")
    entrada_usuario.place(x=35,y=395)


    texto2=Label(pantalla, text="Contraseña",width=40)
    texto2.pack()
    texto2.place(x=20,y=430)

    entrada_contraseña=Entry(pantalla,textvariable=contraseña,width=40,show="*")
    entrada_contraseña.pack()
    entrada_contraseña.config(justify="center")
    entrada_contraseña.place(x=35,y=470)


    valor=Button(pantalla, text="Iniciar Sesión",width=40,command=Validacion_datos)
    valor.pack()
    valor.place(x=16,y=510)


def Registrar():
    pantalla1=Toplevel(root)
    pantalla1.geometry("320x570")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("talk.ico")

    global fondos
    global entrada_usuario
    global entrada_contraseña

    usuario=StringVar()
    contraseña=StringVar()

    fondos=PhotoImage(file="alo.gif")
    campo=Label(pantalla1,image=fondos)
    campo.pack()

    texto1=Label(pantalla1, text="POR FAVOR INGRESE USUARIO Y CONTRASEÑA\nDE SU SELECIÓN PARA EL REGISTRO DE DATOS",font=("Calibri",12))
    texto1.pack()
    texto1.place(x=3,y=280)
    
    texto1=Label(pantalla1, text="Usuario",width=40)
    texto1.pack()
    texto1.place(x=20,y=360)

    entrada_usuario=Entry(pantalla1,textvariable=usuario,width=40,fg="orange")
    entrada_usuario.pack()
    entrada_usuario.config(justify="center")
    entrada_usuario.place(x=35,y=395)


    texto2=Label(pantalla1, text="Contraseña",width=40)
    texto2.pack()
    texto2.place(x=20,y=430)

    entrada_contraseña=Entry(pantalla1,textvariable=contraseña,width=40,show="*")
    entrada_contraseña.pack()
    entrada_contraseña.config(justify="center")
    entrada_contraseña.place(x=35,y=470)


    valor=Button(pantalla1, text="Iniciar Sesión",width=40,command=Insertar_Datos)
    valor.pack()
    valor.place(x=16,y=510)

def Insertar_Datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="12345678",
        db="Data"
        )
    cur=bd.cursor()
    sql="INSERT INTO usuarios_creados(usuario, contraseña) VALUES('{0}','{1}')".format(entrada_usuario.get(),entrada_contraseña.get())

    try:
        cur.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No Registrado", title="Aviso")

    bd.close()

def Validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        password="12345678",
        db="Data"
        )
    cur=bd.cursor()
    cur.execute("SELECT contraseña FROM usuarios_creados WHERE usuario='"+usuario.get()+"' and contraseña='"+contraseña.get()+"'")

    if cur.fetchall():
        messagebox.showinfo(title="Inicio de Sección Correcto", message="Usuario y Contraseña Correcta")

    else:
        messagebox.showinfo(title="Usuario y Contraseña Incorrecta", message="El Usuario No Existe")    
    
    bd.close()

pantalla_principal()


    
