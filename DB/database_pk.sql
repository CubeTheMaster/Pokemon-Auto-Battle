create database lotta;

use lotta;

create table pokemon
(
id int primary key not null,
name varchar(20) not null,
type_1 varchar(20) not null,
type_2 varchar(20),
hp int not null,
attack int not null,
defense int not null,
sp_attack int not null,
sp_defense int not null,
speed int not null
);

create table mossa
(
id int primary key not null,
nome varchar(50) not null,
type_1 varchar(50) not null,
damage int not null,
accuracy int not null,
categoria VARCHAR(20) NOT NULL,
CHECK (categoria IN ('fisica', 'speciale'))
);

CREATE TABLE conosce (
id_pk INT,
id_mossa INT,
PRIMARY KEY (id_pk, id_mossa),
FOREIGN KEY (id_pk) REFERENCES pokemon(id),
FOREIGN KEY (id_mossa) REFERENCES mossa(id)
);

CREATE Table pozione (
    nome varchar(20) primary key not null,
    CHECK (nome IN ('pozione', 'superpozione', 'iperpozione')),
    quatità int not null
);