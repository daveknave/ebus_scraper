
select distinct "index" from articles;

ALTER TABLE articles ADD COLUMN location;



select * from articles inner join locations as l on title like '%in ' || l.city_ascii || ' %';

select  '%' || l.city_ascii || '%' from locations as l;