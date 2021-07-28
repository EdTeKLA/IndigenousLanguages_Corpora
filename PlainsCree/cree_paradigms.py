# Cree Paradigms

'''NOUN PARADIGMS'''
# Noun Possesion

# Kinship nouns
# Rules:
#       - Possesive affix attached to the kinship noun stem to make it a complete possesive noun
#       - If noun begins with mi- it is dropped
#       - If noun begins with long î, keep the long î. in 3rds add -w- before
possesive_kinship_nouns = {
    '1S': ['ni'],                       # My son
    '1S_long': ['nî'],                  # My son (long î)
    '2S': ['ki'],                       # Your son
    '2S_long': ['kî'],                  # Your son (long î)
    '3S': ['o', 'a'],                   # His/her son(s)
    '3S_long': ['wî', 'a'],             # His/her son(s) (change -o- to -w-, long î)
    '1P': ['ni', 'nân'],                # Our son
    '1P_long': ['nî', 'nân'],           # Our son (long î)
    '2I': ['ki', 'naw'],                # Our son
    '2I_long': ['kî', 'naw'],           # Our son (long î)
    '2P': ['ki', 'wâw'],                # Your son
    '2P_long': ['kî', 'wâw'],           # Your son (long î)
    '3P': ['o', 'wâwa'],                # Their son(s)
    '3P_long': ['wî', 'wâwa'],          # Their son(s) (change -o- to -w-, long î)
    '3O': ['o', 'yiwa'],                # 3's son(s)
    '3O_long': ['wî', 'yiwa'],          # 3's son(s) (change -o- to -w-, long î)
}
# Animate noun possesive paradigm
# Rules:
#       - Joiners  -t- if nouns begins with a vowel
#       - If noun begins with mi- it is dropped
noun_possesive_animate = {
    '1S': ['ni', 'nitim'],              # My ________
    '1S_j': ['nit', 'nitim'],           # My ________ (-t- joiner)
    '1S_long': ['nî', 'nitim'],         # My ________ (long î)
    '2S': ['ki', 'im'],                 # Your ______
    '2S_j': ['kit', 'im'],              # Your ______ (-t- joiner)
    '2S_long': ['kî', 'im'],            # Your ______ (long î)
    '3S': ['o', 'ima'],                 # His/her ___
    '3S_j': ['ot', 'ima'],              # His/her ___ (-t- joiner)
    '3S_long': ['wî', 'ima'],           # His/her ___ (change -o- to -w-, long î)
    '1P': ['ni', 'iminân'],             # Our _______
    '1P_j': ['nit', 'iminân'],          # Our _______ (-t- joiner)
    '1P_long': ['nî', 'iminân'],        # Our _______ (long î)
    '2I': ['ki', 'iminaw'],             # Our _______
    '2I_j': ['kit', 'iminaw'],          # Our _______ (-t- joiner)
    '2I_long': ['kî', 'iminaw'],        # Our _______ (long î)
    '2P': ['ki', 'imiwâwa'],            # Your ______
    '2P_j': ['kit', 'imiwâwa'],         # Your ______ (-t- joiner)
    '2P': ['kî', 'imiwâwa'],            # Your ______ (long î)
    '3P': ['o', 'imiwâwa'],             # Their _____
    '3P_j': ['ot', 'imiwâwa'],          # Their _____ (-t- joiner)
    '3P_long': ['wî', 'imiwâwa'],       # Their _____ (change -o- to -w-, long î)
    '3O': ['o', 'imiyiwa'],             # 3's _______
    '3O_j': ['ot', 'imiyiwa'],          # 3's _______ (-t- joiner)
    '3O_long': ['o', 'imiyiwa'],        # 3's _______ (change -o- to -w-, long î)
}
# Inanimate noun possesive paradigm
# Rules:
#       - Joiners  -t- if nouns begins with a vowel
#       - If noun begins with mi- it is dropped
noun_possesive_animate = {
    '1S': ['ni'],                       # My _________
    '1S_j': ['nit'],                    # My _________ (-t- joiner)
    '1S_long': ['nî'],                  # My _________ (long î)
    '2S': ['ki'],                       # Your _______
    '2S_j': ['kit'],                    # Your _______ (-t- joiner)
    '2S_long': ['kî'],                  # Your _______ (long î)
    '3S': ['o'],                        # His/her ____
    '3S_j': ['ot'],                     # His/her ____ (-t- joiner)
    '3S_long': ['wî'],                  # His/her ____ (change -o- to -w-, long î)
    '1P': ['ni', 'inân'],               # Our ________
    '1P_j': ['nit', 'inân'],            # Our ________ (-t- joiner)
    '1P_long': ['nî', 'inân'],          # Our ________ (long î)
    '2I': ['ki', 'inaw'],               # Our ________
    '2I_j': ['kit', 'inaw'],            # Our ________ (-t- joiner)
    '2I_long': ['kî', 'inaw'],          # Our ________ (long î)
    '2P': ['ki', 'iwâwa'],              # Your _______
    '2P_j': ['kit', 'iwâwa'],           # Your _______ (-t- joiner)
    '2P_long': ['kî', 'iwâwa'],         # Your _______ (long î)
    '3P': ['o', 'iwâwa'],               # Their ______
    '3P_j': ['ot', 'iwâwa'],            # Their ______ (-t- joiner)
    '3P_long': ['wî', 'iwâwa'],         # Their ______ (change -o- to -w-, long î)
    '3O': ['o', 'iyiwa'],               # 3's ________
    '3O_j': ['ot', 'iyiwa'],            # 3's ________ (-t- joiner)
    '3O_long': ['wî', 'iyiwa'],         # 3's ________ (change -o- to -w-, long î)
}

''' VERB PARADIGMS '''

# Animate Intransitive Verbs (VAI)
# Rules:
#        - Have no direct object, the subject is doing the verb but neither to anyone nor anything.
#        - VAI ending with a, â, i, î, o, and ô remain the same in all conjunctions


# Independent mode (VAI)
# Rules:
#        - Final "e" to "â" ( 1st & 2nd person only)
#        - Begins with a vowel, -t- joiner
VAI_Independent = {
    '1S': ['ni', 'n'],                  # I ______
    '1S_j': ['nit', 'n'],               # I ______ (-t- joiner)
    '1S_long': ['ni', 'ân'],            # I ______ (change -e- to -â-)
    '1S_j_long': ['nit', 'ân'],         # I ______ (-t- joiner, change -e- to -â-)
    '2S': ['ki', 'n'],                  # You ____
    '2S_j': ['kit', 'n'],               # You ____ (-t- joiner)
    '2S_long': ['ki', 'ân'],            # You ____ (change -e- to -â-)
    '2S_j_long': ['kit', 'ân'],         # You ____ (-t- joiner, change -e- to -â-)
    '3S': ['w'],                        # S/he ___
    '1P': ['ni', 'nân'],                # We(ex.)_
    '1P_j': ['nit', 'nân'],             # We(ex.)_ (-t- joiner)
    '1P_long': ['ni', 'ânân'],          # We(ex.)_ (change -e- to -â-)
    '1P': ['nit', 'ânân'],              # We(ex.)_ (-t- joiner, change -e- to -â-)
    '2I': ['ki', 'naw'],                # We(in.)_
    '2I_j': ['kit', 'naw'],             # We(in.)_ (-t- joiner)
    '2I_long': ['ki', 'ânaw'],          # We(in.)_ (change -e- to -â-)
    '2I_j_long': ['kit', 'ânaw'],       # We(in.)_ (-t- joiner, change -e- to -â-)
    '2P': ['ki', 'nâwâw'],              # You all_
    '2P_j': ['kit', 'nâwâw'],           # You all_ (-t- joiner)
    '2P_long': ['ki', 'ânâwâw'],        # You all_ (change -e- to -â-)
    '2P_j_long': ['kit', 'ânâwâw'],     # You all_ (-t- joiner, change -e- to -â-)
    '3P': ['wak'],                      # They ___
    '3O': ['yiwa'],                     # 3's ____
}

# Conjunct Mode (VAI)
# Rules:
#        - Final 'e' remains the same
#        - Begins with vowel, -h- joiner
VAI_conjunct = {
    '1S': ['e', 'yân'],                 # My ______
    '1S_j': ['eh', 'yân'],              # My ______ (-h- joiner)
    '2S': ['e', 'yan'],                 # Your ____
    '2S_j': ['eh', 'yan'],              # Your ____ (-h- joiner)
    '3S': ['e', 't'],                   # His/her__
    '3S_j': ['eh', 't'],                # His/her__ (-h- joiner)
    '1P': ['e', 'yâhk'],                # We(ex.)__
    '1P_j': ['eh', 'yâhk'],             # We(ex.)__ (-h- joiner)
    '2I': ['e', 'yahk'],                # We(in.)__
    '2I_j': ['eh', 'yahk'],             # We(in.)__ (-h- joiner)
    '2P': ['e', 'yek'],                 # Your ____
    '2P_j': ['eh', 'yek'],              # Your ____ (-h- joiner)
    '3P': ['e', 'cik'],                 # They ____
    '3P_j': ['eh', 'cik'],              # They ____ (-h- joiner)
    '3O': ['e', 'yit'],                 # 3's _____
    '3O_j': ['eh', 'yit'],              # 3's _____ (-h- joiner)
}

