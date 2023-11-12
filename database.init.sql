
-- MSSQL database
	CREATE TABLE SystemUser (
	id int NOT NULL IDENTITY PRIMARY KEY,
	Name VARCHAR(100) NOT NULL,
	Password VARCHAR(max) NOT NULL,
	Role VARCHAR(50) NULL);

-- Password == haslo
	insert into SystemUser values('Madzia','$2b$12$yu4fbAustPMFyu4uSXJhS.qBytm1sRKtX.HhsSu8HEQEn93ofteJe','MASTER');
	insert into SystemUser values('Felix','$2b$12$yu4fbAustPMFyu4uSXJhS.qBytm1sRKtX.HhsSu8HEQEn93ofteJe','MASTER');
	insert into SystemUser values('Tomek','$2b$12$yu4fbAustPMFyu4uSXJhS.qBytm1sRKtX.HhsSu8HEQEn93ofteJe','MASTER');
	insert into SystemUser values('Jadzia','$2b$12$yu4fbAustPMFyu4uSXJhS.qBytm1sRKtX.HhsSu8HEQEn93ofteJe','MASTER');
