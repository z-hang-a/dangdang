# Generated by Django 2.0.6 on 2019-09-04 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'managed': False,
                'db_table': 'auth_group',
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DCategory',
            fields=[
                ('category_id', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
                ('book_counts', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('category_pid', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_category',
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_admin_log',
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_session',
            },
        ),
        migrations.CreateModel(
            name='DOrderiterm',
            fields=[
                ('shop_id', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('shop_bookid', models.DecimalField(decimal_places=0, max_digits=20)),
                ('shop_ordid', models.DecimalField(decimal_places=0, max_digits=20)),
                ('shop_num', models.DecimalField(decimal_places=0, max_digits=20)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'd_orderiterm',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCar',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_id', models.CharField(blank=True, max_length=20, null=True)),
                ('count', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
                ('user_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'shopping_car',
            },
        ),
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('detail_address', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('telphone', models.CharField(blank=True, max_length=20, null=True)),
                ('addr_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('user_id', models.DecimalField(decimal_places=0, max_digits=20)),
            ],
            options={
                'managed': False,
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('book_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(blank=True, max_length=255, null=True)),
                ('book_author', models.CharField(blank=True, max_length=255, null=True)),
                ('book_publish', models.CharField(blank=True, max_length=255, null=True)),
                ('publish_time', models.CharField(blank=True, max_length=255, null=True)),
                ('revision', models.IntegerField(blank=True, null=True)),
                ('book_isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('word_count', models.CharField(blank=True, max_length=64, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('open_type', models.CharField(blank=True, max_length=64, null=True)),
                ('book_category', models.IntegerField(blank=True, null=True)),
                ('book_wrapper', models.CharField(blank=True, max_length=255, null=True)),
                ('book_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('book_dprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('editor_recommendation', models.CharField(blank=True, max_length=2000, null=True)),
                ('content_introduction', models.CharField(blank=True, max_length=2000, null=True)),
                ('author_introduction', models.CharField(blank=True, max_length=2000, null=True)),
                ('menu', models.CharField(blank=True, max_length=2000, null=True)),
                ('media_review', models.CharField(blank=True, max_length=2000, null=True)),
                ('digest_image_path', models.CharField(blank=True, max_length=2000, null=True)),
                ('product_image_path', models.CharField(blank=True, max_length=2000, null=True)),
                ('series_name', models.CharField(blank=True, max_length=128, null=True)),
                ('printing_time', models.DateField(blank=True, null=True)),
                ('impression', models.CharField(blank=True, max_length=64, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('shelves_date', models.DateField(blank=True, null=True)),
                ('customer_socre', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('book_status', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('sales', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('book_size', models.CharField(blank=True, max_length=255, null=True)),
                ('book_pager', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.DecimalField(decimal_places=0, max_digits=20, primary_key=True, serialize=False)),
                ('num', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('create_date', models.DateTimeField()),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('order_addrid', models.DecimalField(decimal_places=0, max_digits=20)),
                ('order_uid', models.DecimalField(decimal_places=0, max_digits=20)),
                ('status', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_order',
            },
        ),
    ]
