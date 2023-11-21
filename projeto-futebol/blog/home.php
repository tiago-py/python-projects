<?php
    include_once './conn/conexao.php';
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz</title> 
    <link rel="stylesheet" href="css/style.css">

</head>
<body>
    <div class="progresso">
        <div class="progressoBarra"></div>
    </div> 

    <div  class="questaoArea">
        <div class="questao">AQUI FICA A QUESTAO</div>

        <div class="options">
       
        </div>
        <div class="feedbackMensagem">
        <p class="feedback"></p>
        </div>
    </div>
    
    <button id="proximoBotao" onclick="proximaQuestao()" class="button">Próxima Questão</button>

    <div class="pontuacaoArea">
        <div class="pontuacaoTitulo">Quiz Completo</div>
        <div class="pontuacaoPontos">Acertou x</div>
    </div>
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
    <div class="feedbackArea">
    <form method="post" action="feedback.php" class="feedbackArea">
    <input type="radio" id="cm_star-empty" name="fb" value="5" checked/>
      <label for="cm_star-1"><i class="fa"></i></label>
      <input class="star-icon ativo"type="radio" id="cm_star-1" name="fb" value="1"/>
      <label for="cm_star-2"><i class="fa"></i></label>
      <input class="star-icon"type="radio" id="cm_star-2" name="fb" value="2"/>
      <label for="cm_star-3"><i class="fa"></i></label>
      <input class="star-icon" type="radio" id="cm_star-3" name="fb" value="3"/>
      <label for="cm_star-4"><i class="fa"></i></label>
      <input class="star-icon" type="radio" id="cm_star-4" name="fb" value="4"/>
      <label for="cm_star-5"><i class="fa"></i></label>
      <input class="star-icon" type="radio" id="cm_star-5" name="fb" value="5"/><br><br>
      <textarea class="text-melhorias" placeholder="Em que podemos melhorar?" name="melhorias"></textarea>
        <br>
      <input class="input-nome" type="text" name="nome"placeholder="Nome:">
      <br>
      <br>
      <input type="submit" value="Enviar Feedback" class="button" id="button">

      </form>
    </div>
    
    <script src="js/questoes.js"></script>
    <script src="js/script.js"></script>
    <script src="js/estrelas.js"></script>
</body>
</body>
</html>