
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

Access the web app in browser:
```
(venv) c:\turbo-potato\python manage.py runserver
```

