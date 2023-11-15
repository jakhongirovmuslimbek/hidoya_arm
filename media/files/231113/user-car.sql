CREATE TABLE car (
    id BIGSERIAL NOT NULL PRIMARY KEY,
    make VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    price NUMERIC(19, 2) NOT NULL);

CREATE TABLE userlar(
    id BIGSERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    gender VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    country VARCHAR(50) NOT NULL,
    car_id BIGINT REFERENCES car(id),
    UNIQUE(car_id));



INSERT INTO userlar (first_name, last_name, email, gender, date_of_birth, country) VALUES ('jas', 'suur', 'jas@gmail.com', 'male', '2001-08-08', 'Uzbekistan');
INSERT INTO userlar (first_name, last_name, email, gender, date_of_birth, country) VALUES ('bek', 'beuk', 'jasbek@gmail.com', 'male', '2001-08-08', 'Uzbekistan');
INSERT INTO userlar (first_name, last_name, email, gender, date_of_birth, country) VALUES ('jovoq', 'jovouq', 'jovoq@gmail.com', 'male', '2001-08-08', 'Uzbekistan');

INSERT INTO car (make, model, price) VALUES ('Chevrolet', 'Gentra', '1500.52');
INSERT INTO car (make, model, price) VALUES ('Chevrolet', 'Cobalt', '1400.52');
INSERT INTO car (make, model, price) VALUES ('Chevrolet', 'Nexia3', '1300.52');