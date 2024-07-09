from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

import numpy as np
import pandas as pd

from z_nombre_apellidos import crear_lista

import sys
import gi
import csv
gi.require_version('Gtk', '4.0')
# from os import remove
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib



#---------------------------------------------------------------------------


def on_quit_action(self, _action):
    quit()


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, simulador, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.simulador = simulador
        self.dia_actual = 0


        # Box principal
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        self.set_child(self.main_box)

        #para que se expanda 
        self.main_box.set_hexpand(True)
        self.main_box.set_vexpand(True)        

#---------------------------------------------------------------------
    # Cajas

        # Caja para boton dia
        self.box_dia = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_dia.set_homogeneous(True)
        self.main_box.append(self.box_dia)

        # Caja labels (cantidad S/I/R)
        self.box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box.set_homogeneous(True)
        self.main_box.append(self.box)

        # Caja botones S / I / R (aquì se mostraran los valores)
        self.box_botones = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_botones.set_homogeneous(True)
        self.main_box.append(self.box_botones)

        self.box_tree = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_tree.set_homogeneous(True)
        self.main_box.append(self.box_tree)

        # Queria hacer un scroll pero flop
        self.window_scroll = Gtk.ScrolledWindow()
        self.window_scroll.set_vexpand(True)
        self.window_scroll.set_hexpand(True)
        self.main_box.append(self.window_scroll)

        self.box_muertos = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_muertos.set_homogeneous(True)
        self.main_box.append(self.box_muertos)


    #Tree TreeView
        #data = []

        self.liststore = Gtk.ListStore(str, str, str, str, str, str)


        treeview = Gtk.TreeView(model=self.liststore, vexpand=True)
        treeview.connect('cursor_changed', self.on_cursor_changed)
        treeview.set_hexpand(True)
        treeview.set_vexpand(True)

        for i, column_title in enumerate(['#', 'Nombre', 'Apellido', 'Susceptible', 'Infectado', 'Recuperado']):
            renderer = Gtk.CellRendererText()
            # column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            column = Gtk.TreeViewColumn(title=column_title)
            column.pack_start(renderer, False)
            column.add_attribute(renderer, "text", i)
            treeview.append_column(column)

        self.box_tree.append(treeview)
        self.set_child(self.main_box)
        self.set_child(self.window_scroll)


        self.cargar_csv("cvs_actualizado.csv")


#---------------------------------------------------------------------

        # Menu
        header_bar = Gtk.HeaderBar.new() #la barrita de arriba / top label
        self.set_titlebar(titlebar=header_bar)
        self.set_title("SIR")

        # Listado del menu
        menu = Gio.Menu.new() #genera interaccionez dentro del menu (acerca de/zalir)

        # Create a popover
        self.popover = Gtk.PopoverMenu() #vviedget del menù
        self.popover.set_menu_model(menu)  #{popover{menu}}

        # crea un menu
        self.menu_popover = Gtk.MenuButton()
        self.menu_popover.set_popover(self.popover)
        self.menu_popover.set_icon_name("open-menu-symbolic")

        # agrega headerbar el menu popover
        header_bar.pack_end(self.menu_popover)

        # Add an about dialog #generamoz una inztancia para dar eventoz
        about_menu = Gio.SimpleAction.new("about", None)
        about_menu.connect("activate", self.show_about_dialog) #evento activate (cuando pazamoz el mouze por encima)
        self.add_action(about_menu)
        menu.append("Acerca de", "win.about") #win.about -> de donde gatilla ezta acciòn (en ezte cazo de la ventana) // app.about (otro) 

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", on_quit_action) #quit forzozo
        self.add_action(action)
        menu.append("Salir", "win.quit")

#---------------------------------------------------------------------
    # Botones header bar

        self.boton_avanzar = Gtk.Button()
        self.boton_avanzar.set_label('Dar un paso')
        self.boton_avanzar.connect('clicked', self.actualizar_todo)
        header_bar.pack_start(self.boton_avanzar)

#---------------------------------------------------------------------
	# Botones estèticos

        self.boton_dia = Gtk.Button()
        self.boton_dia.set_label("Dia: 0")
        self.box_dia.append(self.boton_dia)

        label = Gtk.Label()
        label.set_text("Nùmero de Susceptibles")
        self.box.append(label)

        label_2 = Gtk.Label()
        label_2.set_text("Nùmero de Infectados")
        self.box.append(label_2)

        label_3 = Gtk.Label()
        label_3.set_text("Nùmero de Recuperados")
        self.box.append(label_3)

        self.boton_s = Gtk.Button()
        self.boton_s.set_label("S")
        self.box_botones.append(self.boton_s)

        self.boton_i = Gtk.Button()
        self.boton_i.set_label("I")
        self.box_botones.append(self.boton_i)

        self.boton_r = Gtk.Button()
        self.boton_r.set_label("R")
        self.box_botones.append(self.boton_r)


        self.boton_muertos = Gtk.Button()
        self.boton_muertos.set_label("Muertos: 0")
        self.box_muertos.append(self.boton_muertos)


