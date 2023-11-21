//VAR INICIAIS
let questaoAtual = 0;
let questoesCorretas = 0;
mostrarQuestao();

//EVENTOS CLICK
document.querySelector("#resetarQuiz").addEventListener("click",resetarQuiz);


//FUNÇOES
function mostrarQuestao(){
   if(questoes[questaoAtual]){
        let q = questoes[questaoAtual];

        //BARRA PROGRESSO
        let barraProgresso = Math.floor((questaoAtual /questoes.length)*100);
        document.querySelector(".progressoBarra").style.width = `${barraProgresso}%`
        document.querySelector(".feedbackMensagem").style.display = "none";
        document.querySelector("#proximoBotao").style.display = "none";
        document.querySelector(".pontuacaoArea").style.display = 'none';
        document.querySelector(".feedbackArea").style.display = 'none';
        document.querySelector(".questaoArea").style.display = 'block';

        document.querySelector(".questao").innerHTML = q.questao;
        let optionsHtml = '';

        for (let i in q.opcoes) {
          optionsHtml += `<div class="opcao" alternativa="${i}" class="option"><span>${parseInt(i)+1}-</span> ${q.opcoes[i]}</div><br>`;
        }
        document.querySelector(".options").innerHTML = optionsHtml;

        document.querySelectorAll(".options .opcao").forEach(item =>{
            item.addEventListener("click", botaoClicar);
        } )
   }else{
     //acabou as questoes
     finalizarQuiz();
     console.log("ACABOU");
   } 
}
function botaoClicar(e){
  let opcaoClicada = e.target.getAttribute("alternativa");

  if(questoes[questaoAtual].correta == opcaoClicada){
    document.querySelector(".feedback").innerHTML = "Acertou!!"
    document.querySelector(".feedback").style.color = "green";
     questoesCorretas ++;
  }else{
    document.querySelector(".feedback").innerHTML = "Errou!!"
    document.querySelector(".feedback").style.color = "red";
  }
  document.querySelector(".feedbackMensagem").style.display = "block";
  document.querySelector("#proximoBotao").style.display = "block";
  questaoAtual++;
}

function proximaQuestao(){
  document.querySelector(".feedbackMensagem").style.display = "none";
  document.querySelector("#proximoBotao").style.display = "none";
  mostrarQuestao()
}
// ...


//FINLIZANDO O QUIZ
function finalizarQuiz(){
    document.querySelector(".pontuacaoArea").style.display = 'block';
    document.querySelector(".questaoArea").style.display = 'none';
    document.querySelector(".progressoBarra").style.width = `100%`
    document.querySelector(".pontuacaoPontos").innerHTML = `Acertou ${questoesCorretas} de ${questaoAtual} questoes`;
    document.querySelector(".feedbackArea").style.display = 'block';
}

function resetarQuiz(){
    questaoAtual = 0;
    questoesCorretas = 0;
    mostrarQuestao();
}


$('button.submit').disabled = true; // disable button on load

// Enable button 
function enable_submit() {
  $('button.submit').disabled = false;
  $('button.submit').addClass('not-disabled');
}

// Disable button
function disable_submit() {
  $('button.submit').disabled = true;
  $('button.submit').removeClass('not-disabled');
}

// Display feedback after rating 
$('.rating__input').on('click', function() {
  var rating = this['value'];
    $('.rating__label').removeClass('active');
  $(this).siblings('.rating__label').addClass('active');
  $('.feedback').css('display', "block");
  
  feedback_validate(rating);
  
});

// Run enable button function based on input
$('.feedback textarea').keyup(function() {
  if ($('.feedback textarea').val().length > 3)   {
    enable_submit();
  }
});

// Enable or disable button by validation
function feedback_validate(val) {
  if (val <= 3) {
    disable_submit();
    
  } 
  else if (val > 3) {
    enable_submit();
  }
  
}