from __future__ import unicode_literals

from django.db import models


class Activo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=45)
    costo = models.DecimalField(max_digits=10, decimal_places=0)
    iva = models.DecimalField(max_digits=10, decimal_places=0)
    fecha_compra = models.DateField()
    fecha_registro = models.DateField()
    vida_util = models.IntegerField()
    valor_remanente = models.DecimalField(max_digits=10, decimal_places=0)
    fotografia = models.TextField(blank=True)
    fecha_venta = models.DateField(blank=True, null=True)
    proveedor = models.ForeignKey('Proveedor')
    categoria = models.ForeignKey('Categoria')
    estado = models.ForeignKey('Estado')
    condicion = models.ForeignKey('Condicion')
    responsable = models.ForeignKey('Usuario')

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        managed = False
        db_table = 'activo'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        managed = False
        db_table = 'categoria'


class Condicion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=45)
    observacion = models.CharField(max_length=45)

    def __unicode__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        managed = False
        db_table = 'condicion'


class Depreciacion(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    depreciacion_acumulada = models.DecimalField(max_digits=10, decimal_places=0)
    valor_depreciado = models.DecimalField(max_digits=10, decimal_places=0)
    periodo = models.IntegerField()
    activo = models.ForeignKey(Activo)

    class Meta:
        managed = False
        db_table = 'depreciacion'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        managed = False
        db_table = 'estado'


class Persona(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre + ' ' + self.apellido)

    class Meta:
        managed = False
        db_table = 'persona'


class Proveedor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=45)
    pais = models.CharField(max_length=45)
    provincia = models.CharField(max_length=45)
    canton = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    descripcion = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.CharField(max_length=45)
    pass_field = models.CharField(db_column='pass', max_length=45)  # Field renamed because it was a Python reserved word.
    tipo_usuario = models.ForeignKey(TipoUsuario)
    persona = models.ForeignKey(Persona)

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        managed = False
        db_table = 'usuario'
