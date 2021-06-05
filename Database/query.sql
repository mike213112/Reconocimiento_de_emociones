CREATE TABLE FOTOS(
  id_foto SERIAL primary key not null,
  nombre VARCHAR(50),
  foto bytea
);

CREATE TABLE FOTOS(
  id_foto SERIAL primary key not null,
  nombre VARCHAR(50)
);

insert into FOTOS (nombre) values ('Prueba');

select * from FOTOS;

drop table FOTOS;