#---------------------------------------------------------------------
    # Funciones especìficas

    # Avanzar 1 dia
    def on_clicked_avanzar(self, widget):
    	
    	self.simulador.step()

    	self.dia_actual = self.dia_actual + 1

    	self.actualizar_dia()

    	self.cargar_csv(filepath = "cvs_actualizado.csv")

  

    # Actualizar el dìa que se muestre en el boton_dia
    def actualizar_dia(self):
    	
    	self.boton_dia.set_label(f"Dia: {self.dia_actual}")



    # Botones S/I/R para mostrar la cantidad de c/u
    def mostrar_susceptibles(self):

    	susceptibles = self.simulador.get_comunidad().get_susceptibles()

    	self.boton_s.set_label(f"{susceptibles}")


    def mostrar_infectados(self):

    	infectados = self.simulador.get_comunidad().get_infectados()

    	self.boton_i.set_label(f"{infectados}")    


    def mostrar_recuperados(self):

    	recuperados = self.simulador.get_comunidad().get_recuperados()

    	self.boton_r.set_label(f"{recuperados}")


    # Mostra cuàntos ciudadanos estàn muertos (de los recuperados)
    def mostrar_muertos(self):

    	muertos = self.simulador.get_comunidad().morir_o_no()

    	self.boton_muertos.set_label(f"Muertos: {muertos}")


	# lee un archivo cvs con pandas y se toman las primeras 10 lineas
	# luego esto pasa a la funciòn cargar_cvs que
	# actualizaà el TreeView
    def cargar_datos_np(self,filepath):

        df = pd.read_csv(filepath)

		# Para mostrar sòlo los primeros 1o ciudadanos
        primeros_diez = df.head(10)

		# Convertir a np array
        datos_numpy = primeros_diez.to_numpy()

        return datos_numpy


    # Actualizar el cvs en cada paso
    def cargar_csv(self, filepath): 

    	# Para que se vayan actualizado los datos y no agregando al liststore
    	self.liststore.clear()

    	datos_numpy = self.cargar_datos_np(filepath)

    	for row in datos_numpy:
        	self.liststore.append([str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5])])



    def actualizar_todo(self, widget):
    	#lo de SIR, Dia y CVS cada vez que se haga un paso -> boton_avanzar

    	self.on_clicked_avanzar(widget)

    	self.mostrar_susceptibles()
    	self.mostrar_infectados()
    	self.mostrar_recuperados()

    	self.mostrar_muertos()
    	#self.cargar_csv("cvs_actualizado")


#---------------------------------------------------------------------
    def show_about_dialog(self, action, param): #lo que ze dezpliega del menu
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Sofia"])
        self.about.set_copyright("Copyright 2024 Sofia")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https:")
        self.about.set_website_label("ICB")
        self.about.set_version("1.0")
        self.about.set_logo_icon_name("chuu_do_loona")
        self.about.set_visible(True)

    def on_cursor_changed(self, treeview):
        treeselection = treeview.get_selection()
        model, iter = treeselection.get_selected()

        if iter:
            print(
                model.get_value(iter, 0),
                model.get_value(iter, 1),
                model.get_value(iter, 2),
                model.get_value(iter, 3),
                model.get_value(iter, 4),
                model.get_value(iter, 5))


#.....................................................


class MyApp(Gtk.Application):
    def __init__(self, simulador, **kwargs):
        super().__init__(**kwargs)

        self.simulador = simulador


    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(simulador=self.simulador, application=self)
            self.win.present()




crear_lista("lista.csv")

covid = Enfermedad( infeccion_probable = 0.3 , promedio_pasos = 5, enfermo = False, contador = 0)

talca = Comunidad( num_cuidadano = 20000,
					promedio_conexion_fisica = 3,
					enfermedad = covid,
					num_infectados = 3,
					probabilidad_conexion_fisica = 0.8,
					muertos = 0,
					archivo_csv = "lista.csv",
					u = 3,
					sigma = 1.5)


talca.cvs_actualizado()

# Probando para ver si se crean correctamente - sim
#talca.imprimir_cuidadanos()
#talca.imprimir_grupos()

talca.infectar_random()



sim = Simulador(talca)


sim.step()


app = MyApp(simulador = sim)
app.run(sys.argv)
