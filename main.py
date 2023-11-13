
import oracledb
import datetime
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from tkinter import *
from tkinter.ttk import *
import getpass
import cryptography
import secrets
import ssl
import uuid
import os
un = "aa"
cs = "aa"
pw = "aa"



from tkinter import filedialog
from pathlib import Path



# Función para validar que el número esté entre 1 y 10

def verificar_entrada(*args):
    # Verificar si el valor seleccionado en el ComboBox es "Sí"
    if valor_combobox.get() == "Sí":
        #boton.config(state=tk.NORMAL)
        print("sí")
    else:
        #boton.config(state=tk.DISABLED)
        print("no")

import re
def check_listas2(valores):
    patron = re.compile(r'^\d+(,\d+)*$')
    return bool(patron.match(valores))
    
    
def check_listas(numero):
    if len(str(numero)) == 0:
        raise ValueError("Este campo no puede ser vacio")
    
    elif  not check_listas2(numero):
        raise ValueError("El número debe ser un digito")    
    

def is_float2(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    

def is_float(numero):
    if len(str(numero)) == 0:
        raise ValueError("Este campo no puede ser vacio")
    
    if  not is_float2(numero):
        raise ValueError("El número debe ser un numero")
    
def validar_id_de_campana(id):
    conn1= oracledb.connect(user=un, password=pw, dsn=cs)
    cur = conn1.cursor()
    cur.execute("select  id_campaña from hola4")
    res = pd.DataFrame(cur.fetchall())
    if res.isin([id]).any().any() == True:
        raise ValueError('Este ID CAMPAÑA ya esta en la base de datos')
        
        
def validar_id_de_brief(id):
    conn1= oracledb.connect(user=un, password=pw, dsn=cs)
    cur = conn1.cursor()
    cur.execute("select  id_brief from hola4")
    res = pd.DataFrame(cur.fetchall())
    if res.isin([id]).any().any() == True:
        raise ValueError('Este ID BRIEF ya esta en la base de datos')        



  
def validar_numero_dato3(numero):
    if len(str(numero)) == 0:
        raise ValueError("Este campo Número no puede ser vacio")
    
    elif   is_float(numero):
        raise ValueError("Debe ser un numero")


# Función para validar que el texto tenga 5 caracteres
def validar_texto_dato2(texto):
    if len(str(texto)) == 0:
            raise ValueError("No puede haber campos vacio")

    #elif len(str(texto)) > 500:
        #raise ValueError("El texto debe tener menos de 500 caracteres")

# Función para validar la fecha
def validar_fecha(fecha):
    try:
        
        if len(str(fecha)) == 0:
            raise ValueError("Este campo de fecha puede ser vacio")
        
        datetime.strptime(fecha, "%d/%m/%Y")
        
    except ValueError:
        raise ValueError("La fecha debe tener el formato dd/mm/aaaa")
# Función para validar coherecnia de fechas
def validar_coherencia_fechas(fechas1,fechas2):
    fechas1a=datetime.strptime(fechas1, "%d/%m/%Y")
    fechas2a =datetime.strptime(fechas2, "%d/%m/%Y")
        
    if fechas1a > fechas2a:
        raise ValueError("La fecha de fin debe ser mayor a la fecha inicio")
        


#clases 
class NewWindow(Toplevel):
    
    
    
    def __init__(self, master = None, numberJournes:int = 1, arreglo_valores=[]):
        super().__init__(master = master)
        self.title("Journes")
        self.geometry("400x400")

        for i in range(int(numberJournes)):
            self.addComponent(self,i)
        #boton
        boton_ok2 = tk.Button(self, text="Insertar",command=lambda:self.listas(self, arreglo_valores))# command=lambda: validar_datos()
        gr = int(numberJournes)+3
        boton_ok2.grid(row=gr,column=2)
        
        
        
        
    def addComponent(self, master = None, index = 0):
        label = Label(master, text = "Col1")
        entry = Entry(master)
        label.grid(row = index, column = 0, columnspan = 3)
        entry.grid(row = index, column = 4)

        label2 = Label(master, text = "Col2")
        entry2 = Entry(master)
        label2.grid(row = index, column = 5, columnspan = 3)
        entry2.grid(row = index, column = 9)

        label3 = Label(master, text = "Col3")
        entry3 = Entry(master)
        label3.grid(row = index, column = 10, columnspan = 3)
        entry3.grid(row = index, column = 14)
        
    def listas(self,ventana, valores = []):
        
        lista = all_children(wid=ventana)
        for i in lista:
            #print('tipo: ' + str(type(i)))
            if type(i) == tk.ttk.Entry:
                print(i.get())
                valores.append(i.get())
            


#cursor de insersión
def GetCursor():
    un = "aaa"
    pw = "aa"
    cs = "ssss"

    headers = []
    rows = []
    con = oracledb.connect(user=un, password=pw, dsn=cs)
    cursor = con.cursor()
    return cursor


# In[8]:


#funciones de insercion de archivos


# In[9]:


def InsertBlob(filepath):
    cursor = GetCursor()
    cursor.setinputsizes(valor = oracledb.BLOB)
    blob_var = cursor.var(oracledb.BLOB)
    blob_file = open(filepath, 'rb')
 
    blob_var.setvalue(0,blob_file.read())
    blob_file.close()
       
    cursor.execute(f"""INSERT INTO PRUEBA_IMAGEN(ID, ARCHIVO) VALUES(:id, :valor)""", id = filepath, valor = blob_var)
    cursor.execute("COMMIT")
 
def DownloadBlob():
    cursor = GetCursor()
   
    cursor.execute("SELECT * FROM PRUEBA_IMAGEN")
    path = str(Path.home() / "Downloads")
 
    for row in cursor.fetchall():
        nombre_archivo = os.path.basename(row[0])
 
        #print(f"{path}/database_{nombre_archivo}")
        with open(f"{path}/database_{nombre_archivo}", 'wb') as file:
        #with open(f"{row[0]}", 'wb') as file:
            clob_data = row[1].read()
            file.write(clob_data)
 
def UploadFile():
    filepath = filedialog.askopenfile()
 
    if filepath == None:
        return
    InsertBlob(filepath.name)


# In[10]:


from datetime import datetime


# In[154]:


def validar_numero_dato1(numero):
    if len(str(numero)) == 0:
        raise ValueError("Este campo Número no puede ser vacio")
    
    elif  not str(numero).isdigit():
        raise ValueError("El número debe ser un número entero",numero)
def valor_unico_lista(val2):
    if len(val2) == 0:
        raise ValueError("Tienes que elegir una opción")

def valor_no_unico_lista(val):
    if val == []:
        raise ValueError("Tienes que elegir al menos una opción")
        
def vacio(num):
    if len(str(num))==0:
        raise ValueError("Este campo no puede ser vacio")
        
def longitud(jup,tex):
    if len(str(tex)) > jup:
        raise ValueError("El campo mensaje SMS debe medir al máximo: ",jup,' caractéres')


# In[194]:


def all_children(wid, finList=None, indent=0):
    finList = finList or []
    #print(f"{'   ' * indent}{wid=}")
    children = wid.winfo_children()
    for item in children:
        finList.append(item)
        all_children(item, finList, indent + 1)
    return finList


# In[202]:


def validar_datos():
    try:
        #VALIDACIÓN condicional
        _10 = uni_campo_etiqueta_lista10.get()
        valor_unico_lista(_10)

        #NUMERO


        _01 = str(campo_numero_etiqueta_idd01.get())
        validar_numero_dato1(_01)
        #función si ya esta en la base de datos
        _02 = str(campo_numero_etiqueta_idd02.get())
        validar_numero_dato1(_02)
        #función si ya esta en la base de datos
        version = str(campo_numero_etiqueta_idd022.get())
        validar_numero_dato1(version)
        #función si ya esta en la base de datos el _01 y versión
        
        _01,_02,version = int(_01),int(_02),int(version)
        
        
        if _10 == 'Sí':
            n_jorneys = str(number_entry.get())
            validar_numero_dato1(n_jorneys)
            _40,_42,_43 = 'No aplica','No aplica','No aplica'
            
        else:
            n_jorneys = 0
            _40 = [opcion for opcion ,var  in opciones_3.items() if var.get()]
            valor_no_unico_lista(_40)
            _40 = ",".join(_40)
            _42 = str(campo_numero_etiqueta_idd42.get())
            validar_numero_dato1(_42)
            _43 = str(campo_nombre_etiqueta_nombre43.get())
            vacio(_43)
            longitud(int(_42),_43)
        
        #validar_numero_dato1(_42)
        
        #TEXTO
        _03   = str(campo_nombre_etiqueta_nombre03.get())
        vacio(_03)
        _04   = str(campo_nombre_etiqueta_nombre04.get())
        vacio(_04)
        _05   = str(campo_nombre_etiqueta_nombre05.get())
        vacio(_05)
        _08   = str(campo_nombre_etiqueta_nombre08.get())
        vacio(_08)
        _11   = str(campo_nombre_etiqueta_nombre11.get())
        vacio(_11)
        _12   = str(campo_nombre_etiqueta_nombre12.get()) 
        vacio(_12)
        _13   = str(campo_nombre_etiqueta_nombre13.get())
        vacio(_13)
        _15   = str(campo_nombre_etiqueta_nombre15.get())
        vacio(_15)
        _16   = str(campo_nombre_etiqueta_nombre16.get())
        vacio(_16)
        _18   = str(campo_nombre_etiqueta_nombre18.get())
        vacio(_18)
        _19   = str(campo_nombre_etiqueta_nombre19.get())
        vacio(_19)
        _21   = str(campo_nombre_etiqueta_nombre21.get())
        vacio(_21)
        _22 = str(campo_nombre_etiqueta_nombre22.get())
        vacio(_22)
        _23 = str(campo_nombre_etiqueta_nombre23.get())
        vacio(_23)
        _24 = str(campo_nombre_etiqueta_nombre24.get())
        vacio(_24)
        _25 = str(campo_nombre_etiqueta_nombre25.get())
        vacio(_25)
        _26 = str(campo_nombre_etiqueta_nombre26.get())
        vacio(_26)
        _27 = str(campo_nombre_etiqueta_nombre27.get())
        vacio(_27)
        _28 = str(campo_nombre_etiqueta_nombre28.get())
        vacio(_28)
        _29 = str(campo_nombre_etiqueta_nombre29.get())
        vacio(_29)
        _30 = str(campo_nombre_etiqueta_nombre30.get())
        vacio(_30)
        _31 = str(campo_nombre_etiqueta_nombre31.get())
        vacio(_31)
        _47 = str(campo_nombre_etiqueta_nombre47.get())
        vacio(_47)
        _48 = str(campo_nombre_etiqueta_nombre48.get())
        vacio(_48)
        _49 = str(campo_nombre_etiqueta_nombre49.get())
        vacio(_49)
        _50 = str(campo_nombre_etiqueta_nombre50.get())
        vacio(_50)
        _51 = str(campo_nombre_etiqueta_nombre51.get())
        vacio(_51)
        _52 = str(campo_nombre_etiqueta_nombre52.get())
        vacio(_52)
        
        



     

        #FECHA
        _34  = campo_fecha_etiqueta_fecha34.get()
        validar_fecha(_34)
        _35  = campo_fecha_etiqueta_fecha35.get()
        validar_fecha(_35)
        validar_coherencia_fechas(_34,_35)
        _37  = campo_fecha_etiqueta_fecha37.get()
        validar_fecha(_37)
        _38  = campo_fecha_etiqueta_fecha38.get()
        validar_fecha(_38)
        validar_coherencia_fechas(_37,_38)

        _34=datetime.strptime(_34,'%d/%m/%Y')
        _35=datetime.strptime(_35,'%d/%m/%Y')
        _37=datetime.strptime(_37,'%d/%m/%Y')
        _38=datetime.strptime(_38,'%d/%m/%Y')
        
        
        #Unicampos de entrada

        _06 = uni_campo_etiqueta_lista06.get()
        valor_unico_lista(_06)
        _07 = uni_campo_etiqueta_lista07.get()
        valor_unico_lista(_07)
        _14 = uni_campo_etiqueta_lista14.get()
        valor_unico_lista(_14)
        _17 = uni_campo_etiqueta_lista17.get()
        valor_unico_lista(_17)
        _32 = uni_campo_etiqueta_lista32.get()
        valor_unico_lista(_32)
        _33 = uni_campo_etiqueta_lista33.get()
        valor_unico_lista(_33)
        _36 = uni_campo_etiqueta_lista36.get()
        valor_unico_lista(_36)
        _44 = uni_campo_etiqueta_lista44.get()
        valor_unico_lista(_44)
        _45 = uni_campo_etiqueta_lista45.get()
        valor_unico_lista(_45)
        _53 = uni_campo_etiqueta_lista53.get()
        valor_unico_lista(_53)
        _54 = uni_campo_etiqueta_lista54.get()
        valor_unico_lista(_54)
        _55 = uni_campo_etiqueta_lista55.get()
        valor_unico_lista(_55)
        _56 = uni_campo_etiqueta_lista56.get()
        valor_unico_lista(_56)
        _57 = uni_campo_etiqueta_lista57.get()
        valor_unico_lista(_57)
        
        _10= 1 if _10 == 'Sí' else 0
        _14= 1 if _14 == 'Sí' else 0
        _17= 1 if _17 == 'Sí' else 0
        _33= 1 if _33 == 'Sí' else 0
        _36= 1 if _36 == 'Sí' else 0
        _44= 1 if _44 == 'Sí' else 0
        _53= 1 if _53 == 'Sí' else 0
        _54= 1 if _54 == 'Sí' else 0
        _55= 1 if _55 == 'Sí' else 0
        _56= 1 if _56 == 'Sí' else 0
        _57= 1 if _57 == 'Sí' else 0
     
        
              




        #VALIDAR MULTICAMPOS

        _09 = [opcion for opcion ,var  in opciones_1.items() if var.get()]
        valor_no_unico_lista(_09)
        _09 = ",".join(_09)
        _20 = [opcion for opcion ,var  in opciones_2.items() if var.get()]
        valor_no_unico_lista(_20)
        _20 = ",".join(_20)
        _46 = [opcion for opcion ,var  in opciones_4.items() if var.get()]
        valor_no_unico_lista(_46)
        _46 = ",".join(_46)
        
        for uu in [_01,_02,version,_03,_04,_05,_06,_07,_08,_09,_10,n_jorneys,_11,_12,_13,_14,_15,_16,_17,_18,_19,_20,_21,_22,_23,_24,_25,_26,_27,_28,_29,_30,_31,_32,_33,_34,_35,_36,_37,_38,_40,_42,_43,_44,_45,_46,_47,_48,_49,_50,_51,_52,_53,_54,_55,_56,_57]:
            print(type(uu),uu)
        

        
    except ValueError as e:
        tk.messagebox.showerror("Error", str(e))
               


# In[213]:


############### Ventana principal
ventana = tk.Tk()
ventana.title("Demo Excel Brief")
ventana.geometry('850x600')

#crear canvas y scroll bar

canvas = tk.Canvas(ventana)
scrollbar = tk.Scrollbar(ventana,orient="vertical",command=canvas.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)


canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)


