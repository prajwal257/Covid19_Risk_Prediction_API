impor: str
from xmlrpc.client import boolean
from pydantic import BaseModel

class patient_details(BaseModel):
    sex: str
    age: str
    height: float
    weight: float
    blood_type: str
    race: str
    smoking: str
    public_transport_count: float
    working: str
    worried: float
    covid19_positive: int
    covid19_symptoms: int
    covid19_contact: int
    asthma: int
    kidney_disease: int
    liver_disease: int
    compromised_immune: int
    heart_disease: int
    lung_disease: int
    diabetes: int
    hiv_positive: int
    hypertension: int
    other_chronic: int
    nursing_home: int
    health_worker: int
    country_name: str


country_coded = {
    'United States': 88,
    'Netherlands': 58,
    'Brazil': 11,
    'Switzerland': 81,
    'Spain': 79,
    'Australia': 5,
    'Russia': 72,
    'Japan': 43,
    'Malta': 51,
    'Britain': 12,
    'NewZealand': 59,
    'Pakistan': 62,
    'Chile': 16,
    'Ireland': 40,
    'Ukraine': 86,
    'Canada': 14,
    'India': 36,
    'Belgium': 8,
    'Bhutan': 9,
    'Hungary': 35,
    'Mexico': 53,
    'Greece': 31,
    'Italy': 42,
    'Germany': 30,
    'Singapore': 74,
    'Hong Kong': 34,
    'Egypt': 24,
    'Serbia': 73,
    'Peru': 65,
    'France': 28,
    'Colombia': 17,
    'Palestine': 63,
    'Dominican Republic': 22,
    'Sweden': 80,
    'North Macedonia': 60,
    'Portugal': 68,
    'Thailand': 82,
    'Romania': 71,
    'Philippines': 66,
    'Lithuania': 47,
    'Argentina': 2,
    'Denmark': 21,
    'Georgia': 29,
    'Ecuador': 23,
    'South Africa': 77,
    'Panama': 64,
    'Armenia': 3,
    'Turkey': 84,
    'Bangladesh': 7,
    'Algeria': 0,
    'Qatar': 70,
    'Iraq': 39,
    'Israel': 41,
    'Indonesia': 37,
    'United Arab Emirates': 87,
    'Guatemala': 32,
    'Czechia': 20,
    'Iran': 38,
    'Kazakhstan': 44,
    'Bulgaria': 13,
    'Norway': 61,
    'Austria': 6,
    'Moldova': 54,
    'Slovakia': 75,
    'Honduras': 33,
    'Ethiopia': 26,
    'El Salvador': 25,
    'Poland': 67,
    'Macao': 49,
    'Croatia': 19,
    'The Bahamas': 83,
    'Costa Rica': 18,
    'Slovenia': 76,
    'Andorra': 1,
    'Luxembourg': 48,
    'Bosnia': 10,
    'South Korea': 78,
    'Nepal': 57,
    'Mauritius': 52,
    'Puerto Rico': 69,
    'Finland': 27,
    'Mozambique': 55,
    'U.S. Virgin Islands': 85,
    'Malaysia': 50,
    'Latvia': 46,
    'Aruba': 4,
    'Myanmar': 56,
    'Cayman Islands': 15,
    'Kenya': 45,
}

age_coded = {
    '50_60': 6,
    '80_90': 9,
    '20_30': 3,
    '90_100': 10,
    '30_40': 4,
    '40_50': 5,
    '60_70': 7,
    '10_20': 2,
    '70_80': 8,
    '0_10': 0,
    '100_110': 1,
}

blood_type_coded = {
    'ap': 3,
    'op': 7,
    'abp': 1,
    'bp': 5,
    'on': 6,
    'an': 2,
    'abn': 0,
    'bn': 4,
}

gender_coded={
    'male': 1,
    'female': 0,
    'other': 2,
}

race_coded={
    'white': 6,
    'mixed': 4,
    'blank': 2,
    'black': 1,
    'asian': 0,
    'hispanic': 3,
    'other': 5,
}

smoking_coded={
    'never': 0,
    'quit5': 3,
    'quit0': 1,
    'quit10': 2,
    'yesheavy': 5,
    'vape': 4,
    'yesmedium': 7,
    'yeslight': 6,
}

working_coded={
    'stopped': 2,
    'home': 0,
    'travel non critical': 4,
    'travel critical': 3,
    'never': 1,
}