🧩 Instalação e Configuração

Primeiro, foi feito o download do Visual Studio Code, que é um editor de código. Após a instalação, foi adicionada a extensão de Python para permitir escrever e executar o programa.




📄 Criação do Arquivo

Em seguida, foi criado um arquivo chamado consumo.py, onde todo o código foi desenvolvido.




📥 Entrada de Dados

Na primeira parte do código, é criada uma lista vazia chamada consumo_diario, que serve para armazenar os valores de consumo dos 30 dias.

Depois disso, é utilizado um laço de repetição for que executa 30 vezes. Em cada repetição, o programa solicita ao usuário o consumo do dia, converte o valor para número decimal com float e adiciona na lista com append.



➕ Cálculo do Total e Média

Após a coleta dos dados, é calculado o consumo total utilizando a função sum(). Em seguida, a média é obtida dividindo o total por 30.


🔼 Cálculo do Maior Valor (Manual)

Para encontrar o maior valor sem utilizar a função max(), o programa começa assumindo que o primeiro valor da lista é o maior.

Depois, percorre o restante da lista comparando cada valor. Sempre que encontra um valor maior, atualiza a variável do maior valor e registra o dia correspondente.


🔽 Cálculo do Menor Valor (Manual)

O mesmo processo é feito para encontrar o menor valor, mas comparando para identificar valores menores.




📈 Contagem de Aumentos

Depois, é feita a contagem de quantas vezes o consumo aumentou em relação ao dia anterior.

Para isso, o programa percorre a lista comparando cada valor com o anterior e incrementa um contador sempre que há aumento.


📊 Exibição do Relatório

Por fim, o programa exibe um relatório com todas as informações: consumo total, média, maior consumo com o dia correspondente, menor consumo com o dia correspondente e a quantidade de vezes que houve aumento.




🌐 Envio para o GitHub

Após finalizar o código, foi utilizado o terminal do Visual Studio Code para conectar com o GitHub.

Primeiro, o repositório foi inicializado com:

git init

Depois, o arquivo foi adicionado:

git add consumo.py

Em seguida, foi feito o commit:

git commit -m "Primeira versão do projeto de consumo diário"

Depois, foi criado um repositório no GitHub e copiado o link.

Por fim, o projeto local foi conectado ao repositório online e enviado com:

git remote add origin (link do repositório)
git push -u origin main
