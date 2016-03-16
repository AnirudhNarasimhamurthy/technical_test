use izi;

/* Although there isn't a need for this table but if we were to automate
the entire problem description then I am assuming this is the
table from which the workers will look at the values
and update it in the running inventory to make sure inventory and
feed in stock are in sync 

In the problem description this is like a manual job and whatever values they
have after this is directly entered as updates. I am trying to use values
from this table for the update*/

create table original_inventory
(
food_id int,
food_name varchar(30),
food_qty int
);

alter table original_inventory
add constraint pk_originventory primary key(food_id);

insert into original_inventory(food_id,food_name,food_qty) values (1,'horse_food',50);
insert into original_inventory(food_id,food_name,food_qty) values (2,'zebra_food',50);
insert into original_inventory(food_id,food_name,food_qty) values (3,'lion_food',50);
insert into original_inventory(food_id,food_name,food_qty) values (4,'tiger_food',50);


select * from original_inventory