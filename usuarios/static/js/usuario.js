var btn_avaliacoes = document.getElementById("btn-avaliacoes");
var btn_todos_amigos = document.getElementById("btn-todos_amigos");
var btn_amigos_comum = document.getElementById("btn-amigos_comum");
var btn_editar_dados = document.getElementById("btn-editar_dados");
var btn_alterar_senha = document.getElementById("btn-alterar_senha");

var div_avaliacoes = document.getElementById("div-avaliacoes");
var div_todos_amigos = document.getElementById("div-todos_amigos");
var div_amigos_comum = document.getElementById("div-amigos_comum");
var div_editar_dados = document.getElementById("div-editar_dados");
var div_alterar_senha = document.getElementById("div-alterar_senha");

var botoes = [btn_avaliacoes, btn_todos_amigos, btn_amigos_comum, btn_editar_dados, btn_alterar_senha];
var divs = [div_avaliacoes, div_todos_amigos, div_amigos_comum, div_editar_dados, div_alterar_senha];


// botoes.forEach(function(botao_vez, indice, botoes){
//     if (botao_vez != null){
//         botao_vez.addEventListener("click",function(){
//             if(div_avaliacoes.style.display === "block"){
//                 div_avaliacoes.style.display = "none"
//                 botao_vez.classList.add('btn-outline-dark');
//                 botao_vez.classList.remove('btn-outline-dark-clicked');
//             } else {
//                 divs.forEach(function(div, idx, divs){
//                     if (div != divs[indice] && div != null){
//                         div.style.display = "none"
//                     } else if (div == divs[indice]){
//                         div_avaliacoes.style.display = "block"
//                     }
//                 });
//                 botoes.forEach(function (btn, index, botoes){
//                     if (btn != null){
//                         if (btn.classList.contains('btn-outline-dark-clicked')){
//                             btn.classList.remove('btn-outline-dark-clicked');
//                         }
//                     }
//                 });
//                 botao_vez.classList.remove('btn-outline-dark');
//                 botao_vez.classList.add('btn-outline-dark-clicked');
//             }
//         });
//     }
// });

if (btn_avaliacoes != null){
    btn_avaliacoes.addEventListener("click",function(){
        if(div_avaliacoes.style.display === "block"){
            div_avaliacoes.style.display = "none"
            btn_avaliacoes.classList.add('btn-outline-dark');
            btn_avaliacoes.classList.remove('btn-outline-dark-clicked');
        } else {
            divs.forEach(function (div, index, divs){
                if (div != null){
                    div.style.display = "none"
                }
            });
            div_avaliacoes.style.display = "block"

            botoes.forEach(function (btn, index, botoes){
                if (btn != null){
                    if (btn.classList.contains('btn-outline-dark-clicked')){
                        btn.classList.remove('btn-outline-dark-clicked');
                    }
                }
            });
            btn_avaliacoes.classList.remove('btn-outline-dark');
            btn_avaliacoes.classList.add('btn-outline-dark-clicked');
        }
    });
}

if (btn_todos_amigos != null){
    btn_todos_amigos.addEventListener("click",function(){
        if(div_todos_amigos.style.display === "block"){
            div_todos_amigos.style.display = "none"
            btn_todos_amigos.classList.add('btn-outline-dark');
            btn_todos_amigos.classList.remove('btn-outline-dark-clicked');

        } else {
            divs.forEach(function (div, index, divs){
                if (div != null){
                    div.style.display = "none"
                }
            });
            div_todos_amigos.style.display = "block"
            
            botoes.forEach(function (btn, index, botoes){
                if (btn != null){
                    if (btn.classList.contains('btn-outline-dark-clicked')){
                        btn.classList.remove('btn-outline-dark-clicked');
                    }
                }
            });
            btn_todos_amigos.classList.remove('btn-outline-dark');
            btn_todos_amigos.classList.add('btn-outline-dark-clicked')
        }
    });
}

if (btn_amigos_comum != null){
    btn_amigos_comum.addEventListener("click",function(){
        if(div_amigos_comum.style.display === "block"){
            div_amigos_comum.style.display = "none"
            btn_amigos_comum.classList.add('btn-outline-dark');
            btn_amigos_comum.classList.remove('btn-outline-dark-clicked');
        } else {
            divs.forEach(function (div, index, divs){
                if (div != null){
                    div.style.display = "none"
                }
            });
            div_amigos_comum.style.display = "block"

            botoes.forEach(function (btn, index, botoes){
                if (btn != null){
                    if (btn.classList.contains('btn-outline-dark-clicked')){
                        btn.classList.remove('btn-outline-dark-clicked');
                    }
                }
            });
            btn_amigos_comum.classList.remove('btn-outline-dark');
            btn_amigos_comum.classList.add('btn-outline-dark-clicked')
        }
    });
}

if (btn_editar_dados != null){
    btn_editar_dados.addEventListener("click",function(){
        if(div_editar_dados.style.display === "block"){
            div_editar_dados.style.display = "none"
            btn_editar_dados.classList.add('btn-outline-dark');
            btn_editar_dados.classList.remove('btn-outline-dark-clicked');
        } else {
            divs.forEach(function (div, index, divs){
                if (div != null){
                    div.style.display = "none"
                }
            });
            div_editar_dados.style.display = "block"

            botoes.forEach(function (btn, index, botoes){
                if (btn != null){
                    if (btn.classList.contains('btn-outline-dark-clicked')){
                        btn.classList.remove('btn-outline-dark-clicked');
                    }
                }
            });
            btn_editar_dados.classList.remove('btn-outline-dark');
            btn_editar_dados.classList.add('btn-outline-dark-clicked')
        }
    });
}


if (btn_alterar_senha != null){
    btn_alterar_senha.addEventListener("click",function(){
        if(div_alterar_senha.style.display === "block"){
            div_alterar_senha.style.display = "none"
            btn_alterar_senha.classList.add('btn-outline-dark');
            btn_alterar_senha.classList.remove('btn-outline-dark-clicked');
        } else {
            divs.forEach(function (div, index, divs){
                if (div != null){
                    div.style.display = "none"
                }
            });
            div_alterar_senha.style.display = "block"

            botoes.forEach(function (btn, index, botoes){
                if (btn != null){
                    if (btn.classList.contains('btn-outline-dark-clicked')){
                        btn.classList.remove('btn-outline-dark-clicked');
                    }
                }
            });
            btn_alterar_senha.classList.remove('btn-outline-dark');
            btn_alterar_senha.classList.add('btn-outline-dark-clicked')
        }
    });
}