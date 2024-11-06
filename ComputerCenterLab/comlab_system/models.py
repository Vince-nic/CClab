from django.db import models
from django.utils import timezone


class Account(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('personnel', 'personnel'),
    )
    
    account_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class ComputerLab(models.Model):
    computerlab_id = models.AutoField(primary_key=True)
    lab = models.CharField(max_length=100)
    total_units = models.PositiveIntegerField()
    lab_images = models.ImageField(upload_to='lab_images/', null=True, blank=True)

    def __str__(self):
        return self.lab


class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    remarks = models.TextField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    stat_monitor = models.CharField(max_length=15)
    stat_keyboard = models.CharField(max_length=15)
    stat_mouse = models.CharField(max_length=15)
    stat_ram = models.CharField(max_length=15)
    stat_motherboard = models.CharField(max_length=15)
    stat_cpu = models.CharField(max_length=15)

    def __str__(self):
        return f"Status {self.status_id}"

class Components(models.Model):
    component_id = models.AutoField(primary_key=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)
    monitor = models.CharField(max_length=50, default='No')
    keyboard = models.CharField(max_length=50, default='No')
    mouse = models.CharField(max_length=50, default='No')
    ram = models.CharField(max_length=50, default='No')
    motherboard = models.CharField(max_length=50, default='No')
    cpu = models.CharField(max_length=50, default='No')


    def __str__(self):
        return f"Component {self.component_id}"


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    computerlab = models.ForeignKey(ComputerLab, on_delete=models.CASCADE)
    component = models.ForeignKey(Components, on_delete=models.CASCADE) 
    pc_number = models.CharField(max_length=10)

    def __str__(self):
        return f"PC {self.pc_number} - {self.component} in {self.computerlab.lab}"
