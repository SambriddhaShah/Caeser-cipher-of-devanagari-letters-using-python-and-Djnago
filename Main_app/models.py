from django.db import models

# Create your models here.
class Cipher(models.Model):
    Plaintext=models.CharField(max_length=30)

    def __str__(self):
        return self.Plaintext

class Decipher(models.Model):
    Ciphertext=models.CharField(max_length=30)


    def __str__(self):
        return self.Ciphertext  
