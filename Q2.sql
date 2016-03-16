select temp2.animal_name,avg(temp2.dailyfeed_cnt) as avgfeed_count
from
(
select animal_name, count(feeding_date) as dailyfeed_cnt
from animal_feed
group by animal_name, feeding_date
) as temp2
group by temp2.animal_name