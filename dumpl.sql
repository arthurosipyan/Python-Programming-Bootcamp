BEGIN TRANSACTION;
CREATE TABLE employees(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, f_name TEXT NOT NULL,l_name TEXT NOT NULL, age INT NOT NULL, address TEXT, salary REAL, hire_date TEXT);
INSERT INTO "employees" VALUES(1,'Derek','Banas',43,'121 Main St',500000.0,'2021-06-25');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('employees',1);
COMMIT;
