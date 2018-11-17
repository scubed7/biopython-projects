#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:51:11 2018

@author: padmagopinath
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import Bio
from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq)
print(my_seq + " - Sequence")
print(my_seq.complement() + " - Complement")
print(my_seq.reverse_complement() + " - Reverse Complement")
from Bio import SeqIO
from Bio.Alphabet import generic_nucleotide
from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_id[1]
print(standard_table)
nuc_seq = Seq("GATCGATGC", generic_nucleotide)
print(nuc_seq)
from Bio import ExPASy
from Bio import SeqIO
with ExPASy.get_sprot_raw("O23729") as handle:
    seq_record = SeqIO.read(handle, "swiss")
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])