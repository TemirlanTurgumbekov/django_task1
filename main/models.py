from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(0)
    students = models.ManyToManyField(Student)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
