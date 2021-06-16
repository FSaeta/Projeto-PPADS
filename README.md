# HiperFlix

# Especificação de requisitos
## PROJETO: Aplicativo para Recomendação de Filmes, Séries e Livros
### Curso de Sistemas de Informação
### Prática Profissional em Análise e Desenvolvimento de Sistemas
### Turma 05K
### 1º semestre de 2021

              UNIVERSIDADE PRESBITERIANA MACKENZIE
                      
              FACULDADE DE COMPUTAÇÃO E INFORMÁTICA









                          LETHICIA MARQUEZINI
                     JOAO PEDRO FRANCA DE OLIVEIRA










          Aplicativo para Recomendação de Filmes, Séries e Livros 
                            
                               HiperFlix













                                SÃO PAULO
                                  2021



# 1- Introdução

O presente projeto em questão foi desenvolvido com o intuito de desenvolver uma aplicação de recomendação de filmes, livros e séries. A ideia principal é que seja utilizado por uma empresa e seus colaboradores visando a promoção do desenvolvimento social, do engajamento e da sinergia entre os indivíduos e suas clusterizações dentro da instituição como um todo. O sistema utilizará os insumos gerados pelos próprios usuários para auxiliar nas avaliações, na recomendação de itens de maneira intuitiva e automática.


# 2- Requisitos do Sistema

### 2.1- Requisitos Funcionais

RF1	- O sistema deverá permitir que o colaborador da empresa faça um cadastro.

RF2	- O sistema deverá permitir que o colaborador possa atualizar as informações de cadastro.

RF3 -  O sistema deverá permitir que qualquer membro possa cadastrar novo item (livro, filme ou série).

RF4	- O sistema deverá permitir que o administrador possa validar os novos itens cadastrados.

RF5	- O sistema deverá permitir que os membros possam avaliar os itens.

RF6 - O sistema deverá permitir a pesquisa de outros membros.

RF7 - O sistema deverá permitir que os membros possam enviar solicitações de amizade para outros membros.

RF8 - O sistema deverá permitir que os membros possam aceitar ou recusar solicitações de amizade de outros membros.

RF9 - O sistema deverá permitir que os membros possam reagir ou retirar a reação nas avaliações.

RF10 - O sistema deverá permitir a visualização de amigos em comum entre os membros.

RF11 - O sistema deverá disponibilizar uma página de análise de dados para os gerentes do serviço.


### 2.2- Requisitos não Funcionais

RNF1 - O sistema poderá ser acessado web através de navegador.

RNF2 - O sistema deverá ser responsivo e leve para carregamento das funções.

RNF3 - Os dados devem ser armazenados em uma base de dados, podendo ser relacional ou NoSQL

RNF4 - Aplicação deve ser implementada em um provedor de serviços na internet.

RNF5 - O sistema não pode demorar mais do que 5 segundos para carregar uma página.

RNF6 - A disponibilidade da aplicação deverá atender o padrão 99.99%, em regime 24x7

RNF7 - A documentação do sistema deverá apresentar indicativos de segurança dos dados cadastrais e transacionais para evitar possíveis invasões ao site.

# 3- Casos de uso
## 3.1- Diagrama de casos de uso

![Diagrama de casos de uso](Diagramas/CasosdeUso/CasosDeUso.jpg)

## 3.2- Especificações dos casos de uso

![Fazer Login](/Diagramas/CasosdeUso/FazerLogin.png)

![Cadastrar Usuário](/Diagramas/CasosdeUso/CadastrarUsuario.png)

![Atualizar Cadastro](/Diagramas/CasosdeUso/AtualizarCadastro.jpg)

![Propor Amizade](/Diagramas/CasosdeUso/ProporAmizade.png)

![Cadastrar Item](/Diagramas/CasosdeUso/CadastrarItem.png)

![Validar Item](/Diagramas/CasosdeUso/ValidarItem.png)
![Validar Item2](/Diagramas/CasosdeUso/ValidarItem2.png)

![Fazer Avaliação](/Diagramas/CasosdeUso/AvaliarItem.png)

![Curtir Avaliação](/Diagramas/CasosdeUso/CurtirAvaliacao.png)

![Comentar Avaliação](/Diagramas/CasosdeUso/ComentarAvaliacao.png)

![Solicitar Relatorios](/Diagramas/CasosdeUso/SolicitarRelatorios.png)

![Ver Avaliações Itens](/Diagramas/CasosdeUso/VerAvaliacoesItens.png)

![Ver Avaliações Usuários](/Diagramas/CasosdeUso/VerAvaliacoesUsuarios.png)

![Ver Detalhes Itens](/Diagramas/CasosdeUso/VerDetalhesItens.png)


# 4- Navegação
## 4.1- Diagrama de Navegação

![Diagrama de Navegação](Diagramas/Navegacao.jpg)

