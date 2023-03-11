from inventory_report.inventory.product import Product


def test_cria_produto():
    novo_produto = Product(
        1,
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1"
    )

    assert novo_produto.id == 1
    assert novo_produto.nome_do_produto == "Nicotine Polacrilex"
    assert novo_produto.nome_da_empresa == "Target Corporation"
    assert novo_produto.data_de_fabricacao == "2021-02-18"
    assert novo_produto.data_de_validade == "2023-09-17"
    assert novo_produto.numero_de_serie == "CR25 1551 4467 2549 4402 1"
    assert novo_produto.instrucoes_de_armazenamento == "instrucao 1"
