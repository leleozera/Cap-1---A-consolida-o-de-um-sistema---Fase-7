-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-04-22 20:45:03 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE Aplicacão_agua CASCADE CONSTRAINTS 
;

DROP TABLE Aplicação_nutriente CASCADE CONSTRAINTS 
;

DROP TABLE Area_plantada CASCADE CONSTRAINTS 
;

DROP TABLE Cultura CASCADE CONSTRAINTS 
;

DROP TABLE Leitura_sensor CASCADE CONSTRAINTS 
;

DROP TABLE Produtor CASCADE CONSTRAINTS 
;

DROP TABLE Sensor CASCADE CONSTRAINTS 
;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE Aplicacão_agua 
    ( 
     id_aplicacao_agua     INTEGER  NOT NULL , 
     data_hora             TIMESTAMP  NOT NULL , 
     quantidade_litros     NUMBER  NOT NULL , 
     Area_plantada_id_area INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Aplicacão_agua 
    ADD CONSTRAINT Aplicacão_agua_PK PRIMARY KEY ( id_aplicacao_agua ) ;

CREATE TABLE Aplicação_nutriente 
    ( 
     id_aplicacao_nutriente    INTEGER  NOT NULL , 
     data_hora                 TIMESTAMP  NOT NULL , 
     tipo_nutriente            VARCHAR2 (50)  NOT NULL , 
     quantidade_gramas         NUMBER  NOT NULL , 
     Sensor_id_sensor          INTEGER  NOT NULL , 
     Leitura_sensor_id_leitura INTEGER  NOT NULL 
    ) 
;
CREATE UNIQUE INDEX Aplicação_nutriente__IDX ON Aplicação_nutriente 
    ( 
     Leitura_sensor_id_leitura ASC 
    ) 
;

ALTER TABLE Aplicação_nutriente 
    ADD CONSTRAINT Aplicação_nutriente_PK PRIMARY KEY ( id_aplicacao_nutriente, Sensor_id_sensor ) ;

CREATE TABLE Area_plantada 
    ( 
     Produtor_id_produtor INTEGER  NOT NULL , 
     id_area              INTEGER  NOT NULL , 
     tamanho_hectares     NUMBER  NOT NULL , 
     localizacao          VARCHAR2 (255)  NOT NULL , 
     id_area1             INTEGER  NOT NULL , 
     Sensor_id_sensor     INTEGER  NOT NULL 
    ) 
;
CREATE UNIQUE INDEX Area_plantada__IDX ON Area_plantada 
    ( 
     Sensor_id_sensor ASC 
    ) 
;

ALTER TABLE Area_plantada 
    ADD CONSTRAINT Area_plantada_PK PRIMARY KEY ( id_area ) ;

CREATE TABLE Cultura 
    ( 
     id_cultura INTEGER  NOT NULL , 
     nome       VARCHAR2 (100)  NOT NULL , 
     descrição  VARCHAR2 (255)  NOT NULL , 
     ciclo_dias INTEGER  NOT NULL 
    ) 
;

ALTER TABLE Cultura 
    ADD CONSTRAINT Cultura_PK PRIMARY KEY ( id_cultura ) ;

CREATE TABLE Leitura_sensor 
    ( 
     id_leitura     INTEGER  NOT NULL , 
     data_hora      TIMESTAMP  NOT NULL , 
     valor          NUMBER  NOT NULL , 
     unidade_medida VARCHAR2 (20)  NOT NULL 
    ) 
;

ALTER TABLE Leitura_sensor 
    ADD CONSTRAINT Leitura_sensor_PK PRIMARY KEY ( id_leitura ) ;

CREATE TABLE Produtor 
    ( 
     id_produtor INTEGER  NOT NULL , 
     nome        VARCHAR2 (100)  NOT NULL , 
     email       VARCHAR2 (100)  NOT NULL , 
     telefone    VARCHAR2 (20)  NOT NULL 
    ) 
;

ALTER TABLE Produtor 
    ADD CONSTRAINT Produtor_PK PRIMARY KEY ( id_produtor ) ;

CREATE TABLE Sensor 
    ( 
     id_sensor          INTEGER  NOT NULL , 
     tipo_sensor        VARCHAR2 (50)  NOT NULL , 
     modelo             VARCHAR2 (100)  NOT NULL , 
     Cultura_id_cultura INTEGER  NOT NULL 
    ) 
;
CREATE UNIQUE INDEX Sensor__IDX ON Sensor 
    ( 
     Cultura_id_cultura ASC 
    ) 
;

ALTER TABLE Sensor 
    ADD CONSTRAINT Sensor_PK PRIMARY KEY ( id_sensor ) ;

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE Aplicacão_agua 
    ADD CONSTRAINT Aplicacão_agua_Area_plantada_FK FOREIGN KEY 
    ( 
     Area_plantada_id_area
    ) 
    REFERENCES Area_plantada 
    ( 
     id_area
    ) 
;

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE Aplicação_nutriente 
    ADD CONSTRAINT Aplicação_nutriente_Leitura_sensor_FK FOREIGN KEY 
    ( 
     Leitura_sensor_id_leitura
    ) 
    REFERENCES Leitura_sensor 
    ( 
     id_leitura
    ) 
;

ALTER TABLE Aplicação_nutriente 
    ADD CONSTRAINT Aplicação_nutriente_Sensor_FK FOREIGN KEY 
    ( 
     Sensor_id_sensor
    ) 
    REFERENCES Sensor 
    ( 
     id_sensor
    ) 
;

ALTER TABLE Area_plantada 
    ADD CONSTRAINT Area_plantada_Produtor_FK FOREIGN KEY 
    ( 
     Produtor_id_produtor
    ) 
    REFERENCES Produtor 
    ( 
     id_produtor
    ) 
;

ALTER TABLE Area_plantada 
    ADD CONSTRAINT Area_plantada_Sensor_FK FOREIGN KEY 
    ( 
     Sensor_id_sensor
    ) 
    REFERENCES Sensor 
    ( 
     id_sensor
    ) 
;

ALTER TABLE Sensor 
    ADD CONSTRAINT Sensor_Cultura_FK FOREIGN KEY 
    ( 
     Cultura_id_cultura
    ) 
    REFERENCES Cultura 
    ( 
     id_cultura
    ) 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             7
-- CREATE INDEX                             3
-- ALTER TABLE                             13
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   2
-- WARNINGS                                 0
