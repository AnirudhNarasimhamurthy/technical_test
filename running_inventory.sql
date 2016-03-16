create database izi;

use izi;

/* If create table fails, drop table and then run create table 
Command: drop table running_inventory */

create table running_inventory
(
food_id int,
food_name varchar(30),
food_qty int,
waste int default 0
);

/* I am initializing the waste to be initially zero and will update the 
column when the workers take the feed from stock and update the actual values */

alter table running_inventory
add constraint pk_inventory primary key(food_id);

insert into running_inventory(food_id,food_name,food_qty) values (1,'horse_food',50);
insert into running_inventory(food_id,food_name,food_qty) values (2,'zebra_food',50);
insert into running_inventory(food_id,food_name,food_qty) values (3,'lion_food',50);
insert into running_inventory(food_id,food_name,food_qty) values (4,'tiger_food',50);


select * from running_inventory