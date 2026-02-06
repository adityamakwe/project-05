from django.db.utils import OperationalError
from abc import ABC, abstractmethod
from ..utility.Exceptions import DatabaseUnavailable

class BaseService(ABC):

    def __init__(self):
        self.pageSize = 5

    def _db_execute(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            raise DatabaseUnavailable(
                "Database service is currently unavailable. Please try again later."
            )

    def save(self, obj):
        if obj.id == 0:
            obj.id = None
        return self._db_execute(obj.save)

    def delete(self, obj_id):
        obj = self.get(obj_id)
        if obj:
            return self._db_execute(obj.delete)
        return None

    def get(self, obj_id):
        try:
            return self._db_execute(
                self.get_model().objects.get,
                id=obj_id
            )
        except self.get_model().DoesNotExist:
            return None

    def search(self):
        return self._db_execute(
            self.get_model().objects.all
        )

    def preload(self):
        return self._db_execute(
            self.get_model().objects.all
        )

    @abstractmethod
    def get_model(self):
        pass











# from abc import ABC, abstractmethod

# # ------------------------------------------------------------------------------

# class BaseService(ABC):

#     def __init__(self):
#         self.pageSize = 5

#     def save(self, obj):
#         if (obj.id == 0):
#             obj.id = None
#         obj.save()

#     def delete(self, obj_id):
#         obj = self.get(obj_id)
#         obj.delete()

#     def get(self, obj_id):
#         try:
#             obj = self.get_model().objects.get(id=obj_id)
#             return obj
#         except self.get_model().DoesNotExist:
#             return None

#     def search(self):
#         try:
#             objs = self.get_model().objects.all()
#             return objs
#         except self.get_model().DoesNotExist:
#             return None

#     def preload(self):
#         try:
#             objs = self.get_model().objects.all()
#             return objs
#         except self.get_model().DoesNotExist:
#             return None

#     @abstractmethod
#     def get_model(self):
#         pass
