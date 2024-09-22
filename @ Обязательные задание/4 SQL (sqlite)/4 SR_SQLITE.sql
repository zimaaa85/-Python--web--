-- 1 задача
-- Сформировать базу данных из трёх таблиц
-- "Животные" (кличка, возраст)
-- "Еда" (название)
-- "таблица связей животные - еда"(id животного, id еды, количество данной еды)
-- Получить количество животных, которые едят определённую еду
-- Получить список еды, которую ест определённое животное


CREATE TABLE animals 
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);


CREATE TABLE foods
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL  
);


CREATE TABLE animals_foods;
(
  id INTEGER PRIMARY KEY AUTOINCREMENT,  
  animals_id INTEGER NOT NULL,
  foods_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  FOREIGN KEY (animals_id) REFERENCES animals(id) on DELETE CASCADE,
  FOREIGN Key (foods_id) REFERENCES foods(id) ON DELETE CASCADE
);


INSERT INTO animals (name, age) VALUES
('Шарик',3),('Бобик',5),('Тузик',7),('Хан',10),('Дон',15);
SELECT * from animals;


INSERT INTO foods (id, name) VALUES (1, 'мясо'), (5, 'рис'), (3, 'косточка'), (4, 'вода'),  (7, 'йогурт'), (2, 'рыба'), (6, 'хлеб');
SELECT* from foods;


INSERT INTO animals_foods (animals_id, foods_id, quantity) VALUES
(1,1,3), (1,2,3), (2,1,5), (2,2,5), (2,3,1), (3,3,1), (4,3,10),
(4,5,3), (5,6,6), (5,7,2), (1,4,1), (2,4,1), (3,4,1), (4,4,1), (5,4,1);
SELECT* FROM animals_foods;

--Получить количество животных, которые едят определённую еду (мясо, воду)
SELECT foods.name, COUNT(animals_foods.animals_id) AS animal_count FROM foods
JOIN animals_foods ON foods.id = animals_foods.foods_id
WHERE foods.name IN ('мясо', 'вода')
GROUP BY foods.name;


--Получить список еды, которую ест определённое животное (Тузик, Дон)
SELECT animals.name AS animal_name, foods.name AS food_name, animals_foods.quantity FROM animals
JOIN animals_foods ON animals.id = animals_foods.animals_id
JOIN foods ON foods.id = animals_foods.foods_id
WHERE animals.name IN ('Тузик', 'Дон') ORDER By animals.name;

