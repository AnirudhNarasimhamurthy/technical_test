use izi;

/* If create table fails drop the table and create it
Command: drop table animal_feed */

create table animal_feed
(
animal_id int,
animal_name varchar(50),
f_id int references running_inventory(food_id),
qty int,
feeding_time time,
feeding_date date
);

alter table animal_feed 
add constraint pk_animalfeed primary key(animal_id,feeding_time);

insert into animal_feed values (1, 'horse', 1, 10,curtime(),curdate());
insert into animal_feed values (2, 'zebra', 2, 10,curtime(),curdate());
insert into animal_feed values (3, 'lion', 3, 10,curtime(),curdate());
insert into animal_feed values (4, 'tiger', 4, 10,curtime(),curdate());

select * from animal_feed;