from kivy.app import App
from kivy.lang import Builder
 
root = Builder.load_string('''
FloatLayout:
    canvas.before:
        Color:
            rgba: 255, 0, 255, 0.3
        Rectangle:
            pos: self.pos
            size: self.size
    
    Button:
        text: 'Submit Now'
        size_hint: .3, .1
        pos_hint: {'center_x':.5, 'center_y': .3}
''')
 
class MainApp(App):
 
    def build(self):
        return root
 
if __name__ == '__main__':
    MainApp().run()