# Subjunctive mode (VAI)
VAI_subjunctive_independent = {
    '1S': ['yâni'],                      # If I ______
    '2S': ['yani'],                      # If you ______
    '3S': ['ci'],                        # If he/she ______
    '1P': ['yâhki'],                     # If we ______
    '2I': ['yahki'],                     # If we ______
    '2P': ['yeko'],                      # If you ______
    '3P': ['twâwi'],                     # If they ______
    '3O': ['yici'],                      # If 3'______(s)
}

VAI_subjunctive_conjunct = {
    '1S': ['kâ', 'yân'],                 # When I am ______ing
    '2S': ['kâ', 'yan'],                 # When you are ______ing
    '3S': ['kâ' 't'],                    # When he/she is ______ing
    '1P': ['kâ', 'yâhk'],                # When we are ______ing
    '2I': ['kâ', 'yahk'],                # When we are ______ing
    '2P': ['kâ', 'yek'],                 # When you are______ing
    '3P': ['kâ', 'cik'],                 # When they are______ing
    '3O': ['kâ', 'yit'],                 # When 3' is/are______ing
}

# Transitive Inanimate Verbs (VTI)
# Rules:
#        - Have animate subject and direct inanimate object
#        - VAI ending with short a follow this paradigm (other VTI'S will follow VAI paradigm)
#
#
# Independent mode (VTI)
# Rules:
#        - Final "a" to "e" ( 1st & 2nd person only)
#        - Begins with a vowel, -t- joiner
#        - If VTI does NOT end with a, follow VAI patterm for BOTH modes ****

VTI_Independent = {
    '1S': ['ni', 'en'],                 # I ______ NI (change -a- to -e-)
    '1S_j': ['nit', 'en'],              # I ______ NI (-t- joiner, change -a- to -e-)
    '2S': ['ki', 'en'],                 # You ____ NI (change -a- to -e-)
    '2S_j': ['kit', 'en'],              # You ____ NI (-t- joiner, change -a- to -e-)
    '3S': ['m'],                        # S/he ___ NI
    '1P': ['ni', 'enân'],               # We(ex.)_ NI (change -a- to -e-)
    '1P_j': ['nit', 'enân'],            # We(ex.)_ NI (-t- joiner, change -a- to -e-)
    '2I': ['ki', 'enaw'],               # We(in.)_ NI (change -a- to -e-)
    '2I_j': ['kit', 'enaw'],            # We(in.)_ NI (-t- joiner, change -a- to -e-)
    '2P': ['ki', 'enâwâw'],             # You all_ NI (change -a- to -e-)
    '2P_j': ['kit', 'enâwâw'],          # You all_ NI (-t- joiner, change -a- to -e-)
    '3P': ['mwak'],                     # They ___ NI
    '3O': ['miyiwa'],                   # 3's ____ NI
}
# Conjuct mode (VTI)
# Rules:
#        - Begins with a vowel, -h- joiner
#        - If VTI does NOT end with a, follow VAI patterm for BOTH modes ****
VTI_conjunct = {
    '1S': ['e', 'mân'],                 # I am _________ing NI
    '1S_j': ['eh', 'mân'],              # I am _________ing NI (-h- joiner)
    '2S': ['e', 'man'],                 # You are ______ing NI
    '2S_j': ['eh', 'man'],              # You are ______ing NI (-h- joiner)
    '3S': ['e', 'hk'],                  # He/she is ____ing NI
    '3S_j': ['eh', 'hk'],               # He/she is ____ing NI (-h- joiner)
    '1P': ['e', 'mâhk'],                # We(ex.)are ___ing NI
    '1P_j': ['eh', 'mâhk'],             # We(ex.)are ___ing NI (-h- joiner)
    '2I': ['e', 'mahk'],                # We(in.)are ___ing NI
    '2I_j': ['eh', 'mahk'],             # We(in.)are ___ing NI (-h- joiner)
    '2P': ['e', 'mek'],                 # You are ______ing NI
    '2P_j': ['eh', 'mek'],              # You are ______ing NI (-h- joiner)
    '3P': ['e', 'hkik'],                # They are _____ing NI
    '3P_j': ['eh', 'hkik'],             # They are _____ing NI (-h- joiner)
    '3O': ['e', 'miyit'],               # 3's is/are ___ing NI
    '3O_j': ['eh', 'miyit'],            # 3's is/are ___ing NI (-h- joiner)
}
# Subjunctive mode (VTI)
# Rules:
#       - Transitive inanimate verb ending in short "a"
#       - All other TI verb endings use and follow the AI subjunctive case pattern
VTI_subjunctive_independent = {
    '1S': ['mâni'],                     # If/when I _______
    '2S': ['mani'],                     # If/when you _____
    '3S': ['hki'],                      # If/when he/she __
    '1P': ['mâhki'],                    # If/when we ______
    '2I': ['mahki'],                    # If/when we ______
    '2P': ['meko'],                     # If/when you _____
    '3P': ['hkwâwi'],                   # If/when they ____
    '3O': ['miyici'],                   # If/when 3'_______
}
VTI_subjunctive_conjunct = {
    '1S': ['kâ', 'mân'],                 # If/when I ______
    '2S': ['kâ', 'man'],                 # If/when you ____
    '3S': ['kâ' 'hk'],                   # If/when he/she _
    '1P': ['kâ', 'mâhk'],                # If/when we _____
    '2I': ['kâ', 'mahk'],                # If/when we _____
    '2P': ['kâ', 'mek'],                 # If/when you ____
    '3P': ['kâ', 'hkik'],                # If/when they ___
    '3O': ['kâ', 'miyit'],               # If/when 3' _____
}

''' VTA DIRECT PARADIGMS '''

# Transitive animate verns have an animate subject/actor thay may be expressed by a noun or a pronoun
# 2 forms: Direct and Inverse
# Rules: 
#       - Final -s- to -t- (except set 3 direct and excepy set 1 Inverse)
#       - -t- joiner for independent mode for set 1 & set 3 for both direct and inverse
#       - -h- is used when a tense marker on pre-verb is used, in ALL sets, in both direct and inverse of the conjunct mode,
#         if TA ends in a vowel (in all sets before attaching personal suffix marker)
#       - If a transitive animate verb ends in a -w-, drop the -w- and add thr personal suffix markes for set 3 inverse in both modes
#       - Exceptions: tipah, nitipahwâw, etipahwak & ahi, nitahâw, ehahak

