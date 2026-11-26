CREATE DATABASE biblioteca_jogos;
USE biblioteca_jogos;

CREATE TABLE jogos (
	id INT auto_increment PRIMARY KEY,
    titulo VARCHAR(50) NOT NULL,
	plataforma VARCHAR(20) NOT NULL,
    genero	VARCHAR(30) NOT NULL,
    status_jogo	VARCHAR(15) NOT NULL,
    nota DECIMAL(2,1),
    preco	DECIMAL(7,2)
);

CREATE USER 'desenvolvedor'@'localhost'
IDENTIFIED BY 'desen123';

GRANT SELECT, INSERT ON biblioteca_jogos.jogos
TO 'desenvolvedor'@'localhost';

SHOW GRANTS FOR 'desenvolvedor'@'localhost';

SELECT * FROM jogos;