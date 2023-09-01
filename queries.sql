query = "SELECT id, appid, name, playtime FROM library"
query = "SELECT id, appid, name, playtime FROM (SELECT * FROM library WHERE playtime = 0)"
query = "SELECT id, appid, name, playtime FROM (SELECT * FROM library WHERE playtime != 0)"
query = "SELECT id, appid, name, playtime FROM (SELECT * FROM library) ORDER BY playtime DESC LIMIT 5"
query = "SELECT id, appid, name, playtime FROM (SELECT * FROM library) ORDER BY playtime DESC LIMIT 10"
query = "SELECT id, appid, name, playtime FROM (SELECT * FROM library) ORDER BY playtime DESC LIMIT 20"

/* FIXME: This query that results from all the concat of variables just doen't give any result from the db */
SELECT * FROM (SELECT id, appid, name, playtime FROM (SELECT * FROM library) ORDER BY playtime DESC LIMIT 5) WHERE id = 3;

