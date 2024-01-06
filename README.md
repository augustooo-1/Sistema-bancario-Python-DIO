# Sistema Bancário Simples em Python

## Descrição

Este projeto implementa um sistema bancário básico usando Python. Oferece funcionalidades essenciais como:

- **Depósito**: Adiciona fundos à conta e registra a transação.
- **Saque**: Permite retiradas, respeitando limites diários e de valor.
- **Extrato**: Mostra todas as transações realizadas e o saldo atual.

## Funcionalidades

### Depósito
Ao realizar um depósito, o valor é adicionado ao saldo da conta e registrado para futura consulta no extrato.

### Saque
O sistema permite até 3 saques por dia, com um limite máximo de R$ 500,00 por saque. Verificações são realizadas para garantir que o saque não exceda o saldo disponível.

### Extrato
A funcionalidade de extrato exibe todas as transações realizadas na conta, permitindo uma visão detalhada das atividades e do saldo atual.

## Limitações

- Máximo de 3 saques por dia.
- Limite de R$ 500,00 por saque.
- Controle de saldo para evitar saques sem fundos.

## Execução

Para executar o sistema, certifique-se de ter Python instalado. Depois, simplesmente rode o script e siga as instruções apresentadas no console.

## Contribuições

Sinta-se à vontade para contribuir com melhorias, sugestões ou correções neste projeto.

