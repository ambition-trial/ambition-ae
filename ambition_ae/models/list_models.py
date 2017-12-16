from edc_base.model_mixins import ListModelMixin, BaseUuidModel


class AeClassification(ListModelMixin, BaseUuidModel):

    class Meta:
        verbose_name = 'AE Classification'


class AntibioticTreatment(ListModelMixin, BaseUuidModel):

    pass


class MeningitisSymptom(ListModelMixin, BaseUuidModel):

    pass


class Neurological(ListModelMixin, BaseUuidModel):

    pass
