# Django-Catalog-Courses

How to run project:
1) inside main folder create virtual environment activate it
2) cd to the directory where requirements.txt is located
3) run: pip install -r requirements.txt in your shell
4) cd to catalog_courses folder
5) run: python manage.py makemigrations
6) run: python manage.py migrate
7) run: python manage.py runserver

Endpoints:
- list all courses: GET - domain/api/courses-all/

- add new course: POST - domain/api/course-add
data = {
  'title': 'your_title',
  'start_date': 'YYYY-MM-DD', 
  'end_date': 'YYYY-MM-DD',
  'lectures_qty': 'integer'
}
notes:  - title cannot be empty
        - start_date cannot be > end_date, but start_date and end_date can be equal
        - lectures_qty can be only 0 or positive integer

- course details: GET - domain/api/course/<course_id>

- course search: GET - domain/api/course-search/?title=your_title&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
usage:  - title is required  
        - start_date and end_date are optional
        - if only start_date provided, system will search all courses from provided date
        - if only end_date provided, system will search all courses to provided date
        - if both start_date and end_date provided, system will search all courses in provided date range

- course update: PUT - domain/api/course-update
data = {
  'id': 'course_id'
  'title': 'your_title',
  'start_date': 'YYYY-MM-DD', 
  'end_date': 'YYYY-MM-DD',
  'lectures_qty': 'integer'
}
notes:  - title cannot be empty
        - start_date cannot be > end_date, but start_date and end_date can be equal
        - lectures_qty can be only 0 or positive integer

- course delete: DELETE - domain/api/course-delete
data = {
  'id': 'course_id'
}
