from crptr import corrupt_record
from crptr.synthetic_populations.corruptor_definitions.base import Corruptors


class DeathCorruptors(Corruptors):

    def __init__(self, labels, lookupFilesDir, encoding = 'UTF-8'):
        self.columnLabels = labels
        Corruptors.__init__(self, lookupFilesDir, encoding)


    def setup(self):

        Corruptors.setup(self)

        # =====================================================================
        # Attribute level
        # =====================================================================


        # =====================================================================
        # Record level
        # =====================================================================
        self.dayMonthSwapDeath = corrupt_record.CorruptSwapAttributes(
            attr1='day',
            attr2='month',
            attr_name_list=self.columnLabels
        )

        self.deceasedNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='forename(s) of deceased',
            attr2='surname of deceased',
            attr_name_list=self.columnLabels
        )

        self.fatherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='father\'s forename',
            attr2='father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.motherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='mother\'s forename',
            attr2='mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )