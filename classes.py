import psycopg2


class DBManager:
    """Класс, который подключается к БД PostgreSQL."""

    def __init__(self):
        self.conn = psycopg2.connect(dbname="postgres", user="postgres")
        self.conn.autocommit = True
        self.employer_url = 'https://api.hh.ru/employers?only_with_vacancies=true'

    def get_companies_and_vacancies_count(self, employer_id):
        # — получает список всех компаний и количество вакансий у каждой компании.
        pass

    def get_all_vacancies(self, employer_id):
        # — получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        # вакансию.
        pass

    def get_avg_salary(self):
        # — получает среднюю зарплату по вакансиям.
        pass

    def get_vacancies_with_higher_salary(self):
        # — получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        pass

    def get_vacancies_with_keyword(self):
        # — получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        pass
