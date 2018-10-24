# Climatologia Crawler - ClimaTempo
Esse projeto tem o intuito de estruturar a climatologia de todas as cidades do Brasil por meio do site ClimaTempo

## Execução (sem Spark)

Para executar o código, basta rodar o script `__init__.py` que se encontra na pasta *src/* do projeto. O resultado por cidade será salvo em um arquivo chamado *output.csv* na pasta raiz do projeto.

## Execução (com Spark)

Para executar o código de forma distribuída, é necessrio instalar o pyspark - [Tutorial de como instalar o pyspark](https://spark.apache.org/docs/0.9.0/python-programming-guide.html)
Após a instalação, deve ser executado o comando spark-submit:

```
spark-submit --master local[*] src/__distributed__.py
```


## Código Bonus!!! :)

Para executar a resolução do problema Anjo Bom/Anjo Mal, basta rodar o script `__bonus__.py` que se encontra na pasta *src/* do projeto.