frame = tk.Frame(canvas)
canvas.create_window((0,0),window=frame,anchor="nw")

#JOURNEYS

def on_frame(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    

frame.bind("<Configure>",on_frame)

################# Etiquetas

valores_journey = []

number_label = Label(frame, text ="CUANTOS JOURNES DESEA")
number_entry = Entry(frame)
btn = Button(frame, text ="IR A JOURNES \n SOLO SÍ LA \n RESPUESTA ES SÍ")

btn.bind("<Button>", lambda e: NewWindow(frame, number_entry.get(), valores_journey))


#NUMERO
etiqueta_idd01 = tk.Label(frame, text="D.0.1-ID CAMPAÑA")
etiqueta_idd02 = tk.Label(frame, text=" \n N.0.2-ID BRIEF \n \n Versión")

#TEXTO
etiqueta_nombre03 = tk.Label(frame, text="N.1.1-Nombre de la campaña")
etiqueta_nombre04 = tk.Label(frame, text="N.1.2-Solicitante")
etiqueta_nombre05 = tk.Label(frame, text="N.1.3-Detalle de la campaña")
#UNILISTA
etiqueta_lista06 = tk.Label(frame, text="N.1.4-DIRECCION SOLICITANTE")
etiqueta_lista07 = tk.Label(frame, text="N.2.1-Fase del ciclo de vida:")
#TEXTO
etiqueta_nombre08 = tk.Label(frame, text="N.2.2-Objetivo:¿QUÉ QUIERO COMUNICAR?")
#MULTILISTA
etiqueta_lista09 = tk.Label(frame, text="N.2.3-TIPOLOGÍA")
#Unilista
etiqueta_lista10 = tk.Label(frame, text="N.2.3.1-¿La comunicación va por Jorney?")


#TEXTO
etiqueta_nombre11 = tk.Label(frame, text="N.2.4-¿A QUIÉN LE QUIERO COMUNICAR?")
etiqueta_nombre12 = tk.Label(frame, text="N.2.5-¿EN QUÉ AMBITO TERRITORIAL?")
etiqueta_nombre13 = tk.Label(frame, text="N.2.6-¿QUÉ ESPERO QUE HAGA EL CLIENTE?")
#UNILISTA
etiqueta_lista14 = tk.Label(frame, text="N.2.7-CALL TO ACTION")
#TEXTO
etiqueta_nombre15 = tk.Label(frame, text="I.2.8-INSERTAR VÍNCULO")
etiqueta_nombre16 = tk.Label(frame, text="N.2.9-¿QUÉ BENEFICIO LE DEJA ESTA INICIATIVA AL BANCO?")
#UNILISTA
etiqueta_lista17 = tk.Label(frame, text="N.2.10-¿SE CUENTA CON PRESUPUESTO APROBADO?")
#TEXTO
##
##
##
##ES UN VALOR CONDICIONAL
etiqueta_nombre18 = tk.Label(frame, text="N.2.11-¿DE QUÉ ÁREA PROVIENE?")
etiqueta_nombre19 = tk.Label(frame, text="N.2.12-LEGALES")
#MULTILISTA
etiqueta_lista20 = tk.Label(frame, text="I.3.1-SEGMENTOS")
#TEXTO
etiqueta_nombre21 = tk.Label(frame, text="D.3.2-Filtros aplicables para  \n todas las comunicaciones")
etiqueta_nombre22 = tk.Label(frame, text="D.3.3-Filtros aplicables para  \n  todas las comunicaciones SMS")
etiqueta_nombre23 = tk.Label(frame, text="D.3.4-Filtros aplicables para  \n  todas las comunicaciones MAIL")
etiqueta_nombre24 = tk.Label(frame, text="D.3.5-Filtros aplicables para  \n  todas las comunicaciones CSS OUT y TLMK Externo")
etiqueta_nombre25 = tk.Label(frame, text="D.3.6-Filtros aplicables para  \n  todas las comunicaciones ATM")
etiqueta_nombre26 = tk.Label(frame, text="D.3.7-Filtros aplicables para  \n  todas las comunicaciones REDES SOCIALES")
etiqueta_nombre27 = tk.Label(frame, text="I.3.8-Filtros especificos SMS")
etiqueta_nombre28 = tk.Label(frame, text="I.3.9-Filtros especificos MAIL")
etiqueta_nombre29 = tk.Label(frame, text="I.3.10-Filtros especificos  \n  CSS OUT y TLMK Externo")
etiqueta_nombre30 = tk.Label(frame, text="I.3.11-Filtros especificos ATM")
etiqueta_nombre31 = tk.Label(frame, text="I.3.12-Filtros especificos  \n  Redes Sociales")
#UNILISTA
etiqueta_lista32 = tk.Label(frame, text="N.4.1-PERIODICIDAD")
etiqueta_lista33 = tk.Label(frame, text="N.4.2-¿SERÁ UNA COMUNICACIÓN PERMANENTE?")
#FECHA
etiqueta_fecha34 = tk.Label(frame, text="N.4.3-Inicio periodo activo  \n  de la comunicación (dd/mm/aaaa)")
etiqueta_fecha35 = tk.Label(frame, text="N.4.4-Fin periodo activo  \n  de la comunicación (dd/mm/aaaa)")
#UNILISTA
etiqueta_lista36 = tk.Label(frame, text="N.4.5-¿TIENE UNA PROMOCIÓN \n ASOCIADA LA COMUNICACIÓN?")
#FECHA
etiqueta_fecha37 = tk.Label(frame, text="N.4.6-Inicio Vigencia  \n  de la oferta (dd/mm/aaaa)")
etiqueta_fecha38= tk.Label(frame,  text="N.4.7-Fin de Vigencia  \n  de la oferta(dd/mm/aaaa)")
#CHARLY DESARROLLO 4.8
etiqueta_archivo39= tk.Label(frame,  text="N.4.8-Archivo soporte \n de programación de calendario")
guardar = tk.Button(frame,text='Guardar Archivo', command=UploadFile)



#5 ES CONDICIONAL DE 2.3.1
#Multilista
etiqueta_lista40 = tk.Label(frame, text="N.5.1-Canal sugerido para  \n el envio de comunicación")

#CHARLY DESARROLLO 5.1.2  multiple archivos maximo 15 

#NUMERO
#
#
#
#ESTO HACE QUE FUNCIONE UN CONDICIONAL
etiqueta_idd42 = tk.Label(frame, text="D.5.1.2-Longitud del mensaje")
#TEXTO
etiqueta_nombre43 = tk.Label(frame, text="D.5.1.3-Inserte el texto si aplica SMS")
guardar2 = tk.Button(frame,text='Inserte archivo con \n nombre por canal', command=UploadFile)

#UNILISTA
etiqueta_lista44 = tk.Label(frame, text="N.6.1-¿APLICA MEDICIÓN?")
etiqueta_lista45 = tk.Label(frame, text="N.6.2-PERIODICIDAD")
#Multilista
etiqueta_lista46 = tk.Label(frame, text="N.6.3-TIPO KPI")                             
#TEXTO
etiqueta_nombre47 = tk.Label(frame, text="N.6.4-Describir a detalle los KPIs solicitados")
etiqueta_nombre48 = tk.Label(frame, text="N.7.1-Responsable de Negocio")
etiqueta_nombre49 = tk.Label(frame, text="I.7.2-Responsable de Marketing")
etiqueta_nombre50 = tk.Label(frame, text="D.7.3-Responsable de Ejecución")
etiqueta_nombre51 = tk.Label(frame, text="D.7.4-Responsable de CRM")
etiqueta_nombre52 = tk.Label(frame, text="D.7.5-Responsable de Incidencias")

 #UNILISTA
etiqueta_lista53 = tk.Label(frame, text="N.7.5-¿Se cuenta con plantillas  avaladas por Jurídico?")
etiqueta_lista54 = tk.Label(frame, text="N.7.6-¿Se cuenta con plantillas avaladas por Contraloría?")
etiqueta_lista55 = tk.Label(frame, text="N.7.7-¿Se cuenta con plantillas avaladas por Marca(Publicidad)?")
etiqueta_lista56 = tk.Label(frame, text="N.7.8-¿Se cuenta con plantillas avaladas por \n CISO (solo aplica en el caso de OTP \n y si en el texto de SMS o email enviarán una URL.)?")
etiqueta_lista57 = tk.Label(frame, text="N.7.9-¿Se cuenta con plantillas avaladas por Propiedad intelectual?")
   
#guardar
guardar3 = tk.Button(frame,text='Insertar documentos que avalen \n VoBos con nombre específico por área', command=UploadFile)

    
#CHARLY DESARROLLO 7.5
#CHARLY DESARROLLO 7.6
#CHARLY DESARROLLO 7.7
#CHARLY DESARROLLO 7.8
#CHARLY DESARROLLO 7.9  
                             

opciones_1 = {}
opciones_2 = {}
opciones_3 = {}
opciones_4 = {}
opciones_5 = {}


############# Campos de entrada
letiqueta_lista06=['Aclaraciones','Adquisición','Alianzas Comerciales','Autorización','Cobrand','Contact Center','Estrategia, Aceptación y Prevención Fraude','Retención','Recuperaciones','Producto','Prevención Fraude MdP','Prevención de Fraude Canales','Unique Rewards','Facturación']
letiqueta_lista07=['Adquisición','Tracking','On Boarding Activación (0-15 días)','Onboarding Uso temprano (15-30 días)','Recurrencia (30-45 días)','Reactivación de clientes (Día 60)','Postcancelación','Cancelación','Aniversario','Relacional','Retención','Reactivación','Cross selling','Up selling','Clientes Stock','Propensión a cancelación (+120 días)','Propensión a no uso (Día 90)']
letiqueta_lista09=['Transaccional',  'Informativa', 'Comercial', 'Normativa', 'Relacional']

lsino=['Sí', 'No']
#14,17,33,36,44,45,53,54,55,56,57

letiqueta_lista20=['Clásicos y Preferentes',  'Select', 'Select Black', 'Banca Privada']
letiqueta_lista32=['Diaria','Semanal','Quincenal','Mensual','Trimestral','Cuatrimestral','Contingente','One Shot','RT','N/A'] 
letiqueta_lista40=['Email','SMS','Doble Vía','Push','Pop Up','Banner','STV','TV','Cine','Radio','Prensa','Whatsapp','Redes Sociales','Sucursales','Contac Center IN','Contac Center OUT','ATM','Intranet','Cell Blaster']
letiqueta_lista46=['Volumen de envíos','Transferencia de puntos','Redención de puntos en POS','Incremento en línea de crédito','Retención','Transccionalidad','Contratación','Click Rate','Otros','Redención de puntos','Acumulación de puntos','Incremento de facturación','Churn','Activación','Conversion Rate','Open rate']
letiqueta_lista45=['Diaria','Semanal','Quincenal','Mensual','Trimestral','Cuatrimestral','Contingente','One Shot','RT','N/A','Termino de Campaña'] 
                             
                             


#campos texto



#NUMERO
campo_numero_etiqueta_idd01 = tk.Entry(frame)
campo_numero_etiqueta_idd02 = tk.Entry(frame)
campo_numero_etiqueta_idd022 = tk.Entry(frame)
campo_numero_etiqueta_idd42 = tk.Entry(frame)
                             

#TEXTO
campo_nombre_etiqueta_nombre03 = tk.Entry(frame)
campo_nombre_etiqueta_nombre04 = tk.Entry(frame)
campo_nombre_etiqueta_nombre05 = tk.Entry(frame)
campo_nombre_etiqueta_nombre08 = tk.Entry(frame)
campo_nombre_etiqueta_nombre11 = tk.Entry(frame)
campo_nombre_etiqueta_nombre12 = tk.Entry(frame)
campo_nombre_etiqueta_nombre13 = tk.Entry(frame)
campo_nombre_etiqueta_nombre15 = tk.Entry(frame)
campo_nombre_etiqueta_nombre16 = tk.Entry(frame)
campo_nombre_etiqueta_nombre18 = tk.Entry(frame)
campo_nombre_etiqueta_nombre19 = tk.Entry(frame)
campo_nombre_etiqueta_nombre21 = tk.Entry(frame)
campo_nombre_etiqueta_nombre22 = tk.Entry(frame)
campo_nombre_etiqueta_nombre23 = tk.Entry(frame)
campo_nombre_etiqueta_nombre24 = tk.Entry(frame)
campo_nombre_etiqueta_nombre25 = tk.Entry(frame)
campo_nombre_etiqueta_nombre26 = tk.Entry(frame)
campo_nombre_etiqueta_nombre27 = tk.Entry(frame)
campo_nombre_etiqueta_nombre28 = tk.Entry(frame)
campo_nombre_etiqueta_nombre29 = tk.Entry(frame)
campo_nombre_etiqueta_nombre30 = tk.Entry(frame)                           
campo_nombre_etiqueta_nombre31 = tk.Entry(frame)
campo_nombre_etiqueta_nombre43 = tk.Entry(frame)
campo_nombre_etiqueta_nombre47 = tk.Entry(frame)
campo_nombre_etiqueta_nombre48 = tk.Entry(frame)
campo_nombre_etiqueta_nombre49 = tk.Entry(frame)
campo_nombre_etiqueta_nombre50 = tk.Entry(frame)
campo_nombre_etiqueta_nombre51 = tk.Entry(frame)
campo_nombre_etiqueta_nombre52 = tk.Entry(frame)



#FECHA
campo_fecha_etiqueta_fecha34 = tk.Entry(frame)
campo_fecha_etiqueta_fecha35 = tk.Entry(frame)
campo_fecha_etiqueta_fecha37 = tk.Entry(frame)
campo_fecha_etiqueta_fecha38 = tk.Entry(frame)

#archivo



#Unicampos de entrada

uni_campo_etiqueta_lista06 = ttk.Combobox(frame,values=letiqueta_lista06)
uni_campo_etiqueta_lista07 = ttk.Combobox(frame,values=letiqueta_lista07)

valor_combobox = tk.StringVar()

#uni_campo_etiqueta_lista10 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista10 = ttk.Combobox(root, textvariable=valor_combobox, values=lsino)
valor_combobox.trace("w", verificar_entrada)

uni_campo_etiqueta_lista14 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista17 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista32 = ttk.Combobox(frame,values=letiqueta_lista32)
uni_campo_etiqueta_lista33 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista36 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista44 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista45 = ttk.Combobox(frame,values=letiqueta_lista45)
uni_campo_etiqueta_lista53 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista54 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista55 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista56 = ttk.Combobox(frame,values=lsino)
uni_campo_etiqueta_lista57 = ttk.Combobox(frame,values=lsino)

#multi campos de entrada
multi_campo_etiqueta_mlista09 = [opcion for opcion, var in opciones_1.items() if var.get()]
multi_campo_etiqueta_mlista20 = [opcion for opcion, var in opciones_2.items() if var.get()]
multi_campo_etiqueta_mlista40 = [opcion for opcion, var in opciones_3.items() if var.get()]
multi_campo_etiqueta_mlista46 = [opcion for opcion, var in opciones_4.items() if var.get()]


#INSERTAR 3 COLUMNAS



#Acomodo de botones

#meter 3 columnas
number_label.grid(row = 9, column=1)
number_entry.grid(row=9,column=2,columnspan=1)
btn.grid(row=9, column=3,columnspan=2)
                             
#insertar archivos
etiqueta_archivo39.grid(row=38, column=0, columnspan=1)
guardar.grid(row=38, column=1)
    
guardar2.grid(row=42, column=2)

guardar3.grid(row=57, column=0)
#NUMERO
                             
                             
etiqueta_idd01.grid(row=0, column=0)
campo_numero_etiqueta_idd01.grid(row=0, column=1)

etiqueta_idd02.grid(row=1, column=0)
campo_numero_etiqueta_idd02.grid(row=1, column=1,rowspan =1,pady =10)
campo_numero_etiqueta_idd022.grid(row=1, column=1,rowspan =2,pady =50)

etiqueta_idd42.grid(row=41, column=0)
campo_numero_etiqueta_idd42.grid(row=41, column=1)





                             


#NOMBRE
etiqueta_nombre03.grid(row=2, column=0)
campo_nombre_etiqueta_nombre03.grid(row=2, column=1)
etiqueta_nombre04.grid(row=3, column=0)
campo_nombre_etiqueta_nombre04.grid(row=3, column=1)
etiqueta_nombre05.grid(row=4, column=0)
campo_nombre_etiqueta_nombre05.grid(row=4, column=1)
etiqueta_nombre08.grid(row=7, column=0 )
campo_nombre_etiqueta_nombre08.grid(row=7, column=1) 

etiqueta_nombre11.grid(row=10, column=0 )
campo_nombre_etiqueta_nombre11.grid(row=10, column=1)
etiqueta_nombre12.grid(row=11, column=0 )
campo_nombre_etiqueta_nombre12.grid(row=11, column=1) 
etiqueta_nombre13.grid(row=12, column=0 )
campo_nombre_etiqueta_nombre13.grid(row=12, column=1) 
etiqueta_nombre15.grid(row=14, column=0 )
campo_nombre_etiqueta_nombre15.grid(row=14, column=1) 
etiqueta_nombre16.grid(row=15, column=0)
campo_nombre_etiqueta_nombre16.grid(row=15, column=1)
etiqueta_nombre18.grid(row=17, column=0)
campo_nombre_etiqueta_nombre18.grid(row=17, column=1)
etiqueta_nombre19.grid(row=18, column=0)
campo_nombre_etiqueta_nombre19.grid(row=18, column=1)
etiqueta_nombre21.grid(row=20, column=0 )
campo_nombre_etiqueta_nombre21.grid(row=20, column=1) 
etiqueta_nombre22.grid(row=21, column=0 )
campo_nombre_etiqueta_nombre22.grid(row=21, column=1) 
etiqueta_nombre23.grid(row=22, column=0 )
campo_nombre_etiqueta_nombre23.grid(row=22, column=1) 

                             
                             
                             
etiqueta_nombre24.grid(row=23,column=0) 
campo_nombre_etiqueta_nombre24.grid(row=23,column=1)
etiqueta_nombre25.grid(row=24,column=0)  
campo_nombre_etiqueta_nombre25 .grid(row=24,column=1)
etiqueta_nombre26.grid(row=25,column=0)  
campo_nombre_etiqueta_nombre26 .grid(row=25,column=1)
etiqueta_nombre27.grid(row=26,column=0) 
campo_nombre_etiqueta_nombre27.grid(row=26,column=1)
etiqueta_nombre28.grid(row=27,column=0)  
campo_nombre_etiqueta_nombre28 .grid(row=27,column=1)
etiqueta_nombre29.grid(row=28,column=0)  
campo_nombre_etiqueta_nombre29 .grid(row=28,column=1)
etiqueta_nombre30.grid(row=29,column=0)                         
campo_nombre_etiqueta_nombre30.grid(row=29,column=1)      
etiqueta_nombre31.grid(row=30,column=0) 
campo_nombre_etiqueta_nombre31.grid(row=30,column=1)
etiqueta_nombre43.grid(row=42,column=0) 
campo_nombre_etiqueta_nombre43.grid(row=42,column=1)
etiqueta_nombre47.grid(row=46,column=0) 
campo_nombre_etiqueta_nombre47.grid(row=46,column=1)
etiqueta_nombre48.grid(row=47,column=0) 
campo_nombre_etiqueta_nombre48.grid(row=47,column=1)
etiqueta_nombre49.grid(row=48,column=0) 
campo_nombre_etiqueta_nombre49.grid(row=48,column=1)
etiqueta_nombre50.grid(row=49,column=0) 
campo_nombre_etiqueta_nombre50.grid(row=49,column=1)
etiqueta_nombre51.grid(row=50,column=0) 
campo_nombre_etiqueta_nombre51.grid(row=50,column=1) 
etiqueta_nombre52.grid(row=51,column=0)                            
campo_nombre_etiqueta_nombre52.grid(row=51,column=1)                            



#FECHA
etiqueta_fecha34.grid(row=33,column=0)
campo_fecha_etiqueta_fecha34.grid(row=33,column=1)                             
etiqueta_fecha35.grid(row=34,column=0)
campo_fecha_etiqueta_fecha35.grid(row=34,column=1)                             
etiqueta_fecha37.grid(row=36,column=0)
campo_fecha_etiqueta_fecha37.grid(row=36,column=1)                             
etiqueta_fecha38.grid(row=37,column=0)
campo_fecha_etiqueta_fecha38.grid(row=37,column=1)                             


#Unicampos de entrada

etiqueta_lista06.grid(row=5,column=0)
uni_campo_etiqueta_lista06.grid(row=5,column=1)                             
etiqueta_lista07.grid(row=6,column=0)
uni_campo_etiqueta_lista07.grid(row=6,column=1)   
etiqueta_lista10.grid(row=9,column=0)
uni_campo_etiqueta_lista10.grid(row=9,column=1)   

etiqueta_lista14.grid(row=13,column=0)
uni_campo_etiqueta_lista14.grid(row=13,column=1)                             
etiqueta_lista17.grid(row=16,column=0)
uni_campo_etiqueta_lista17.grid(row=16,column=1)                             
etiqueta_lista32.grid(row=31,column=0)
uni_campo_etiqueta_lista32.grid(row=31,column=1)                             
etiqueta_lista33.grid(row=32,column=0)
uni_campo_etiqueta_lista33.grid(row=32,column=1)                             
etiqueta_lista36.grid(row=35,column=0)
uni_campo_etiqueta_lista36.grid(row=35,column=1)                             
etiqueta_lista44.grid(row=43,column=0)
uni_campo_etiqueta_lista44.grid(row=43,column=1)                             
etiqueta_lista45.grid(row=44,column=0)
uni_campo_etiqueta_lista45.grid(row=44,column=1)                             
etiqueta_lista53.grid(row=52,column=0)
uni_campo_etiqueta_lista53.grid(row=52,column=1)                             
etiqueta_lista54.grid(row=53,column=0)
uni_campo_etiqueta_lista54.grid(row=53,column=1)                             
etiqueta_lista55.grid(row=54,column=0)
uni_campo_etiqueta_lista55.grid(row=54,column=1)                             
etiqueta_lista56.grid(row=55,column=0)
uni_campo_etiqueta_lista56.grid(row=55,column=1)                             
etiqueta_lista57.grid(row=56,column=0)
uni_campo_etiqueta_lista57.grid(row=56,column=1)                             
                             

#multi campos de entrada
multi_campo_etiqueta_mlista09 = [opcion for opcion, var in opciones_1.items() if var.get()]
multi_campo_etiqueta_mlista20 = [opcion for opcion, var in opciones_2.items() if var.get()]
multi_campo_etiqueta_mlista40 = [opcion for opcion, var in opciones_3.items() if var.get()]
multi_campo_etiqueta_mlista46 = [opcion for opcion, var in opciones_4.items() if var.get()]
                           



#MULTILISTA




etiqueta_lista09.grid(row=8, column=0 ) 
etiqueta_lista20.grid(row=19, column=0 ) 
etiqueta_lista40.grid(row=39, column=0 ) 
etiqueta_lista46.grid(row=45, column=0 ) 




frame_1 = tk.Frame(frame)
frame_1.grid(row=8, column=1, sticky='nw')  # Coloca el frame en la fila 0, columna 1
tk.Label(frame_1, text="Opciones del Grupo 1").grid(row=0, column=0, sticky='w')
for index, item in enumerate(letiqueta_lista09):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_1, text=item, variable=var)
    chk.grid(row=index+1, column=0, sticky='w')  # Coloca cada casilla de verificación en su propia fila
    opciones_1[item] = var
    
