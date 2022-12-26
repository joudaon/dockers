DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id int NOT NULL auto_increment,
  username VARCHAR(128) NOT NULL UNIQUE,
  email VARCHAR(128) NOT NULL UNIQUE,
  password VARCHAR(128) NOT NULL,
  created_on DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);