# Set 1 direct  (VTA)
# Actor/subject: 1s, 2s, 1p, 2i, 2p
# Object/goal: 3s, 3p, 3'
firstpersonsingular_thirdperson = {
    '1S_3S_ind': ['ni', 'âw'],              # I __________him/her/NA
    '1S_3S_ind_jtb': ['nit', 'âw'],         # I __________him/her/NA (Beginning -t- joiner)
    '1S_3S_ind_jtf': ['ni', 'tâw'],         # I __________him/her/NA (Final -t- joiner)
    '1S_3S_ind_jtbf': ['nit', 'tâw'],       # I __________him/her/NA (Beginning -t- joiner, and final -t- joiner)

    '1S_3P_ind': ['ni', 'âwak'],            # I __________they/NA(pl)
    '1S_3P_ind_jtb': ['nit', 'âwak'],       # I __________they/NA(pl) (Beginning -t- joiner)
    '1S_3P_ind_jtf': ['ni', 'tâwak'],       # I __________they/NA(pl) (Final -t- joiner)
    '1S_3P_ind_jtbf': ['nit', 'tâwak'],     # I __________they/NA(pl) (Beginning -t- joiner, and final -t- joiner)

    '1S_3O_ind': ['ni', 'imâwa'],           # I __________3'
    '1S_3O_ind_jtb': ['nit', 'imâwa'],      # I __________3' (Beginning -t- joiner)
    '1S_3O_ind_jtf': ['ni', 'timâwa'],      # I __________3' (Final -t- joiner)
    '1S_3O_ind_jtbf': ['nit', 'imâwa'],     # I __________3' (Beginning -t- joiner, and final -t- joiner)

    '1S_3S_con': ['e', 'ak'],               # I am _______ing him/her/NA
    '1S_3S_con_jh': ['eh', 'ak'],           # I am _______ing him/her/NA (Beginning -h- joiner) 
    '1S_3S_con_jt': ['e', 'tak'],           # I am _______ing him/her/NA (Final -t- joiner)
    '1S_3S_con_jht': ['eh', 'tak'],         # I am _______ing him/her/NA (Beginning -h- joiner, and final -t- joiner) 

    '1S_3P_con': ['e', 'akik'],             # I am _______ing them/NA(pl)
    '1S_3P_con_jh': ['eh', 'akik'],         # I am _______ing them/NA(pl) (Beginning -h- joiner)
    '1S_3P_con_jtf': ['e', 'takik'],        # I am _______ing them/NA(pl) (Final -t- joiner)
    '1S_3P_con_jht': ['eh', 'takik'],       # I am _______ing them/NA(pl) (Beginning -h- joiner, and final -t- joiner)

    '1S_3O_con': ['e', 'imak'],             # I am _______ing 3'
    '1S_3O_con_jh': ['eh', 'imak'],         # I am _______ing 3' (Beginning -h- joiner)
    '1S_3O_con_jtf': ['e', 'timak'],        # I am _______ing 3' (Final -t- joiner)
    '1S_3O_con_jht': ['eh', 'timak'],       # I am _______ing 3' (Beginning -h- joiner, and final -t- joiner)
}
secondpersonsingular_thirdperson = {
    '2S_3S_ind': ['ki', 'âw'],              # You ________him/her/NA
    '2S_3S_ind_jtb': ['kit', 'âw'],         # You ________him/her/NA (Beginning -t- joiner)
    '2S_3S_ind_jtf': ['ki', 'tâw'],         # You ________him/her/NA (Final -t- joiner)
    '2S_3S_ind_jtbf': ['kit', 'tâw'],       # You ________him/her/NA (Beginning -t- joiner, and final -t- joiner)

    '2S_3P_ind': ['ki', 'âwak'],            # You ________they/NA(pl)
    '2S_3P_ind_jtb': ['kit', 'âwak'],       # You ________they/NA(pl) (Beginning -t- joiner)
    '2S_3P_ind_jtf': ['ki', 'tâwak'],       # You ________they/NA(pl) (Final -t- joiner)
    '2S_3P_ind_jtbf': ['kit', 'tâwak'],     # You ________they/NA(pl) (Beginning -t- joiner, and final -t- joiner)

    '2S_3O_ind': ['ki', 'imâwa'],           # You ________3'
    '2S_3O_ind_jtb': ['kit', 'imâwa'],      # You ________3' (Beginning -t- joiner)
    '2S_3O_ind_jtf': ['ki', 'timâwa'],      # You ________3' (Final -t- joiner)
    '2S_3O_ind_jtbf': ['kit', 'timâwa'],    # You ________3' (Beginning -t- joiner, and final -t- joiner)

    '2S_3S_con': ['e', 'at'],               # You are ____ing him/her/NA
    '2S_3S_con_jh': ['eh', 'at'],           # You are ____ing him/her/NA (Beginning -h- joiner)
    '2S_3S_con_jtf': ['e', 'tat'],          # You are ____ing him/her/NA (Final -t- joiner)
    '2S_3S_con_jht': ['eh', 'tat'],         # You are ____ing him/her/NA (Beginning -h- joiner, and final -t- joiner)

    '2S_3P_con': ['e', 'acik'],             # You are ____ing them/NA(pl)
    '2S_3P_con_jh': ['eh', 'acik'],         # You are ____ing them/NA(pl) (Beginning -h- joiner)
    '2S_3P_con_jtf': ['e', 'tacik'],        # You are ____ing them/NA(pl) (Final -t- joiner)
    '2S_3P_con_jht': ['eh', 'tacik'],       # You are ____ing them/NA(pl) (Beginning -h- joiner, and final -t- joiner)

    '2S_3O_con': ['e', 'imat'],             # You are ____ing 3'
    '2S_3O_con_jh': ['eh', 'imat'],         # You are ____ing 3' (Beginning -h- joiner)
    '2S_3O_con_jtf': ['e', 'iymat'],        # You are ____ing 3' (Final -t- joiner)
    '2S_3O_con_jht': ['eh', 'timat'],       # You are ____ing 3' (Beginning -h- joiner, and final -t- joiner)
}
firstpersonpluaral_thirdperson = {
    '1p_3S_ind': ['ni', 'ânân'],            # We _________him/her/NA
    '1p_3S_ind_jtb': ['nit', 'ânân'],       # We _________him/her/NA (Beginning -t- joiner)
    '1p_3S_ind_jtf': ['ni', 'tânân'],       # We _________him/her/NA (Final -t- joiner)
    '1p_3S_ind_jtbf': ['nit', 'tânân'],     # We _________him/her/NA (Beginning -t- joiner, and final -t- joiner)

    '1p_3P_ind': ['ni', 'ânânak'],          # We _________they/NA(pl)
    '1p_3P_ind_jtb': ['nit', 'ânânak'],     # We _________they/NA(pl) (Beginning -t- joiner)
    '1p_3P_ind_jtf': ['ni', 'tânânak'],     # We _________they/NA(pl) (Final -t- joiner)
    '1p_3P_ind_jtbf': ['nit', 'tânânak'],   # We _________they/NA(pl) (Beginning -t- joiner, and final -t- joiner)

    '1p_3O_ind': ['ni', 'imânâna'],         # We _________3'
    '1p_3O_ind_jtb': ['nit', 'imânâna'],    # We _________3' (Beginning -t- joiner)
    '1p_3O_ind_jtf': ['ni', 'timânâna'],    # We _________3' (Final -t- joiner)
    '1p_3O_ind_jtbf': ['nit', 'timânâna'],  # We _________3' (Beginning -t- joiner, and final -t- joiner)

    '1p_3S_con': ['e', 'âyâhk'],            # We are _____ing him/her/NA
    '1p_3S_con_jh': ['eh', 'âyâhk'],        # We are _____ing him/her/NA (Beginning -h- joiner)
    '1p_3S_con_jtf': ['e', 'tâyâhk'],       # We are _____ing him/her/NA (Final -t- joiner)
    '1p_3S_con_jht': ['e', 'âyâhk'],        # We are _____ing him/her/NA (Beginning -h- joiner, and final -t- joiner)

    '1p_3P_con': ['e', 'âyâhkik'],          # We are _____ing them/NA(pl)
    '1p_3P_con_jh': ['eh', 'âyâhkik'],      # We are _____ing them/NA(pl) (Beginning -h- joiner)
    '1p_3P_con_jtf': ['e', 'tâyâhkik'],     # We are _____ing them/NA(pl) (Final -t- joiner)
    '1p_3P_con_jht': ['eh', 'tâyâhkik'],    # We are _____ing them/NA(pl) (Beginning -h- joiner, and final -t- joiner)

    '1p_3O_con': ['e', 'imâyâhk'],          # We are _____ing 3'
    '1p_3O_con_jh': ['eh', 'imâyâhk'],      # We are _____ing 3' (Beginning -h- joiner)
    '1p_3O_con_jtf': ['e', 'timâyâhk'],     # We are _____ing 3' (Final -t- joiner)
    '1p_3O_con_jht': ['eh', 'timâyâhk'],    # We are _____ing 3' (Beginning -h- joiner, and final -t- joiner)
}
secondinclusive_thirdperson = {
    '2I_3S_ind': ['ki', 'ânaw'],            # We _________him/her/NA
    '2I_3S_ind_jtb': ['kit', 'ânaw'],       # We _________him/her/NA (Beginning -t- joiner)
    '2I_3S_ind_jtf': ['ki', 'tânaw'],       # We _________him/her/NA (Final -t- joiner)
    '2I_3S_ind_jtbf': ['kit', 'tânaw'],     # We _________him/her/NA (Beginning -t- joiner, and final -t- joiner)

    '2I_3P_ind': ['ki', 'ânawak'],          # We _________they/NA(pl)
    '2I_3P_ind_jtb': ['kit', 'ânawak'],     # We _________they/NA(pl) (Beginning -t- joiner)
    '2I_3P_ind_jtf': ['ki', 'tânawak'],     # We _________they/NA(pl) (Final -t- joiner)
    '2I_3P_ind_jtbf': ['kit', 'tânawak'],   # We _________they/NA(pl) (Beginning -t- joiner, and final -t- joiner)

    '2I_3O_ind': ['ki', 'imânawa'],         # We _________3'
    '2I_3O_ind_jtb': ['kit', 'imânawa'],    # We _________3' (Beginning -t- joiner)
    '2I_3O_ind_jtf': ['ki', 'timânawa'],    # We _________3' (Final -t- joiner)
    '2I_3O_ind_jtbf': ['kit', 'timânawa'],  # We _________3' (Beginning -t- joiner, and final -t- joiner)

    '2I_3S_con': ['e', 'âyahk'],            # We are _____ing him/her/NA
    '2I_3S_con_jh': ['eh', 'âyahk'],        # We are _____ing him/her/NA (Beginning -h- joiner)
    '2I_3S_con_jtf': ['e', 'tâyahk'],       # We are _____ing him/her/NA (Final -t- joiner)
    '2I_3S_con_jht': ['eh', 'tâyahk'],      # We are _____ing him/her/NA (Beginning -h- joiner, and final -t- joiner)

    '2I_3P_con': ['e', 'âyahkik'],          # We are _____ing them/NA(pl)
    '2I_3P_con_jh': ['eh', 'âyahkik'],      # We are _____ing them/NA(pl) (Beginning -h- joiner)
    '2I_3P_con_jtf': ['e', 'tâyahkik'],     # We are _____ing them/NA(pl) (Final -t- joiner)
    '2I_3P_con_jht': ['eh', 'tâyahkik'],    # We are _____ing them/NA(pl) (Beginning -h- joiner, and final -t- joiner)

    '2I_3O_con': ['e', 'imâyahk'],          # We are _____ing 3'
    '2I_3O_con_jh': ['eh', 'imâyahk'],      # We are _____ing 3' (Beginning -h- joiner)
    '2I_3O_con_jtf': ['e', 'timâyahk'],     # We are _____ing 3' (Final -t- joiner)
    '2I_3O_con_jht': ['eh', 'timâyahk'],    # We are _____ing 3' (Beginning -h- joiner, and final -t- joiner)
}
secondplural_thirdperson = {
    '2P_3S_ind': ['ki', 'âwaw'],            # You ________him/her/NA
    '2P_3S_ind_jtb': ['kit', 'âwaw'],       # You ________him/her/NA (Beginning -t- joiner)
    '2P_3S_ind_jtf': ['ki', 'tâwaw'],       # You ________him/her/NA (Final -t- joiner)
    '2P_3S_ind_jtbf': ['kit', 'tâwaw'],     # You ________him/her/NA (Beginning -t- joiner, and final -t- joiner)

    '2P_3P_ind': ['ki', 'âwâwak'],          # You ________they/NA(pl)
    '2P_3P_ind_jtb': ['kit', 'âwâwak'],     # You ________they/NA(pl) (Beginning -t- joiner)
    '2P_3P_ind_jtf': ['ki', 'tâwâwak'],     # You ________they/NA(pl)(Final -t- joiner)
    '2P_3P_ind_jtbf': ['kit', 'tâwâwak'],   # You ________they/NA(pl) (Beginning -t- joiner, and final -t- joiner)

    '2P_3O_ind': ['ki', 'imâwâwa'],         # You ________3'
    '2P_3O_ind_jtb': ['kit', 'imâwâwa'],    # You ________3' (Beginning -t- joiner)
    '2P_3O_ind_jtf': ['ki', 'timâwâwa'],    # You ________3' (Final -t- joiner)
    '2P_3O_ind_jtbf': ['kit', 'timâwâwa'],  # You ________3' (Beginning -t- joiner, and final -t- joiner)

    '2P_3S_con': ['e', 'âyahk'],            # You are ____ing him/her/NA
    '2P_3S_con_jh': ['eh', 'âyahk'],        # You are ____ing him/her/NA (Beginning -h- joiner)
    '2P_3S_con_jtf': ['e', 'tâyahk'],       # You are ____ing him/her/NA (Final -t- joiner)
    '2P_3S_con_jht': ['eh', 'tâyahk'],      # You are ____ing him/her/NA (Beginning -h- joiner, and final -t- joiner)

    '2P_3P_con': ['e', 'âyahkik'],          # You are ____ing them/NA(pl)
    '2P_3P_con_jh': ['eh', 'âyahkik'],      # You are ____ing them/NA(pl) (Beginning -h- joiner)
    '2P_3P_con_jtf': ['e', 'tâyahkik'],     # You are ____ing them/NA(pl) (Final -t- joiner)
    '2P_3P_con_jht': ['eh', 'tâyahkik'],    # You are ____ing them/NA(pl) (Beginning -h- joiner, and final -t- joiner)

    '2P_3O_con': ['e', 'imâyahk'],          # You are ____ing 3'
    '2P_3O_con_jh': ['eh', 'imâyahk'],      # You are ____ing 3' (Beginning -h- joiner)
    '2P_3O_con_jtf': ['e', 'timâyahk'],     # You are ____ing 3' (Final -t- joiner)
    '2P_3O_con_jht': ['eh', 'timâyahk'],    # You are ____ing 3' (Beginning -h- joiner, and final -t- joiner)
}
# Set 2 direct (VTA)
# Actor/subject: 3s, 3p, 3'
# Object/goal: 3'
thirdperson_thirdobviative = {
    '3S_3O_ind': ['ew'],                    # Him/her/NA ______3'
    '3S_3O_ind_jtb': ['t', 'ew'],           # Him/her/NA ______3' (Beginning -t- joiner)
    '3S_3O_ind_jtf': ['tew'],               # Him/her/NA ______3' (Final -t- joiner)
    '3S_3O_ind_jtbf': ['t', 'tew'],         # Him/her/NA ______3' (Beginning -t- joiner, and final -t- joiner)

    '3P_3O_ind': ['ewak'],                  # Them/NA(pl) _____3'
    '3P_3O_ind_jtb': ['t', 'ewak'],         # Them/NA(pl) _____3' (Beginning -t- joiner)
    '3P_3O_ind_jtf': ['tewak'],             # Them/NA(pl) _____3' (Final -t- joiner)
    '3P_3O_ind_jtbf': ['ewak'],             # Them/NA(pl) _____3' (Beginning -t- joiner, and final -t- joiner)

    '3O_3O_ind': ['eyiwa'],                 # 3'_______________3'
    '3O_3O_ind_jtb': ['t', 'eyiwa'],        # 3'_______________3' (Beginning -t- joiner)
    '3O_3O_ind_jtf': ['teyiwa'],            # 3'_______________3' (Final -t- joiner)
    '3O_3O_ind_jtbf': ['eyiwa'],            # 3'_______________3' (Beginning -t- joiner, and final -t- joiner)

    '2S_3S_con': ['e', 'ât'],               # Him/her/NA ____ing 3'
    '2S_3S_con_jh': ['eh', 'ât'],           # Him/her/NA ____ing 3' (Beginning -h- joiner)
    '2S_3S_con_jtf': ['e', 'tât'],          # Him/her/NA ____ing 3' (Final -t- joiner)
    '2S_3S_con_jht': ['eh', 'tât'],         # Him/her/NA ____ing 3' (Beginning -h- joiner, and final -t- joiner)

    '2S_3P_con': ['e', 'âcik'],             # Them/NA(pl) ___ing 3'
    '2S_3P_con_jk': ['eh', 'âcik'],         # Them/NA(pl) ___ing 3' (Beginning -h- joiner)
    '2S_3P_con_jtf': ['e', 'tâcik'],        # Them/NA(pl) ___ing 3' (Final -t- joiner)
    '2S_3P_con_jht': ['eh', 'tâcik'],       # Them/NA(pl) ___ing 3' (Beginning -h- joiner, and final -t- joiner)

    '2S_3O_con': ['e', 'âyit'],             # 3' is/are _____ing 3'
    '2S_3O_con_jh': ['eh', 'âyit'],         # 3' is/are _____ing 3' (Beginning -h- joiner)
    '2S_3O_con_jtf': ['e', 'tâyit'],        # 3' is/are _____ing 3' (Final -t- joiner)
    '2S_3O_con_jht': ['eh', 'tâyit'],       # 3' is/are _____ing 3' (Beginning -h- joiner, and final -t- joiner)
}
# Set 3 direct (VTA)
# Actor/subject: 2s, 2p
# Object/goal: 1s, 2p
secondperson_firstperson = {
    '2P_1S_ind': ['ki', 'in'],              # You ____________ me
    '2P_1S_ind_jtf': ['kit', 'in'],         # You ____________ me (Beginning -t- joiner)

    '2S_1P_ind': ['ki', 'inân'],            # You ____________ us
    '2S_1P_ind_jtf': ['kit', 'inân'],       # You ____________ us (Beginning -t- joiner)

    '2P_1S_ind': ['ki', 'inâwâw'],          # You (pl) _______ me
    '2P_1S_ind_jtf': ['kit', 'inâwâw'],     # You (pl) _______ me (Beginning -t- joiner)
    
    '2P_1P_ind': ['ki', 'inân'],            # You (pl) _______ us
    '2P_1P_ind_jtf': ['kit', 'inân'],       # You (pl) _______ us (Beginning -t- joiner)

    '2P_1S_con': ['e', 'iyan'],             # You are ________ing me
    '2P_1S_con_jhf': ['eh', 'iyan'],        # You are ________ing me (Beginning -h- joiner)

    '2S_1P_con': ['e', 'iyâhk'],            # You are ________ing us
    '2S_1P_con_jhf': ['eh', 'iyâhk'],       # You are ________ing us (Beginning -h- joiner)

    '2P_1S_con': ['e', 'iyek'],             # You (pl) are ___ing me
    '2P_1S_con_jhf': ['eh', 'iyek'],        # You (pl) are ___ing me (Beginning -h- joiner)

    '2P_1P_con': ['e', 'iyâhk'],            # You (pl) are ___ing us
    '2P_1P_con_jhf': ['eh', 'iyâhk'],       # You (pl) are ___ing us (Beginning -h- joiner)
}

