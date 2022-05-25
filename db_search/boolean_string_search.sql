-- Create virtual table for advanced search functionallity.
DROP TABLE IF EXISTS searchable_articles;
create virtual table searchable_articles USING FTS5(date, source, title, text, index);

-- Import data into virtual table.
INSERT INTO searchable_articles select date, source, title, text, "index" source from articles;

-- Search the DB
select distinct * from searchable_articles where
                           searchable_articles MATCH 'tender* ' ||
                                                     'OR order* ' ||
                                                     'OR buy_ ' ||
                                                     'OR win_ ' ||
                                                     'OR won ' ||
                                                     'OR rollout ' ||
                                                     'OR aqui* ' ||
                                                     'OR deliver*' ||
                                                     'OR purchase_'
order by date;

select distinct "index" from articles;

ALTER TABLE articles ADD COLUMN location;



select * from articles inner join locations as l on title like '%in ' || l.city_ascii || ' %';

select  '%' || l.city_ascii || '%' from locations as l;