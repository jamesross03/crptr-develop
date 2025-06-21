from crptr.corrupt_records import base
from crptr.synthetic_populations.corruptor_definitions.base import Corruptors

class BirthCorruptors(Corruptors):

    def __init__(self, labels, lookupFilesDir, encoding = 'UTF-8'):
        self.columnLabels = labels
        Corruptors.__init__(self, lookupFilesDir, encoding)

    def setup(self):

        Corruptors.setup(self)

        # =====================================================================
        # Record level
        # =====================================================================
        self.dayMonthSwapMarriage = base.CorruptSwapAttributes(
            attr1='day of parents\' marriage',
            attr2='month of parents\' marriage',
            attr_name_list=self.columnLabels
        )

        self.childNameSwap = base.CorruptSwapAttributes(
            attr1='child\'s forname(s)',
            attr2='child\'s surname',
            attr_name_list=self.columnLabels
        )

        self.fatherNameSwap = base.CorruptSwapAttributes(
            attr1='father\'s forename',
            attr2='father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.motherNameSwap = base.CorruptSwapAttributes(
            attr1='mother\'s forename',
            attr2='mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )