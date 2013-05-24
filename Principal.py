#~ #! /usr/bin/env python3
# -*- coding:utf-8 -*-
from gi.repository import Gtk
import psycopg2             #para conexion con base de datos
import gtk
from datetime import date
#import pygtk

#comentario web1
#comentario  maquina 1
=======
#modificar web
>>>>>>> 0a312d19f16e3bd34be9dc39b96fd60fb505e10e
def llenar_estado(combo):
	##cnxn = psycopg2.connect("dbname=Prueba user=postgres password=hjesustb")
	#cnxn = psycopg2.connect("dbname=postgres  user=postgres password=123456")
	cnxn = psycopg2.connect("host=127.0.0.1 dbname=postgres  user=postgres password=123456")
	#cnxn = psycopg2.connect(PostgreSQL30)
	cursor = cnxn.cursor()
	cursor.execute("select * from estado")
	name_store = Gtk.ListStore(str )
	while 1:
		row = cursor.fetchone()
		if not row:
			break
		name_store.append([  row[1]  ])
	combo.set_model(name_store)
	render = Gtk.CellRendererText()
	combo.pack_start(render, True)
	combo.add_attribute(render, 'text', 0)  # agrega la descripcion si pongo 1 agrega el estado
	cursor.close
	cnxn.close

def llenar_combo(Laboratorio, Diagnostico,vista  ,  Digitador , cmbConsultaHisEstado):
	##cnxn = psycopg2.connect("dbname=Prueba user=postgres password=hjesustb")
#	cnxn = psycopg2.connect("dbname=postgres  user=postgres password=123456")
	cnxn = psycopg2.connect("host=127.0.0.1 dbname=postgres  user=postgres password=123456")
	cursor = cnxn.cursor()
	cursor.execute("select * from uno")
	name_store = Gtk.ListStore(str ,int)
	while 1:
		row = cursor.fetchone()
		if not row:
			break
		name_store.append([  row[1] , row[2] ])
	Laboratorio.set_model(name_store)
	render = Gtk.CellRendererText()
	Laboratorio.pack_start(render, True)
	Laboratorio.add_attribute(render, 'text', 0)  # agrega la descripcion si pongo 1 agrega el estado

	Digitador.set_model(name_store)
	Digitador.pack_start(render, True)
	Digitador.set_active(0)
	Digitador.add_attribute(render, 'text', 0)
    #Digitador.set_text_column(0)
	#Digitador.add_attribute(render, 'text', 0)  # agrega la descripcion si pongo 1 agrega el estado
    
	cursor = cnxn.cursor()
	cursor.execute("select * from uno")

	name_store1 = Gtk.ListStore(int, str ,int, str)

	for fila  in cursor.fetchall():
		name_store1.append(fila)

	cellp1=Gtk.CellRendererText()
	col1=Gtk.TreeViewColumn('Id', cellp1, text=0)
	vista.append_column(col1)

	cellp2=Gtk.CellRendererText()
	col2=Gtk.TreeViewColumn('Nombre', cellp2, text=1)
	vista.append_column(col2)
    
    
	cellp3=Gtk.CellRendererText()
	col3=Gtk.TreeViewColumn('IdArea', cellp3, text=2)
	vista.append_column(col3)
    
	cellp4=Gtk.CellRendererText()
	col4=Gtk.TreeViewColumn('dni', cellp4, text=3)
	vista.append_column(col4)


	vista.set_model(name_store1)
	vista.show()
	
    # agrega la descripcion si pongo 1 agrega el estado
    #vista.append_column(columna)
	#vista2.set_model(name_store2)
	##vista.append_column(columna)
	#vista2.show()
    #vista.set_text_column(0)
	cursor.execute("select * from uno1")
	name_store = Gtk.ListStore(str ,int)
	while 1:
		row = cursor.fetchone()
		if not row:
			break
		name_store.append([  row[1] , row[2] ])
	Diagnostico.set_model(name_store)
	render = Gtk.CellRendererText()
	Diagnostico.pack_start(render, True)
	Diagnostico.add_attribute(render, 'text', 0)  # agrega la descripcion si pongo 1 agrega el estado
    
	cursor.execute("select * from estado")
	name_store = Gtk.ListStore( str )
	while 1:
		row = cursor.fetchone()
		if not row:
			break
		name_store.append([   row[1] ])
	cmbConsultaHisEstado.set_model(name_store)
	render = Gtk.CellRendererText()
	cmbConsultaHisEstado.pack_start(render, True)
	cmbConsultaHisEstado.add_attribute(render, 'text', 0)  # agrega la descripcion si pongo 1 agrega el estado
    
	
    
	#establecimientos = ['Cajamarca', 'Magdalena', 'Cutervo','Celendin', 'San Marcos']
	#name_store = Gtk.ListStore(str)
	#for puestos in establecimientos:
		#name_store.append([puestos])
	#combo.set_model(name_store)
	#render = Gtk.CellRendererText()
	#combo.pack_start(render, True)
	#combo.add_attribute(render, 'text', 0)
	cursor.close
	cnxn.close
    
def valor_combobox(combobox):
    modelo = combobox.get_model()
    activo = combobox.get_active()
    if activo < 0:
        return None
    return modelo[activo][0]
def cambiarTexto():
    # obtenemos de la descripción de la interfaz
    # aquel objeto que deseamos acceder (label1 y entry1)
    # accedemos a sus métodos para obtener el texto del entry1
    # y poner ese texto en el label1
    lbl = builder.get_object("txtLote")
    txtentry = builder.get_object("txtNumeroFormularios")
    lbl.set_text(txtentry.get_text())
        # combobox2.additem("gggg") UN COMBO NO TIENE EL ATRIBUTO ADDITEM
        # ESTA FUNCION NO TIENE SENTIDO, TIENES QUE USAR UNA FUNCIÓN QUE TE  PERMITA
        # LLENAR UNA LISTSTRORE PRIMERO, LUEGO CREAS EL MODELO Y LO POBLAS CON EL RENDER
class Gui:
    """Clase que crea la interfaz de usuario"""
    def __init__ (self):
        """Inicialización de la interface"""

        build = Gtk.Builder()
        #build.add_from_file("VentanaHis.glade")
        build.add_from_file("VentanaHis14.glade")
        

        # Cargar las ventanas
        self.window2 = build.get_object("window2")
        self.window1 = build.get_object("window1")
        self.window3 = build.get_object("window3")
        self.ConsultaHis = build.get_object("ConsultaHis")

        # AQUI-1
        self.txtentry = (build.get_object("txtNumeroFormularios"))
        self.lbl = (build.get_object("txtLote"))

        ############coger valores d ventana 1 
        self.Digitador=build.get_object("cmbDigitador")
        self.Ups=build.get_object("cmbUps")
        self.ResponsableAtencion=build.get_object("cmbResp")
        self.Lote=build.get_object("txtLote")
        self.NumeroFormularios=build.get_object("txtNumeroFormularios")
        self.Anio=build.get_object("txtAño")
        self.Mes=build.get_object("txtMes")
        self.btnPersona=build.get_object("btnPersona")
            ########desahbiliatar botones  para validar buen regustro de informacion
        self.NumeroFormularios.set_property("editable", False)
        self.Anio.set_property("editable", False)
        self.Mes.set_property("editable", False)
        
        self.Dni=build.get_object("cmbDni")
        self.Nombre=build.get_object("cmbNombre")
        self.Historia=build.get_object("cmbHistoria")
        self.Financiamiento=build.get_object("cmbFinanciamiento")
        self.Dia=build.get_object("txtDia")
        self.Servicio=build.get_object("cmbServicio")
        self.Procedencia=build.get_object("txtProcedencia")
        self.vista=build.get_object("treeview2")

        self.Dia.set_property("editable", False)
        self.Procedencia.set_property("editable", False)
        
        self.Laboratorio=build.get_object("cmbLaboratorio")
        self.Diagnostico=build.get_object("cmbDiagnostico")
            ############# ayuda cuando no ingresen bien la data
        self.AyudaLote=build.get_object("lblAyudaLote")
        self.AyudaNumForm=build.get_object("blAyudaNumForm")
        self.AyudaAnio=build.get_object("lblAyudaAnio")
        self.AyudaMes=build.get_object("lblAyudaMes")
        self.AyudaDia=build.get_object("lblAyudaDia")
        self.AyudaProcedencia=build.get_object("lblAyudaProcedencia")
           ############## botones insertar, elimianr  cancelar
        self.btnEliminar=build.get_object("button3")        
            
        #########################################coger valores d ventana de busqueda window2 
        self.vista2=build.get_object("treeviewBuscar")
        self.DniBuscar=build.get_object("txtDni")
        self.NumeroConsultas=build.get_object("txtNumeroConsulta")

        #################################coger valores d ventana principal window3 
        self.btnSeleccionar=build.get_object("btnSeleccionar")
        self.Seleccionar=build.get_object("txtseleccionar")

        #################################coger valores d ventana principal ConsultaHIS 
        self.btnConsultaHis=build.get_object("btnConsultaHis")
        self.NumeroConsultasHis=build.get_object("txtNumeroConsutasHis")
        self.DetalleconsultaHis=build.get_object("trvConsultaHis")
        self.cmbConsultaHisEstado=build.get_object("cmbConsultaHisEstado")
        self.cmbConsultaHisLote=build.get_object("cmbConsultaHisEstadoLote")
        self.cmbConsultaHisPagina=build.get_object("cmbConsultaHisEstadoPagina")
        self.cmbConsultaHisRegistro=build.get_object("cmbConsultaHisEstadoRegistro")


        build.connect_signals(self)
        
         ##Auto conectar con las señales
        self.window3.show()
        #self.window1.show()

        # Destruir ventana
        #self.window1.connect("delete-event", Gtk.main_quit)
        self.window3.connect("delete-event", Gtk.main_quit)
        
        ###################################################################################activar eventos para lso controles
        self.Lote.connect("key_press_event",self.callback1)
        self.NumeroFormularios.connect("key_press_event",self.callback2)
        #self.Anio.connect("key_press_event",self.callback3)
        #self.Mes.connect("key_press_event",self    .callback4)
        self.Dia.connect("key_press_event",self.callback5)
        self.Procedencia.connect("key_press_event",self.callback6)

        self.btnEliminar.connect("clicked", self.on_button3_clicked) #"on_button_clicked",self.BotonEliminar)
        
        ##########################################################################################llenar_combo
        llenar_combo(self.Laboratorio,self.Diagnostico, self.vista , self.Digitador , self.cmbConsultaHisEstado)
        llenar_estado(self.cmbConsultaHisLote)
        llenar_estado(self.cmbConsultaHisPagina)
        llenar_estado(self.cmbConsultaHisRegistro)
        
        # PRIMERO DEBES LLENAR EL COMBO
        #llenar_combo(self.Establecimiento,self.vista)
        self.Laboratorio.set_active(0)
        self.Diagnostico.set_active(0)
        self.btnPersona.grab_focus()
    
    def on_button3_clicked(self, widget):
        valor=valor_combobox(self.Laboratorio)
        valor2=valor_combobox(self.Diagnostico)
        self.Mes.set_property("editable", True)
        self.txtentry.set_text(self.lbl.get_text())
        self.txtentry.set_text(self.NumeroFormularios.get_text() + " ----" )
        self.txtentry.set_text(valor + " --- " + valor2)
        
    def callback1(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                int(self.Lote.get_text())
                self.NumeroFormularios.grab_focus()
                self.NumeroFormularios.set_property("editable", True)
                self.AyudaLote.set_text("")
            except: 
                self.Lote.grab_focus()
                self.AyudaLote.set_text("Ingrese en formato de numeros")
                
    def callback2(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                int(self.NumeroFormularios.get_text())
                self.Dia.grab_focus()
                self.Dia.set_property("editable", True)
                self.AyudaNumForm.set_text("")
            except: 
                self.NumeroFormularios.grab_focus()
                self.AyudaNumForm.set_text("Ingrese en formato de numeros")

    def callback3(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                int(self.Anio.get_text())
                if len(self.Anio.get_text())==4:
                    self.Mes.grab_focus()
                    self.Mes.set_property("editable", True)
                    self.AyudaAnio.set_text("")
                else:
                    self.Anio.grab_focus()
                    self.AyudaAnio.set_text("Ingrese 4 digitos")
            except: 
                self.Anio.grab_focus()
                self.AyudaAnio.set_text("Ingrese en formato de numeros")
                        
    def callback4(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                int(self.Mes.get_text())
                if len(self.Mes.get_text())<=2:
                    if int(self.Mes.get_text())<=12:
                        self.Digitador.grab_focus()
                        self.Dia.set_property("editable", True)
                        self.AyudaMes.set_text("")
                    else:
                        self.Mes.grab_focus()
                        self.AyudaMes.set_text("Ingrese el mes menor o igual que 12")
                else:
                    self.Mes.grab_focus()
                    self.AyudaMes.set_text("Ingrese maximo 2 digitos")
            except: 
                self.Mes.grab_focus()
                self.AyudaMes.set_text("Ingrese en formato de numeros")
    def callback5(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                int(self.Dia.get_text())
                if len(self.Dia.get_text())<=2:
                    if int(self.Dia.get_text())<=31:
                        self.Procedencia.grab_focus()
                        self.Procedencia.set_property("editable", True)
                        self.AyudaDia.set_text("")
                    else:
                        self.Dia.grab_focus()
                        self.AyudaDia.set_text("Ingrese el numero de dia correcto")
                else:
                    self.Dia.grab_focus()
                    self.AyudaDia.set_text("Ingrese maximo 2 digitos")
            except: 
                self.Dia.grab_focus()
                self.AyudaDia.set_text("Ingrese en formato de numeros")
    def callback6(self,source,event):
        keyname = (event.keyval)
        if keyname==65293:
            try: 
                str(self.Procedencia.get_text())
                if len(self.Procedencia.get_text())!=0:
                    self.Digitador.grab_focus()
                    self.AyudaProcedencia.set_text("")
                else:
                    self.Procedencia.grab_focus()
                    self.AyudaProcedencia.set_text("Ingrese Procedencia")
            except: 
                self.Procedencia.grab_focus()
                self.AyudaProcedencia.set_text("Ingrese en formato de caracteres")
        
        
    def on_txtLote_key_press_event(self, widget, data=None):
        #cogemos el valor de busqueda y le asignamos  a la otra venta
        self.window2.hide()
    def on_btnSalirHis_clicked(self, widget, data=None):
        #cogemos el valor de busqueda y le asignamos  a la otra ventana
        self.window1.hide()
        #self.Seleccionar.Set_Text("")
        self.DniBuscar.set_text("")
        self.btnPersona.grab_focus()

        #####################################################################################btnSeleccionar
        

############################################################################################ Botnes de pantalla windows 2        
    def on_button12_clicked(self, widget, data=None):
        #cogemos el valor de busqueda y le asignamos  a la otra ventana
        for column in self.vista2.get_columns():
            if column:
                self.vista2.remove_column(column)
        aa=self.DniBuscar.get_text()
        self.DniBuscar.set_text("")
        self.window2.hide()
        self.Lote.set_text(aa)
        self.btnPersona.grab_focus()

    def on_btnBuscarDni_clicked(self, widget, data=None):
        #eliminar columnas para no repretir
        VarVer=self.NumeroConsultas.get_text()
        for column in self.vista2.get_columns():
            if column:
                self.vista2.remove_column(column)        
        
        # buscar y caragr el grid con el texto tipeado  
        cnxn = psycopg2.connect("dbname=postgres  user=postgres password=123456")
        cursor = cnxn.cursor()
        filtro=self.DniBuscar.get_text()
        cursor.execute("""select * from uno where descripcion  like '%""" + filtro + """%'""")
        #cursor.execute("""select * from uno """)
        name_store3 = Gtk.ListStore(int , str , int, str)
        for fila  in cursor.fetchall():
            name_store3.append(fila)
        cellp1=Gtk.CellRendererText()
        col1=Gtk.TreeViewColumn('Id', cellp1, text=0)
        self.vista2.append_column(col1)
        
        cellp2=Gtk.CellRendererText()
        col2=Gtk.TreeViewColumn('Nombre', cellp2, text=1)
        self.vista2.append_column(col2)

        cellp3=Gtk.CellRendererText()
        col3=Gtk.TreeViewColumn('IdArea', cellp3, text=2)
        self.vista2.append_column(col3)

        cellp4=Gtk.CellRendererText()
        col4=Gtk.TreeViewColumn('dni', cellp4, text=3)
        self.vista2.append_column(col4)
    
        self.vista2.set_model(name_store3)
        self.vista2.show()
        
        VarVer=int(VarVer) + 1
        self.NumeroConsultas.set_text(str(VarVer))
############################################################################################ Botnes de pantalla windows 2        

################################################################botnes de ventana principal
    def on_btnRegistroHis_clicked(self, widget, data=None):
        self.window1.show()
        d = date.today()
        self.Anio.set_text(str(d.year))
        self.Mes.set_text(str(d.month))
#print "Día: ",d.day
#print "Mes: ",d.month
    def on_btnConsultaHis_clicked(self, widget, data=None):
        self.ConsultaHis.show()
        self.NumeroConsultasHis.set_text("0")

################################################################botnes de ventana principal


############################################################################################ Botnes de pantalla de registro HIS
    def on_button4_clicked(self, widget, data=None):
        # caragr windows 2 y cargar la data en el grid
        cnxn = psycopg2.connect("dbname=postgres  user=postgres password=123456")
        cursor = cnxn.cursor()
        cursor.execute("""select * from uno """)
        name_store3 = Gtk.ListStore( int , str   )
        #name_store3 = Gtk.ListStore(str)
        #name_store3 = Gtk.ListStore(str  )
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            name_store3.append([  row[0] , row[1] ])
            #name_store3.append([  row[1]  ])
        self.window2.show()
        self.vista2.set_model(name_store3)
        self.vista2.show()
        self.NumeroConsultas.set_text("0")
        self.NumeroConsultas.grab_focus()
        
    def on_btnGridSeleccion_clicked(self, widget, data=None):
        # ver que registro fue seleccionado del grid
        selected, iter = self.vista2.get_selection().get_selected()
        valor= selected.get_value(iter,0)
        valor1= selected.get_value(iter,1)
        self.DniBuscar.set_text(str(valor1))
        
    def on_button2_clicked(self, widget, data=None):
        valor=valor_combobox(self.Laboratorio)
        valor2=valor_combobox(self.Diagnostico)
        self.Mes.set_property("editable", True)
        #Var1=self.Establecimiento.currentText()
        self.txtentry.set_text(self.lbl.get_text())
        self.txtentry.set_text(self.NumeroFormularios.get_text() + " ----" )
        self.txtentry.set_text(valor + " --- " + valor2)
        ######################################################################################Inseratr registro
        #cnxn = psycopg2.connect("dbname=postgres user=postgres password=123456")
        #cursor = cnxn.cursor()
        #Var="""insert into uno ( descripcion , "IdEstado" ) VALUES('"""+ (self.Lote.get_text()) + """' , """+ (self.NumeroFormularios.get_text()) + """)"""
        #cursor.execute(Var )
        #cnxn.commit()
        #self.Anio.set_text(Var)
        #########################################################################################Actualizar registro
        #cnxn = psycopg2.connect("dbname=postgres user=postgres password=123456")
        #cursor = cnxn.cursor()
        #Var="""update  uno  set descripcion ='"""+ (self.Lote.get_text()) + """' where  "IdUno"= """+ (self.NumeroFormularios.get_text()) + """"""
        #cursor.execute(Var )
        #cnxn.commit()
        #self.Anio.set_text(Var)
        #habilitar control para ingreso
	
    def on_cmbDigitador_changed(self, text):
        modelo = cmbDigitador.get_model()
        activo = cmbDigitador.get_active()
        if activo >= 0: self.Mes = modelo[activo][0]
############################################################################################ Botnes de pantalla de registro HIS



############################################################################################ Botnes de pantalla consulta HIS
    def on_btnConsultaHisSalir_clicked(self, widget, data=None):
        #cogemos el valor de busqueda y le asignamos  a la otra ventana
        self.ConsultaHis.hide()
    def on_btnConsultaHisVer_clicked(self, widget, data=None):
        #cogemos el valor de busqueda y le asignamos  a la otra ventana
        #eliminar columnas para no repretir
        VarVer=self.NumeroConsultasHis.get_text()
        for column in self.DetalleconsultaHis.get_columns():
            if column:
                self.DetalleconsultaHis.remove_column(column)        
        
        # buscar y caragr el grid con el texto tipeado  
        cnxn = psycopg2.connect("dbname=postgres  user=postgres password=123456")
        cursor = cnxn.cursor()
        filtro=self.DniBuscar.get_text()
        cursor.execute("""select * from uno where descripcion  like '%""" + filtro + """%'""")
        #cursor.execute("""select * from uno """)
        name_store3 = Gtk.ListStore(int , str , int, str)
        for fila  in cursor.fetchall():
            name_store3.append(fila)
        cellp1=Gtk.CellRendererText()
        col1=Gtk.TreeViewColumn('Id', cellp1, text=0)
        self.DetalleconsultaHis.append_column(col1)
        
        cellp2=Gtk.CellRendererText()
        col2=Gtk.TreeViewColumn('Nombre', cellp2, text=1)
        self.DetalleconsultaHis.append_column(col2)

        cellp3=Gtk.CellRendererText()
        col3=Gtk.TreeViewColumn('IdArea', cellp3, text=2)
        self.DetalleconsultaHis.append_column(col3)

        cellp4=Gtk.CellRendererText()
        col4=Gtk.TreeViewColumn('dni', cellp4, text=3)
        self.DetalleconsultaHis.append_column(col4)
    
        self.vista2.set_model(name_store3)
        self.DetalleconsultaHis.show()
        
        VarVer=int(VarVer) + 1
        self.NumeroConsultasHis.set_text(str(VarVer))
############################################################################################ Botnes de pantalla consulta HIS

    #def on_toolbtnReportes_clicked(self, widget, data=None):
        #self.notebook1.set_current_page(3)
	
if __name__ == "__main__":
    interfaz = Gui()
    Gtk.main()
