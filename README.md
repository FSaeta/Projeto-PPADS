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

# 6- Diagrama de Domínio
![Diagrama de Dominio](Diagramas/DiagramaDominio.jpg)
&nbsp;

# 7- Diagrama de Classes
![Diagrama de Classes](Diagramas/DiagramaClasses.jpg)

# 8 - Diagrama de Navegação
![Diagrama de Navegação](Diagramas/Navegacao.jpg)

# 9 - Wireframes
### 1. Tela de Login
<img src="Diagramas/Wireframes/FazerLogin.png" width="300">

### 2. Tela de Cadastro de Usuário
<img src="Diagramas/Wireframes/CadastrarUsuario.png" width="300">

### 3. Atualizar Cadastro
<img src="Diagramas/Wireframes/AtualizarCadastro.png" width="300">

### 4. Cadastro de Item
<img src="Diagramas/Wireframes/CadastrarItem.png" width="300">

### 5. Tela de Amigos
<img src="Diagramas/Wireframes/ProporAmizade.png" width="300">

### 6. Tela Principal
<img src="Diagramas/Wireframes/Index.png" width="300">

### 7. Ver Avaliações dos Itens / Usuários
<img src="Diagramas/Wireframes/VerAvaliacoesUsuario.png" width="300">

### 8. Curtir / Comentar Avaliação
<img src="Diagramas/Wireframes/VerAvaliacoesUsuario.png" width="300">

### 9. Tela dos Itens na Biblioteca
<img src="Diagramas/Wireframes/VerDetalhesItem.png" width="300">

### 10. Tela dos Relatórios
<img src="Diagramas/Wireframes/SolicitarRelatorios.png" width="300">

### 11. Tela da Validação de Itens
<img src="Diagramas/Wireframes/ValidarItem.png" width="300">
