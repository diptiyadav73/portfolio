from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from flask_appbuilder import Model

class Exams(Model):
    exam_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(50))
    phone_number = Column(String(50))
    email = Column(String(50))
    exam_name = Column(String(50))
    timezone = Column(String(50))
    date = Column(String(50))
    time_duration = Column(String(50))
    grade = Column(String(50))
    def __str__(self):
        return str(self.exam_name)


