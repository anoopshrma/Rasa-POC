from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class SupportForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "support_form_query"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["subject", "summary","email","number","priority"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "subject": [
                self.from_text(),
            ],
            "summary": [
                self.from_text(),
            ],

            "email": [
                self.from_text(),
            ],
            "number": [
                self.from_text(),
            ],
            "priority": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # Display thank you note after sccesful form completion
        dispatcher.utter_message("Thanks for answering all our questions and being this patient. We appreciate it!")
        return []

