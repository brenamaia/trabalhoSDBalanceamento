# Balanceamento de carga entre servidores

Este repositório contém códigos referentes a um sistema distribuído composto por cliente, middleware e servidores, onde a comunicação entre os mesmos foi realizada utilizando o protocolo REST, e a programação foi realizada com a linguagem de programação Python, utilizando o framework Flask.

O cliente (simula_cliente.py) realiza a leitura de um arquivo (ArquivoGerado.txt) e envia para o middleware (middleware.py) uma requisição para contagem de palavras do texto. O middleware recebe o texto enviado pelo cliente e realiza o balanceamento de carga de modo dinâmico, levando em consideração a disponibilidade dos servidores (servidor1.py e servidor2.py) e a utilização de CPU dos mesmos. Caso um dos servidores esteja indisponível, o middleware direciona a requisição para outro servidor. Se os dois servidores estiverem disponíveis, o middleware irá analisar o consumo de cpu dos mesmos para verificar qual deles está trabalhando menos e enviar a requisiçao. Após receber a resposta do servidor, o middleware a encaminha para o cliente. 


