# Projeto Job Insights

Foi aplicado os conhecimentos desenvolvendo soluções de análise de dados reais sobre empregos. Nessas soluções foram testadas e incorporadas em um projeto web, aceitando os parâmetros especificados e retornando os resultados corretos.

## Foi realizado:
  - Individual
  
## Linguagens e Ferramentas utilizadas:
  - Python
  - Pytest

## Estrutura do projeto
  ```
  Legenda:
  🔸Arquivos que não foram alterados.
  🔹Arquivos que foram alterados por mim.
  .
  ├──🔸README.md
  ├──🔸Dockerfile
  ├──🔸docker-compose.yml
  ├──🔸dev-requirements.txt
  ├──🔸requirements.txt
  ├── data
  │   └──🔸jobs.csv
  ├── src
  │   ├── flask_app
  │   │   ├── templates
  │   │   │   ├── includes
  │   │   │   │   └──🔸nav.jinja2
  │   │   │   ├──🔸base.jinja2
  │   │   │   ├──🔸index.jinja2
  │   │   │   ├──🔸job.jinja2
  │   │   │   └──🔸list_jobs.jinja2
  │   │   ├──🔸app.py
  │   │   ├──🔸more_insights.py
  │   │   └──🔹routes_and_views.py
  │   ├── insights
  │   │   ├──🔹industries.py
  │   │   ├──🔹jobs.py
  │   │   └──🔹salaries.py
  │   ├── pre_built
  │   │   ├──🔸brazilian_jobs.py
  │   │   ├──🔸counter.py
  │   │   └──🔸sorting.py
  ├── tests
  │   ├──🔸__init__.py
  │   ├──🔸conftest.py
  │   ├──🔸marker.py
  │   ├── brazilian
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_brazilian_jobs.py
  │   ├── counter
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   ├──🔹test_counter.py
  │   ├── mocks
  │   │   ├──🔸job_1.html
  │   │   ├──🔸jobs.csv
  │   │   ├──🔸jobs_with_industries.csv
  │   │   ├──🔸jobs_with_salaries.csv
  │   │   └──🔸jobs_with_types.csv
  │   ├── sorting
  │   │   ├──🔸__init__.py
  │   │   ├──🔸conftest.py
  │   │   ├──🔸mocks.py
  │   │   └──🔹test_sorting.py
  │   ├──🔸test_flask_app.py
  │   ├──🔸test_industries.py
  │   ├──🔸test_jobs.py
  │   ├──🔸test_salaries.py
  │   ├──🔸test_more_insights.py
  │   └──🔸test_routes_and_views.py
  ```
