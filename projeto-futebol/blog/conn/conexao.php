<?php
$username = 'root';
$password = ''; //aluno123 -- aqui na escola
try {
    $conn = new PDO('mysql:host=localhost;dbname=banco_expoete',
    $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    echo 'erro ao conectar com o mysql: ' . $e->getMessage();
}
?>