# TRANSITIVE ANIMATE // INVERSE

# Set 1 INVERSE  (VTA)
# Actor/subject: 3s, 3p, 3'
# Object/goal: 1s, 2s, 1p, 2i, 2p

thirdperson_firstpersonsingular = {
    '3S_1S_ind': ['ni', 'ik'],              # He/she/NA _______ me
    '3S_1S_ind_jtb': ['nit', 'ik'],         # He/she/NA _______ me (Beginning -t- joiner)
    '3S_1S_ind_jtf': ['ni', 'tik'],         # He/she/NA _______ me (Final -t- joiner)
    '3S_1S_ind_jtbf': ['nit', 'tik'],       # He/she/NA _______ me (Beginning -t- joiner, and final -t- joiner)

    '3P_1S_ind': ['ni', 'ikwak'],           # They/NA(pl) _____ me
    '3P_1S_ind_jtb': ['nit', 'ikwak'],      # They/NA(pl) _____ me (Beginning -t- joiner)
    '3P_1S_ind_jtf': ['ni', 'tikwak'],      # They/NA(pl) _____ me (Final -t- joiner)
    '3P_1S_ind_jtbf': ['nit', 'tikwak'],    # They/NA(pl) _____ me (Beginning -t- joiner, and final -t- joiner)

    '3O_1S_ind': ['ni', 'ikoyiwa'],         # 3' ______________ me
    '3O_1S_ind_jtb': ['nit', 'ikoyiwa'],    # 3' ______________ me (Beginning -t- joiner)
    '3O_1S_ind_jtf': ['ni', 'tikoyiwa'],    # 3' ______________ me (Final -t- joiner)
    '3O_1S_ind_jtbf': ['nit', 'tikoyiwa'],  # 3' ______________ me (Beginning -t- joiner, and final -t- joiner)

    '3S_1S_con': ['e', 'it'],               # He/she/NA ____ing me
    '3S_1S_con_jh': ['e', 'it'],            # He/she/NA ____ing me (Beginning -h- joiner)

    '3P_1S_con': ['e', 'icik'],             # They/NA(pl) __ing me
    '3P_1S_con_jh': ['e', 'icik'],          # They/NA(pl) __ing me (Beginning -h- joiner)

    '3O_1S_con': ['e', 'iyit'],             # 3' ___________ing me
    '3O_1S_con_jh': ['e', 'iyit'],          # 3' ___________ing me (Beginning -h- joiner)
}
thirdperson_firstpersonsingular = {
    '3S_2S_ind': ['ki', 'ik'],              # He/she/NA _______ you
    '3S_2S_ind_jtb': ['kit', 'ik'],         # He/she/NA _______ you (Beginning -t- joiner)
    '3S_2S_ind_jtf': ['ki', 'tik'],         # He/she/NA _______ you (Final -t- joiner)
    '3S_2S_ind_jtbf': ['kit', 'tik'],       # He/she/NA _______ you (Beginning -t- joiner, and final -t- joiner)

    '3P_2S_ind': ['ki', 'ikwak'],           # They/NA(pl) _____ you
    '3P_2S_ind_jtb': ['kit', 'ikwak'],      # They/NA(pl) _____ you (Beginning -t- joiner)
    '3P_2S_ind_jtf': ['ki', 'tikwak'],      # They/NA(pl) _____ you (Final -t- joiner)
    '3P_2S_ind_jtbf': ['kit', 'tikwak'],    # They/NA(pl) _____ you (Beginning -t- joiner, and final -t- joiner)

    '3O_2S_ind': ['ki', 'ikoyiwa'],         # 3' ______________ you
    '3O_2S_ind_jtb': ['kit', 'ikoyiwa'],    # 3' ______________ you (Beginning -t- joiner)
    '3O_2S_ind_jtf': ['ki', 'tikoyiwa'],    # 3' ______________ you (Final -t- joiner)
    '3O_2S_ind_jtbf': ['kit', 'tikoyiwa'],  # 3' ______________ you (Beginning -t- joiner, and final -t- joiner)

    '3S_2S_con': ['e', 'isk'],              # He/she/NA ____ing you
    '3S_2S_con_jh': ['eh', 'isk'],          # He/she/NA ____ing you (Beginning -h- joiner)

    '3P_2S_con': ['e', 'iskik'],            # They/NA(pl) __ing you
    '3P_2S_con_jh': ['eh', 'iskik'],        # They/NA(pl) __ing you (Beginning -h- joiner)

    '3O_2S_con': ['e', 'isk'],              # 3' ___________ing you
    '3O_2S_con_jh': ['eh', 'isk'],          # 3' ___________ing you (Beginning -h- joiner)
}
thirdperson_firstpersonsplural = {
    '3S_1S_ind': ['ni', 'ikonân'],          # He/she/NA _______ us
    '3S_1S_ind_jtb': ['nit', 'ikonân'],     # He/she/NA _______ us (Beginning -t- joiner)
    '3S_1S_ind_jtf': ['ni', 'tikonân'],     # He/she/NA _______ us (Final -t- joiner)
    '3S_1S_ind_jtbf': ['nit', 'tikonân'],   # He/she/NA _______ us (Beginning -t- joiner, and final -t- joiner)

    '3P_1S_ind': ['ni', 'ikonânak'],        # They/NA(pl) _____ us
    '3P_1S_ind_jtb': ['nit', 'ikonânak'],   # They/NA(pl) _____ us (Beginning -t- joiner)
    '3P_1S_ind_jtf': ['ni', 'tikonânak'],   # They/NA(pl) _____ us (Final -t- joiner)
    '3P_1S_ind_jtbf': ['nit', 'tikonânak'], # They/NA(pl) _____ us (Beginning -t- joiner, and final -t- joiner)

    '3O_1S_ind': ['ni', 'ikonân'],          # 3' ______________ us
    '3O_1S_ind_jtb': ['nit', 'ikonân'],     # 3' ______________ us (Beginning -t- joiner)
    '3O_1S_ind_jtf': ['ni', 'tikonân'],     # 3' ______________ us (Final -t- joiner)
    '3O_1S_ind_jtbf': ['nit', 'tikonân'],   # 3' ______________ us (Beginning -t- joiner, and final -t- joiner)

    '3S_1S_con': ['e', 'ikoyâhk'],          # He/she/NA ____ing us
    '3S_1S_con_jh': ['eh', 'ikoyâhk'],      # He/she/NA ____ing us (Beginning -h- joiner)

    '3P_1S_con': ['e', 'ikoyâhkik'],        # They/NA(pl) __ing us
    '3P_1S_con_jh': ['eh', 'ikoyâhkik'],    # They/NA(pl) __ing us (Beginning -h- joiner)

    '3O_1S_con': ['e', 'ikoyâhk'],          # 3' ___________ing us
    '3O_1S_con_jh': ['eh', 'ikoyâhk'],      # 3' ___________ing us (Beginning -h- joiner)
}
thirdperson_secondpersonsinclusive = {
    '3S_2I_ind': ['ki', 'ikonaw'],          # He/she/NA _______ us
    '3S_2I_ind_jtb': ['kit', 'ikonaw'],     # He/she/NA _______ us (Beginning -t- joiner)
    '3S_2I_ind_jtf': ['ki', 'tikonaw'],     # He/she/NA _______ us (Final -t- joiner)
    '3S_2I_ind_jtbf': ['kit', 'tikonaw'],   # He/she/NA _______ us (Beginning -t- joiner, and final -t- joiner)

    '3P_2I_ind': ['ki', 'ikonawak'],        # They/NA(pl) _____ us
    '3P_2I_ind_jtb': ['kit', 'ikonawak'],   # They/NA(pl) _____ us (Beginning -t- joiner)
    '3P_2I_ind_jtf': ['ki', 'tikonawak'],   # They/NA(pl) _____ us (Final -t- joiner)
    '3P_2I_ind_jtbf': ['kit', 'tikonawak'], # They/NA(pl) _____ us (Beginning -t- joiner, and final -t- joiner)

    '3O_2I_ind': ['ki', 'ikonaw'],          # 3' ______________ us
    '3O_2I_ind_jtb': ['kit', 'ikonaw'],     # 3' ______________ us (Beginning -t- joiner)
    '3O_2I_ind_jtf': ['ki', 'tikonaw'],     # 3' ______________ us (Final -t- joiner)
    '3O_2I_ind_jtbf': ['kit', 'tikonaw'],   # 3' ______________ us (Beginning -t- joiner, and final -t- joiner)

    '3S_1S_con': ['e', 'ikoyahk'],          # He/she/NA ____ing us
    '3S_1S_con_jh': ['eh', 'ikoyahk'],      # He/she/NA ____ing us (Beginning -h- joiner)

    '3P_1S_con': ['e', 'ikoyahkik'],        # They/NA(pl) __ing us
    '3P_1S_con_jh': ['eh', 'ikoyahkik'],    # They/NA(pl) __ing us (Beginning -h- joiner)

    '3O_1S_con': ['e', 'ikoyahk'],          # 3' ___________ing us
    '3O_1S_con_jh': ['eh', 'ikoyahk'],      # 3' ___________ing us (Beginning -h- joiner)
}
thirdperson_secondpersonsplural = {
    '3S_2P_ind': ['ki', 'ikowâw'],          # He/she/NA _______ you
    '3S_2P_ind_jtb': ['kit', 'ikowâw'],     # He/she/NA _______ you (Beginning -t- joiner)
    '3S_2P_ind_jtf': ['ki', 'tikowâw'],     # He/she/NA _______ you (Final -t- joiner)
    '3S_2P_ind_jtbf': ['kit', 'tikowâw'],   # He/she/NA _______ you (Beginning -t- joiner, and final -t- joiner)

    '3P_2P_ind': ['ki', 'ikowâwak'],        # They/NA(pl) _____ you
    '3P_2P_ind_jtb': ['kit', 'ikowâwak'],   # They/NA(pl) _____ you (Beginning -t- joiner)
    '3P_2P_ind_jtf': ['ki', 'tikowâwak'],   # They/NA(pl) _____ you (Final -t- joiner)
    '3P_2P_ind_jtbf': ['kit', 'tikowâwak'], # They/NA(pl) _____ you (Beginning -t- joiner, and final -t- joiner)

    '3O_2P_ind': ['ki', 'ikowâw'],          # 3' ______________ you (pl)
    '3O_2P_ind_jtb': ['kit', 'ikowâw'],     # 3' ______________ you (pl) (Beginning -t- joiner)
    '3O_2P_ind_jtf': ['ki', 'tikowâw'],     # 3' ______________ you (pl) (Final -t- joiner)
    '3O_2P_ind_jtbf': ['kit', 'tikowâw'],   # 3' ______________ you (pl) (Beginning -t- joiner, and final -t- joiner)

    '3S_2P_con': ['e', 'ikoyek'],           # He/she/NA ____ing you
    '3S_2P_con_jh': ['eh', 'ikoyek'],       # He/she/NA ____ing you (Beginning -h- joiner)

    '3P_2P_con': ['e', 'ikoyekok'],         # They/NA(pl) __ing you
    '3P_2P_con_jh': ['eh', 'ikoyekok'],     # They/NA(pl) __ing you (Beginning -h- joiner)

    '3O_2P_con': ['e', 'ikoyek'],           # 3' ___________ing you
    '3O_2P_con_jh': ['eh', 'ikoyek'],       # 3' ___________ing you (Beginning -h- joiner)
}

