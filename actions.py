# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import re
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class ActionFormInfo(FormAction):
    def name(self):
        return "basic_info"
    
    @staticmethod  
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["email", "mobile"]
    
    def validate_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
        if re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z]+\.[^@]+", str(value)):
            # entity was picked up, validate slot
            print("inside if")   
            dispatcher.utter_message(text="valid email entered")
            return {"email": value}
        else:
            # no entity was picked up, we want to ask again
            print("inside else")
            dispatcher.utter_message(text="enter valid email")
            return {"email": None}
            
    def validate_mobile(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any] ) -> Dict[Text, Any]:
        if re.match(r"(0/91)?[7-9][0-9]{9}", str(value)):
            # entity was picked up, validate slot            
            print("inside if")   
            dispatcher.utter_message(text="valid mobile entered")
            return {"mobile": value}
        else:
            # no entity was picked up, we want to ask again
            print("inside else")
            dispatcher.utter_message(text="enter valid mobile")
            return {"mobile": None}
        
    def slot_mappings(self) -> Dict[Text, Any]:
        return {"email": [self.from_text()],
                "mobile":[self.from_text()]}   
    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message("Thanks for getting in touch, we’ll contact you soon")
        return []