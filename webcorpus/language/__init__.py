"""
Copyright © Divyanshu Kakwani 2019, all rights reserved
"""

import string
import unicodedata as ud

LC_NAME = {
    "as": "assamese",
    "bd": "bodo",
    "bn": "bengali",
    "bh": "bihari",
    "en": "english",
    "gu": "gujarati",
    "hi": "hindi",
    "kn": "kannada",
    "ks": "kashmiri",
    "ml": "malayalam",
    "mr": "marathi",
    "ne": "nepali",
    "or": "oriya",
    "pa": "punjabi",
    "sa": "sanskrit",
    "sd": "sindhi",
    "ta": "tamil",
    "te": "telugu",
    "ur": "urdu",
}


LC_SCRIPT = {
    "hi": "devanagari",
    "kn": "kannada",
    "mr": "devanagari",
    "te": "telugu",
    "ta": "tamil",
    "gu": "gujarati",
    "or": "oriya",
    "bn": "bengali",
    "ml": "malayalam",
    "ne": "devanagari",
    "pa": "gurmukhi",
    "as": "bengali",
    "en": "latin",
    "ur": "arabic",
    "bd": "devanagari",
    "san": "ol chiki",
    "dg": "dogra",
    "mni": "meitei",
}


SCRIPT_DIGITS = {
    "devanagari": "०१२३४५६७८९",
    "gujarati": "૦૧૨૩૪૫૬૭૮૯",
    "telugu": "౦౧౨౩౪౫౬౭౮౯",
    "bengali": "০১২৩৪৫৬৭৮৯",
    "malayalam": "൦൧൨൩൪൫൬൭൮൯",
    "tamil": "௦௧௨௩௪௫௬௭௮௯௰",
    "kannada": "೦೧೨೩೪೫೬೭೮",
    "oriya": "୦୧୨୩୪୫୬୭୮୯",
    "gurmukhi": "੦੧੨੩੪੫੬੭੮੯",
    "latin": "0123456789",
    "urdu": "٠١٢٣٤٥٦٧٨٩٪",
}

dogri = ""
manipuri = (
    "ꯀꯁꯂꯃꯄꯅꯆꯇꯈꯉꯊꯋꯌꯍꯎꯏꯐꯑꯒꯓꯔꯕꯖꯗꯘꯙꯚꯛꯜꯝꯞꯟꯠꯡꯢꯣꯤꯥꯦꯧꯨꯩꯪ꯫꯬꯭꯰꯱꯲꯳꯴꯵꯶꯷꯸꯹ꫠꫡꫢꫣꫤꫥꫦꫧꫨꫩꫪꫫꫬꫭꫮꫯ꫰꫱ꫲꫳꫴꫵ"
)
santhali = "᱐᱑᱒᱓᱔᱕᱖᱗᱘᱙ᱚᱛᱜᱝᱞᱟᱠᱡᱢᱣᱤᱥᱦᱧᱨᱩᱪᱫᱬᱭᱮᱯᱰᱱᱲᱳᱴᱵᱶᱷᱸᱹᱺᱻᱼᱽ᱾᱿"


def name2code(lang):
    for k, v in LC_NAME.items():
        if v.lower() == lang.lower():
            return k
    return None


def code2script(iso_code):
    iso_code = iso_code.lower()
    for c, s in LC_SCRIPT.items():
        if c == iso_code:
            return s.lower()
    return None


def in_script(char, script_name):
    if char == "।" or char.isspace() or char in string.punctuation:
        return True
    try:
        if script_name not in ud.name(char).lower():
            return False
    except:
        if char in santhali:
            return True
        elif char in dogri:
            return True
        elif char in manipuri:
            return True
        return False
    return True
