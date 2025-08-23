from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Brand(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('APROBADA', 'Aprobada'),
        ('RECHAZADA', 'Rechazada'),
    ]

    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="brands")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
