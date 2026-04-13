Documentação do Projeto: Análise de Consumo Diário
=====================================================

Este documento detalha as etapas de configuração, a lógica de desenvolvimento e o processo de versionamento do script de controle de consumo.

1. Preparação do Ambiente
Editor de Código: Download e instalação do Visual Studio Code.

Configuração: Adição da extensão oficial de Python para permitir a escrita e execução do programa.

Criação do Arquivo: Todo o código foi desenvolvido centralizado em um arquivo chamado consumo.py.

2. Desenvolvimento e Lógica do Código
Entrada de Dados

Criação de uma lista vazia chamada consumo_diario para armazenar os registros dos 30 dias.

Utilização de um laço de repetição for programado para rodar 30 vezes.

A cada repetição, o programa realiza os seguintes passos:

Solicita ao usuário o consumo daquele dia específico.

Converte o valor digitado para número decimal utilizando float().

Adiciona o número à lista através do método .append().

Cálculo do Total e Média

Total: O consumo acumulado é calculado de forma direta utilizando a função sum().

Média: O resultado é obtido dividindo o consumo total por 30.

Cálculo de Extremos (Implementação Manual)

Maior Valor: * O programa assume que o primeiro valor da lista é o maior.

Percorre o restante dos dados comparando cada um.

Se encontrar um valor superior, atualiza a variável do maior valor e salva o dia correspondente.

Menor Valor: * Segue exatamente o mesmo processo acima, mas a condição de comparação busca identificar o menor número da lista.

Análise de Tendência (Aumentos)

Calcula quantas vezes o consumo foi maior que o do dia anterior.

O laço percorre a lista comparando o índice atual com o índice anterior, incrementando um contador sempre que detecta uma alta.

3. Exibição do Relatório
Ao final da execução, o programa imprime na tela um relatório gerencial contendo:

O consumo total do mês.

A média diária de consumo.

O pico de maior consumo (incluindo qual foi o dia).

O pico de menor consumo (incluindo qual foi o dia).

A quantidade total de vezes que o consumo aumentou de um dia para o outro.

4. Versionamento e Envio (GitHub)
Após a finalização e teste do código, o terminal integrado do Visual Studio Code foi utilizado para subir o projeto para a nuvem. Os comandos executados foram:

1. Inicialização do repositório local:

git init

2. Adição do arquivo para o pacote de envio:

git add consumo.py

3. Criação do ponto de histórico (Commit):

git commit -m "Primeira versão do projeto de consumo diário"

4. Conexão com o repositório remoto (criado previamente no GitHub):

git remote add origin <link_do_repositorio>

5. Envio do código final para a branch principal:

git push -u origin main
