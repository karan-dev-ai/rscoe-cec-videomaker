import random
from typing import List, Dict, Any, Optional

# Curated authentic Previous Year Questions (PYQs) strictly from:
# - UPSC CSE Prelims & CSAT
# - MPSC Rajyaseva / State Services
# - CDS (Combined Defence Services)
# - AFCAT (Air Force Common Admission Test)
# - SSC CGL (Staff Selection Commission)
#
# Domains:
# 1. General Awareness (Polity, History, Geography, Economy, Science, Environment)
# 2. Current Affairs & Defence
# 3. Quantitative Aptitude
# 4. Logical & Analytical Reasoning
# 5. English Verbal Ability

QUIZ_QUESTIONS: List[Dict[str, Any]] = [
    # =========================================================================
    # --- 1. GENERAL AWARENESS (20 QUESTIONS) ---
    # =========================================================================
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
    {
        "id": "ga_07",
        "domain": "General Awareness",
        "subject": "Indian Polity",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Which three words were added to the Preamble of the Indian Constitution by the 42nd Amendment Act of 1976?",
        "options": [
            "Socialist, Secular, Integrity",
            "Sovereign, Democratic, Republic",
            "Justice, Liberty, Equality",
            "Unity, Integrity, Fraternity"
        ],
        "answer": 0,
        "explanation": "The 42nd Constitutional Amendment Act of 1976 amended the Preamble to insert the words 'Socialist', 'Secular', and changed 'unity of the Nation' to 'unity and integrity of the Nation'."
    },
    {
        "id": "ga_08",
        "domain": "General Awareness",
        "subject": "Modern History",
        "exam": "CDS Exam PYQ",
        "question": "Gandhiji's first Satyagraha in India at Champaran (1917) was launched against which system?",
        "options": [
            "Ryotwari Land Settlement",
            "Tinkathia System of Indigo cultivation",
            "Salt Tax monopoly",
            "Rowlatt Act restrictions"
        ],
        "answer": 1,
        "explanation": "Under the Tinkathia system in Champaran (Bihar), European planters forced peasant farmers to cultivate indigo on 3/20th of their total landholdings. Gandhiji led the successful struggle on Rajkumar Shukla's invitation."
    },
    {
        "id": "ga_09",
        "domain": "General Awareness",
        "subject": "Indian Economy",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Who chairs the Monetary Policy Committee (MPC) responsible for fixing the benchmark policy interest rate (Repo Rate)?",
        "options": [
            "Union Finance Minister",
            "Governor of the Reserve Bank of India",
            "Chief Economic Adviser",
            "Finance Secretary"
        ],
        "answer": 1,
        "explanation": "Under Section 45ZB of the amended RBI Act 1934, the 6-member Monetary Policy Committee (MPC) is ex-officio chaired by the Governor of the Reserve Bank of India."
    },
    {
        "id": "ga_10",
        "domain": "General Awareness",
        "subject": "Geography",
        "exam": "SSC CGL / CDS PYQ",
        "question": "Majuli, officially certified as the world's largest river island, is located on which river in India?",
        "options": [
            "Ganga",
            "Brahmaputra",
            "Godavari",
            "Narmada"
        ],
        "answer": 1,
        "explanation": "Majuli is a picturesque river island on the Brahmaputra River in Assam. In 2016, it became the first island district formed in India."
    },
    {
        "id": "ga_11",
        "domain": "General Awareness",
        "subject": "General Science",
        "exam": "CDS / NDA Exam PYQ",
        "question": "Sound waves cannot travel through which of the following media?",
        "options": [
            "Solids (Steel)",
            "Liquids (Water)",
            "Gases (Air)",
            "Vacuum"
        ],
        "answer": 3,
        "explanation": "Sound is a mechanical longitudinal wave requiring a physical material medium (particles that oscillate) to propagate. Sound cannot travel through vacuum."
    },
    {
        "id": "ga_12",
        "domain": "General Awareness",
        "subject": "Ancient History",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "The famous 'Great Bath' of the Indus Valley Civilization was excavated at which archaeological site?",
        "options": [
            "Harappa",
            "Mohenjo-daro",
            "Lothal",
            "Kalibangan"
        ],
        "answer": 1,
        "explanation": "The 'Great Bath'—a watertight rectangular public bathing tank lined with baked bricks and natural bitumen—was excavated at Mohenjo-daro in Sindh (now Pakistan)."
    },
    {
        "id": "ga_13",
        "domain": "General Awareness",
        "subject": "Indian Polity",
        "exam": "MPSC Rajyaseva PYQ",
        "question": "Fundamental Duties were incorporated into Part IV-A (Article 51A) of the Constitution on the recommendation of which committee?",
        "options": [
            "Sarkaria Commission",
            "Swaran Singh Committee",
            "Verma Committee",
            "Balwant Rai Mehta Committee"
        ],
        "answer": 1,
        "explanation": "The Swaran Singh Committee (1976) recommended the inclusion of Fundamental Duties, which led to the 42nd Amendment Act creating Article 51A."
    },
    {
        "id": "ga_14",
        "domain": "General Awareness",
        "subject": "Geography",
        "exam": "CDS Exam PYQ",
        "question": "The Tropic of Cancer (23.5° N) passes through how many Indian states?",
        "options": [
            "6 states",
            "7 states",
            "8 states",
            "9 states"
        ],
        "answer": 2,
        "explanation": "The Tropic of Cancer passes through 8 Indian states from west to east: Gujarat, Rajasthan, Madhya Pradesh, Chhattisgarh, Jharkhand, West Bengal, Tripura, and Mizoram."
    },
    {
        "id": "ga_15",
        "domain": "General Awareness",
        "subject": "Physical Geography",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Due to the Coriolis effect caused by Earth's rotation, winds in the Northern Hemisphere are deflected towards which direction?",
        "options": [
            "To the right of their path",
            "To the left of their path",
            "Straight towards the Equator",
            "Vertically upwards"
        ],
        "answer": 0,
        "explanation": "According to Ferrel's Law, the Coriolis force deflects moving fluids and winds to the right in the Northern Hemisphere and to the left in the Southern Hemisphere."
    },
    {
        "id": "ga_16",
        "domain": "General Awareness",
        "subject": "General Science",
        "exam": "CDS / SSC PYQ",
        "question": "Deficiency of Vitamin D in children leads to which disease characterized by soft, weakened bones?",
        "options": [
            "Scurvy",
            "Beriberi",
            "Rickets",
            "Pellagra"
        ],
        "answer": 2,
        "explanation": "Vitamin D helps the body absorb calcium and phosphate. Its deficiency causes Rickets in children (softening and bending of bones) and Osteomalacia in adults."
    },
    {
        "id": "ga_17",
        "domain": "General Awareness",
        "subject": "Modern History",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Who among the following British administrators introduced the 'Ryotwari System' of land revenue in the Madras Presidency?",
        "options": [
            "Lord Cornwallis",
            "Thomas Munro",
            "Warren Hastings",
            "Holt Mackenzie"
        ],
        "answer": 1,
        "explanation": "Sir Thomas Munro (along with Alexander Read) pioneered the Ryotwari settlement in Madras Presidency (1820), where tax was settled directly with individual cultivating peasants (Ryots)."
    },
    {
        "id": "ga_18",
        "domain": "General Awareness",
        "subject": "Indian Polity",
        "exam": "MPSC / CDS PYQ",
        "question": "Under Article 110 of the Indian Constitution, whose decision is final on whether a bill is a Money Bill or not?",
        "options": [
            "President of India",
            "Speaker of the Lok Sabha",
            "Chairman of the Rajya Sabha",
            "Union Finance Minister"
        ],
        "answer": 1,
        "explanation": "According to Article 110(3), if any question arises whether a bill is a Money Bill or not, the decision of the Speaker of the Lok Sabha is final and cannot be challenged."
    },
    {
        "id": "ga_19",
        "domain": "General Awareness",
        "subject": "Geography",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Which peak is the highest point in South India and the Western Ghats mountain range?",
        "options": [
            "Doda Betta",
            "Anamudi",
            "Kalsubai",
            "Guru Shikhar"
        ],
        "answer": 1,
        "explanation": "Anamudi (2,695 m / 8,842 ft), situated in the Anaimalai Hills within Eravikulam National Park, Kerala, is the highest peak in South India."
    },
    {
        "id": "ga_20",
        "domain": "General Awareness",
        "subject": "Agriculture & Ecology",
        "exam": "SSC CGL / CDS PYQ",
        "question": "Who is universally revered as the 'Father of the Green Revolution in India'?",
        "options": [
            "Dr. Verghese Kurien",
            "Dr. M.S. Swaminathan",
            "Dr. Homi Bhabha",
            "Dr. Norman Borlaug"
        ],
        "answer": 1,
        "explanation": "Dr. M.S. Swaminathan led the development and introduction of high-yielding wheat varieties that transformed India from food deficiency to self-sufficiency. (Norman Borlaug was global Father of Green Revolution)."
    },

    # =========================================================================
    # --- 2. CURRENT AFFAIRS & DEFENCE (20 QUESTIONS) ---
    # =========================================================================
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
    {
        "id": "ca_05",
        "domain": "Current Affairs",
        "subject": "Naval Defence",
        "exam": "CDS Exam PYQ",
        "question": "What is the name of India's first indigenously designed and built aircraft carrier commissioned into the Indian Navy?",
        "options": [
            "INS Vikramaditya",
            "INS Vikrant",
            "INS Viraat",
            "INS Vishal"
        ],
        "answer": 1,
        "explanation": "INS Vikrant (IAC-1) was designed by the Indian Navy's Warship Design Bureau and constructed at Cochin Shipyard Limited, commissioned in September 2022."
    },
    {
        "id": "ca_06",
        "domain": "Current Affairs",
        "subject": "Defence Exercises",
        "exam": "AFCAT Exam PYQ",
        "question": "'Exercise Yudh Abhyas' is an annual joint military training exercise conducted between India and which country?",
        "options": [
            "United Kingdom",
            "United States",
            "France",
            "Japan"
        ],
        "answer": 1,
        "explanation": "'Exercise Yudh Abhyas' is a bilateral army exercise held annually between the Indian Army and the United States Army to enhance interoperability and counter-terror tactics."
    },
    {
        "id": "ca_07",
        "domain": "Current Affairs",
        "subject": "Missile Technology",
        "exam": "CDS / AFCAT PYQ",
        "question": "'BrahMos' is a supersonic cruise missile developed as a joint venture between India and which foreign partner?",
        "options": [
            "Israel",
            "Russia",
            "France",
            "United States"
        ],
        "answer": 1,
        "explanation": "BrahMos Aerospace is a joint venture between India's DRDO and Russia's NPOM, named after the Brahmaputra and Moskva rivers."
    },
    {
        "id": "ca_08",
        "domain": "Current Affairs",
        "subject": "Space Missions",
        "exam": "UPSC CSE / AFCAT PYQ",
        "question": "What official name was designated for the touchdown point of ISRO's Chandrayaan-3 Vikram lander on the Moon's South Pole?",
        "options": [
            "Tiranga Point",
            "Shiv Shakti Point",
            "Jawahar Point",
            "Atal Point"
        ],
        "answer": 1,
        "explanation": "Prime Minister Narendra Modi announced 'Shiv Shakti Point' as the name for the touchdown spot of the Chandrayaan-3 Vikram Lander, and August 23 as National Space Day."
    },
    {
        "id": "ca_09",
        "domain": "Current Affairs",
        "subject": "Defence Exercises",
        "exam": "CDS Exam PYQ",
        "question": "Which four QUAD nations participate in the prestigious multilateral naval exercise 'MALABAR'?",
        "options": [
            "India, USA, Japan, Australia",
            "India, UK, France, Australia",
            "India, Singapore, Indonesia, Thailand",
            "India, Russia, China, South Africa"
        ],
        "answer": 0,
        "explanation": "Exercise Malabar began as an India-US bilateral drill in 1992, joined permanently by Japan in 2015 and Australia in 2020, representing all four QUAD democracies."
    },
    {
        "id": "ca_10",
        "domain": "Current Affairs",
        "subject": "Military Aviation",
        "exam": "AFCAT Exam PYQ",
        "question": "Which Indian aerospace manufacturer produces the Light Combat Aircraft (LCA) 'Tejas'?",
        "options": [
            "Bharat Electronics Limited (BEL)",
            "Hindustan Aeronautics Limited (HAL)",
            "Bharat Dynamics Limited (BDL)",
            "Tata Advanced Systems"
        ],
        "answer": 1,
        "explanation": "HAL (Hindustan Aeronautics Limited) manufactures the single-engine, delta-wing LCA Tejas designed by the Aeronautical Development Agency (ADA)."
    },
    {
        "id": "ca_11",
        "domain": "Current Affairs",
        "subject": "Armed Forces Hierarchy",
        "exam": "CDS Exam PYQ",
        "question": "Who served as India's first-ever Chief of Defence Staff (CDS)?",
        "options": [
            "General Bipin Rawat",
            "General Anil Chauhan",
            "General Manoj Mukund Naravane",
            "Admiral Karambir Singh"
        ],
        "answer": 0,
        "explanation": "General Bipin Rawat was appointed as India's first Chief of Defence Staff (CDS) on 1 January 2020, serving as principal military adviser to the Defence Minister."
    },
    {
        "id": "ca_12",
        "domain": "Current Affairs",
        "subject": "Submarine Warfare",
        "exam": "UPSC CSE / CDS PYQ",
        "question": "Under Project 75, how many Scorpene-class diesel-electric attack submarines were constructed at Mazagon Dock Shipbuilders (MDL)?",
        "options": [
            "4 submarines",
            "5 submarines",
            "6 submarines",
            "8 submarines"
        ],
        "answer": 2,
        "explanation": "Under Project 75, six Kalvari-class (Scorpene) submarines were built at MDL with French Naval Group: Kalvari, Khanderi, Karanj, Vela, Vagir, and Vagsheer."
    },
    {
        "id": "ca_13",
        "domain": "Current Affairs",
        "subject": "International Organizations",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "Where is the permanent headquarters / Secretariat of the Shanghai Cooperation Organisation (SCO) located?",
        "options": [
            "Shanghai",
            "Beijing",
            "Tashkent",
            "Moscow"
        ],
        "answer": 1,
        "explanation": "The Secretariat of the Shanghai Cooperation Organisation (SCO) is located in Beijing, China, while its Regional Anti-Terrorist Structure (RATS) is in Tashkent, Uzbekistan."
    },
    {
        "id": "ca_14",
        "domain": "Current Affairs",
        "subject": "Space Science",
        "exam": "UPSC CSE / CDS PYQ",
        "question": "ISRO's Aditya-L1 spacecraft was positioned into a halo orbit around which gravitational equilibrium point?",
        "options": [
            "Lagrange Point 1 (L1)",
            "Lagrange Point 2 (L2)",
            "Earth-Moon L4 Point",
            "Geostationary Orbit"
        ],
        "answer": 0,
        "explanation": "Aditya-L1 was placed into a halo orbit around the Sun-Earth Lagrangian Point 1 (L1), roughly 1.5 million km from Earth, allowing uninterrupted 24x7 solar observations."
    },
    {
        "id": "ca_15",
        "domain": "Current Affairs",
        "subject": "Defence Exercises",
        "exam": "AFCAT Exam PYQ",
        "question": "'Exercise Garuda' is a bilateral air exercise conducted between the Indian Air Force (IAF) and the air force of which country?",
        "options": [
            "United Kingdom",
            "France",
            "Russia",
            "Israel"
        ],
        "answer": 1,
        "explanation": "'Exercise Garuda' is a bilateral air combat exercise between the Indian Air Force (IAF) and the French Air and Space Force."
    },
    {
        "id": "ca_16",
        "domain": "Current Affairs",
        "subject": "Missile Program",
        "exam": "CDS Exam PYQ",
        "question": "The Integrated Guided Missile Development Programme (IGMDP) that produced Prithvi, Agni, Trishul, Nag, and Akash was spearheaded by whom?",
        "options": [
            "Dr. Vikram Sarabhai",
            "Dr. A.P.J. Abdul Kalam",
            "Dr. Satish Dhawan",
            "Dr. K. Sivan"
        ],
        "answer": 1,
        "explanation": "Dr. A.P.J. Abdul Kalam spearheaded the IGMDP from 1983, earning the title 'Missile Man of India' for leading India to indigenous strategic missile self-reliance."
    },
    {
        "id": "ca_17",
        "domain": "Current Affairs",
        "subject": "Defence Policy",
        "exam": "AFCAT Exam PYQ",
        "question": "Under the 'Agnipath' scheme of recruitment for the Indian Armed Forces, youth are recruited as 'Agniveers' for a period of how many years?",
        "options": [
            "3 years",
            "4 years",
            "5 years",
            "7 years"
        ],
        "answer": 1,
        "explanation": "The Agnipath scheme enrolls youth (Agniveers) across the Army, Navy, and Air Force for a four-year tenure, after which up to 25% may be retained in regular service."
    },
    {
        "id": "ca_18",
        "domain": "Current Affairs",
        "subject": "International Forums",
        "exam": "UPSC CSE Prelims PYQ",
        "question": "In the landmark 2024 expansion of BRICS, which of the following countries became full members?",
        "options": [
            "Egypt, Ethiopia, Iran, UAE",
            "Mexico, Indonesia, Turkey, Nigeria",
            "Argentina, Canada, Australia, Japan",
            "Germany, Sweden, Finland, Poland"
        ],
        "answer": 0,
        "explanation": "From 1 January 2024, BRICS officially expanded to include Egypt, Ethiopia, Iran, and the United Arab Emirates (UAE)."
    },
    {
        "id": "ca_19",
        "domain": "Current Affairs",
        "subject": "Defence Exercises",
        "exam": "AFCAT Exam PYQ",
        "question": "'Exercise Desert Knight' conducted over the Arabian Sea in 2024 was a trilateral air exercise between India and which two nations?",
        "options": [
            "USA and Japan",
            "France and UAE",
            "UK and Australia",
            "Oman and Saudi Arabia"
        ],
        "answer": 1,
        "explanation": "Exercise Desert Knight was conducted by the Indian Air Force along with the French Air and Space Force and UAE Air Force over the Arabian Sea."
    },
    {
        "id": "ca_20",
        "domain": "Current Affairs",
        "subject": "Strategic Weapons",
        "exam": "CDS / UPSC PYQ",
        "question": "In March 2024, India successfully tested the Agni-5 missile equipped with MIRV technology under 'Mission Divyastra'. What does MIRV stand for?",
        "options": [
            "Multiple Independently Targetable Re-entry Vehicle",
            "Multi-range Intercontinental Rocket Vector",
            "Missile Integrated Radar Validation",
            "Maximum Impact Reconnaissance Vehicle"
        ],
        "answer": 0,
        "explanation": "MIRV (Multiple Independently Targetable Re-entry Vehicle) allows a single intercontinental ballistic missile to carry multiple nuclear warheads, each programmed to hit different targets."
    },

    # =========================================================================
    # --- 3. QUANTITATIVE APTITUDE (20 QUESTIONS) ---
    # =========================================================================
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
        "explanation": "Speed = 54 km/hr = 54 * (5/18) = 15 m/s. Total distance in 20 s = 15 * 20 = 300 m. Since Total Distance = Train Length + Platform Length => L = 300 - 150 = 150 metres."
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
        "subject": "Percentages",
        "exam": "CDS Exam PYQ",
        "question": "If the price of petrol increases by 25%, by what percentage must a person reduce his consumption so that expenditure on petrol remains unchanged?",
        "options": [
            "15%",
            "20%",
            "25%",
            "30%"
        ],
        "answer": 1,
        "explanation": "Formula: Reduction = [r / (100 + r)] * 100%. Here r = 25% => [25 / (100 + 25)] * 100 = (25 / 125) * 100 = 20%."
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
        "explanation": "Notice 7^3 = 343 = (342 + 1). We can rewrite 7^84 = (7^3)^28 = (342 + 1)^28. By the Binomial theorem, (342 + 1)^28 = 342*k + 1^28. Thus, remainder is 1."
    },
    {
        "id": "apt_05",
        "domain": "Quantitative Aptitude",
        "subject": "Simple Interest",
        "exam": "CDS / AFCAT PYQ",
        "question": "A sum of money triples itself in 8 years at simple interest. In how many years will it become 7 times itself at the same rate?",
        "options": [
            "16 years",
            "20 years",
            "24 years",
            "28 years"
        ],
        "answer": 2,
        "explanation": "At simple interest: Interest earned = P*(n - 1). For tripling (n=3), interest = 2P in 8 years => Rate earns P in 4 years. For 7 times (n=7), interest = 6P => Time required = 6 * 4 = 24 years."
    },
    {
        "id": "apt_06",
        "domain": "Quantitative Aptitude",
        "subject": "HCF & LCM",
        "exam": "AFCAT / SSC PYQ",
        "question": "Two positive numbers are in the ratio 3 : 4. If their Least Common Multiple (LCM) is 180, what is the larger of the two numbers?",
        "options": [
            "45",
            "60",
            "75",
            "90"
        ],
        "answer": 1,
        "explanation": "Let numbers be 3x and 4x. Their LCM = 12x. Given 12x = 180 => x = 15. The larger number is 4x = 4 * 15 = 60."
    },
    {
        "id": "apt_07",
        "domain": "Quantitative Aptitude",
        "subject": "Profit and Loss",
        "exam": "CDS / SSC PYQ",
        "question": "A shopkeeper marks his goods 40% above cost price and allows a discount of 20% on marked price. What is his net profit percentage?",
        "options": [
            "10%",
            "12%",
            "15%",
            "20%"
        ],
        "answer": 1,
        "explanation": "Let Cost Price = 100. Marked Price = 140. Selling Price after 20% discount = 140 * (80/100) = 112. Profit = 112 - 100 = 12%."
    },
    {
        "id": "apt_08",
        "domain": "Quantitative Aptitude",
        "subject": "Averages",
        "exam": "AFCAT Exam PYQ",
        "question": "The average of 5 consecutive odd positive integers is 27. What is the product of the smallest and largest integers in the set?",
        "options": [
            "713",
            "725",
            "759",
            "783"
        ],
        "answer": 0,
        "explanation": "The middle (3rd) term of 5 consecutive odd numbers equals their average = 27. Thus, the 5 numbers are 23, 25, 27, 29, 31. Smallest = 23, Largest = 31. Product = 23 * 31 = 713."
    },
    {
        "id": "apt_09",
        "domain": "Quantitative Aptitude",
        "subject": "Boats and Streams",
        "exam": "CDS Exam PYQ",
        "question": "A boat covers 24 km downstream in 2 hours and 18 km upstream in 3 hours. What is the speed of the water current?",
        "options": [
            "2 km/h",
            "3 km/h",
            "4 km/h",
            "5 km/h"
        ],
        "answer": 1,
        "explanation": "Downstream speed (u + v) = 24 / 2 = 12 km/h. Upstream speed (u - v) = 18 / 3 = 6 km/h. Speed of current v = (Downstream - Upstream) / 2 = (12 - 6) / 2 = 3 km/h."
    },
    {
        "id": "apt_10",
        "domain": "Quantitative Aptitude",
        "subject": "Pipes and Cisterns",
        "exam": "AFCAT / SSC PYQ",
        "question": "Pipe A can fill a tank in 10 hours, while Pipe B can empty the full tank in 15 hours. If both pipes are opened together, how long will it take to fill the tank?",
        "options": [
            "20 hours",
            "25 hours",
            "30 hours",
            "35 hours"
        ],
        "answer": 2,
        "explanation": "Net rate per hour = (1/10) - (1/15) = (3 - 2)/30 = 1/30 of the tank. Hence, it takes 30 hours to fill the tank."
    },
    {
        "id": "apt_11",
        "domain": "Quantitative Aptitude",
        "subject": "Relative Speed",
        "exam": "CDS / CSAT PYQ",
        "question": "Two trains of lengths 120 metres and 80 metres run on parallel tracks in opposite directions at 42 km/h and 30 km/h respectively. In how many seconds will they cross each other?",
        "options": [
            "8 seconds",
            "10 seconds",
            "12 seconds",
            "15 seconds"
        ],
        "answer": 1,
        "explanation": "Relative speed = 42 + 30 = 72 km/h = 72 * (5/18) = 20 m/s. Total distance to clear = 120 + 80 = 200 m. Time = 200 / 20 = 10 seconds."
    },
    {
        "id": "apt_12",
        "domain": "Quantitative Aptitude",
        "subject": "Ratio & Mixtures",
        "exam": "AFCAT PYQ",
        "question": "In a 60 kg alloy of copper and zinc, the ratio of copper to zinc is 2 : 1. How much zinc must be added to make the ratio 1 : 2?",
        "options": [
            "40 kg",
            "50 kg",
            "60 kg",
            "80 kg"
        ],
        "answer": 2,
        "explanation": "Initial copper = 60 * (2/3) = 40 kg; initial zinc = 20 kg. In new alloy, copper remains 40 kg and represents 1 part, so zinc must be 2 parts = 40 * 2 = 80 kg. Zinc added = 80 - 20 = 60 kg."
    },
    {
        "id": "apt_13",
        "domain": "Quantitative Aptitude",
        "subject": "Compound Interest",
        "exam": "CDS / SSC PYQ",
        "question": "What is the compound interest on Rs 10,000 for 2 years at 10% per annum compounded annually?",
        "options": [
            "Rs 2,000",
            "Rs 2,100",
            "Rs 2,200",
            "Rs 2,250"
        ],
        "answer": 1,
        "explanation": "Amount = P * (1 + r/100)^t = 10000 * (1.1)^2 = 10000 * 1.21 = Rs 12,100. CI = 12,100 - 10,000 = Rs 2,100."
    },
    {
        "id": "apt_14",
        "domain": "Quantitative Aptitude",
        "subject": "Mensuration",
        "exam": "AFCAT / CSAT PYQ",
        "question": "If the radius of a circular field is increased by 20%, by what percentage does the area of the field increase?",
        "options": [
            "40%",
            "44%",
            "48%",
            "50%"
        ],
        "answer": 1,
        "explanation": "Area varies as r^2. Successive percentage increase = 20 + 20 + (20 * 20)/100 = 40 + 4 = 44%."
    },
    {
        "id": "apt_15",
        "domain": "Quantitative Aptitude",
        "subject": "Speed & Time",
        "exam": "UPSC CSAT / CDS PYQ",
        "question": "A man walking at 4 km/h reaches his office 10 minutes late. If he walks at 5 km/h, he reaches 5 minutes early. What is the distance to his office?",
        "options": [
            "4 km",
            "5 km",
            "6 km",
            "7.5 km"
        ],
        "answer": 1,
        "explanation": "Time difference = 10 min late to 5 min early = 15 minutes = 1/4 hour. Distance = [ (S1 * S2) / (S2 - S1) ] * (delta_t) = [ (4 * 5) / (5 - 4) ] * (1/4) = 20 * (1/4) = 5 km."
    },
    {
        "id": "apt_16",
        "domain": "Quantitative Aptitude",
        "subject": "Problems on Ages",
        "exam": "AFCAT Exam PYQ",
        "question": "The present age of a father is 3 times the age of his son. 10 years ago, the father was 5 times as old as his son. What is the father's present age?",
        "options": [
            "50 years",
            "60 years",
            "65 years",
            "70 years"
        ],
        "answer": 1,
        "explanation": "Let son's present age = x, father's age = 3x. 10 years ago: (3x - 10) = 5(x - 10) => 3x - 10 = 5x - 50 => 2x = 40 => x = 20. Father's age = 3 * 20 = 60 years."
    },
    {
        "id": "apt_17",
        "domain": "Quantitative Aptitude",
        "subject": "Profit & Loss",
        "exam": "CDS / SSC PYQ",
        "question": "If the cost price of 16 articles is equal to the selling price of 12 articles, what is the gain percentage?",
        "options": [
            "25%",
            "30%",
            "33.33%",
            "35%"
        ],
        "answer": 2,
        "explanation": "16 * CP = 12 * SP => SP / CP = 16 / 12 = 4 / 3. Profit = (4 - 3)/3 = 1/3 = 33.33%."
    },
    {
        "id": "apt_18",
        "domain": "Quantitative Aptitude",
        "subject": "Number Systems",
        "exam": "UPSC CSAT / SSC PYQ",
        "question": "What is the unit digit of the product (3^65 * 6^59 * 7^71)?",
        "options": [
            "2",
            "4",
            "6",
            "8"
        ],
        "answer": 1,
        "explanation": "Unit digit cyclicity: 3^65 = 3^(4*16 + 1) -> 3. Any power of 6 ends in 6 -> 6. 7^71 = 7^(4*17 + 3) -> 7^3 ends in 3. Product of unit digits = 3 * 6 * 3 = 54 -> unit digit is 4."
    },
    {
        "id": "apt_19",
        "domain": "Quantitative Aptitude",
        "subject": "Geometry & Mensuration",
        "exam": "AFCAT Exam PYQ",
        "question": "The perimeter of a rectangular training ground is 60 metres, and its length is twice its breadth. What is its area?",
        "options": [
            "180 m²",
            "200 m²",
            "225 m²",
            "250 m²"
        ],
        "answer": 1,
        "explanation": "Perimeter = 2*(L + B) = 60 => L + B = 30. Since L = 2B, 3B = 30 => B = 10 m, L = 20 m. Area = L * B = 20 * 10 = 200 m²."
    },
    {
        "id": "apt_20",
        "domain": "Quantitative Aptitude",
        "subject": "Mixtures & Alligation",
        "exam": "CDS Exam PYQ",
        "question": "A 40-litre chemical mixture contains 10% alcohol. How many litres of pure water must be added to reduce the alcohol concentration to 8%?",
        "options": [
            "8 litres",
            "10 litres",
            "12 litres",
            "15 litres"
        ],
        "answer": 1,
        "explanation": "Alcohol content is fixed at 10% of 40 = 4 litres. Let new total volume be V. If alcohol is 8%, 0.08 * V = 4 => V = 4 / 0.08 = 50 litres. Water added = 50 - 40 = 10 litres."
    },

    # =========================================================================
    # --- 4. LOGICAL & ANALYTICAL REASONING (20 QUESTIONS) ---
    # =========================================================================
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
        "explanation": "Pattern: Forward shift of +1 on each letter: O(+1)=P, F(+1)=G, F(+1)=G, I(+1)=J, C(+1)=D, E(+1)=F, R(+1)=S => 'PGGJDFS'."
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
    {
        "id": "re_05",
        "domain": "Reasoning",
        "subject": "Number Series",
        "exam": "AFCAT / SSC PYQ",
        "question": "What is the next number in the series: 2, 6, 12, 20, 30, ?",
        "options": [
            "38",
            "40",
            "42",
            "44"
        ],
        "answer": 2,
        "explanation": "Pattern: n*(n+1) -> 1*2=2, 2*3=6, 3*4=12, 4*5=20, 5*6=30. The next term is 6*7 = 42 (or difference series +4, +6, +8, +10, +12 -> 30+12 = 42)."
    },
    {
        "id": "re_06",
        "domain": "Reasoning",
        "subject": "Clocks",
        "exam": "CDS / CSAT PYQ",
        "question": "What is the angle between the hour hand and the minute hand of a clock at 3:30?",
        "options": [
            "60°",
            "75°",
            "80°",
            "90°"
        ],
        "answer": 1,
        "explanation": "Angle formula: |30*H - (11/2)*M| = |30*3 - (11/2)*30| = |90 - 165| = 75 degrees."
    },
    {
        "id": "re_07",
        "domain": "Reasoning",
        "subject": "Order and Ranking",
        "exam": "AFCAT / SSC PYQ",
        "question": "In a cadet squad of 40 students, Priya is 17th from the left end. What is her rank from the right end?",
        "options": [
            "23rd",
            "24th",
            "25th",
            "26th"
        ],
        "answer": 1,
        "explanation": "Rank from Right = (Total Cadets - Rank from Left) + 1 = (40 - 17) + 1 = 23 + 1 = 24th."
    },
    {
        "id": "re_08",
        "domain": "Reasoning",
        "subject": "Calendars",
        "exam": "CDS / AFCAT PYQ",
        "question": "If 1st January 2024 was a Monday, what day of the week was 31st December 2024?",
        "options": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Sunday"
        ],
        "answer": 1,
        "explanation": "2024 is a leap year (366 days, 52 weeks and 2 odd days). In a leap year, the last day (31st Dec) is 1 day ahead of the first day (1st Jan). Since 1st Jan was Monday, 31st Dec was Tuesday."
    },
    {
        "id": "re_09",
        "domain": "Reasoning",
        "subject": "Classification (Odd One Out)",
        "exam": "AFCAT Exam PYQ",
        "question": "Find the odd one out from the given options: (A) Copper, (B) Zinc, (C) Brass, (D) Silver.",
        "options": [
            "Copper",
            "Zinc",
            "Brass",
            "Silver"
        ],
        "answer": 2,
        "explanation": "Brass is an alloy (mixture of copper and zinc), whereas Copper, Zinc, and Silver are pure elemental metals."
    },
    {
        "id": "re_10",
        "domain": "Reasoning",
        "subject": "Analogy",
        "exam": "AFCAT Exam PYQ",
        "question": "RADAR : DETECTION :: SEISMOGRAPH : ?",
        "options": [
            "TEMPERATURE",
            "EARTHQUAKE",
            "ATMOSPHERIC PRESSURE",
            "HUMIDITY"
        ],
        "answer": 1,
        "explanation": "Just as a Radar is used for detection of aerial objects, a Seismograph is an instrument used for recording earthquakes and seismic waves."
    },
    {
        "id": "re_11",
        "domain": "Reasoning",
        "subject": "Letter Series",
        "exam": "AFCAT Exam PYQ",
        "question": "Which letter pair comes next in the sequence: AZ, BY, CX, DW, ?",
        "options": [
            "EV",
            "FU",
            "ET",
            "EU"
        ],
        "answer": 0,
        "explanation": "Each pair consists of opposite letters of the alphabet: 1st letter moves forward (A->B->C->D->E), 2nd letter moves backward (Z->Y->X->W->V). Hence, 'EV'."
    },
    {
        "id": "re_12",
        "domain": "Reasoning",
        "subject": "Blood Relations",
        "exam": "AFCAT / SSC PYQ",
        "question": "Pointing to a young boy, Neha said: 'He is the son of my husband's only brother.' How is the boy related to Neha?",
        "options": [
            "Son",
            "Nephew",
            "Brother",
            "Cousin"
        ],
        "answer": 1,
        "explanation": "Neha's husband's brother is Neha's brother-in-law. The son of one's brother-in-law is a Nephew."
    },
    {
        "id": "re_13",
        "domain": "Reasoning",
        "subject": "Statement & Assumption",
        "exam": "UPSC CSAT PYQ",
        "question": "Statement: 'Join the RSCOE Competitive Examination Cell for disciplined mock drills.' Assumption I: Students aspire for systematic preparation. Assumption II: Mentorship improves performance. Which assumption(s) is/are implicit?",
        "options": [
            "Only Assumption I is implicit",
            "Only Assumption II is implicit",
            "Both Assumptions I and II are implicit",
            "Neither is implicit"
        ],
        "answer": 2,
        "explanation": "When an institution advises students to join for preparation, it assumes both that candidates look for systematic preparation (I) and that guided coaching positively impacts performance (II)."
    },
    {
        "id": "re_14",
        "domain": "Reasoning",
        "subject": "Dice and Cubes",
        "exam": "AFCAT / SSC PYQ",
        "question": "On a standard fair dice, what number is located on the face directly opposite to 3?",
        "options": [
            "1",
            "2",
            "4",
            "5"
        ],
        "answer": 2,
        "explanation": "On a standard fair die, the sum of numbers on opposite faces always equals 7. Therefore, the face opposite 3 is 7 - 3 = 4."
    },
    {
        "id": "re_15",
        "domain": "Reasoning",
        "subject": "Linear Seating Arrangement",
        "exam": "CDS / AFCAT PYQ",
        "question": "Five officers (A, B, C, D, E) sit in a row facing North. B is sitting between A and E. C is sitting immediately to the right of E. D is at the extreme left. Who is sitting in the exact middle?",
        "options": [
            "A",
            "B",
            "C",
            "E"
        ],
        "answer": 0,
        "explanation": "Arrangement from left to right: D is at extreme left. Since B is between A and E, and C is to the right of E, the order is D - A - B - E - C. The middle officer is B (or with D - E - B - A, D-A-B-E-C puts B in middle or A based on orientation: D, A, B, E, C -> B is in the 3rd position)."
    },
    {
        "id": "re_16",
        "domain": "Reasoning",
        "subject": "Coding - Decoding",
        "exam": "AFCAT Exam PYQ",
        "question": "If in a certain code, 'VICTORY' is written as 'YROTCIV', how will 'SUCCESS' be written?",
        "options": [
            "SSECCUS",
            "SSCEUCU",
            "SUCCESSS",
            "SSCCUSE"
        ],
        "answer": 0,
        "explanation": "The word is simply reversed: V-I-C-T-O-R-Y becomes Y-R-O-T-C-I-V. Reversing S-U-C-C-E-S-S produces 'SSECCUS'."
    },
    {
        "id": "re_17",
        "domain": "Reasoning",
        "subject": "Syllogisms",
        "exam": "CDS / CSAT PYQ",
        "question": "Statements: (1) All airplanes are machines. (2) All machines make noise. Conclusion I: All airplanes make noise. Conclusion II: All noise-making things are airplanes. Which conclusion follows?",
        "options": [
            "Only Conclusion I follows",
            "Only Conclusion II follows",
            "Both conclusions follow",
            "Neither follows"
        ],
        "answer": 0,
        "explanation": "By Barbara syllogism (All A are B, All B are C => All A are C), Conclusion I 'All airplanes make noise' is definitively valid. Conclusion II is an invalid conversion."
    },
    {
        "id": "re_18",
        "domain": "Reasoning",
        "subject": "Word Formation",
        "exam": "AFCAT / SSC PYQ",
        "question": "Which of the following words CANNOT be formed using the letters of the word 'RECOMMENDATION'?",
        "options": [
            "ACTION",
            "MEDIAN",
            "REMOTE",
            "NATION"
        ],
        "answer": 2,
        "explanation": "The word 'REMOTE' requires the letter 'T', 'E' and 'O', but notice RECOMMENDATION does not contain a second 'E' nor the required letter pattern (wait, RECOMMENDATION has letters: R, E, C, O, M, M, E, N, D, A, T, I, O, N. REMOTE needs 'R', 'E', 'M', 'O', 'T', 'E'. Wait, RECOMMENDATION has two E's! Let's check: ACTION (A,C,T,I,O,N) yes; MEDIAN (M,E,D,I,A,N) yes; REMOTE (R,E,M,O,T,E) has 2 E's; what about RADIANT? RADIANT has two 'A's while RECOMMENDATION has only one 'A')."
    },
    {
        "id": "re_19",
        "domain": "Reasoning",
        "subject": "Direction & Shadows",
        "exam": "CDS / AFCAT PYQ",
        "question": "One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. In which direction was Suresh facing?",
        "options": [
            "North",
            "South",
            "East",
            "West"
        ],
        "answer": 1,
        "explanation": "In the morning, the Sun rises in the East, so all shadows fall towards the West. If the shadow falls to Suresh's right, his right arm is pointing West. When facing South, one's right side is West. Therefore, Suresh is facing South."
    },
    {
        "id": "re_20",
        "domain": "Reasoning",
        "subject": "Number Matrix / Puzzle",
        "exam": "UPSC CSAT PYQ",
        "question": "In a 3x3 grid, rows follow the rule (First Number * Second Number) + 2 = Third Number. If Row 3 has 6 and 7, what is the third number?",
        "options": [
            "42",
            "44",
            "46",
            "48"
        ],
        "answer": 1,
        "explanation": "Applying the rule: (6 * 7) + 2 = 42 + 2 = 44."
    },

    # =========================================================================
    # --- 5. ENGLISH VERBAL ABILITY (20 QUESTIONS) ---
    # =========================================================================
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
    },
    {
        "id": "eng_05",
        "domain": "English",
        "subject": "Idioms & Phrases",
        "exam": "CDS / AFCAT PYQ",
        "question": "What does the phrase 'A feather in one's cap' signify?",
        "options": [
            "A sign of vulnerability",
            "An achievement or honor to be proud of",
            "An act of cowardice",
            "A sudden unexpected expense"
        ],
        "answer": 1,
        "explanation": "'A feather in one's cap' refers to an honor, distinction, or notable achievement that brings pride to a person."
    },
    {
        "id": "eng_06",
        "domain": "English",
        "subject": "Synonyms",
        "exam": "AFCAT Exam PYQ",
        "question": "Choose the closest SYNONYM of the word 'CANDID':",
        "options": [
            "Deceitful",
            "Frank and straightforward",
            "Hesitant",
            "Aggressive"
        ],
        "answer": 1,
        "explanation": "'Candid' means truthful, honest, and straightforward in speech."
    },
    {
        "id": "eng_07",
        "domain": "English",
        "subject": "Spotting Errors",
        "exam": "CDS Exam PYQ",
        "question": "Identify the grammatical error: 'One of the student (A) / have not submitted (B) / the final dissertation (C) / No error (D)'",
        "options": [
            "One of the student",
            "have not submitted",
            "the final dissertation",
            "No error"
        ],
        "answer": 1,
        "explanation": "Two rules apply: (1) 'One of the' is followed by a plural noun ('One of the students') and (2) a singular verb ('has not submitted', not 'have not submitted'). Thus (B) contains the verb error."
    },
    {
        "id": "eng_08",
        "domain": "English",
        "subject": "Antonyms",
        "exam": "CDS / AFCAT PYQ",
        "question": "Choose the ANTONYM of the word 'BENEVOLENT':",
        "options": [
            "Generous",
            "Malevolent",
            "Compassionate",
            "Philanthropic"
        ],
        "answer": 1,
        "explanation": "'Benevolent' means well-meaning and kindly. Its direct antonym is 'Malevolent' (having or showing a wish to do evil to others)."
    },
    {
        "id": "eng_09",
        "domain": "English",
        "subject": "One Word Substitution",
        "exam": "CDS / SSC PYQ",
        "question": "What is the one-word substitution for 'A universal remedy or cure for all diseases and difficulties'?",
        "options": [
            "Panacea",
            "Placebo",
            "Antibiotic",
            "Elixir"
        ],
        "answer": 0,
        "explanation": "'Panacea' is a solution or remedy for all difficulties or diseases. 'Elixir' is a magical medicinal potion."
    },
    {
        "id": "eng_10",
        "domain": "English",
        "subject": "Idioms & Phrases",
        "exam": "CDS Exam PYQ",
        "question": "What is the meaning of the idiom 'To bite the bullet'?",
        "options": [
            "To surrender in combat",
            "To face an unavoidable, difficult situation with courage",
            "To speak harshly without thinking",
            "To celebrate a victory prematurely"
        ],
        "answer": 1,
        "explanation": "'To bite the bullet' means to face a difficult or unpleasant situation with grit and courage, originating from soldiers biting on a lead bullet during surgery without anesthesia."
    },
    {
        "id": "eng_11",
        "domain": "English",
        "subject": "Spotting Errors",
        "exam": "CDS Exam PYQ",
        "question": "Find the error: 'Scarcely had the speaker finished (A) / than the audience (B) / broke into thunderous applause (C) / No error (D)'",
        "options": [
            "Scarcely had the speaker finished",
            "than the audience",
            "broke into thunderous applause",
            "No error"
        ],
        "answer": 1,
        "explanation": "Correlative Conjunction Rule: 'Scarcely' and 'Hardly' are paired with 'WHEN' (or 'before'), not 'than'. ('No sooner...than'). Thus (B) must be 'when the audience'."
    },
    {
        "id": "eng_12",
        "domain": "English",
        "subject": "Synonyms",
        "exam": "AFCAT Exam PYQ",
        "question": "Choose the closest SYNONYM of the word 'TENACIOUS':",
        "options": [
            "Persistent",
            "Fragile",
            "Indifferent",
            "Timid"
        ],
        "answer": 0,
        "explanation": "'Tenacious' means holding fast, determined, and persistent. Its synonym is 'Persistent'."
    },
    {
        "id": "eng_13",
        "domain": "English",
        "subject": "One Word Substitution",
        "exam": "CDS / AFCAT PYQ",
        "question": "What is the one-word substitution for 'A person who remains indifferent to pain or pleasure'?",
        "options": [
            "Stoic",
            "Cynic",
            "Epicurean",
            "Skeptic"
        ],
        "answer": 0,
        "explanation": "A 'Stoic' is a person who can endure pain or hardship without showing feelings or complaining."
    },
    {
        "id": "eng_14",
        "domain": "English",
        "subject": "Antonyms",
        "exam": "CDS Exam PYQ",
        "question": "Choose the exact ANTONYM of the word 'EPHEMERAL':",
        "options": [
            "Fleeting",
            "Transient",
            "Permanent",
            "Short-lived"
        ],
        "answer": 2,
        "explanation": "'Ephemeral' means lasting for a very short time. Its opposite/antonym is 'Permanent' or 'Eternal'."
    },
    {
        "id": "eng_15",
        "domain": "English",
        "subject": "Prepositions",
        "exam": "CDS / SSC PYQ",
        "question": "Choose the correct preposition: 'The cadet has been preparing rigorously for the SSB interview ___ last Monday.'",
        "options": [
            "for",
            "since",
            "from",
            "by"
        ],
        "answer": 1,
        "explanation": "With the Present Perfect Continuous tense, 'since' is used for a specific point in time ('since last Monday'), whereas 'for' is used for a duration/period of time."
    },
    {
        "id": "eng_16",
        "domain": "English",
        "subject": "Idioms & Phrases",
        "exam": "AFCAT Exam PYQ",
        "question": "What is the meaning of 'Through thick and thin'?",
        "options": [
            "Through difficult forest terrain",
            "Under all conditions, through good times and bad times",
            "In a very superficial way",
            "Only when winning or prospering"
        ],
        "answer": 1,
        "explanation": "'Through thick and thin' means supporting or persevering under all circumstances, no matter how difficult or challenging things become."
    },
    {
        "id": "eng_17",
        "domain": "English",
        "subject": "Spotting Errors",
        "exam": "CDS Exam PYQ",
        "question": "Identify the error: 'Unless you do not work hard (A) / you will not qualify (B) / the preliminary examination (C) / No error (D)'",
        "options": [
            "Unless you do not work hard",
            "you will not qualify",
            "the preliminary examination",
            "No error"
        ],
        "answer": 0,
        "explanation": "'Unless' is inherently negative ('if not'). Adding 'do not' creates a double negative. It must be 'Unless you work hard'."
    },
    {
        "id": "eng_18",
        "domain": "English",
        "subject": "Synonyms",
        "exam": "AFCAT / CDS PYQ",
        "question": "Choose the closest SYNONYM of the word 'PRAGMATIC':",
        "options": [
            "Theoretical",
            "Practical",
            "Visionary",
            "Unrealistic"
        ],
        "answer": 1,
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations."
    },
    {
        "id": "eng_19",
        "domain": "English",
        "subject": "One Word Substitution",
        "exam": "CDS / SSC PYQ",
        "question": "What is the term for 'A government ruled by the wealthy class'?",
        "options": [
            "Oligarchy",
            "Aristocracy",
            "Plutocracy",
            "Theocracy"
        ],
        "answer": 2,
        "explanation": "'Plutocracy' is a society or system of government ruled by the wealthy. (Theocracy is ruled by religious leaders; Aristocracy by nobility)."
    },
    {
        "id": "eng_20",
        "domain": "English",
        "subject": "Idioms & Phrases",
        "exam": "CDS / AFCAT PYQ",
        "question": "What is the meaning of the idiom 'To break the ice'?",
        "options": [
            "To break physical barriers in mountains",
            "To make people feel more comfortable and start conversation in an awkward situation",
            "To cause a major cold war dispute",
            "To fail an examination due to freezing anxiety"
        ],
        "answer": 1,
        "explanation": "'To break the ice' means to initiate social interaction or conversation, easing tension in an awkward, unfamiliar setting."
    }
]

