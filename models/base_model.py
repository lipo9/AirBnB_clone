#!/usr/bin/pyhon3
"""
This is the parent class
"""
import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
    Defines all common methods & attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        initialization of all attributes

        Args:
            *args (any): Unused
            **kwargs (dict): Key/value pairs of attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if not kwargs:
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, f)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """
        A method that returns a string containing the class name,
        id and the attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        class_dict = {
            k: v for (k, v) in self.__dict__.items() if (not v) is False
        }
        return class_name + " (" + self.id + ") " + str(class_dict)

    def save(self):
        """
        this method changes the update time to current
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        This method creates and returns a new dictionary of keys and datetimes
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dict[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not value:
                    pass
                else:
                    new_dict[key] = value
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
