CREATE TABLE `database_assignment_3`.`department` (
  `did` INT NOT NULL,
  `dname` VARCHAR(45) NOT NULL,
  `dtype` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NULL,
  PRIMARY KEY (`did`));
  
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('1', 'Central', 'tech', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('2', 'Central', 'toys', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('3', 'Central', 'food', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('4', 'Central', 'tech', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('5', 'Central', 'toys', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('6', 'Central', 'food', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('7', 'Central', 'tech');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('8', 'Central', 'toys');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('9', 'Central', 'food');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('10', 'tesco', 'tech', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('11', 'tesco', 'toys', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('12', 'tesco', 'food', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('13', 'tesco', 'tech', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('14', 'tesco', 'toys', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('15', 'tesco', 'food', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('16', 'tesco', 'tech');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('17', 'tesco', 'toys');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('18', 'tesco', 'food');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('19', 'tkmax', 'tech', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('20', 'tkmax', 'toys', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('21', 'tkmax', 'food', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('22', 'tkmax', 'tech', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('23', 'tkmax', 'toys', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('24', 'tkmax', 'food', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('25', 'tkmax', 'tech');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('26', 'tkmax', 'toys');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('27', 'tkmax', 'food');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('28', 'robinson', 'tech', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('29', 'robinson', 'toys', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('30', 'robinson', 'food', 'liverpool');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('31', 'robinson', 'tech', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('32', 'robinson', 'toys', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`, `address`) VALUES ('33', 'robinson', 'food', 'everton');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('34', 'robinson', 'tech');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('35', 'robinson', 'toys');
INSERT INTO `database_assignment_3`.`department` (`did`, `dname`, `dtype`) VALUES ('36', 'robinson', 'food');

CREATE TABLE `database_assignment_3`.`product` (
  `pid` INT NOT NULL,
  `pname` VARCHAR(45) NOT NULL,
  `ptype` VARCHAR(45) NOT NULL,
  `pcolor` VARCHAR(45) NULL,
  PRIMARY KEY (`pid`));

INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('1', 'tool1', 'tool', 'red');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('2', 'tool2', 'tool', 'blue');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('3', 'toy1', 'toy', 'blue');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`) VALUES ('4', 'toy2', 'toy');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('5', 'wear1', 'wear', 'red');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('6', 'wear2', 'wear', 'blue');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('7', 'gadget1', 'gadget', 'blue');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`) VALUES ('8', 'gadget2', 'gadget');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('9', 'drink1', 'drink', 'red');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('10', 'drink2', 'drink', 'red');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('11', 'snack1', 'snack', 'blue');
INSERT INTO `database_assignment_3`.`product` (`pid`, `pname`, `ptype`, `pcolor`) VALUES ('12', 'snack2', 'snack', 'red');

  
CREATE TABLE `database_assignment_3`.`sells` (
  `did` INT NOT NULL,
  `pid` INT NOT NULL,
  `quantity` INT NOT NULL DEFAULT '1',
  PRIMARY KEY (`did`, `pid`),
  INDEX `pid_idx` (`pid` ASC) VISIBLE,
  CONSTRAINT `did`
    FOREIGN KEY (`did`)
    REFERENCES `database_assignment_3`.`department` (`did`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `pid`
    FOREIGN KEY (`pid`)
    REFERENCES `database_assignment_3`.`product` (`pid`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('25', '2', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('25', '7', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('25', '5');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('35', '7');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('9', '3', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('9', '5');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('9', '7');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('9', '9', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('9', '11');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('10', '1', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('10', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('10', '5', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('10', '7');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('10', '9');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('20', '1');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('20', '3', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('20', '5');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('20', '7');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('20', '9');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('20', '12', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('34', '1');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('34', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('34', '3');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('34', '8', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('1', '5');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('1', '6');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`, `quantity`) VALUES ('1', '9', '2');
INSERT INTO `database_assignment_3`.`sells` (`did`, `pid`) VALUES ('1', '10');

CREATE TABLE `database_assignment_3`.`works_in` (
  `eid` INT NOT NULL,
  `did` INT NOT NULL,
  `since` DATE NULL,
  PRIMARY KEY (`eid`, `did`),
  FOREIGN KEY (eid) REFERENCES employee(eid) 
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (did) REFERENCES department(did) 
  ON DELETE CASCADE 
  ON UPDATE CASCADE) ;
  
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '1', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '2', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '5', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '7', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '10', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '13', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '16', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '17', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('1', '20', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('1', '25');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('1', '35');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '1', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '2', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '5', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '7', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '10', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '13', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '16', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '17', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('2', '20');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('2', '25');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('2', '35', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '1', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '2', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '5', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '7', '1990-09-03');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '10', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '13', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '16', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '17', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('7', '20');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('7', '25', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`) VALUES ('7', '35');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '1', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '2', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '5', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '7', '1990-09-01');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '10', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '13', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '16', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '17', '1990-09-02');
INSERT INTO `database_assignment_3`.`works_in` (`eid`, `did`, `since`) VALUES ('9', '20', '1990-09-02');

CREATE TABLE `database_assignment_3`.`employee` (
  `eid` INT NOT NULL,
  `ename` VARCHAR(45) NOT NULL,
  `age` INT NOT NULL,
  PRIMARY KEY (`eid`));
  
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('1', 'saeth', '20');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('2', 'saeth', '21');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('3', 'saeth', '22');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('4', 'prang', '30');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('5', 'prang', '31');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('6', 'prang', '32');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('7', 'champ', '40');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('8', 'champ', '41');
INSERT INTO `database_assignment_3`.`employee` (`eid`, `ename`, `age`) VALUES ('9', 'champ', '42');

#a
SELECT DISTINCT dname 
FROM database_assignment_3.department NATURAL JOIN database_assignment_3.sells NATURAL JOIN database_assignment_3.product
WHERE product.pcolor = 'blue';

#b
(SELECT DISTINCT dname 
FROM database_assignment_3.department NATURAL JOIN database_assignment_3.sells NATURAL JOIN database_assignment_3.product
WHERE product.ptype = 'tool')
#intersect
(SELECT DISTINCT dname 
FROM database_assignment_3.department NATURAL JOIN database_assignment_3.sells NATURAL JOIN database_assignment_3.product
WHERE product.ptype = 'toy')

#c
SELECT DISTINCT dname 
FROM database_assignment_3.department NATURAL JOIN database_assignment_3.sells 
NATURAL JOIN database_assignment_3.product
WHERE product.pcolor = 'blue' AND did IN (SELECT DISTINCT did from database_assignment_3.works_in) AND 
did NOT IN (SELECT DISTINCT did 
FROM database_assignment_3.employee NATURAL JOIN database_assignment_3.works_in 
WHERE employee.age > 40)

#d
SELECT did, max(age)
FROM database_assignment_3.employee NATURAL JOIN database_assignment_3.works_in
GROUP BY did;

#e
SELECT DISTINCT ename 
FROM database_assignment_3.employee 
WHERE age > (SELECT min(age) FROM database_assignment_3.department NATURAL JOIN database_assignment_3.works_in 
NATURAL JOIN database_assignment_3.employee
WHERE dname = 'Central');

#f
SELECT DISTINCT ename 
FROM database_assignment_3.employee NATURAL JOIN database_assignment_3.works_in
WHERE did IN (SELECT did 
FROM database_assignment_3.product NATURAL JOIN database_assignment_3.sells
GROUP BY did
HAVING count(DISTINCT ptype) >= 5)
