from django.db import models

# Create your models here.


class Dept(models.Model):
    ''' 部门类 '''

    def __str__(self):
        return self.name

    no = models.IntegerField(primary_key=True, db_column='dno', verbose_name='部门编号')
    name = models.CharField(max_length=20, db_column='dname', verbose_name='部门名称')
    location = models.CharField(max_length=10, db_column='dloc', verbose_name='部门所在地')

    class Meta:
        db_table = 'tb_dept'


class Emp(models.Model):
    ''' 员工类 '''

    no = models.IntegerField(primary_key=True, db_column='eno', verbose_name='员工编号')
    name = models.CharField(max_length=20, db_column='ename', verbose_name='员工姓名')
    job = models.CharField(max_length=10, verbose_name='职位')

    # 自参照完整性多对一外键关联

    # mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='主管编号')
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='直接主管')
    sal = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='月薪')
    comm = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='补贴')
    dept = models.ForeignKey(Dept, db_column='dno', on_delete=models.PROTECT, verbose_name='所在部门')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_emp'