## 4.2- Wireframes
###1. Tela de Login
![Realizar Login](Diagramas/Wireframes/FazerLogin.png)
&nbsp;
&nbsp;
###2. Tela de Registro de Usuário
![Realizar Registro](Diagramas/Wireframes/FazerRegistro.png)
&nbsp;
&nbsp;
###3. Alterar Registro
![Alterar Registro](Diagramas/Wireframes/AlterarRegistro.png)
&nbsp;
&nbsp;
###4. Excluir Registro
![Excluir Registro](Diagramas/Wireframes/ExcluirRegistro.png)
&nbsp;
&nbsp;
###5. Tela de senha/username incorretos
![Excluir Registro](Diagramas/Wireframes/LoginIncorreto.png)
&nbsp;
&nbsp;
###6. Menu de opções no perfil do usuário
![Menu de opções do perfil](Diagramas/Wireframes/MenuOpcoesPerfil.png)
&nbsp;
&nbsp;
###7. Tela Principal de Cadastro
![Principal de Cadastro](Diagramas/Wireframes/PrincipalDeCadastro.jpeg)
&nbsp;
&nbsp;
###8. Tela de Cadastro de Filme
![Principal de Cadastro](Diagramas/Wireframes/CadastrarFilme.jpeg)
&nbsp;
&nbsp;
###9. Tela de Cadastro de Serie
![Principal de Cadastro](Diagramas/Wireframes/CadastrarSerie.jpeg)
&nbsp;
&nbsp;
###10. Tela de Cadastro de Livro
![Principal de Cadastro](Diagramas/Wireframes/CadastrarLivro.jpeg)
&nbsp;
&nbsp;
###11. Tela de Cadastro Efetuado
![Cadastro Efetuado](Diagramas/Wireframes/CadastroEfetuado.jpeg)
&nbsp;
&nbsp;
###12. Tela de Cadastro de livro inválido
![Cadastro de livro inválido](Diagramas/Wireframes/LivroCadastrado.jpg)
&nbsp;
&nbsp;
###13. Tela de Cadastro de série inválido
![Cadastro de série inválido](Diagramas/Wireframes/SerieCadastrada.jpg)
&nbsp;
&nbsp;
###13. Tela de Cadastro de filme inválido
![Cadastro de filme inválido](Diagramas/Wireframes/FilmeCadastrado.jpg)
&nbsp;
&nbsp;
###14. Tela de Nova Avaliação
![Nova Avaliação](Diagramas/Wireframes/FazerAvaliacao.png)
&nbsp;
&nbsp;
###15. Tela de Reagir e Comentar Avaliações e Comentários
![Reações e comentarios](Diagramas/Wireframes/ReagirAvaliacao.png)
&nbsp;
&nbsp;
###16. Tela de Itens cadastrados a serem validados
![Itens cadastrados](Diagramas/Wireframes/ValidarCadastros.png)
&nbsp;
&nbsp;
###17. Tela de validar Cadastro de Item
![Validar cadastro](Diagramas/Wireframes/ValidarCadastro.png)
&nbsp;
&nbsp;
###18. Tela de Procurar Amigos
![Validar cadastro](Diagramas/Wireframes/ProcurarAmigos.jpeg)
&nbsp;
&nbsp;
###19. Tela de Receber recomendações
![Receber recomendações](Diagramas/Wireframes/Recomendacoes.jpg)
&nbsp;
&nbsp;
###20. Tela de Receber sugestões de amizades
![Receber sugestões de amizades](Diagramas/Wireframes/SugestoesAmizades.png)
&nbsp;
&nbsp;
###21. Tela de Busca de amigos
![Busca de amigos](Diagramas/Wireframes/BuscaAmigos.png)
&nbsp;
&nbsp;
###22. Tela de de amigos
![Amigos](Diagramas/Wireframes/Amigos.png)
&nbsp;
&nbsp;
###23. Tela de Propor relacionamento
![Propor relacionamento](Diagramas/Wireframes/ProporRelacionamento.png)
&nbsp;
&nbsp;
###24. Tela de avaliação excluida
![Avaliação excluida](Diagramas/Wireframes/AvaliacaoExcluida.png)
&nbsp;
&nbsp;
###25. Tela de comentário excluido
![Comentário excluido](Diagramas/Wireframes/ComentarioExcluido.png)
&nbsp;
&nbsp;

# 5- Diagramas de Sequencias

## Fazer Login
![Fazer Login](Diagramas/Sequencias/FazerLogin.jpg)

## Cadastrar Usuario
![Cadastrar Usuario](Diagramas/Sequencias/CadastrarUsuario.jpg)

## Atualizar Cadastro
![Atualizar Cadastro](Diagramas/Sequencias/AtualizarCadastro.jpg)

## Propor Amizade
![Propor Amizade](Diagramas/Sequencias/ProporAmizade.jpg)

## Cadastrar Item
![Cadastrar Item](Diagramas/Sequencias/CadastrarItem.jpg)

## Validar Item
![Validar Item](Diagramas/Sequencias/ValidarCadastro.jpg)

## Solicitar Relatório
![Solicitar Relatório](Diagramas/Sequencias/SolicitarRelatorio.jpg)

## Avaliar Item
![Avaliar Item](Diagramas/Sequencias/AvaliarItem.jpg)

## Curtir Avaliação
![Curtir Avaliação](Diagramas/Sequencias/CurtirAvaliacao.jpg)

## Comentar Avaliação
![Comentar Avaliação](Diagramas/Sequencias/ComentarAvaliacao.jpg)

## Ver Avaliações Itens
![Ver Avaliações Itens](Diagramas/Sequencias/VerAvaliacoesItens.jpg)

## Ver Avaliações Membros
![Ver Avaliações Membros](Diagramas/Sequencias/VerAvaliacoesMembros.jpg)

## Ver Detalhes Itens
![Ver Detalhes Itens](Diagramas/Sequencias/VerDetalhesItem.jpg)

&nbsp;
# 6- Diagrama de Classes

![Diagrama de Classes](Diagramas/Classes/classes.png)
&nbsp;

# 7- Diagrama de Domínio
![Diagrama de Dominio](Diagramas/DiagramaDominio.jpg)
