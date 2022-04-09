# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import  pandas  as pd
import os

def append_data_to_excel(excel_name, data):
    df = pd.read_excel(excel_name)
    x = df.append(data, ignore_index=True)
    x.to_excel(excel_name,index=False)

class ActionSave(Action):

    def name(self) -> Text:
        return "action_save"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Passed Here")
        data = pd.DataFrame({'Name': tracker.get_slot('name'), 'Room': tracker.get_slot('room'), 'Date': tracker.get_slot('date'),'Start_Time': tracker.get_slot('start_time'), 'End_Time': tracker.get_slot('end_time')}, index=[0])
        append_data_to_excel('C:/Users/Soulaimani Badr/Desktop/IMT Atlantique/FISE A2/NLP/CaraeBot/actions/test.xlsx', data)
        dispatcher.utter_message("Your reservation has been made.")
        return [AllSlotsReset()]

class ActionReset(Action):

    def name(self) -> Text:
        return "action_reset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("Passed Here")
        dispatcher.utter_message("Try to make another reservation.")
        return [AllSlotsReset()]






