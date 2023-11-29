from fastapi import FastAPI
from pydantic import BaseModel

# команда в терминал для старта программы
# uvicorn main:app --reload

# Описание для документации
description = """

## Cars

You can:
* Create record about car;
* Get info about all cars;
* Get info about one car;
* Delete record about car;
* Update info about car.

## Drivers

You can:
* Create record about driver;
* Get info about all drivers;
* Get info about one driver;
* Delete record about driver;
* Update info about driver.

"""

# Теги для сущностей
tags_metadata = [
    {
        "name": "cars",
        "description": "Operations with cars.",
    },
    {
        "name": "drivers",
        "description": "Operations with drivers.",
    },

]

# Создание объекта класса FastAPI
app = FastAPI(
    title="GIBDD API",  # Название API
    description=description,  # Описание
    summary="GIBDD API helps you do awesome THINGS 🚙",  # Заголовок описания
    version="1.0",  # Версия
    terms_of_service="https://fastapi.netlify.app/ru/tutorial/",  # Ссылка на документацию FastAPI
    contact={  # Мои контакты
        'name': "Slobodchikov Dmitry",
        'group': "РИ-130971",
        'email': "dmitryslo@yandex.ru",
    },
    license_info={  # Ссылка на используемую лицензию
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,  # Теги для сущностей
)


# Список словарей с машинами
cars = [
    {'id': 1, 'brand': 'Toyota', 'model': 'Camry', 'state_reg': 96, 'number_car': 'В287УЦ', 'owner': "Иван Петров"},
    {'id': 2, 'brand': 'Honda', 'model': 'Civic', 'state_reg': 58, 'number_car': 'А666ДА', 'owner': "Роман Кириллов"},
    {'id': 3, 'brand': 'Ford', 'model': 'Mondeo', 'state_reg': 11, 'number_car': 'Л321ЧС', 'owner': "Артем Сидоров"},
    {'id': 4, 'brand': 'Nissan', 'model': 'Almera', 'state_reg': 196, 'number_car': 'А231ДБ', 'owner': "Денис Королев"},
]


# Класс машин
class Cars(BaseModel):
    id: int
    brand: str
    model: str
    state_reg: int
    number_car: str
    owner: str


# Список словарей с водителями
drivers = [
    {'id': 1, 'name': 'Артём', 'surname': 'Королев', 'birthday': '12.04.1993', 'driver_license': 3213321579},
    {'id': 2, 'name': 'Роман', 'surname': 'Кириллов', 'birthday': '23.10.2000', 'driver_license': 5439342148},
    {'id': 3, 'name': 'Иван', 'surname': 'Петров', 'birthday': '29.03.1990', 'driver_license': 4554309238},
    {'id': 4, 'name': 'Денис', 'surname': 'Сидоров', 'birthday': '05.01.2002', 'driver_license': 5439098534},
]

# Класс водителей
class Drivers(BaseModel):
    id: int
    name: str
    surname: str
    birthday: str
    driver_license: int


# Эндпоинт для получения списка всех автомобилей
@app.get('/cars', tags=["cars"])
def get_cars():
    return cars, 200


# Эндпоинт для создания нового автомобиля
@app.post('/cars', tags=["cars"])
def create_car(Cars: Cars):
    new_car = {
        'id': len(cars) + 1,
        'brand': Cars.brand,
        'model': Cars.model,
        'state_reg': Cars.state_reg,
        'number_car': Cars.number_car,
        'owner': Cars.owner,
    }
    cars.append(new_car)
    return new_car, 201


# Эндпоинт для получения информации о конкретном автомобиле
@app.get('/cars/{car_id}', tags=["cars"])
def get_car(car_id: int):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        return car, 200
    return {"message": "Car not found"}, 404


# Эндпоинт для обновления информации об автомобиле
@app.put('/cars/{car_id}', tags=["cars"])
def update_car(car_id: int, Cars: Cars):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car:
        car['id'] = Cars.id
        car['brand'] = Cars.brand
        car['model'] = Cars.model
        car['state_reg'] = Cars.state_reg
        car['number_car'] = Cars.number_car
        car['owner'] = Cars.owner
        return car, 200
    return {"message": "Car not found"}, 404


# Эндпоинт для удаления информации об автомобиле
@app.delete('/cars/{car_id}', tags=["cars"])
def delete_car(car_id: int):
    global cars
    cars = [car for car in cars if car['id'] != car_id]
    return {"message": "Car deleted"}, 200

#########################################################################

# Эндпоинт для получения списка всех водителей
@app.get('/drivers', tags=["drivers"])
def get_drivers():
    return drivers, 200


# Эндпоинт для создания записи о новом водителе
@app.post('/drivers', tags=["drivers"])
def create_driver(Drivers: Drivers):
    new_driver = {
        'id': len(drivers) + 1,
        'name': Drivers.name,
        'surname': Drivers.surname,
        'birthday': Drivers.birthday,
        'driver_license': Drivers.driver_license,
    }
    drivers.append(new_driver)
    return new_driver, 201


# Эндпоинт для получения информации о конкретном водителе
@app.get('/drivers/{driver_id}', tags=["drivers"])
def get_driver(driver_id: int):
    driver = next((driver for driver in drivers if driver['id'] == driver_id), None)
    if driver:
        return driver, 200
    return {"message": "Driver not found"}, 404


# Эндпоинт для обновления информации о водителе
@app.put('/drivers/{driver_id}', tags=["drivers"])
def update_driver(driver_id: int, Drivers: Drivers):
    driver = next((driver for driver in drivers if driver['id'] == driver_id), None)
    if driver:
        driver['id'] = Drivers.id
        driver['name'] = Drivers.name
        driver['surname'] = Drivers.surname
        driver['birthday'] = Drivers.birthday
        driver['driver_license'] = Drivers.driver_license
        return driver, 200
    return {"message": "Driver not found"}, 404


# Эндпоинт для удаления информации о водителе
@app.delete('/drivers/{driver_id}', tags=["drivers"])
def delete_driver(driver_id: int):
    global drivers
    drivers = [driver for driver in drivers if driver['id'] != driver_id]
    return {"message": "Driver deleted"}, 200

