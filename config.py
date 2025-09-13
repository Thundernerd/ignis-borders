import gi

gi.require_version("GioUnix", "2.0")
gi.require_version("Gtk", "4.0")

from widgets.border import Border
from widgets.config_window import ConfigWindow
from styling.style_manager import StyleManager
from ignis.app import IgnisApp
from ignis.css_manager import CssInfoPath


css_path = CssInfoPath(name="default", path="style.css")
IgnisApp.get_initialized()._css_manager.apply_css(css_path)

# load style with flat border color
StyleManager.get_default().initialize("style.json")

# load style with gradient border color
#StyleManager.get_default().initialize("style-gradient.json")

Border()

