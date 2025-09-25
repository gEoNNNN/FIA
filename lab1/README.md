# Cyber-City Character Detection Expert System

## Overview
This project implements an expert system for character detection in a futuristic Cyber-City environment using forward and backward chaining algorithms. The system can identify 8 different character types (5 humans and 3 animals) through strategic questioning and rule-based inference.

## Project Structure
```
lab1/
├── main.py              # Main expert system interface
├── rules.py             # Character detection rules and data
├── production.py        # Forward/backward chaining algorithms
├── utils.py             # Utility functions
├── README.md            # This documentation
└── __pycache__/         # Python cache files
```

---

## Task Implementation Documentation

### Task 1: Define Character Types and Goal Tree (1p)

#### Character Types Defined
The system identifies **8 character types** in the Cyber-City environment:

**Human Characters (5 types):**
1. **Cyber Hacker** - Digital specialists with neural implants
2. **Bio Engineer** - Scientists working with biological samples
3. **Space Mechanic** - Technical specialists maintaining spacecraft
4. **Quantum Scientist** - Researchers working with quantum technology
5. **Ice World Explorer** - Specialists adapted to extreme cold environments

**Animal Characters (3 types):**
6. **Cyber Dog** - Cybernetically enhanced canines
7. **Hover Bird** - Anti-gravity enabled avians with metallic features
8. **Phase Cat** - Felines with phase-shifting abilities

#### Goal Tree Structure
```
Character Detection
├── Human Characters
│   ├── Cyber Hacker
│   │   ├── has digital_implants
│   │   │   ├── wears neural_headset
│   │   │   ├── types_rapidly
│   │   │   └── speaks_in_code
│   │   └── has glowing_eyes
│   ├── Bio Engineer
│   │   ├── has lab_coat
│   │   ├── carries_samples
│   │   └── wears safety_goggles
│   ├── Space Mechanic
│   │   ├── has oil_stains
│   │   ├── carries_plasma_torch
│   │   └── has reinforced_gloves
│   ├── Quantum Scientist
│   │   ├── has energy_scanner
│   │   ├── wears quantum_suit
│   │   └── has particle_detector
│   └── Ice World Explorer
│       ├── has thermal_gear
│       ├── has frost_crystals
│       └── moves_carefully
└── Animal Characters
    ├── Cyber Dog
    │   ├── has_cyber_fur
    │   ├── emits_electronic_barks
    │   └── has_data_collar
    ├── Hover Bird
    │   ├── has_metallic_feathers
    │   ├── hovers_with_antigrav
    │   └── makes_digital_chirps
    └── Phase Cat
        ├── has_sensor_whiskers
        ├── purrs_electronically
        └── phases_through_walls
```

---

### Task 2: Implement Rules from Goal Tree (1p)

#### Rules Implementation
The rules are implemented in `rules.py` using the provided IF, AND, OR, THEN framework:

```python
# Example: Cyber Hacker Rules
IF( AND( '(?x) has digital_implants',         # T1
         '(?x) has glowing_eyes' ),
    THEN( '(?x) is cyber_hacker' )),

IF( AND( '(?x) wears neural_headset',         # T2  
         '(?x) types_rapidly',
         '(?x) speaks_in_code' ),
    THEN( '(?x) has digital_implants' )),

# Example: Bio Engineer Rules  
IF( AND( '(?x) has lab_coat',                 # T3
         '(?x) carries_samples',
         '(?x) wears safety_goggles' ),
    THEN( '(?x) is bio_engineer' )),

# Example: Animal Rules
IF( AND( '(?x) has_cyber_fur',                # T7
         '(?x) emits_electronic_barks',
         '(?x) has_data_collar' ),
    THEN( '(?x) is cyber_dog' )),
```

#### Rule Structure Features
- **13 main rules** defining character types
- **Variable binding** using `(?x)` pattern matching
- **Hierarchical rules** supporting intermediate conclusions
- **Cross-connections** between related characteristics

---

### Task 3: Forward Chaining Implementation (0.5p)

#### Forward Chaining Algorithm
The Forward Chaining algorithm is implemented in `production.py` and works by:

1. **Starting with facts** (known information)
2. **Applying rules** to derive new facts
3. **Iterating** until no new facts can be derived

#### Example Execution
```python
# Input facts for Zara (Cyber Hacker)
facts = [
    "zara has glowing_eyes",
    "zara wears neural_headset", 
    "zara types_rapidly",
    "zara speaks_in_code"
]

# Forward chaining process:
# Step 1: Apply Rule T2
# IF (wears neural_headset AND types_rapidly AND speaks_in_code)
# THEN has digital_implants
# Result: "zara has digital_implants"

# Step 2: Apply Rule T1  
# IF (has digital_implants AND has glowing_eyes)
# THEN is cyber_hacker
# Result: "zara is cyber_hacker"
```

#### Usage in Code
```python
from production import forward_chain
from rules import TOURIST_RULES

initial_facts = ["zara has glowing_eyes", "zara wears neural_headset"]
derived_facts = forward_chain(TOURIST_RULES, initial_facts, verbose=True)
```

