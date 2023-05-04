-- creates a view need_meeting that lists all
-- students that have a score under 80

DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting
As
SELECT name FROM students 
    WHERE score < 80 and (last_meeting is null or last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH));
