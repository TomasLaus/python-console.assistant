CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE users(
    id int(25) auto_increment not null,
    name varchar(100),
    lastname varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    createdat date not null,
    CONSTRAINT PK_users PRIMARY KEY(id),
    CONSTRAINT UQ_email UNIQUE(email) 
)ENGINE=InnoDB;

CREATE TABLE notes(
    id int(25) auto_increment not null,
    user_id int(25) not null,
    title varchar(255) not null,
    description MEDIUMTEXT,
    createdat date not null,
    CONSTRAINT PK_notes PRIMARY KEY(id),
    CONSTRAINT FK_note_user FOREIGN KEY(user_id) REFERENCES users(id)
)ENGINE=InnoDB;