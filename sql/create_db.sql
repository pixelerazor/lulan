CREATE SCHEMA lulan DEFAULT CHARACTER SET utf8;
CREATE TABLE lulan.users (
  id INT NOT NULL,
  nickName VARCHAR(90) NULL,
  password VARCHAR(90) NULL,
  firstName MEDIUMBLOB NULL,
  lastName MEDIUMBLOB NULL,
  PRIMARY KEY (id),
  UNIQUE INDEX nickname_UNIQUE (nickName ASC));

  CREATE TABLE lulan.games (
    id INT NOT NULL,
    gameName VARCHAR(90) NULL,
    version VARCHAR(90) NULL,
    PRIMARY KEY (id));

  CREATE TABLE lulan.turniere (
    id INT NOT NULL,
    teamList VARCHAR(90) NULL,
    PRIMARY KEY (id));