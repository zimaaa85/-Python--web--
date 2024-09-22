--Получить количество животных, которые едят определённую еду (мясо, воду)
--SELECT foods.name, COUNT(animals_foods.animals_id) AS animal_count FROM foods
--JOIN animals_foods ON foods.id = animals_foods.foods_id
--WHERE foods.name IN ('мясо', 'вода')
--GROUP BY foods.name;


--Получить список еды, которую ест определённое животное (Тузик, Дон)
SELECT animals.name AS animal_name, foods.name AS food_name, animals_foods.quantity FROM animals
JOIN animals_foods ON animals.id = animals_foods.animals_id
JOIN foods ON foods.id = animals_foods.foods_id
WHERE animals.name IN ('Тузик', 'Дон') ORDER By animals.name;

