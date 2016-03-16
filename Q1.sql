

use izi;

select temp.animal_name, avg(temp.daily_qty)
from
(
select animal_name,sum(qty) as daily_qty
from animal_feed
group by animal_name, feeding_date
)as temp
group by temp.animal_name;