---

### Task 4: Backward Chaining Implementation (2p)

#### Backward Chaining Algorithm
The Backward Chaining algorithm works by:

1. **Starting with a goal** (what we want to prove)
2. **Finding rules** that could prove the goal
3. **Recursively proving** the preconditions
4. **Building a proof tree**

#### Implementation Example
```python
from production import backward_chain

# Goal: Prove someone is a cyber_hacker
goal = "zara is cyber_hacker"
proof_tree = backward_chain(TOURIST_RULES, goal, verbose=True)

# The algorithm will:
# 1. Find Rule T1: IF (digital_implants AND glowing_eyes) THEN cyber_hacker
# 2. Try to prove: "zara has digital_implants" 
# 3. Find Rule T2: IF (neural_headset AND types_rapidly AND speaks_in_code) THEN digital_implants
# 4. Try to prove each precondition recursively
```

#### Verification in Expert System
```python
def analyze_person(self):
    # ... forward chaining analysis ...
    
    # Backward chaining verification for confirmed types
    if found_types:
        for found_type in found_types:
            goal_template = f"(?x) is {found_type.lower().replace(' ', '_')}"
            goal = goal_template.replace('(?x)', self.person_name)
            goal_tree = backward_chain(self.rules, goal, verbose=False)
            print(f"🎯 Verification for {found_type}:")
            print(f"   Goal: {goal}")
            print(f"   Tree: {goal_tree}")
```

---

### Task 5: Question Generation System (2p)

#### Three Types of Questions Implemented

**1. Yes/No Questions (Primary)**
```python
questions = {
    'yes_no': {
        "(?x) has digital_implants": "Does the person have digital implants?",
        "(?x) has glowing_eyes": "Does the person have glowing eyes?",
        "(?x) wears neural_headset": "Does the person wear a neural headset?",
        "(?x) carries_samples": "Does the person carry biological samples?",
        # ... more questions
    }
}
```

**2. Strategic Questions (Context-Aware)**
The system generates strategic questions based on:
- Current evidence gathered
- Partially matched character types
- Completion percentages for each character type

```python
def get_strategic_questions(self, max_questions=5):
    scores = self.calculate_tourist_scores()
    viable_types = self.get_viable_character_types()
    
    # Focus on character types with highest potential
    # Prioritize questions that could complete a character type
    for character_type, score in sorted_types:
        if score['completion'] > 0 and score['completion'] < 1.0:
            # Add questions for remaining conditions
            for condition_template in score['remaining']:
                strategic_questions.append((condition_template, questions_map[condition_template]))
```

**3. Adaptive Questions (Dynamic)**
Questions adapt based on user responses:
- After first "yes" answer, focus only on related character types
- Eliminate irrelevant questions from unrelated categories
- Show immediate feedback after each answer

#### Question Selection Logic
```python
def get_viable_character_types(self):
    """Get character types that are still possible based on current facts"""
    viable_types = []
    scores = self.calculate_tourist_scores()
    
    for character_type, conditions in character_conditions.items():
        score = scores.get(character_type, {'completion': 0})
        if score['completion'] > 0 or len(self.facts) == 0:
            viable_types.append(character_type)
    
    return viable_types
```

---

### Task 6: Interactive Expert System (2p)

#### System Architecture
The expert system integrates both Forward and Backward Chaining:

```python
class TouristExpertSystem:
    def __init__(self):
        self.rules = TOURIST_RULES
        self.facts = set()
        self.person_name = "person"
    
    def interactive_session(self):
        """Main interactive session with strategic questioning"""
        # 1. Get character name
        # 2. Strategic questioning rounds
        # 3. Forward chaining analysis
        # 4. Backward chaining verification
```

#### Interactive Flow
```
1. Character Name Input
   ↓
2. Strategic Question Rounds (5 rounds max, 3 questions each)
   ├── Display current analysis
   ├── Ask strategic questions
   ├── Update facts
   └── Check for definitive classification
   ↓
3. Final Analysis
   ├── Forward Chaining Results
   ├── Progress Report
   └── Backward Chaining Verification
```

#### Dual Algorithm Integration
```python
def analyze_person(self):
    # Forward Chaining Analysis
    initial_facts = list(self.facts)
    derived_facts = forward_chain(self.rules, initial_facts, verbose=False)
    
    # Find character types
    found_types = []
    for fact in derived_facts:
        for character_type in character_types:
            if f"{self.person_name} is {character_type}" in fact:
                found_types.append(character_type.replace('_', ' ').title())
    
    # Backward Chaining Verification
    if found_types:
        for found_type in found_types:
            goal = f"(?x) is {found_type.lower().replace(' ', '_')}"
            goal = goal.replace('(?x)', self.person_name)
            goal_tree = backward_chain(self.rules, goal, verbose=False)
```

---

### Task 7: Human-Readable Output Format (Grammar Compliance)

#### Formatted Output Examples

