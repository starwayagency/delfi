from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = 'Renames a Django project'
    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')
        # parser.add_arguments('-p', '--prefix')
    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        # bit of logic to rename the project

        files_to_rename = ['djangoprojects/settings/base.py', 'djangoprojects/wsgi.py', 'manage.py']
        folder_to_rename = 'djangoprojects'
        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('djangoprojects', new_project_name)
            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS(f'Project has been renamed to {new_project_name}'))
