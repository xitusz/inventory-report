import statistics


class SimpleReport:
    def generate(data):
        oldest = sorted(
            data, key=lambda item: item["data_de_fabricacao"]
        )[0]["data_de_fabricacao"]

        closest = sorted(
            data, key=lambda item: item["data_de_validade"]
        )[0]["data_de_validade"]

        company = statistics.mode(item["nome_da_empresa"] for item in data)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {company}"
        )
