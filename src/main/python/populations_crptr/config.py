#!/usr/bin/python
# Author: James Ross (jar35@st-andrews.ac.uk)
# 24/6/2015
#
# Config object for population_corruptor.py example population corruptor.

from population_crptr.example_profiles.profile_a import CorruptionProfileA
from population_crptr.example_profiles.profile_a import CorruptionProfileB
from population_crptr.example_profiles.profile_a import CorruptionProfileC
import population_crptr.example_corruptors.ocr_corruptors_td as OcrCorruptorsTD 
import population_crptr.example_corruptors.standard_corruptors_td as StandardCorruptorsTD 

class Config:
    CORRUPTION_PROFILE = CorruptionProfileA
    CORRUPTORS = StandardCorruptorsTD
    OUTPUT_DIR = "results"
    PURPOSE = "default"
    LOOKUP_FILES_DIR = "src/main/resources/lookup-files"
    DETERMINISTIC = False
    SEED = None