**1. Character Analysis Display**
```
📊 Character Type Analysis:
============================================================
🧑 HUMAN CHARACTERS:
   🔄 Cyber Hacker        : 2/2 conditions (100.0%)
   ⚪ Bio Engineer        : 0/3 conditions (0.0%)
   ⚪ Space Mechanic      : 0/3 conditions (0.0%)
   ⚪ Quantum Scientist   : 0/3 conditions (0.0%)
   ⚪ Ice World Explorer  : 0/3 conditions (0.0%)

🐾 ANIMAL CHARACTERS:
   ⚪ Cyber Dog           : 0/3 conditions (0.0%)
   ⚪ Hover Bird          : 0/3 conditions (0.0%)
   ⚪ Phase Cat           : 0/3 conditions (0.0%)
```

**2. Question Formatting**
```python
# Proper grammar and natural language
"Does the person have digital implants?"
"Does the person wear a neural headset?"
"Can the animal phase through walls?"
"Has the person survived gang wars?"
```

**3. Results Display**
```
🔍 Forward Chaining Analysis for Zara:
----------------------------------------
✅ Zara is identified as: Cyber Hacker

📋 Facts collected about Zara:
   • zara has digital_implants
   • zara has glowing_eyes
   • zara speaks_in_code
   • zara types_rapidly
   • zara wears neural_headset

🧠 Additional facts derived:
   • zara is cyber_hacker

🔄 Backward Chaining Verification:
----------------------------------------
🎯 Verification for Cyber Hacker:
   Goal: zara is cyber_hacker
   Tree: [Proof tree structure]
```

#### Grammar Features
- **Proper capitalization** in all outputs
- **Complete sentences** for questions
- **Consistent terminology** throughout
- **Professional formatting** with emojis for clarity
- **Progressive tense** for ongoing analysis
- **Clear status indicators** (✅, 🔄, ⚪, 📊, 🎯)

---

## Usage Instructions

### Running the System
```bash
python main.py
```

### Menu Options
1. **Interactive Analysis** - Smart questioning system
2. **Demo Mode** - Pre-configured character examples
3. **Exit** - Close the application

### Example Session
```
Cyber-City Character Detection Expert System
Choose an option:
1. Interactive Analysis (Smart Questioning)
2. Demo Mode
3. Exit

Enter your choice (1-3): 1

What is the name of the character you want to analyze? Alex

Great! Now I'll ask you strategic questions about Alex.
The system will focus on the most promising character types based on your answers.

==================================================
ROUND 1
==================================================

📊 Character Type Analysis:
[... character analysis display ...]

Does the person have glowing eyes? (yes/no): yes
✓ Noted: Alex Has Glowing Eyes
   📈 Most likely: Cyber Hacker (50%)

Does the person wear a neural headset? (yes/no): yes
✓ Noted: Alex Wears Neural Headset
   📈 Most likely: Cyber Hacker (67%)

🎉 Definitive classification found: Cyber Hacker
```

---

## Technical Implementation Details

### Key Classes and Methods

#### TouristExpertSystem Class
- `__init__()` - Initialize system with rules and facts
- `get_rule_conditions()` - Extract conditions from rules by character type
- `generate_questions()` - Create question mappings
- `calculate_tourist_scores()` - Calculate completion percentages
- `get_strategic_questions()` - Generate context-aware questions
- `interactive_session()` - Main user interaction loop
- `analyze_person()` - Comprehensive analysis with both algorithms

### Algorithm Integration
- **Forward Chaining**: Used for deriving conclusions from facts
- **Backward Chaining**: Used for verification and proof construction
- **Strategic Questioning**: Optimizes question selection based on current evidence

### Performance Features
- **Smart question filtering** avoids irrelevant questions
- **Immediate feedback** after each user response  
- **Progress tracking** shows completion percentages
- **Early termination** when classification is found

---

## Character Data Examples

### Sample Characters in System
```python
# Zara - Cyber Hacker
'zara has glowing_eyes',
'zara wears neural_headset',
'zara types_rapidly',
'zara speaks_in_code'

# Dr. Kane - Bio Engineer  
'kane has lab_coat',
'kane carries_samples', 
'kane wears safety_goggles'

# Byte - Cyber Dog
'byte has_cyber_fur',
'byte emits_electronic_barks',
'byte has_data_collar'
```

---

## Conclusion

This expert system successfully implements all required tasks:

✅ **Task 1**: 8 character types defined with comprehensive goal tree  
✅ **Task 2**: Rules implemented using IF/AND/OR/THEN framework  
✅ **Task 3**: Forward chaining with detailed examples  
✅ **Task 4**: Backward chaining for goal verification  
✅ **Task 5**: Three types of question generation systems  
✅ **Task 6**: Interactive expert system with dual algorithm integration  
✅ **Task 7**: Human-readable, grammatically correct output formatting  

The system provides an efficient, user-friendly interface for character detection in the Cyber-City environment while demonstrating both forward and backward chaining inference capabilities.