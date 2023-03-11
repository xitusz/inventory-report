# Inventory Report
[2/6] [Ciência da Computação](https://github.com/xitusz/Trybe/tree/main/04_Ci%C3%AAncia-da-Computa%C3%A7%C3%A3o)

---

## Sumário

- [Contexto](#contexto)
- [Habilidades Desenvolvidas](#habilidades-desenvolvidas)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Clonando Repositório](#clonando-repositório)
- [Instalando Dependências](#instalando-dependências)
- [Executando Aplicação](#executando-aplicação)
- [Executando Testes](#executando-testes)

---

## Contexto

* Projeto desenvolvido para colocar em prática conhecimentos adquiridos em padrões de projeto / POO em python

---

## Habilidades Desenvolvidas

* Aplicar conceitos de Orientação a Objetos em Python;
* Aplicar padrões de projeto;
* Leitura e escrita de arquivos (XML, CSV, JSON).

---

## Tecnologias Utilizadas

* Python

---

## Clonando Repositório:

* Clone o repositório
  ```sh
    git clone git@github.com:xitusz/inventory-report.git
  ```

---

## Instalando Dependências

* Entre na pasta do repositório que você clonou:
  ```sh
    cd inventory-report
  ```

* Crie o ambiente virtual
  ```sh
    python3 -m venv .venv && source .venv/bin/activate
  ```

* Instale as dependências
  ```sh
    python3 -m pip install -r dev-requirements.txt
  ```

* Se aparecer algum erro relacionado a 'wheel', instale-o
  ```sh
    python3 -m pip install wheel && python3 -m pip install -r dev-requirements.txt
  ```

---

## Executando Aplicação

* Aplicação não concluída a ponto de execução

---

## Executando Testes

* Os testes que eu desenvolvi foram 'tests/product/test_product.py' e 'tests/product_report/test_product_report.py'. Os demais foram desenvolvidos pela [Trybe](https://www.betrybe.com/)

* Entre na pasta do repositório que você clonou:
  ```sh
    cd job-insights
  ```

* Rode os testes
  ```sh
    python3 -m pytest
  ```

---
