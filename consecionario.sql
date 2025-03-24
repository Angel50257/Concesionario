create database concesionario

use concesionario

create table vehiculos(
	id int identity (1,1) primary key,
	marca varchar(100) not null,
	modelo varchar(100) not null,
	anio varchar(100) not null,
	precio float not null,
	disponibilidad bit not null default 1
)

create table clientes(
	id int identity (1,1) primary key,
	nombre varchar(100) not null,
	dpi varchar(13) unique not null,
	correo varchar(100) unique not null,
	telefono varchar(11) not null,
)

create table ventas(
	id int identity (1,1) primary key,
	id_vehiculo int not null,
	id_cliente int not null,
	fecha_venta date not null,
	constraint fk_ventas_vehiculos foreign key (id_vehiculo) references vehiculos(id),
	constraint fk_ventas_clientes foreign key (id_cliente) references clientes(id)
)

select * from clientes

select * from vehiculos

select * from ventas
