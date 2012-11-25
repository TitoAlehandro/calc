<<<<<<< HEAD
mysqldump -u root -p -,f book_tab > C:\mydb_backup_name_database.txt;drop DATABASE book_tab;
--для русского языка
create DATABASE book_tab CHARACTER SET utf8 COLLATE utf8_general_ci;set names 'cp1251';use book_tab;
--гранты
GRANT ALL ON book_tab.* TO tito@localhost;
=======
mysqldump -u root -p -,f book_tab > C:\mydb_backup_name_database.txt;drop DATABASE book_tab;create DATABASE book_tab CHARACTER SET utf8 COLLATE utf8_general_ci;set names 'cp1251';use book_tab;



>>>>>>> aac6b884346dd56421712c0b014b825e17a5b894
create TABLE book (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
	   		 	  date DATE,
				  id_branch varchar(30), 
				  price INT, 
				  id_place varchar(30), 
				  id_product varchar(30));

create TABLE branch (branch varchar(30));

create TABLE place (place varchar(30));

create TABLE product (product varchar(30));

create TABLE price (price INT);

create TABLE balance (cur_date DATE, 
	   		 		  calc_date DATE, 
					  balance float);