# Set 2 INVERSE (VTA)
# Actor/subject: 3'
# Object/goal: 3s, 3p, 3'

thirdperson_thirdobviative = {
    '3O_3S_ind': ['ik'],                    # 3'______Him/her/NA
    '3O_3S_ind_jtf': ['tik'],               # 3'______Him/her/NA (Final -t- joiner)

    '3O_3P_ind': ['ikwak'],                 # 3' _____Them/NA(pl)
    '3O_3P_ind_jtf': ['tikwak'],            # 3' _____Them/NA(pl) (Final -t- joiner)

    '3O_3O_ind': ['ikoyiwa'],               # 3'_______________3'
    '3O_3O_ind_jtf': ['tikoyiwa'],          # 3'_______________3' (Final -t- joiner)

    '3O_3S_con': ['e', 'ikot'],             # 3' is/are __ing him/her/NA
    '3O_3S_con_jh': ['eh', 'ikot'],         # 3' is/are __ing him/her/NA (Beginning -h- joiner)
    '3O_3S_con_jtf': ['e', 'tikot'],        # 3' is/are __ing him/her/NA (Final -t- joiner)
    '3O_3S_con_jht': ['eh', 'tikot'],       # 3' is/are __ing him/her/NA (Beginning -h- joiner, and final -h- joiner)

    '3O_3P_con': ['e', 'ikocik'],           # 3' is/are __ing them/NA(pl)
    '3O_3P_con_jh': ['eh', 'ikocik'],       # 3' is/are __ing them/NA(pl) (Beginning -h- joiner)
    '3O_3P_con_jtf': ['e', 'tikocik'],      # 3' is/are __ing them/NA(pl) (Final -t- joiner)
    '3O_3P_con_jht': ['eh', 'tikocik'],     # 3' is/are __ing them/NA(pl) (Beginning -h- joiner, and final -h- joiner)

    '3O_3O_con': ['e', 'ikoyit'],           # 3' is/are ___ing 3'
    '3O_3O_con_jh': ['eh', 'ikoyit'],       # 3' is/are ___ing 3' (Beginning -h- joiner)
    '3O_3O_con_jtf': ['e', 'tikoyit'],      # 3' is/are ___ing 3' (Final -t- joiner)
    '3O_3O_con_jht': ['eh', 'tikoyit'],     # 3' is/are ___ing 3' (Beginning -h- joiner, and final -h- joiner)
}

