from crptr.corrupt_records import base
from crptr.synthetic_populations.corruptor_definitions.base import Corruptors


class MarriageCorruptors(Corruptors):

    def __init__(self, labels, lookupFilesDir, encoding = 'UTF-8'):
        self.columnLabels = labels
        Corruptors.__init__(self, lookupFilesDir, encoding)


    def setup(self):

        Corruptors.setup(self)

        self.dayMonthSwapDeath = base.CorruptSwapAttributes(
            attr1='day',
            attr2='month',
            attr_name_list=self.columnLabels
        )

        self.groomNameSwap = base.CorruptSwapAttributes(
            attr1='forename of groom',
            attr2='surname of groom',
            attr_name_list=self.columnLabels
        )

        self.brideNameSwap = base.CorruptSwapAttributes(
            attr1='forename of bride',
            attr2='surname of bride',
            attr_name_list=self.columnLabels
        )

        self.groomFatherNameSwap = base.CorruptSwapAttributes(
            attr1='groom\'s father\'s forename',
            attr2='groom\'s father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.groomMotherNameSwap = base.CorruptSwapAttributes(
            attr1='groom\'s mother\'s forename',
            attr2='groom\'s mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )

        self.brideFatherNameSwap = base.CorruptSwapAttributes(
            attr1='bride\'s father\'s forename',
            attr2='bride\'s father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.brideMotherNameSwap = base.CorruptSwapAttributes(
            attr1='bride\'s mother\'s forename',
            attr2='bride\'s mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )

