from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def import_data(file_path, type_report):
        with open(file_path) as file:
            if file_path.endswith(".csv"):
                inventory_list = list(csv.DictReader(file))
            if file_path.endswith(".json"):
                inventory_list = json.load(file)
            if file_path.endswith(".xml"):
                inventory_list = xmltodict.parse(
                    file.read())["dataset"]["record"]

        if type_report == "simples":
            return SimpleReport.generate(inventory_list)

        return CompleteReport.generate(inventory_list)
