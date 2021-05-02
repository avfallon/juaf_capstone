# imports

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label


# Boxlayout is the App class

class AdminApp(App):

    def build(self):
        parentBox = BoxLayout(orientation='vertical')

        horizontalBox = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, .2))

        button1 = Button(text="Lookup Account")

        button2 = Button(text="Add Account")

        button3 = Button(text="Send Update Emails")

        horizontalBox.add_widget(button1)

        horizontalBox.add_widget(button2)

        horizontalBox.add_widget(button3)

        verticalBox = BoxLayout(orientation='vertical')

        button5 = Button(text="Three", opacity=0)

        button4 = Button(text="Four")

        verticalBox.add_widget(button5)

        verticalBox.add_widget(button4)

        parentBox.add_widget(horizontalBox)

        parentBox.add_widget(verticalBox)

        return parentBox

    def create_account_view(self, parentBoxLayout):
        # Get the array of stuff from the database

        verticalBox = BoxLayout(orientation='vertical')

        test_arr = [{"id":"1","account_name":"usa","account_email":"gw@usa.gov","current_funds":"1776","recent_purcahse":"1 Declaration of Independence, purchased 1776, $13.65, zehnfunds: 1365"}]
        for myKey in test_arr.keys():
            horizontalBox = BoxLayout(orientation='horizontal')



# Instantiate and run the kivy app

if __name__ == '__main__':
    AdminApp().run()

