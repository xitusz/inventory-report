from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def company_products(data):
        result = ""

        counter = Counter(item["nome_da_empresa"] for item in data)

        for company, quantity in counter.items():
            result += f"- {company}: {quantity}\n"

        return result

    def generate(data):
        simple_report = SimpleReport.generate(data)
        quantity = CompleteReport.company_products(data)

        return (
            simple_report +
            f"\nProdutos estocados por empresa:"
            f"\n{quantity}"
        )
