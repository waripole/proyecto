import sys
import gi
gi.require_version('Gtk', '4.0')
# from os import remove
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib


def on_quit_action(self, _action):
    quit()

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Box principal
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        self.set_child(self.main_box)

        #para que se expanda el 
        self.main_box.set_hexpand(True)
        self.main_box.set_vexpand(True)        

#---------------------------------------------------------------------
    # 3 cajas o botones donde se indique el nùmero de S/I/R aki

        self.box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box.set_homogeneous(True)
        self.main_box.append(self.box)

        self.box_botones = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_botones.set_homogeneous(True)
        self.main_box.append(self.box_botones)

        self.box_tree = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.box_tree.set_homogeneous(True)
        self.main_box.append(self.box_tree)



    #Tree TreeView
        data = []

        self.liststore = Gtk.ListStore(str, str, str, bool, bool, bool)
        for data_ref in data:
            self.liststore.append(list(data_ref))

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
        self.set_child(self.box_tree)

#---------------------------------------------------------------------

        # Menu
        header_bar = Gtk.HeaderBar.new() #la barrita de arriba / top label
        self.set_titlebar(titlebar=header_bar)
        self.set_title("SIMULADOR SIR")

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
    #Botones header bar

        self.boton_avanzar = Gtk.Button()
        self.boton_avanzar.set_label('DAR 1 PASO')
        #self.boton_avanzar.connect('clicked', self.on_clicked_avanzar)
        header_bar.pack_start(self.boton_avanzar)

        self.boton_graficar = Gtk.Button()
        self.boton_graficar.set_label('GRAFICAR')
        #self.boton_graficar.connect('clicked', self.on_clicked_graficar)
        header_bar.pack_end(self.boton_graficar)

#---------------------------------------------------------------------

        self.boton_s = Gtk.Button()
        self.boton_s.set_label("miau s")
        self.box_botones.append(self.boton_s)

        self.boton_i = Gtk.Button()
        self.boton_i.set_label("miau i")
        self.box_botones.append(self.boton_i)

        self.boton_r = Gtk.Button()
        self.boton_r.set_label("miau r")
        self.box_botones.append(self.boton_r)

        label = Gtk.Label()
        label.set_text("numero de Susceptibles")
        self.box.append(label)

        label_2 = Gtk.Label()
        label_2.set_text("numero de Infectados")
        self.box.append(label_2)

        label_3 = Gtk.Label()
        label_3.set_text("numero de Recuperados")
        self.box.append(label_3)




#---------------------------------------------------------------------

    def actualizar_cvs(self):
        pass















#---------------------------------------------------------------------
    def show_about_dialog(self, action, param): #lo que ze dezpliega del menu
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)
        self.about.set_modal(self)

        self.about.set_authors(["Sofia Mieres Vignolo"])
        self.about.set_copyright("Copyright 2024 Sofia Anaelle Mieres Vignolo")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://icb.utalca.cl/")
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
                model.get_value(iter, 2))

#.....................................................


class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

app = MyApp()
app.run(sys.argv)
