# Class to handle containing all the info for each row in the table output (and database)
from handle_db import HandleDB


class VulnInfo:
    cve_id = ""
    cost_hour = 0
    total_hours = 0
    item_name = ""
    item_cost = 0
    total_cost = 0
    description = ""
    severity = ""
    bussiness_info = []  # 0 for size 1 for type
    db_handler = HandleDB()

    def __init__(self, bussiness_info):
        self.cve_id = ""
        self.item_name = ""
        self.item_cost = 0
        self.bussiness_info = bussiness_info
        self.cost_hour = 0
        self.total_hours = 0
        self.description = ""
        self.severity = ""

    def __init__(self, cve_id, bussiness_info):
        self.cve_id = cve_id
        # self.db_handler.pull_item_name(cve_id) # TODO:Database doesn't contain this info yet
        self.item_name = ""
        # self.db_handler.pull_item_cost(cve_id)  # TODO:Database doesn't contain this info yet
        self.item_cost = 0
        self.bussiness_info = bussiness_info
        self.cost_hour = self.db_handler.pull_cost_hrs(cve_id)
        self.total_hours = self.db_handler.pull_total_hrs(cve_id)
        self.description = self.db_handler.pull_description(cve_id)
        self.description = self.description[2:-5]
        self.severity = self.db_handler.pull_severity(cve_id)
        # git rid of the junk at the tails of the description
        
