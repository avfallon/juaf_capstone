# imports
from Controller import *
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



# Boxlayout is the App class

class ZehnFunds_AdministratorApp(App):


    def build(self):
        self.controller = Controller()
        self.search_results = ["", "", "", ""]
        self.parent_box = BoxLayout(id='parentBox', orientation='vertical', padding=10, spacing=20)

        self.parent_box.add_widget(self.button_menu_builder())

        self.search_bar = self.search_bar_builder()
        self.parent_box.add_widget(self.search_bar)

        self.account_view = self.account_view_builder()
        self.parent_box.add_widget(self.account_view)

        return self.parent_box

    def openLookup(self, lookup_btn):
        self.search_bar.opacity = 1
        self.account_view.opacity = 0;
        # self.email_view.opacity = 0;

    def open_edit_account(self, edit_btn):
        self.create_account_textboxes(self.search_results)


    # This function displays the textboxes for adding a new account to the database
    def open_add_account(self, add_btn):
        self.search_bar.opacity = 0;
        self.set_account_opacity(True)

        # print(self.account_view.children[0].children[0].children)
        self.create_account_textboxes(["", "", "", ""])

    # This function replaces the labels or textboxes on the right side of account_view with empty textboxes
    def create_account_textboxes(self, contents_list):
        # This accesses children of the horizontal box layout underneath the 'save/edit/delete' buttons in account_view
        input_layout = self.account_view.children[0].children[0]
        if input_layout.id == 'textboxes':
            i = len(contents_list)
            for textbox in input_layout.children:
                i-=1
                textbox.text = contents_list[i]
        else:
            print("textbox column doesnt exist")
            textinputBox = BoxLayout(id='textboxes', orientation='vertical', size_hint=(.65, 1),  spacing=20)
            for i in range(4):
                textinputBox.add_widget(TextInput(text=contents_list[i]))

            self.account_view.children[0].remove_widget(input_layout)
            self.account_view.children[0].add_widget(textinputBox)

        self.set_account_opacity(True)

    # This function replaces the labels or textboxes on the right side of account_view with labels
    # containing the account's information
    def create_account_labels(self, contents_list):
        input_layout = self.account_view.children[0].children[0]
        if input_layout.id == 'input_labels':
            i = len(contents_list)
            for label in input_layout.children:
                i-=1
                label.text = contents_list[i]
        else:
            print("label column doesnt exist")
            input_labels = BoxLayout(id='input_labels', orientation='vertical', size_hint=(.65, 1),  spacing=20)
            index = 3
            for i in range(4):
                input_labels.add_widget(Label(text=contents_list[i]))

            self.account_view.children[0].remove_widget(input_layout)
            self.account_view.children[0].add_widget(input_labels)

        self.set_account_opacity(False)



    # This function sets the visibility of the edit, dave, and delete buttons based on whether the account is being edited
    def set_account_opacity(self, editing_account):
        self.account_view.opacity = 1
        if editing_account:
            # set save button to be visible
            self.account_view.children[1].children[2].opacity = 1
            # Set edit button to be invisibe
            self.account_view.children[1].children[1].opacity = 0
            # Set delete button to be visible
            self.account_view.children[1].children[0].opacity = 1
        else:
            # Set save button to be invisible
            self.account_view.children[1].children[2].opacity = 0
            # Set edit button to be visibe
            self.account_view.children[1].children[1].opacity = 1
            # set delete button to be invisible
            self.account_view.children[1].children[0].opacity = 0


    def save_account(self, save_btn):
        print("saving account")
        input_box = self.account_view.children[0].children[0].children
        self.controller.save_account(input_box[3].text, input_box[2].text, input_box[0].text)
        self.account_view.opacity = 0

    def delete_account(self, delete_btn):
        self.controller.delete_account(self.account_view.children[0].children[0].children[2])
        self.account_view.opacity = 0


    def searchEmail(self, search_btn):
        print("Searching email")
        #print(self.search_bar.children[1].text)
        # self.search_results = self.controller.lookupAccount(self.search_bar.children[1].text)
        # print(self.search_results)
        if self.search_bar.children[1].text != "andrew@gmail.com":
            self.search_bar.children[1].text = ""
            self.search_bar.children[1].hint_text = "Email Not Found"
        else:
            self.search_results = ["andrew", "andrew@gmail.com", "2356", "password"]
            self.create_account_labels(self.search_results)


    # This function is called by the "Send Emails" button at the top of the screen
    def sendEmails(self, email_btn):
        print("Sending Emails")
        # self.controller.sendEmails()


    def button_menu_builder(self):
        horizontalBox = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, .1))

        horizontalBox.add_widget(Button(text="Lookup Account", on_press=self.openLookup))
        horizontalBox.add_widget(Button(text="Add Account", on_press=self.open_add_account))
        horizontalBox.add_widget(Button(text="Send Update Emails", on_press=self.sendEmails))

        return horizontalBox


    def search_bar_builder(self):
        horizontalBox = BoxLayout(id='searchBar', orientation='horizontal', opacity=0, size_hint=(1, .1), spacing=10, padding=10)

        textbox = TextInput(id='searchBox', hint_text='Enter email here', size_hint=(.7, 1))
        horizontalBox.add_widget(textbox)

        searchBtn = Button(text='Search', size_hint=(.3, 1), on_press=self.searchEmail)
        horizontalBox.add_widget(searchBtn)
        return horizontalBox


    def account_view_builder(self):
        # Get the array of stuff from the database
        accountBoxLayout = BoxLayout(id='account', orientation='vertical', opacity=0, size_hint=(1, .6), spacing=10, padding=10)

        editBtns = BoxLayout(orientation='horizontal', spacing=20, size_hint=(1, .2))
        editBtns.add_widget(Button(text="Save", on_press=self.save_account))
        editBtns.add_widget(Button(text="Edit", on_press=self.open_edit_account))
        editBtns.add_widget(Button(text="Delete", on_press=self.delete_account))
        accountBoxLayout.add_widget(editBtns)

        account_info = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, .8))

        labelBox = BoxLayout(orientation='vertical', size_hint=(.35, 1), spacing=20)
        textinputBox = BoxLayout(id='textboxes', orientation='vertical', size_hint=(.65, 1),  spacing=20)
        account_info.add_widget(labelBox)
        account_info.add_widget(textinputBox)

        test_arr = [{"account_name":"usa","account_email":"gw@usa.gov","current_funds":"1776","password":"password"}]
        for myKey in test_arr[0].keys():

            category_label = Label(text=myKey)
            labelBox.add_widget(category_label)

            textbox = TextInput()
            textinputBox.add_widget(textbox)

        accountBoxLayout.add_widget(account_info)

        return accountBoxLayout



# Instantiate and run the kivy app

if __name__ == '__main__':
    ZehnFunds_AdministratorApp().run()