# Set 3 INVERSE (VTA)
# Actor/subject: 1s, 2p
# Object/goal: 2s, 2p 
# Rules:
#       - final 'w' drops, preceding voewl is lengthened
#       - two vowles cannot be joined together, therfore the vowel in the suffix is deleted
#       - Rule applies to both modes

secondperson_firstperson = {
    '1S_2S_ind': ['ki', 'itin'],            # I ____________ you
    '1S_2S_ind_jtb': ['kit', 'itin'],       # I ____________ you (Beginning -t- joiner)
    '1S_2S_ind_jtf': ['ki', 'titin'],       # I ____________ you (Final -t- joiner)
    '1S_2S_ind_jtbf': ['kit', 'titin'],     # I ____________ you (Beginning -t- joiner, and final -t- joiner)
    '1S_2S_ind_vca': ['ki', 'âtin'],        # I ____________ you (â vowel change)
    '1S_2S_ind_vci': ['ki', 'îtin'],        # I ____________ you (î vowel change)
    '1S_2S_ind_vco': ['ki', 'ôtin'],        # I ____________ you (ô vowel change)
    '1S_2S_ind_jtb_vca': ['kit', 'âtin'],   # I ____________ you (Beginning -t- joiner, and â vowel change)
    '1S_2S_ind_jtb_vci': ['kit', 'îtin'],   # I ____________ you (Beginning -t- joiner, and î vowel change)
    '1S_2S_ind_jtb_vco': ['kit', 'ôtin'],   # I ____________ you (Beginning -t- joiner, and ô vowel change)


    '1P_2S_ind': ['ki', 'itinân'],          # We ___________ you
    '1P_2S_ind_jtb': ['kit', 'itinân'],          # We ___________ you (Beginning -t- joiner)
    '1P_2S_ind_jtf': ['ki', 'titinân'],     # We ___________ you (Final -t- joiner)
    '1P_2S_ind_jtbf': ['kit', 'titinân'],          # We ___________ you (Beginning -t- joiner, and final -t- joiner)
    '1P_2S_ind_vca': ['ki', 'âtinân'],       # We ___________ you (â vowel change)
    '1P_2S_ind_vci': ['ki', 'îtinân'],       # We ___________ you (î vowel change)
    '1P_2S_ind_vco': ['ki', 'ôtinân'],       # We ___________ you (ô vowel change)
    '1P_2S_ind_vca': ['ki', 'âtinân'],       # We ___________ you (Beginning -t- joiner, and â vowel change)
    '1P_2S_ind_vci': ['ki', 'îtinân'],       # We ___________ you (Beginning -t- joiner, and î vowel change)
    '1P_2S_ind_vco': ['ki', 'ôtinân'],       # We ___________ you (Beginning -t- joiner, and ô vowel change)

    '1S_2P_ind': ['ki', 'itinâwâw'],        # I ____________ you (pl)
    '1S_2P_ind_jtf': ['ki', 'titinâwâw'],    # I ____________ you (pl) (Final -t- joiner)
    '1S_2P_ind_vc': ['ki', 'âtinâwâw'],     # I ____________ you (pl) (vowel change)

    '1P_2P_ind': ['ki', 'titinân'],         # We ___________ you (pl)
    '1P_2P_ind_jtf': ['ki', 'itinân'],       # We ___________ you (pl) (Final -t- joiner)
    '1P_2P_ind_vc': ['ki', 'âtinân'],       # We ___________ you (pl) (vowel change)

    '1S_2S_con': ['e', 'itân'],             # I am _________ing you
    '1S_2S_con_jtf': ['e', 'itân'],          # I am _________ing you (Final -t- joiner)
    '1S_2S_con_vc': ['e', 'âtân'],          # I am _________ing you (vowel change)

    '1P_2P_con': ['e', 'itâhk'],            # We are _______ing you
    '1P_2P_con_jtf': ['e', 'itâhk'],         # We are _______ing you (Final -t- joiner)
    '1P_2P_con_vc': ['e', 'âtâhk'],         # We are _______ing you (vowel change)

    '1S_2P_con': ['e', 'itakok'],           # I am _________ing you (pl)
    '1S_2P_con_jtf': ['e', 'itakok'],        # I am _________ing you (pl) (Final -t- joiner)
    '1S_2P_con_vc': ['e', 'âtakok'],        # I am _________ing you (pl) (vowel change)

    '1P_2P_con': ['e', 'itâhk'],            # We are _______ing you (pl)
    '1P_2P_con_jtf': ['e', 'itâhk'],         # We are _______ing you (pl) (Final -t- joiner)
    '1P_2P_con_vc': ['e', 'âtâhk'],         # We are _______ing you (pl) (vowel change)
}

# TRANSITIVE ANIMATE // Subjunctive mode // Direct

# Set 1 - Direct - SUBJUNCTIVE (VTA)
# Actor/subject: 1st's and 2nd's
# Object/goal: 3rd persons

sub_firstpersonsingular_thirdperson = {
    '1S_3S_ind': ['aki'],                   # If I _________him/her/NA
    '1S_3S_ind_jtf': ['taki'],               # If I _________him/her/NA (Final -t- joiner)
    '1S_3P_ind': ['akwâwi'],                # If I _________they/NA(pl)
    '1S_3P_ind_jtf': ['takwâwi'],            # If I _________they/NA(pl) (Final -t- joiner)
    '1S_3O_ind': ['imaki'],                 # If I _________3'
    '1S_3O_ind_jtf': ['timaki'],             # If I _________3' (Final -t- joiner)

    '1S_3S_con': ['kâ', 'ak'],              # When I am ____ing him/her/NA
    '1S_3S_con_jtf': ['kâ', 'tak'],          # When I am ____ing him/her/NA (Final -t- joiner)
    '1S_3P_con': ['kâ', 'akik'],            # When I am ____ing them/NA(pl)
    '1S_3P_con_jtf': ['kâ', 'takik'],        # When I am ____ing them/NA(pl) (Final -t- joiner)
    '1S_3O_con': ['kâ', 'imak'],            # When I am ____ing 3'
    '1S_3O_con_jtf': ['kâ', 'timak'],        # When I am ____ing 3' (Final -t- joiner)
}

