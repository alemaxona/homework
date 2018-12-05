__author__ = 'alemaxona'


'''
[22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); (params None)
[22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.022) CREATE TABLE "django_content_type" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL); args=None
[22/Jun/2017 13:53:22] DEBUG [django.db.backends.schema:103] ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); (params [])
[22/Jun/2017 13:53:22] DEBUG [django.db.backends:90] (0.001) ALTER TABLE "django_content_type" ADD CONSTRAINT "django_content_type_app_label_76bd3d3b_uniq" UNIQUE ("app_label", "model"); args=[]
'''

# Go to https://pythex.org/
# Date (22/Jun/2017)
# (\d.{1}.\w.{3}.\d.{2})

# Where? (django.db.backends.schema)
# (django.*):

# Text (CREATE TABLE "django_content_type" ("id" serial...)
# ([CA].*)


'''
Задачи

+ Реализовать две функции: write_to_file(data) и read_file_data().
Которые соотвественно: пишут данные в файл и читают данные из файла.

'''


def write_to_file(data):
    with open(data, 'a') as f:
        return f.write('Max\n')


def read_file_data(data):
    with open(data) as f:
        return f.read()


file = '/Users/alemaxona/Documents/Projects/homework/my_file_test'

print(write_to_file(file))
print(read_file_data(file))



