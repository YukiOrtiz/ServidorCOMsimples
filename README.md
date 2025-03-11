# ServidorCOMsimples

Henrique Carvalho Ferreira - 2210732 [CRIADOR DO REPOSITÓRIO]
Jean Carlos Araujo Medrado - 2212305
Alex Carlos do Nascimento Filho - 2212063

[ATENÇÃO: LEIA ATENTAMENTE AS RECOMENDAÇÕES E AVISOS ABAIXO]

- No repositório haverão - além do arquivo phyton com o script do servidor - algumas prints de como o servidor respondeu as requisições, como prova dos testes feitos. 
- Recomendo utilizar Postman para o teste, pois foi nele que o servidor recebeu as solicitações POST e onde foi realizado os testes.
- A seguir há uma imagem de uma das ações necessárias no Postman para o teste funcionar apropriadamente, o usuário deverá criar um novo header com a key e value sendo respectivamente igual a: "Content-Type" e "application/json". Em seguida na aba "Body" deverá ser enviado um parametro json que serão os dados que o usuário enviou ao servidor na hora de realizar login, lembrando que deverá ser marcada a opção "raw". O parametro utilizado durante os testes foi:
 
{
   "login": "meu_usuario",
   "senha": "minha_senha"
}

-Em seguida, o Postman retornou 200 para a solicitação, atestando que o servidor criado no arquivo phyton respondeu bem a requisição enviada pelo Postman.

- ![image](https://github.com/user-attachments/assets/84edfb72-ac61-46dc-8b6f-cf6039fa0356) [PARAMETROS JSON]

- ![image](https://github.com/user-attachments/assets/e6c17cdf-554d-4b89-9f7e-1288e26ab61f) [KEY + VALUE]

- ![image](https://github.com/user-attachments/assets/c1c68846-2ca5-42e7-8da5-d256355c46eb) [SAÍDA DO POSTMAN AO TESTE BEM SUCEDIDO]

- ![image](https://github.com/user-attachments/assets/898e0a84-7153-463f-88ad-e1c9cce9e867) [SAÍDA DO CONSOLE PHYTON EVIDENCIANDO O INICIO DO SERVIDOR E O ENVIO DE UMA MENSAGEM CODIGO 200 A REQUISIÇÃO DO POSTMAN]

  

