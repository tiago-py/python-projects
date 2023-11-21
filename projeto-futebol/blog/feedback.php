<?php
include_once './conn/conexao.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    try {
        // Recuperar os dados do formulário
        $nome = $_POST["nome"];
        $rating = $_POST["fb"];
        $melhorias = $_POST["melhorias"];

        // Conectar ao banco de dados usando PDO
        $conn = new PDO("mysql:host=localhost;dbname=banco_expoete", "root", "");
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Preparar a consulta SQL com placeholders
        $sql = "INSERT INTO feedback (estrelas, nome, melhorias) VALUES (:estrelas, :nome, :melhorias)";
        $stmt = $conn->prepare($sql);

        // Vincular os valores aos placeholders
        $stmt->bindParam(":nome", $nome);
        $stmt->bindParam(":estrelas", $rating);
        $stmt->bindParam(":melhorias", $melhorias);

        // Executar a consulta
        $stmt->execute();

        header("Location: index.php");
        exit();
    } catch (PDOException $e) {
        echo "Erro ao enviar feedback: " . $e->getMessage();
    }
}
?>
