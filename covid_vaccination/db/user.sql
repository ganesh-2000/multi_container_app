CREATE DATABASE first;
use first;
GRANT ALL on first to root@localhost;


CREATE TABLE student (
  id int AUTO_INCREMENT,
  reg_no VARCHAR(20),
  name VARCHAR(50) NOT NULL,
  vaccinated BOOLEAN NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


insert into student(id,reg_no,name,vaccinated) values
(1,'A123', 'Ganesh Bhagat', true),
(2,'A124', 'Om Sathe', false);
