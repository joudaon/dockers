DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id int NOT NULL auto_increment,
  email VARCHAR(128) NOT NULL UNIQUE,
  created_on DATETIME NOT NULL DEFAULT NOW(),
  PRIMARY KEY (id)
);