sub_secondpersonsingular_thirdperson = {
    '2S_3S_ind': ['aci'],                   # If you ________him/her/NA
    '2S_3S_ind_jtf': ['taci'],               # If you ________him/her/NA (Final -t- joiner)
    '2S_3P_ind': ['atwâwi'],                # If you ________they/NA(pl)
    '2S_3P_ind_jtf': ['tatwâwi'],            # If you ________they/NA(pl) (Final -t- joiner)
    '2S_3O_ind': ['imaci'],                 # If you ________3'
    '2S_3O_ind_jtf': ['timaci'],             # If you ________3' (Final -t- joiner)

    '2S_3S_con': ['kâ', 'at'],              # When you are ____ing him/her/NA
    '2S_3S_con_jtf': ['kâ', 'tat'],          # When you are ____ing him/her/NA (Final -t- joiner)
    '2S_3P_con': ['kâ', 'acik'],            # When you are ____ing them/NA(pl)
    '2S_3P_con_jtf': ['kâ', 'tacik'],        # When you are ____ing them/NA(pl) (Final -t- joiner)
    '2S_3O_con': ['kâ', 'imat'],            # When you are ____ing 3'
    '2S_3O_con_jtf': ['kâ', 'timat'],        # When you are ____ing 3' (Final -t- joiner)
}
sub_firstpersonplural_thirdperson = {
    '1P_3S_ind': ['âyâhki'],                # If we ________him/her/NA
    '1P_3S_ind_jtf': ['tâyâhki'],            # If we ________him/her/NA (Final -t- joiner)
    '1P_3P_ind': ['âyâhkwâwi'],             # If we ________they/NA(pl)
    '1P_3P_ind_jtf': ['tâyâhkwâwi'],         # If we ________they/NA(pl) (Final -t- joiner)
    '1P_3O_ind': ['imâyâhki'],              # If we ________3'
    '1P_3O_ind_jtf': ['timâyâhki'],          # If we ________3' (Final -t- joiner)

    '1P_3S_con': ['kâ', 'âyâhk'],           # When we are ____ing him/her/NA
    '1P_3S_con_jtf': ['kâ', 'tâyâhk'],       # When we are ____ing him/her/NA (Final -t- joiner)
    '1P_3P_con': ['kâ', 'âyâhkik'],         # When we are ____ing them/NA(pl)
    '1P_3P_con_jtf': ['kâ', 'tâyâhkik'],     # When we are ____ing them/NA(pl) (Final -t- joiner)
    '1P_3O_con': ['kâ', 'imâyâhk'],         # When we are ____ing 3'
    '1P_3O_con_jtf': ['kâ', 'timâyâhk'],     # When we are ____ing 3' (Final -t- joiner)
}
sub_secondpersoninclusive_thirdperson = {
    '2I_3S_ind': ['âyâhki'],                # If we ________him/her/NA
    '2I_3S_ind_jtf': ['tâyâhki'],            # If we ________him/her/NA (Final -t- joiner)
    '2I_3P_ind': ['âyâhkwâwi'],             # If we ________they/NA(pl)
    '2I_3P_ind_jtf': ['tâyâhkwâwi'],         # If we ________they/NA(pl) (Final -t- joiner)
    '2I_3O_ind': ['imâyâhki'],              # If we ________3'
    '2I_3O_ind_jtf': ['timâyâhki'],          # If we ________3' (Final -t- joiner)

    '2I_3S_con': ['kâ', 'âyâhk'],           # When we are ____ing him/her/NA
    '2I_3S_con_jtf': ['kâ', 'âyâhk'],        # When we are ____ing him/her/NA (Final -t- joiner)
    '2I_3P_con': ['kâ', 'âyâhkwâw'],        # When we are ____ing them/NA(pl)
    '2I_3P_con_jtf': ['kâ', 'âyâhkwâw'],     # When we are ____ing them/NA(pl) (Final -t- joiner)
    '2I_3O_con': ['kâ', 'imâyâhk'],         # When we are ____ing 3'
    '2I_3O_con_jtf': ['kâ', 'imâyâhk'],      # When we are ____ing 3' (Final -t- joiner)
}
sub_secondpersonplural_thirdperson = {
    '2P_3S_ind': ['âyeko'],                 # If we ________him/her/NA
    '2P_3S_ind_jtf': ['tâyeko'],             # If we ________him/her/NA (Final -t- joiner)
    '2P_3P_ind': ['âyekwâwi'],              # If we ________they/NA(pl)
    '2P_3P_ind_jtf': ['tâyekwâwi'],          # If we ________they/NA(pl) (Final -t- joiner)
    '2P_3O_ind': ['imâyeko'],               # If we ________3'
    '2P_3O_ind_jtf': ['timâyeko'],           # If we ________3' (Final -t- joiner)

    '2P_3S_con': ['kâ', 'âyek'],            # When we are ____ing him/her/NA
    '2P_3S_con_jtf': ['kâ', 'tâyek'],        # When we are ____ing him/her/NA (Final -t- joiner)
    '2P_3P_con': ['kâ', 'âyekok'],          # When we are ____ing them/NA(pl)
    '2P_3P_con_jtf': ['kâ', 'tâyekok'],      # When we are ____ing them/NA(pl) (Final -t- joiner)
    '2P_3O_con': ['kâ', 'imâyek'],          # When we are ____ing 3'
    '2P_3O_con_jtf': ['kâ', 'timâyek'],      # When we are ____ing 3' (Final -t- joiner)
}

# Set 2 - Direct - SUBJUNCTIVE (VTA)
# Actor/subject: 3rd's
# Object/goal: 3'
sub_thirdperson_thirdperson = {
    '3S_3O_ind': ['imâci'],                 # If him/her/NA ______ 3'
    '3S_3O_ind_jtf': ['imâci'],              # If him/her/NA ______ 3' (Final -t- joiner)
    '3P_3O_ind': ['imâtwâwi'],              # If them/NA(pl) _____ 3'
    '3P_3O_ind_jtf': ['imâtwâwi'],           # If them/NA(pl) _____ 3' (Final -t- joiner)
    '3O_3O_ind': ['imâyici'],               # 3'_______________3'
    '3O_3O_ind_jtf': ['imâyici'],            # 3'_______________3' (Final -t- joiner)

    '3S_3O_con': ['kâ', 'imât'],            # When him/her/NA is __ing 3'
    '3S_3O_con_jtf': ['kâ', 'timât'],        # When him/her/NA is __ing 3' (Final -t- joiner)
    '3P_3O_con': ['kâ', 'imâcik'],          # When they/NA(pl) are __ing
    '3P_3O_con_jtf': ['kâ', 'timâcik'],      # When they/NA(pl) are __ing (Final -t- joiner)
    '3O_3O_con': ['kâ', 'imâyit'],          # When 3' is/are ___ing 3'
    '3O_3O_con_jtf': ['kâ', 'timâyit'],      # When 3' is/are ___ing 3' (Final -t- joiner)
}

# Set 3 - Direct - SUBJUNCTIVE (VTA)
# Actor/subject: 2nd's
# Object/goal: 1st's
secondperson_firstperson = {
    '2S_1S_ind': ['iyani'],                 # If you _____________ me
    '2S_1P_ind': ['iyâhki'],                # If you _____________ us
    '2P_1S_ind': ['iyeko'],                 # If you (pl) ________ me
    '2P_1P_ind': ['iyâhki'],                # If you (pl) ________ us


    '2S_1S_con': ['kâ', 'iyan'],            # When you are ________ing me
    '2S_1P_con': ['kâ', 'iyâhk'],           # When you are ________ing you 
    '2P_1S_con': ['kâ', 'iyek'],            # When you (pl) are ___ing you
    '2P_1P_con': ['kâ', 'iyâhk'],           # When you (pl) are ___ing you 
}

# TRANSITIVE ANIMATE // SUBJUNCTIVE MODE // INVERSE

# Set 1 - Inverse - SUBJUNCTIVE(VTA)
# Actor/subject: 3S, 3P, 3'
# Object/goal: 1st's and 2nd's

