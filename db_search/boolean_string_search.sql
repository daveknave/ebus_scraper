-- Create virtual table for advanced search functionallity.
DROP TABLE IF EXISTS searchable_articles;
create virtual table searchable_articles USING FTS5(date, source, title, text, index, tags, location);

-- Import data into virtual table.
INSERT INTO searchable_articles select date, source, title, text, "index", tags, location from articles;

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