frame_2 = tk.Frame(frame)
frame_2.grid(row=19, column=1, sticky='nw')  # Coloca el frame en la fila 0, columna 1
tk.Label(frame_2, text="Opciones del Grupo 2").grid(row=0, column=0, sticky='w')
for index, item in enumerate(letiqueta_lista20):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_2, text=item, variable=var)
    chk.grid(row=index+1, column=0, sticky='w')  # Coloca cada casilla de verificación en su propia fila
    opciones_2[item] = var
    
frame_3 = tk.Frame(frame)
frame_3.grid(row=39, column=1, sticky='nw')  # Coloca el frame en la fila 0, columna 1
tk.Label(frame_3, text="Opciones del Grupo 3").grid(row=0, column=0, sticky='w')
for index, item in enumerate(letiqueta_lista40):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_3, text=item, variable=var)
    chk.grid(row=index+1, column=0, sticky='w')  # Coloca cada casilla de verificación en su propia fila
    opciones_3[item] = var

frame_4 = tk.Frame(frame)
frame_4.grid(row=45, column=1, sticky='nw')  # Coloca el frame en la fila 0, columna 1
tk.Label(frame_4, text="Opciones del Grupo 4").grid(row=0, column=0, sticky='w')
for index, item in enumerate(letiqueta_lista46):
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_4, text=item, variable=var)
    chk.grid(row=index+1, column=0, sticky='w')  # Coloca cada casilla de verificación en su propia fila
    opciones_4[item] = var



    
    
    
# Botones
boton_ok = tk.Button(frame, text="Aceptar", command=lambda: validar_datos())
boton_ok.grid(row=60,column=1)


# Función para validar los datos ingresados

# Ejecutar la aplicación
ventana.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




