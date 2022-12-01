from policyengine_canada.model_api import *


class is_married(Variable):
    value_type = bool
    entity = Household
    label = "Is married"
    documentation = "Household head is married"
    definition_period = YEAR
