from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicNamesApp(App):
    name_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Simon", "Memafu", "Dante", "Sean", "Olani"]

    def build(self):
        self.title = "Dynamic Names App"
        self.root = Builder.load_file('list_of_names.kv')
        for name in self.names:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_name)
            self.root.ids.names_box.add_widget(temp_button)

        return self.root

    def press_name(self, instance):
        name = instance.text
        self.name_text = "My name is {}".format(name)


DynamicNamesApp().run()