sub_thirdperson_firstpersonsingular = {
    '3S_1S_ind': ['ici'],                   # If he/she/NA (pl) _________ me
    '3S_1S_ind_jtf': ['tici'],               # If he/she/NA (pl) _________ me (Final -t- joiner)
    '3P_1S_ind': ['atwâwi'],                # If they/NA(pl) ____________ me
    '3P_1S_ind_jtf': ['tatwâwi'],            # If they/NA(pl) ____________ me (Final -t- joiner)
    '3O_1S_ind': ['iyici'],                 # If 3' _____________________ me
    '3O_1S_ind_jtf': ['tiyici'],             # If 3' _____________________ me (Final -t- joiner)

    '3S_1S_con': ['kâ', 'it'],              # When he/she/NA _________ing me
    '3P_1S_con': ['kâ', 'icik'],            # When they/NA(PL) are____ing me
    '3O_1S_con': ['kâ', 'iyit'],            # When 3' is/are _________ing me
}
sub_thirdperson_secondpersonsingular = {
    '3S_2S_ind': ['iski'],                  # If he/she/NA ____________ you
    '3S_2S_ind_jtf': ['tiski'],              # If he/she/NA ____________ you (Final -t- joiner)
    '3P_2S_ind': ['iskwâwi'],               # If they/NA(pl) __________ you
    '3P_2S_ind_jtf': ['tiskwâwi'],           # If they/NA(pl) __________ you (Final -t- joiner)
    '3O_2S_ind': ['iski'],                  # If 3' ___________________ you
    '3O_2S_ind_jtf': ['tiski'],              # If 3' ___________________ you (Final -t- joiner)

    '3S_2S_con': ['kâ', 'isk'],             # When he/she/NA _______ing you
    '3P_2S_con': ['kâ', 'iskik'],           # When they/NA(PL) are__ing you
    '3O_2S_con': ['kâ', 'isk'],             # When 3' is/are _______ing you
}
sub_thirdperson_firstpersonplural = {
    '3S_1P_ind': ['ikoyâhki'],              # If he/she/NA ____________ us
    '3S_1P_ind_jtf': ['tikoyâhki'],          # If he/she/NA ____________ us (Final -t- joiner)
    '3P_1P_ind': ['ikoyâhkwâwi'],           # If they/NA(PL) are_______ us
    '3P_1P_ind_jtf': ['tikoyâhkwâwi'],       # If they/NA(PL) are_______ us (Final -t- joiner)
    '3O_1P_ind': ['ikoyâhki'],              # If 3' is/are ____________ us
    '3O_1P_ind_jtf': ['tikoyâhki'],          # If 3' is/are ____________ us (Final -t- joiner)

    '3S_1P_con': ['kâ', 'ikoyâhk'],         # When he/she/NA _______ing us
    '3P_1P_con': ['kâ', 'ikoyâhkik'],       # When they/NA(PL) are__ing us
    '3O_1P_con': ['kâ', 'ikoyâhk'],         # When 3' is/are _______ing us
}
sub_thirdperson_secondpersoninclusive = {
    '3S_2I_ind': ['ikoyahki'],              # If he/she/NA ____________ us
    '3S_2I_ind_jtf': ['tikoyahki'],          # If he/she/NA ____________ us (Final -t- joiner)
    '3P_2I_ind': ['ikoyahkwâwi'],           # If they/NA (pl) _________ us
    '3P_2I_ind_jtf': ['tikoyahkwâwi'],       # If they/NA (pl) _________ us (Final -t- joiner)
    '3O_2I_ind': ['ikoyahki'],              # If 3' ___________________ us
    '3O_2I_ind_jtf': ['tikoyahki'],          # If 3' ___________________ us (Final -t- joiner)

    '3S_2I_con': ['kâ', 'ikoyek'],          # When he/she/NA _______ing us
    '3P_2I_con': ['kâ', 'ikoyekok'],        # When they/NA(PL) are__ing us
    '3O_2I_con': ['kâ', 'ikoyek'],          # When 3' is/are _______ing us
}
sub_thirdperson_secondpersonplural = {
    '3S_2P_ind': ['ikoyeko'],               # If he/she/NA _______ you (pl)
    '3S_2P_ind_jtf': ['tikoyeko'],           # If he/she/NA _______ you (pl) (Final -t- joiner)
    '3P_2P_ind': ['ikoyekwâwi'],            # If they/NA _________ you (pl)
    '3P_2P_ind_jtf': ['tikoyekwâwi'],        # If they/NA _________ you (pl) (Final -t- joiner)
    '3O_2P_ind': ['ikoyeko'],               # If 3' ______________ you (pl)
    '3O_2P_ind_jtf': ['tikoyeko'],           # If 3' ______________ you (pl) (Final -t- joiner)

    '3S_2P_con': ['kâ', 'ikoyek'],          # When he/she/NA is __ing you (pl)
    '3P_2P_con': ['kâ', 'ikoyekok'],        # When they/NA are ___ing them/NA( pl)
    '3O_2P_con': ['kâ', 'ikoyek'],          # When 3' is/are _____ing you (pl)
}

# Set 2 - Inverse - Subjunctive (VTA)
# Actor/subject: 3rd's
# Object/goal: 3'
sub_thirdperson_thirdperson = {
    '3O_3S_ind': ['ikoci'],                 # If 3'______ him/her/NA
    '3O_3S_ind_jtf': ['tikoci'],             # If 3'______ him/her/NA (Final -t- joiner)
    '3O_3P_ind': ['ikotwâwi'],              # If 3' _____ them/NA(pl)
    '3O_3P_ind_jtf': ['tikotwâwi'],          # If 3' _____ them/NA(pl) (Final -t- joiner)
    '3O_3O_ind': ['ikoyici'],               # If 3'________________3'
    '3O_3O_ind_jtf': ['tikoyici'],           # If 3'________________3' (Final -t- joiner)

    '3O_3S_con': ['kâ', 'ikot'],            # When 3' is/are __ing him/her/NA
    '3O_3S_con_jtf': ['kâ', 'tikot'],        # When 3' is/are __ing him/her/NA (Final -t- joiner)
    '3O_3P_con': ['kâ', 'ikocik'],          # When 3' is/are __ing them/NA(pl)
    '3O_3P_con_jtf': ['kâ', 'tikocik'],      # When 3' is/are __ing them/NA(pl) (Final -t- joiner)
    '3O_3O_con': ['kâ', 'ikoyit'],          # When 3' is/are ___ing 3'
    '3O_3O_con_jtf': ['kâ', 'tikoyit'],      # When 3' is/are ___ing 3' (Final -t- joiner)
}

# Set 3 - Inverse - Subjunctive (VTA)
# Actor/subject: 1st's
# Object/goal: 2nd's
firstperson_secondperson = {
    '1S_2S_ind': ['itâni'],                 # If I _______________ you
    '1S_2S_ind_jtf': ['titâni'],             # If I _______________ you (Final -t- joiner)
    '1P_2S_ind': ['itâhki'],                # If we ______________ you
    '1P_2S_ind_jtf': ['titâhki'],            # If we ______________ you (Final -t- joiner)
    '1S_2P_ind': ['itakwâwi'],              # If I _______________ you (pl)
    '1S_2P_ind_jtf': ['titakwâwi'],          # If I _______________ you (pl) (Final -t- joiner)
    '1P_2P_ind': ['itâhki'],                # If we ______________ you (pl)
    '1P_2P_ind_jtf': ['titâhki'],            # If we ______________ you (pl) (Final -t- joiner)

    '1S_2S_con': ['kâ', 'itân'],            # When I am ________ing me
    '1S_2S_con_jtf': ['kâ', 'titân'],        # When I am ________ing me (Final -t- joiner)
    '1P_2S_con': ['kâ', 'itâhk'],           # When we are _____ing you
    '1P_2S_con_jtf': ['kâ', 'titâhk'],       # When we are _____ing you (Final -t- joiner)
    '2P_1S_con': ['kâ', 'itakok'],          # When I am _______ing you (pl)
    '2P_1S_con_jtf': ['kâ', 'titakok'],      # When I am _______ing you (pl) (Final -t- joiner)
    '2P_1P_con': ['kâ', 'itâhk'],           # When we are _____ing you (pl)
    '2P_1P_con_jtf': ['kâ', 'titâhk'],       # When we are _____ing you (pl) (Final -t- joiner)
}

# INANIMATE INTRANSITIVE (VII)

# Inanimate intransitive verbs descrive inanimate nouns (ni)
# Rules:
#       - Final -w is dropped execpt for O and OP independent mode
#       - Final -n is dropped for O and OP in conjunct mode and the pre-asporated 'h' is used
#       - Final consonant is dropped for O and OP in conjunct mode
VII_paradigm = {
    'O_ind': [''],                          # It (NIsg) is __________ 

    'O_con': ['e', 'k'],                    # It is being ___________
    'O_con': ['e', 'hk'],                   # It is being ___________

    'OP_ind': ['a'],                        # They (NIsg) are _______
    'OP_ind': ['wa'],                       # They (NIsg) are _______
  
    'OP_con': ['e', 'ki'],                  # They are being ________
    'OP_con': ['e', 'hki'],                 # They are being ________

    'OO_ind': ['yiw'],                      # His/her (NIsg) is _____
    'OO_ind': ['iyiw'],                     # His/her (NIsg) is _____

    'OO_con': ['e', 'yik'],                 # 3S' NI is being _______
    'OO_con': ['e', 'iyik'],                # 3S' NI is being _______
 
    'OOP_ind': ['yiwa'],                    # His/her (NIsg) are ____
    'OOP_ind': ['iyiwa'],                   # His/her (NIsg) are ____

    'OOP_con': ['e', 'yiki'],               # 3S' NI's are being ____
    'OOP_con': ['e', 'iyiki'],              # 3S' NI's are being ____  
}
