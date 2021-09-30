

from suds.client import Client
from suds import WebFault
from zeep import Client
from model.project import Project




class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")

        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        projects = []
        try:

            for project in client.service.mc_enum_projections(username, password):
                          # client.service.mc_projects_get_user_accessible(username, password)
                projects.append(Project(id=project.id, name=project.name))

            return projects


        except WebFault:
            return False


