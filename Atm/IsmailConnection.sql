CREATE TABLE Demo (
   key NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
   id int not null,
   name varchar2(10) unique,
   LastName varchar2(10) check(LastName = 'Ismail'),
   cnic int default 33202,
   Email varchar2(25) check(Email != 'ahsan@gmail.com'),
   primary key(key, id),
   BirthDay date check(BirthDay >= TO_DATE('01-JAN-2002', 'DD-MON-YYYY')),
   UNIQUE (Email)
);

insert into demo (id,  LastName, Email, BirthDay) VALUES (0, 'Ismail', 'Hsan@gmail.com', TO_DATE('15-AUG-2002', 'DD-MON-YYYY')); 
insert into demo(id,  LastName, Email, BirthDay) VALUES (1, 'Ismail', 'Ism@gmail.com', TO_DATE('15-AUG-2005', 'DD-MON-YYYY'));
insert into demo(id,  LastName, Email, BirthDay) VALUES (2, 'Ismail', 'Kha@gmail.com', TO_DATE('15-AUG-2003', 'DD-MON-YYYY'));
insert into demo(id,  LastName, Email, BirthDay) VALUES (3, 'Ismail', 'Ismalie@gmail.com', TO_DATE('15-AUG-2004', 'DD-MON-YYYY'));
insert into demo(id,  LastName, Email, BirthDay) VALUES (4, 'Ismail', 'Zimda@gmail.com', TO_DATE('15-AUG-2024', 'DD-MON-YYYY'));

select * from demo;

truncate table Demo;

select * from demo where birthday ='15-AUG-2005';



create unique index  Indx1 on demo(name,LastName); 

select index_name , column_name ,column_position from user_ind_columns where table_name ='DEMO';

drop index indx1;




alter table demo drop column name;

alter table demo add name varchar2(25) default 'Ahsan';

alter table demo modify name varchar(10) ;

alter table demo modify name UNIQUE; // not possible , will trhow error now , bcz we  inserted before same ...

alter table demo add( NewDays Date default trunc(sysdate));

alter table demo modify email varchar(19) check(Email !='Khan@gmail.com');

alter table demo add age number(10) default 20;

update demo set age=25 where key in(1,2,3,4,5); 

update demo set age=null where id = 0;

DELETE FROM DEMO WHERE ID=0;





create view V1 as select name , age from demo where id in(0,1);

create view V2 as select * from demo where email ='Ism@gmail.com' and  birthDay = '15-AUG-2005' ;

Create or replace VIEW V1 as select age,name ,LastName from demo where id in(0,1,2);

select * from V1;
select * from V2;
Drop view V1;



select distinct lastname,name from demo ;
select count(distinct name  )from demo;
select * from demo where age between 20 and 25;

select * from demo where lastname like ( 'I%' );
select * from demo where lastname like ( '%l' );
select * from demo where lastname like ( '%mai%' );
select * from demo where id = 0 and (email like '.%com' or email like 'H%');

select * from demo where not cnic = 33202;
select * from demo where email not like '%asd%' ;
SELECT * FROM demo WHERE id NOT BETWEEN 2 AND 3;
select name from demo where email not in ('Zimda@gmail.com' ,'Ismalie@gmail.com') ;
select * from demo where not age < 20;




select name,age ,cnic , key from demo where name is  null;
select name,age ,cnic , key from demo where name is not null;

select name,age,lastname,cnic from demo order by id,key desc;
select * from demo where NewDays = '24-JUL-2024';



select * from demo where id in(0,1,2) and key in(1,2,3) fetch first 3 rows only;


select min(id) from demo where id in(0,1);
select Max(key) from demo where id in(0,1);
select count(key ) from demo where id in(0,1);
select count(id) as COUNT_ID from demo;         // give a name by Use Of ALias
select sum(id *5 ) as Summed from demo where key in(1,2,3) ;
select Avg(id) , Avg(key) As AVG_ID FROM DEMO where id in (0,1,2,3,4);























create table D2(
Name_Id varchar2(25),
PhoneNumber number(20),
Age number(10)
);



















