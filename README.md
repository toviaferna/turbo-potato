
<p align="center">
 <kbd>
  <img src="https://user-images.githubusercontent.com/33908299/158191854-45c2fef1-0d19-482a-b539-f3abcd4d14fe.png" width="100" />
 </kbd>
 <h2 align="center">Turbo-Potato</h2>
</p>


 [![GitHub contributors](https://badgen.net/github/contributors/toviaferna/turbo-potato)](https://GitHub.com/toviaferna/turbo-potato/graphs/contributors/) [![GitHub issues](https://badgen.net/github/issues/toviaferna/turbo-potato/)](https://GitHub.com/toviaferna/turbo-potato/issues/) [![GitHub total-pull-requests](https://badgen.net/github/prs/toviaferna/turbo-potato/)](https://GitHub.com/toviaferna/turbo-potato/pull/)

### Cómo usarlo
### ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
Crear un entorno virtual de Python.
```
cd turbo-potato
c:\turbo-potato> python -m venv venv
```
Activar el entorno virtual.
```
c:\turbo-potato> cd venv\Scripts
c:\turbo-potato\venv\Scripts> activate
```
Instalar dependencias
```
(venv) c:\turbo-potato\pip install -r requirements.txt
```
Migrar
```
(venv) c:\turbo-potato\python manage.py migrate
```
Iniciar la aplicación
```
(venv) c:\turbo-potato\python manage.py runserver
```
Acceda a la aplicación web en el navegador:
```
http://127.0.0.1:8000/
```

@startuml
!define AWSPUML https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/v19.0/dist
!define SPRITESURL https://raw.githubusercontent.com/rabelenda/cicon-plantuml-sprites/v0.8/sprites
!define PERSONURL https://raw.githubusercontent.com/rabelenda/cicon-plantuml-sprites/v0.8/sprites/person
!define COUNTRYURL https://raw.githubusercontent.com/rabelenda/cicon-plantuml-sprites/v0.8/sprites/country
!define CITYURL https://raw.githubusercontent.com/rabelenda/cicon-plantuml-sprites/v0.8/sprites/city

!includeurl AWSPUML/Database/AmazonRDS.puml
!includeurl SPRITESURL/cicon.puml
!includeurl PERSONURL/person.puml
!includeurl COUNTRYURL/country.puml
!includeurl CITYURL/city.puml

skinparam monochrome true

entity "Person" as person {
  + id : int <<generated>>
  --
  + name : string
  + last_name : string
  + email : string
  + phone : string
  --
  o country_id : int
}

entity "Country" as country {
  + id : int <<generated>>
  --
  + name : string
  --
  o city_id : int
}

entity "City" as city {
  + id : int <<generated>>
  --
  + name : string
}

person -d- country : belongs to
country -d- city : contains
@enduml