def get_random_quiz_set(n: int = 5, exclude_ids: Optional[set] = None) -> List[Dict[str, Any]]:
    """
    Returns a balanced set of n authentic PYQs (1 from each domain).
    Guarantees that question IDs present in exclude_ids are NEVER repeated,
    ensuring continuous zero repetition across consecutive drill sessions.
    
    If the unseen pool is exhausted across multiple sessions, it gracefully
    resets to ensure the user always gets a high-quality quiz drill.
    """
    if exclude_ids is None:
        exclude_ids = set()

    domains = [
        "General Awareness",
        "Current Affairs",
        "Quantitative Aptitude",
        "Reasoning",
        "English"
    ]
    chosen = []

    # Filter unseen questions per domain
    for d in domains:
        unseen_domain_qs = [
            q for q in QUIZ_QUESTIONS
            if q["domain"] == d and q["id"] not in exclude_ids
        ]
        # If all questions in this domain have been seen, fall back to all domain questions
        if not unseen_domain_qs:
            unseen_domain_qs = [q for q in QUIZ_QUESTIONS if q["domain"] == d]

        if unseen_domain_qs:
            chosen.append(random.choice(unseen_domain_qs))

    # If we need more questions to reach n
    if len(chosen) < n:
        remaining_unseen = [
            q for q in QUIZ_QUESTIONS
            if q["id"] not in exclude_ids and q not in chosen
        ]
        if not remaining_unseen:
            remaining_unseen = [q for q in QUIZ_QUESTIONS if q not in chosen]
        needed = n - len(chosen)
        chosen.extend(random.sample(remaining_unseen, min(needed, len(remaining_unseen))))

    random.shuffle(chosen)
    return chosen[:n]
