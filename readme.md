# Desafio: Lucro da Ação

## O problema
O código tem por objetivo resolver o seguinte problema:

```
O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.

Determine o maior lucro dado esse array K de preços.

Exemplo 1:


* Input: [7,1,5,3,6,4]

* Output: 5

* Explicação: Este valor acontece quando compramos a ação no 2º dia e a vendemos no 5º dia (6 - 1)




Exemplo 2:


* Input: [7,6,4,3,1]

* Output: 0

* Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.
```

## Solução

A solução considera o array uma série temporal e que não existem ações compradas previamente, ou seja, só é possivel vender ações depois de comprar. Assim, no exemplo, é impossível vender ações no primeiro dia e não faz sentido comprá-las no último, pois não há informação sobre a venda posterior a esse dia.

Para escrever o código, foi utilizada a linguagem Python na versão 3.7.5.

## Código´

O código consiste de três etapas: a inserção dos dados, a análise e a resposta.

Na inserção de dados, o programa recebe a resposta do usuário e a insere na lista `acoes`, caso seja um número, para a inserção de dados caso o usuário digite "p" ou "P" ou avisa que a opção digitada é inválida caso o usuário digite qualquer outra coisa.

Na análise, o array é percorrido completamente e, para cada item, o array é novamente percorrido, somente a partir do item seguinte (pois só é necessário verificar a diferença entre um valor e ). Caso a diferença entre os itens analisados seja maior que o valor armazenado na variável `maior_lucro`, este valor é substituído pela diferença. 

Na resposta, o programa responde se é possível obter lucro com alguma operação e, em caso afirmativo, qual é essa operação.