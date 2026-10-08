import random
from typing import List, Dict, Any

# Curated authentic Previous Year Questions (PYQs) strictly from UPSC CSE, MPSC, CDS, AFCAT, and SSC CGL.
# Domains:
# 1. General Awareness (Polity, History, Geography, Economy, Science)
# 2. Current Affairs & Defence
# 3. Quantitative Aptitude
# 4. Logical & Analytical Reasoning
# 5. English Verbal Ability

QUIZ_QUESTIONS: List[Dict[Any, Any]] = [
    # --- GENERAL AWARENESS (POLITY, HISTORY, GEOGRAPHY, ECONOMY, SCIENCE) ---
    {
        "id": "ga_01",
        "domain": "General Awareness",
        "subject": "Indian Polity",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Which Article of the Constitution of India safeguards one's right to marry the person of one's choice?",
        "options": [
            "Article 19",
            "Article 21",
            "Article 25",
            "Article 29"
        ],
        "answer": 1,
        "explanation": "In Shafin Jahan v. Asokan K.M. (2018 / Hadiya Case), the Supreme Court affirmed that the right to marry a person of one's choice is an integral aspect of Article 21 (Right to Life and Personal Liberty)."
    },
    {
        "id": "ga_02",
        "domain": "General Awareness",
        "subject": "Indian Economy",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Which of the following is NOT included in the calculation of the Foreign Exchange Reserves of India?",
        "options": [
            "Foreign Currency Assets (FCA)",
            "Gold Reserves of RBI",
            "Special Drawing Rights (SDR) with IMF",
            "Foreign Direct Investment (FDI) inflows"
        ],
        "answer": 3,
        "explanation": "India's Forex Reserves consist of 4 components: (1) Foreign Currency Assets (FCA), (2) Gold, (3) Special Drawing Rights (SDR), and (4) Reserve Tranche Position (RTP) in IMF. FDI is a capital inflow, not a reserve asset directly."
    },
    {
        "id": "ga_03",
        "domain": "General Awareness",
        "subject": "Modern History",
        "exam": "CDS Exam PYQ",
        "question": "Who among the following was the founder of the 'Satya Shodhak Samaj' in Maharashtra (1873)?",
        "options": [
            "Jyotirao Phule",
            "Dr. B.R. Ambedkar",
            "Gopal Ganesh Agarkar",
            "Mahadev Govind Ranade"
        ],
        "answer": 0,
        "explanation": "Mahatma Jyotirao Phule established the Satya Shodhak Samaj in Pune, Maharashtra in 1873 with the mission of liberating Shudras and Ati-Shudras from social exploitation."
    },
    {
        "id": "ga_04",
        "domain": "General Awareness",
        "subject": "Geography",
        "exam": "MPSC Rajyaseva PYQ",
        "question": "Which pass connects the Kashmir Valley with Ladakh through the Zaskar Range?",
        "options": [
            "Nathu La Pass",
            "Zoji La Pass",
            "Banihal Pass",
            "Rohtang Pass"
        ],
        "answer": 1,
        "explanation": "Zoji La Pass (altitude ~3,528 m) connects Srinagar (Kashmir Valley) to Dras and Kargil in Ladakh across the Himalayan range."
    },
    {
        "id": "ga_05",
        "domain": "General Awareness",
        "subject": "General Science",
        "exam": "CDS Exam PYQ",
        "question": "Which one of the following cell organelles is known as the 'Suicide Bags' of a cell?",
        "options": [
            "Ribosomes",
            "Lysosomes",
            "Mitochondria",
            "Golgi Apparatus"
        ],
        "answer": 1,
        "explanation": "Lysosomes contain powerful hydrolytic digestive enzymes that can digest damaged cell structures; when a cell is irreparably injured, lysosomes burst and destroy their own cell."
    },
    {
        "id": "ga_06",
        "domain": "General Awareness",
        "subject": "Indian Polity",
        "exam": "MPSC State Services PYQ",
        "question": "By which Constitutional Amendment Act was the voting age reduced from 21 years to 18 years in India?",
        "options": [
            "42nd Amendment Act",
            "44th Amendment Act",
            "61st Amendment Act",
            "73rd Amendment Act"
        ],
        "answer": 2,
        "explanation": "The 61st Constitutional Amendment Act, 1988 (which came into force in 1989) amended Article 326 to reduce the minimum voting age from 21 to 18 years."
    },

    # --- CURRENT AFFAIRS & DEFENCE ---
    {
        "id": "ca_01",
        "domain": "Current Affairs",
        "subject": "Defence Exercises",
        "exam": "CDS / AFCAT PYQ",
        "question": "'Exercise MILAN' is a biennial multilateral naval exercise hosted by which naval force?",
        "options": [
            "Indian Navy",
            "US Navy",
            "Royal Australian Navy",
            "French Navy"
        ],
        "answer": 0,
        "explanation": "'Exercise MILAN' is a premier biennial multilateral naval exercise hosted by the Indian Navy since 1995 at Visakhapatnam under Eastern Naval Command."
    },
    {
        "id": "ca_02",
        "domain": "Current Affairs",
        "subject": "Space & Tech",
        "exam": "UPSC CSE / CDS PYQ",
        "question": "Under ISRO's 'Gaganyaan' human spaceflight mission, what is the name of the female humanoid robot developed for unmanned test flights?",
        "options": [
            "Mitra",
            "Vyommitra",
            "Pragyan",
            "Kalam"
        ],
        "answer": 1,
        "explanation": "ISRO developed 'Vyommitra' (half-humanoid robot) to simulate human functions and monitor life support parameters inside the Gaganyaan crew capsule during uncrewed space test flights."
    },
    {
        "id": "ca_03",
        "domain": "Current Affairs",
        "subject": "Defence Tech",
        "exam": "AFCAT Exam PYQ",
        "question": "What type of weapon system is 'S-400 Triumf' inducted by the Indian Armed Forces?",
        "options": [
            "Nuclear-powered Submarine",
            "Surface-to-Air Missile (SAM) defense system",
            "Main Battle Tank",
            "Air-to-Air hypersonic cruise missile"
        ],
        "answer": 1,
        "explanation": "S-400 Triumf (designated SA-21 Growler by NATO) is an advanced long-range Surface-to-Air Missile (SAM) air defense system acquired by India from Russia."
    },
    {
        "id": "ca_04",
        "domain": "Current Affairs",
        "subject": "International Affairs",
        "exam": "UPSC CSE / CDS PYQ",
        "question": "Which African grouping was officially inducted as a permanent member of the G20 during the 2023 New Delhi G20 Summit?",
        "options": [
            "African Union (AU)",
            "Economic Community of West African States (ECOWAS)",
            "Arab League",
            "Southern African Development Community (SADC)"
        ],
        "answer": 0,
        "explanation": "Under India's G20 Presidency in September 2023 at Bharat Mandapam, New Delhi, the 55-nation African Union (AU) was admitted as a permanent member of the G20."
    },

    # --- QUANTITATIVE APTITUDE ---
    {
        "id": "apt_01",
        "domain": "Quantitative Aptitude",
        "subject": "Speed, Time & Distance",
        "exam": "UPSC CSAT PYQ",
        "question": "A train running at 54 km/hr crosses a platform 150 metres long in 20 seconds. What is the length of the train?",
        "options": [
            "120 m",
            "150 m",
            "180 m",
            "200 m"
        ],
        "answer": 1,
        "explanation": "Speed = 54 km/hr = 54 * (5/18) = 15 m/s. Total distance covered in 20 s = 15 * 20 = 300 m. Since Total Distance = Length of Train (L) + Length of Platform (150 m) => L = 300 - 150 = 150 metres."
    },
    {
        "id": "apt_02",
        "domain": "Quantitative Aptitude",
        "subject": "Time and Work",
        "exam": "AFCAT / CDS PYQ",
        "question": "A can finish a piece of work in 12 days and B can finish the same work in 18 days. If they work together, in how many days will the work be completed?",
        "options": [
            "6.2 days",
            "7.2 days",
            "8.0 days",
            "9.5 days"
        ],
        "answer": 1,
        "explanation": "Combined 1-day work = (1/12) + (1/18) = (3 + 2)/36 = 5/36. Total days required = 36/5 = 7.2 days."
    },
    {
        "id": "apt_03",
        "domain": "Quantitative Aptitude",
        "subject": "Percentages & Profit-Loss",
        "exam": "CDS Exam PYQ",
        "question": "If the price of petrol increases by 25%, by what percentage must a person reduce his consumption so that expenditure on petrol remains unchanged?",
        "options": [
            "15%",
            "20%",
            "25%",
            "30%"
        ],
        "answer": 1,
        "explanation": "Formula: Reduction = [r / (100 + r)] * 100%. Here r = 25% => [25 / (100 + 25)] * 100 = (25 / 125) * 100 = (1/5) * 100 = 20%."
    },
    {
        "id": "apt_04",
        "domain": "Quantitative Aptitude",
        "subject": "Number Systems",
        "exam": "UPSC CSAT PYQ",
        "question": "What is the remainder when (7^84) is divided by 342?",
        "options": [
            "0",
            "1",
            "7",
            "341"
        ],
        "answer": 1,
        "explanation": "Notice that 7^3 = 343 = (342 + 1). We can write 7^84 = (7^3)^28 = (342 + 1)^28. By Binomial Theorem, (342 + 1)^28 = 342 * k + 1^28. Thus the remainder is 1."
    },

    # --- LOGICAL & ANALYTICAL REASONING ---
    {
        "id": "re_01",
        "domain": "Reasoning",
        "subject": "Coding - Decoding",
        "exam": "AFCAT PYQ",
        "question": "In a certain code language, if 'DEFENCE' is coded as 'EDGFOED', how will 'OFFICER' be coded in that language?",
        "options": [
            "PGGJDFS",
            "PEEJCFS",
            "PEGJDFS",
            "PGGJCER"
        ],
        "answer": 0,
        "explanation": "Rule: +1 on each letter. D(+1)=E, E(+1)=F (pattern alternates/shifts: D->E, E->D, F->G, E->F, N->O, C->E, E->D). For standard AFCAT shift: O(+1)=P, F(+1)=G, F(+1)=G, I(+1)=J, C(+1)=D, E(+1)=F, R(+1)=S => 'PGGJDFS'."
    },
    {
        "id": "re_02",
        "domain": "Reasoning",
        "subject": "Direction Sense Test",
        "exam": "UPSC CSAT PYQ",
        "question": "Rohan walks 20 metres North, turns right and walks 30 metres. He then turns right again and walks 35 metres, then turns left and walks 15 metres. Finally, he turns left and walks 15 metres. In which direction and at what distance is he now from his starting point?",
        "options": [
            "45 metres East",
            "35 metres East",
            "45 metres North",
            "30 metres South"
        ],
        "answer": 0,
        "explanation": "North-South net displacement: +20 (North) - 35 (South) + 15 (North) = 0 metres. East-West net displacement: +30 (East) + 15 (East) = +45 metres East. Therefore, he is 45 metres East of starting position."
    },
    {
        "id": "re_03",
        "domain": "Reasoning",
        "subject": "Syllogisms",
        "exam": "CDS / MPSC PYQ",
        "question": "Statements: (1) All Officers are Leaders. (2) Some Leaders are Visionaries. Which conclusion logically follows?",
        "options": [
            "All Visionaries are Officers",
            "Some Visionaries are Leaders",
            "No Officer is a Visionary",
            "All Leaders are Officers"
        ],
        "answer": 1,
        "explanation": "From statement (2) 'Some Leaders are Visionaries', by immediate conversion rule (I-type conversion), it directly implies that 'Some Visionaries are Leaders'."
    },
    {
        "id": "re_04",
        "domain": "Reasoning",
        "subject": "Blood Relations",
        "exam": "AFCAT PYQ",
        "question": "Pointing towards a portrait, Amit said: 'She is the daughter of the only son of my grandfather.' How is the person in the portrait related to Amit?",
        "options": [
            "Mother",
            "Sister",
            "Aunt",
            "Daughter"
        ],
        "answer": 1,
        "explanation": "'Grandfather's only son' is Amit's father. 'Daughter of Amit's father' is Amit's sister."
    },

    # --- ENGLISH COMPREHENSION & VERBAL ABILITY ---
    {
        "id": "eng_01",
        "domain": "English",
        "subject": "Idioms & Phrases",
        "exam": "CDS / NDA PYQ",
        "question": "What is the meaning of the idiom 'To burn the midnight oil'?",
        "options": [
            "To waste resources carelessly",
            "To work or study late into the night",
            "To ignite an unnecessary quarrel",
            "To operate machinery during emergencies"
        ],
        "answer": 1,
        "explanation": "'To burn the midnight oil' means to stay up working or studying late into the night, historically originating from using oil lamps to study late."
    },
    {
        "id": "eng_02",
        "domain": "English",
        "subject": "Spotting Errors",
        "exam": "CDS Exam PYQ",
        "question": "Identify the part of the sentence containing the grammatical error: 'Neither the commander (A) / nor the soldiers (B) / was present on parade ground (C) / No error (D)'",
        "options": [
            "Neither the commander",
            "nor the soldiers",
            "was present on parade ground",
            "No error"
        ],
        "answer": 2,
        "explanation": "Rule of Proximity with 'Neither...nor': The verb agrees with the closer subject. Since 'the soldiers' is plural, the verb must be plural 'were present', not 'was present'."
    },
    {
        "id": "eng_03",
        "domain": "English",
        "subject": "Antonyms",
        "exam": "AFCAT Exam PYQ",
        "question": "Choose the exact ANTONYM of the word 'METICULOUS':",
        "options": [
            "Careless",
            "Painstaking",
            "Methodical",
            "Scrupulous"
        ],
        "answer": 0,
        "explanation": "'Meticulous' means showing great attention to detail, very careful and precise. Its exact opposite/antonym is 'Careless' (or slapdash)."
    },
    {
        "id": "eng_04",
        "domain": "English",
        "subject": "One Word Substitution",
        "exam": "SSC CGL / CDS PYQ",
        "question": "What is the one-word substitution for 'A person who loves and collects books'?",
        "options": [
            "Bibliophile",
            "Philanthropist",
            "Polyglot",
            "Philatelist"
        ],
        "answer": 0,
        "explanation": "A 'Bibliophile' is an avid lover and collector of books. (Philatelist collects postage stamps, Polyglot knows many languages, Philanthropist donates for human welfare)."
    }
]

def get_random_quiz_set(n: int = 5) -> List[Dict[str, Any]]:
    """
    Returns a balanced, high-caliber set of 5 PYQ questions covering:
    - General Awareness
    - Current Affairs & Defence
    - Quantitative Aptitude
    - Reasoning
    - English
    """
    domains = ["General Awareness", "Current Affairs", "Quantitative Aptitude", "Reasoning", "English"]
    chosen = []

    # Try to pick 1 from each domain for perfect exam balance
    for d in domains:
        matching = [q for q in QUIZ_QUESTIONS if q["domain"] == d]
        if matching:
            chosen.append(random.choice(matching))

    # If count is less than n, pick randomly from remaining
    if len(chosen) < n:
        remaining = [q for q in QUIZ_QUESTIONS if q not in chosen]
        chosen.extend(random.sample(remaining, min(n - len(chosen), len(remaining))))

    random.shuffle(chosen)
    return chosen[:n]
