class MixinRelation(object):
    @classmethod
    def object_from_file(cls, file, dic):
        for row in reader_csv(file):
            obj = {key: row[value] for key, value in dic.items()}
            yield obj
            
            
class Enterprise(TimestampMixin, CreateFromFile, MixinRelation, models.Model):
    enterprise_number = models.CharField(max_length=15, primary_key=True)
    status = models.ForeignKey(Status)
    juridical_situation = models.ForeignKey(JuridicalSituation)
    type_of_enterprise = models.ForeignKey(TypeOfEnterprise)
    juridical_form = models.ForeignKey(JuridicalForm, blank=True, null=True, default='')
    start_date = models.DateField()
    deleted = models.BooleanField(default=False, blank=True)
    deleted_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.enterprise_number
        
    @classmethod
    def object_from_file(cls, file, dic=None):
        dic = {
            'enterprise_number': 'EnterpriseNumber',
            'status_id': 'Status',
            'juridical_situation_id': 'JuridicalSituation',
            'type_of_enterprise_id': 'TypeOfEnterprise',
            'juridical_form_id': 'JuridicalForm',
            'start_date': 'StartDate'
        }
        super().object_from_file(file, dic)
        
