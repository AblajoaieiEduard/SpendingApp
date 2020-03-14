"""
Modul in care voi crea ierarhia de exceptii
"""
class ValidationException(Exception):
    pass

class CategorieException(ValidationException):
    pass

class CheltuialaException(ValidationException):
    pass

class RepoException(Exception):
    pass


class ServiceException(Exception):
    pass