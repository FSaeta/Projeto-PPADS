var btn_avaliacoes = document.getElementById("btn-avaliacoes");
var btn_todos_amigos = document.getElementById("btn-todos_amigos");
var btn_amigos_comum = document.getElementById("btn-amigos_comum");

var div_avaliacoes = document.getElementById("div-avaliacoes");
var div_todos_amigos = document.getElementById("div-todos_amigos");
var div_amigos_comum = document.getElementById("div-amigos_comum");

btn_avaliacoes.addEventListener("click",function(){
    if(div_avaliacoes.style.display === "block"){
        div_avaliacoes.style.display = "none"
    } else {
        div_avaliacoes.style.display = "block"
        div_todos_amigos.style.display = "none"
        div_amigos_comum.style.display = "none"
    }
});

btn_todos_amigos.addEventListener("click",function(){
    if(div_todos_amigos.style.display === "block"){
        div_todos_amigos.style.display = "none"
    } else {
        div_todos_amigos.style.display = "block"
        div_avaliacoes.style.display = "none"
        div_amigos_comum.style.display = "none"
    }
});

btn_amigos_comum.addEventListener("click",function(){
    if(div_amigos_comum.style.display === "block"){
        div_amigos_comum.style.display = "none"
    } else {
        div_amigos_comum.style.display = "block"
        div_avaliacoes.style.display = "none"
        div_todos_amigos.style.display = "none"
    }
});
