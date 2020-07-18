# Notes on this application

## AbstractBaseUser

(From the documentation) provides the core implementation of a user model, including hashed passwords and tokenized password resets. Implementation details also come along side.

The best way of creating a custom Django user model is to inherit from the AbstractBaseUser. AbstractBaseUser provides the core implementation of a User model, including hashed passwords and tokenized password resets.

## PermissionsMixin

PermissionsMixin makes it really easy for me to include Django's permission franework into the user class. It is an abstract model I can include in the class hierarchy for the user model.

If you add the mixin to one your models, it will add fields that are specific for objects that have permissions.

### What is a mixin?

A mixin is a special kind of inheritance in Python. I can use a mixin to allow classes in Python to share between any class that inherits from that mixin.

## BaseUserManager

By default the AbstractBaseUser uses a username not an email as the identifier. For this example we want to use the email, not the username. Therefore we need to use the BaseUserManager to override functions such as create_user() and create_superuser() to create users.

## UserAdmin as BaseUserAdmin

This is done in the admin file. If your custom user model extends django.contrib.auth.models.AbstractUser, you can use Django’s existing `django.contrib.auth.admin.UserAdmin` class. However, if your user model extends `AbstractBaseUser`, you’ll need to define a custom `ModelAdmin` class. It may be possible to subclass the default `django.contrib.auth.admin.UserAdmin`; however, you’ll need to override any of the definitions that refer to fields on `django.contrib.auth.models.AbstractUser` that aren’t on your custom user class.

```python
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
```

### fieldsets and add_fieldsets

We use fieldsets for the fields we can edit for a user

We use add_fieldets for the fields to be used when creating a user

## CreateAPIView

Used for create-only endpoints. Provides a `post` method handler.

## AuthTokenSerializer

To do any validation that requires access to multiple fields, add a method called `.validate()` to the Serializer subclass. This method takes a single argument, which is a dictionary of field values.

## ObtainAuthToken

If you need a customized version of the `obtain_auth_token` view, you can do so by subclassing the ObtainAuthToken view class, and using that in your url conf instead.
