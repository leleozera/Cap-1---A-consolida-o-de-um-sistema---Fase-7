CREATE TABLE Produtor (
    id_produtor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
);

CREATE TABLE Cultura (
    id_cultura INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    ciclo_dias INTEGER NOT NULL
);

CREATE TABLE Sensor (
    id_sensor INTEGER PRIMARY KEY,
    tipo_sensor TEXT NOT NULL,
    modelo TEXT NOT NULL,
    Cultura_id_cultura INTEGER NOT NULL,
    FOREIGN KEY (Cultura_id_cultura) REFERENCES Cultura (id_cultura)
);

CREATE TABLE Leitura_sensor (
    id_leitura INTEGER PRIMARY KEY,
    data_hora TEXT NOT NULL,
    valor REAL NOT NULL,
    unidade_medida TEXT NOT NULL
);

CREATE TABLE Area_plantada (
    id_area INTEGER PRIMARY KEY,
    Produtor_id_produtor INTEGER NOT NULL,
    tamanho_hectares REAL NOT NULL,
    localizacao TEXT NOT NULL,
    id_area1 INTEGER NOT NULL,
    Sensor_id_sensor INTEGER NOT NULL,
    FOREIGN KEY (Produtor_id_produtor) REFERENCES Produtor (id_produtor),
    FOREIGN KEY (Sensor_id_sensor) REFERENCES Sensor (id_sensor)
);

CREATE TABLE Aplicacao_agua (
    id_aplicacao_agua INTEGER PRIMARY KEY,
    data_hora TEXT NOT NULL,
    quantidade_litros REAL NOT NULL,
    Area_plantada_id_area INTEGER NOT NULL,
    FOREIGN KEY (Area_plantada_id_area) REFERENCES Area_plantada (id_area)
);

CREATE TABLE Aplicacao_nutriente (
    id_aplicacao_nutriente INTEGER NOT NULL,
    data_hora TEXT NOT NULL,
    tipo_nutriente TEXT NOT NULL,
    quantidade_gramas REAL NOT NULL,
    Sensor_id_sensor INTEGER NOT NULL,
    Leitura_sensor_id_leitura INTEGER NOT NULL,
    PRIMARY KEY (id_aplicacao_nutriente, Sensor_id_sensor),
    FOREIGN KEY (Sensor_id_sensor) REFERENCES Sensor (id_sensor),
    FOREIGN KEY (Leitura_sensor_id_leitura) REFERENCES Leitura_sensor (id_leitura)
);
