# SIAFI Numerário Analysis

Este projeto realiza a análise de combinações de numerários enviados pela setorial contábil no SIAFI, útil para Unidades Gestoras (UG) identificarem possíveis somas de valores específicos. O projeto foi pensado para ser de fácil utilização por qualquer pessoa.

## Funcionalidades

- Encontra combinações de valores que somam um total específico.
- Carrega dados de um arquivo CSV.
  
## Como usar

### Pré-requisitos

- Python 3.x instalado em sua máquina.

### Passo a passo

1. Clone o repositório para sua máquina:
   ```bash
   git clone https://github.com/usuario/SIAFI-Numerario-Analysis.git
   ```
   
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Coloque seu arquivo CSV no diretório `data/`. O arquivo deve conter uma coluna com os valores para análise.

4. Execute o script principal:
   ```bash
   python numerario_analysis.py
   ```

### Exemplo de entrada

Arquivo CSV (`example_input.csv`):
```csv
82040.80
64933.22
16200.00
8339.60
3853.66
50378.50
14172.50
319842.20
2583.00
5593.00
```

### Testes

Há uma pasta `tests/` que contém um exemplo de teste unitário. Para rodar os testes, use `pytest`:
```bash
pytest
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar *pull requests*.

## Licença

Este projeto está sob a licença MIT.
