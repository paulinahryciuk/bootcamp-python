from sqlalchemy import (
Column, Integer, String, ForeignKey, create_engine, Table
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()
student_course_table = Table(
    'student_course', Base.metadata,
     Column('student_id', Integer, ForeignKey= True)),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship("Course", secondary=student_course_table, back_populates='students')

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    students = relationship('Student', secondary=student_course_table, back_populates="courses")