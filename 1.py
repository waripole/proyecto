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
        self.main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.set_child(self.main_box)

        self.file_data = None

#---------------------------------------------------------------------

#---------------------------------------------------------------------

        # Menu
        header_bar = Gtk.HeaderBar.new() #la barrita de arriba / top label
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Formato APP")

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
        self.boton_avanzar.set_label('Avanzar')
        #self.boton_avanzar.connect('clicked', self.on_clicked_avanzar)
        header_bar.pack_start(self.boton_avanzar)

        self.boton_retroceder = Gtk.Button()
        self.boton_retroceder.set_label('Retroceder')
        #self.boton_retroceder.connect('clicked', self.on_clicked_retroceder)
        header_bar.pack_end(self.boton_retroceder)

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