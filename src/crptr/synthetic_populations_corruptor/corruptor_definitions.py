import crptr.corrupt_value as corrupt_value  # Main classes to corrupt attribute values of records
import crptr.corrupt_record as corrupt_record  # Main classes to corrupt whole records
import crptr.base_functions as base_functions  # Helper functions
import crptr.position_functions as position_functions


class Corruptors:


    def __init__(self, lookupFilesDir, encoding = 'UTF-8'):
        self.encoding = encoding
        self.lookupFilesDir = lookupFilesDir
        self.setup()

    def setup(self):
        # =====================================================================
        # Character level
        # =====================================================================
        self.generalCharacter = corrupt_value.CorruptValueEdit(
            position_function = position_functions.position_mod_normal,
            char_set_funct = base_functions.char_set_ascii,
            insert_prob = 0.2,
            delete_prob = 0.2,
            substitute_prob = 0.5,
            transpose_prob = 0.1
        )

        self.marritalStatus = corrupt_value.CorruptCategoricalDomain(
            categories_list=["R", "M", "W", "D", "B", "S"]
        )

        self.surnameMisspell = corrupt_value.CorruptCategoricalValue(
            lookup_file_name = self.lookupFilesDir + '/surname-misspell.csv',
            has_header_line = False,
            unicode_encoding = self.encoding
        )

        self.keyboardShift = corrupt_value.CorruptValueKeyboard(
            position_function = position_functions.position_mod_normal,
            row_prob = 0.4,
            col_prob = 0.6
        )

        self.unknownCharacter = corrupt_value.CorruptUnknownCharacter(
            position_function=position_functions.position_mod_uniform,
            unknown_char="?"
        )

        self.deceasedFlip = corrupt_value.CorruptCategoricalDomain(
            categories_list=["D", ""]
        )

        self.ocr = corrupt_value.CorruptValueOCR(
            lookup_file_name = self.lookupFilesDir + '/ocr-variations.csv',
            has_header_line=False,
            unicode_encoding=self.encoding,
            position_function=position_functions.position_mod_uniform
        )

        # =====================================================================
        # Attribute level
        # =====================================================================


        self.abbreviateToInitial = corrupt_value.CorruptAbbreviatedNameForms(
            num_of_char = 1
        )

        self.sexFlip = corrupt_value.CorruptCategoricalDomain(
            categories_list = ["m", "f"]
        )

        self.missingValue = corrupt_value.CorruptMissingValue(
            missing_val='missing'
        )

        self.dateDDMMYYYY = corrupt_value.CorruptDate(
            date_order = "yyyy-mm-dd",
            separator = "-",
            components_to_modify = ['day', 'month', 'year'],
            date_corruption_methods = ['add', 'decline', 'swap_digit','swap_comp', 'random', 'first','full_month','abbr_month']
        )

        self.phoneticVariation = corrupt_value.CorruptValuePhonetic(
            lookup_file_name = self.lookupFilesDir + '/phonetic-variations.csv',
            has_header_line = False,
            unicode_encoding = self.encoding
        )

        self.forenameCorruptionGrouping = [(0.2, self.generalCharacter),
                                           (0.1, self.keyboardShift),
                                           (0.1, self.unknownCharacter),
                                           (0.2, self.abbreviateToInitial),
                                           (0.05, self.missingValue),
                                           (0.35, self.phoneticVariation)]

        self.forenameCorruptionGroupingOCR = [(0.6, self.ocr),
                                           (0.05, self.missingValue),
                                           (0.35, self.phoneticVariation)]

        self.addressCorruptionGrouping = [(0.3, self.generalCharacter),
                                          (0.4, self.keyboardShift),
                                          (0.2, self.unknownCharacter),
                                          (0.1, self.missingValue)]

        self.addressCorruptionGroupingOCR = [(0.9, self.ocr),
                                          (0.1, self.missingValue)]

        self.occupationCorruptionGrouping = [(0.3, self.generalCharacter),
                                             (0.2, self.keyboardShift),
                                             (0.2, self.unknownCharacter),
                                             (0.3, self.missingValue)]

        self.occupationCorruptionGroupingOCR = [(0.7, self.ocr),
                                             (0.3, self.missingValue)]

        self.surnameCorruptionGrouping = [(0.2, self.generalCharacter),
                                          (0.1, self.keyboardShift),
                                          (0.1, self.unknownCharacter),
                                          (0.2, self.surnameMisspell),
                                          (0.05, self.missingValue),
                                          (0.35, self.phoneticVariation)]

        self.surnameCorruptionGroupingOCR = [(0.4, self.ocr),
                                          (0.2, self.surnameMisspell),
                                          (0.05, self.missingValue),
                                          (0.35, self.phoneticVariation)]

        self.splitDateCorruptionGrouping = [(0.7, self.keyboardShift),
                                       (0.2, self.generalCharacter),
                                       (0.1, self.missingValue)]

        self.splitDateCorruptionGroupingOCR = [(0.9, self.ocr),
                                            (0.1, self.missingValue)]

        self.deceasedCorruptionGrouping = [(0.5, self.deceasedFlip),
                                           (0.2, self.keyboardShift),
                                           (0.05, self.unknownCharacter),
                                           (0.25, self.missingValue)]

        self.deceasedCorruptionGroupingOCR = [(0.5, self.deceasedFlip),
                                           (0.5, self.ocr)]

        # =====================================================================
        # Record level
        # =====================================================================
        self.blankRecord = corrupt_record.CorruptClearRecord(
            clear_val=' '
        )



class BirthCorruptors(Corruptors):

    def __init__(self, labels, lookupFilesDir, encoding = 'UTF-8'):
        self.columnLabels = labels
        Corruptors.__init__(self, lookupFilesDir, encoding)

    def setup(self):

        Corruptors.setup(self)

        # =====================================================================
        # Record level
        # =====================================================================
        self.dayMonthSwapMarriage = corrupt_record.CorruptSwapAttributes(
            attr1='day of parents\' marriage',
            attr2='month of parents\' marriage',
            attr_name_list=self.columnLabels
        )

        self.childNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='child\'s forname(s)',
            attr2='child\'s surname',
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


class MarriageCorruptors(Corruptors):

    def __init__(self, labels, lookupFilesDir, encoding = 'UTF-8'):
        self.columnLabels = labels
        Corruptors.__init__(self, lookupFilesDir, encoding)


    def setup(self):

        Corruptors.setup(self)

        self.dayMonthSwapDeath = corrupt_record.CorruptSwapAttributes(
            attr1='day',
            attr2='month',
            attr_name_list=self.columnLabels
        )

        self.groomNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='forename of groom',
            attr2='surname of groom',
            attr_name_list=self.columnLabels
        )

        self.brideNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='forename of bride',
            attr2='surname of bride',
            attr_name_list=self.columnLabels
        )

        self.groomFatherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='groom\'s father\'s forename',
            attr2='groom\'s father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.groomMotherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='groom\'s mother\'s forename',
            attr2='groom\'s mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )

        self.brideFatherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='bride\'s father\'s forename',
            attr2='bride\'s father\'s surname',
            attr_name_list=self.columnLabels
        )

        self.brideMotherNameSwap = corrupt_record.CorruptSwapAttributes(
            attr1='bride\'s mother\'s forename',
            attr2='bride\'s mother\'s maiden surname',
            attr_name_list=self.columnLabels
        )

