from production import forward_chain, backward_chain, IF, AND, OR, THEN, match, instantiate
from rules import TOURIST_RULES, TOURIST_DATA, TOURIST_GOALS
import random

class TouristExpertSystem:
    def __init__(self):
        self.rules = TOURIST_RULES
        self.facts = set()
        self.person_name = "person"
        
    def get_rule_conditions(self):
        """Extract all conditions from rules organized by character type"""
        character_conditions = {}
        
        for rule in self.rules:
            consequent = rule.consequent()[0] if rule.consequent() else ""
            if " is " in consequent:
                # Extract character type from consequent
                character_type = consequent.split(" is ")[-1]
                if character_type not in character_conditions:
                    character_conditions[character_type] = []
                
                # Extract conditions from antecedent
                antecedent = rule.antecedent()
                if isinstance(antecedent, AND):
                    for condition in antecedent:
                        if condition not in character_conditions[character_type]:
                            character_conditions[character_type].append(condition)
                else:
                    if antecedent not in character_conditions[character_type]:
                        character_conditions[character_type].append(antecedent)
        
        return character_conditions
        
    def generate_questions(self):
        """Generate THREE types of questions based on rule antecedents"""
        questions = {
            # TYPE 1: Yes/No Questions
            'yes_no': {
                "(?x) has digital_implants": "Does the person have digital implants?",
                "(?x) has glowing_eyes": "Does the person have glowing eyes?",
                "(?x) wears neural_headset": "Does the person wear a neural headset?",
                "(?x) types_rapidly": "Does the person type rapidly?",
                "(?x) speaks_in_code": "Does the person speak in code?",
                "(?x) glitches_frequently": "Does the person glitch frequently?",
                "(?x) speaks_binary": "Does the person speak binary?",
                "(?x) complains_about_system_lag": "Does the person complain about system lag?",
                "(?x) has lab_coat": "Does the person wear a lab coat?",
                "(?x) carries_samples": "Does the person carry biological samples?",
                "(?x) wears safety_goggles": "Does the person wear safety goggles?",
                "(?x) has oil_stains": "Does the person have oil stains on their clothes?",
                "(?x) carries_plasma_torch": "Does the person carry a plasma torch?",
                "(?x) has reinforced_gloves": "Does the person wear reinforced gloves?",
                "(?x) has energy_scanner": "Does the person have an energy scanner?",
                "(?x) wears quantum_suit": "Does the person wear a quantum suit?",
                "(?x) has particle_detector": "Does the person have a particle detector?",
                "(?x) has thermal_gear": "Does the person have thermal gear?",
                "(?x) has frost_crystals": "Does the person have frost crystals on their equipment?",
                "(?x) moves_carefully": "Does the person move carefully?",
                "(?x) has_cyber_origins": "Does the person have cyber origins?",
                # Animal characteristics
                "(?x) has_cyber_fur": "Does the animal have cyber fur?",
                "(?x) emits_electronic_barks": "Does the animal emit electronic barks?",
                "(?x) has_data_collar": "Does the animal have a data collar?",
                "(?x) has_metallic_feathers": "Does the animal have metallic feathers?",
                "(?x) hovers_with_antigrav": "Does the animal hover with anti-gravity?",
                "(?x) makes_digital_chirps": "Does the animal make digital chirping sounds?",
                "(?x) has_sensor_whiskers": "Does the animal have sensor whiskers?",
                "(?x) purrs_electronically": "Does the animal purr electronically?",
                "(?x) phases_through_walls": "Can the animal phase through walls?",
            },
            
            # TYPE 2: Multiple Choice Questions (Fixed with "Other" option)
            'multiple_choice': {
                "(?x) has digital_implants": {
                    'question': "What type of technological enhancement does the person have?",
                    'options': {
                        'a': "Digital implants and neural interfaces",
                        'b': "Basic communication device only", 
                        'c': "No technological enhancements",
                        'd': "Unknown/Not visible",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) has digital_implants"},
                    'skip_options': ['b', 'c', 'd', 'e']  # Options that don't generate facts
                },
                "(?x) wears neural_headset": {
                    'question': "What kind of headgear is the person/animal wearing?",
                    'options': {
                        'a': "Neural headset with blinking lights",
                        'b': "Standard protective helmet",
                        'c': "No headgear",
                        'd': "Simple hat or cap",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) wears neural_headset"},
                    'skip_options': ['b', 'c', 'd', 'e']
                },
                "(?x) has lab_coat": {
                    'question': "What type of clothing is the person/animal wearing?",
                    'options': {
                        'a': "White laboratory coat",
                        'b': "Casual street clothes",
                        'c': "Heavy protective armor",
                        'd': "Business suit",
                        'e': "Other/None of the above (including animals with fur/feathers)"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) has lab_coat"},
                    'skip_options': ['b', 'c', 'd', 'e']
                },
                "(?x) carries_plasma_torch": {
                    'question': "What tools is the person/animal carrying or using?",
                    'options': {
                        'a': "Plasma torch and welding equipment",
                        'b': "Scientific instruments and samples",
                        'c': "Computer and digital equipment",
                        'd': "No visible tools",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) carries_plasma_torch"},
                    'skip_options': ['b', 'c', 'd', 'e']
                },
                "(?x) has energy_scanner": {
                    'question': "What type of scanning equipment does the person have?",
                    'options': {
                        'a': "Energy scanner and quantum detection devices",
                        'b': "Basic medical scanner",
                        'c': "Simple communication device",
                        'd': "No scanning equipment",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) has energy_scanner"},
                    'skip_options': ['b', 'c', 'd', 'e']
                },
                "(?x) has thermal_gear": {
                    'question': "What type of protective gear does the person/animal have?",
                    'options': {
                        'a': "Thermal protection and cold-weather gear",
                        'b': "Standard protective clothing",
                        'c': "Light casual wear",
                        'd': "No protective gear",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) has thermal_gear"},
                    'skip_options': ['b', 'c', 'd', 'e']
                },
                "(?x) has_cyber_fur": {
                    'question': "What type of fur/coating does the animal have?",
                    'options': {
                        'a': "Cybernetic fur with electronic components",
                        'b': "Natural fur without modifications",
                        'c': "Synthetic coating",
                        'd': "No fur/smooth skin",
                        'e': "Other/None of the above"
                    },
                    'correct_answers': ['a'],
                    'fact_mapping': {'a': "(?x) has_cyber_fur"},
                    'skip_options': ['b', 'c', 'd', 'e']
                }
            },
            
            # TYPE 3: Scale/Rating Questions  
            'scale': {
                "(?x) types_rapidly": {
                    'question': "How would you rate the person's typing speed? (1-5 scale)",
                    'scale_range': (1, 5),
                    'threshold': 4,  # 4 or 5 means "types rapidly"
                    'labels': {1: "Very slow", 2: "Slow", 3: "Average", 4: "Fast", 5: "Extremely fast"}
                },
                "(?x) moves_carefully": {
                    'question': "How carefully does the person/animal move? (1-5 scale)",
                    'scale_range': (1, 5),
                    'threshold': 4,  # 4 or 5 means "moves carefully"
                    'labels': {1: "Reckless", 2: "Careless", 3: "Normal", 4: "Careful", 5: "Extremely cautious"}
                },
                "(?x) glitches_frequently": {
                    'question': "How often does the person/animal experience glitches or malfunctions? (1-5 scale)",
                    'scale_range': (1, 5),
                    'threshold': 4,  # 4 or 5 means "glitches frequently"
                    'labels': {1: "Never", 2: "Rarely", 3: "Sometimes", 4: "Often", 5: "Constantly"}
                },
                "(?x) speaks_in_code": {
                    'question': "How often does the person use technical jargon or code language? (1-5 scale)",
                    'scale_range': (1, 5),
                    'threshold': 4,  # 4 or 5 means "speaks in code"
                    'labels': {1: "Never", 2: "Rarely", 3: "Sometimes", 4: "Frequently", 5: "Always"}
                }
            }
        }
        return questions
    
    def calculate_tourist_scores(self):
        """Calculate how close we are to proving each character type"""
        scores = {}
        character_conditions = self.get_rule_conditions()
        
        for character_type, conditions in character_conditions.items():
            if not conditions:
                continue
                
            matched = 0
            total = len(conditions)
            
            for condition_template in conditions:
                condition = condition_template.replace('(?x)', self.person_name)
                if condition in self.facts:
                    matched += 1
            
            # Calculate completion percentage
            completion = matched / total if total > 0 else 0
            scores[character_type] = {
                'matched': matched,
                'total': total,
                'completion': completion,
                'remaining': [c for c in conditions if c.replace('(?x)', self.person_name) not in self.facts]
            }
        
        return scores
    
    def get_viable_character_types(self):
        """Get character types that are still possible based on current facts"""
        scores = self.calculate_tourist_scores()
        character_conditions = self.get_rule_conditions()
        
        viable_types = []
        
        for character_type, conditions in character_conditions.items():
            score = scores.get(character_type, {'completion': 0})
            if score['completion'] > 0:
                viable_types.append(character_type)
            elif len(self.facts) == 0:  # If no facts yet, all types are viable
                viable_types.append(character_type)
            else:
                viable_types.append(character_type)  # For now, keep all types viable
        
        return viable_types
    
    def get_strategic_questions(self, max_questions=3):
        """Get strategic questions of different types based on current evidence"""
        scores = self.calculate_tourist_scores()
        questions_data = self.generate_questions()
        viable_types = self.get_viable_character_types()
        
        # Filter scores to only include viable character types
        viable_scores = {k: v for k, v in scores.items() if k in viable_types}
        
        # Sort character types by completion percentage (descending)
        sorted_types = sorted(viable_scores.items(), key=lambda x: x[1]['completion'], reverse=True)
        
        strategic_questions = []
        asked_conditions = set()
        
        print(f"\n📊 Character Type Analysis:")
        print("=" * 60)
        
        # Group character types
        human_types = []
        animal_types = []
        
        for character_type, score in sorted_types:
            if character_type in ['cyber_dog', 'hover_bird', 'phase_cat']:
                animal_types.append((character_type, score))
            else:
                human_types.append((character_type, score))
        
        # Display Human characters
        if human_types:
            print("🧑 HUMAN CHARACTERS:")
            for character_type, score in human_types:
                status_icon = "✅" if score['completion'] == 1.0 else "🔄" if score['completion'] > 0 else "⚪"
                character_name = character_type.replace('_', ' ').title()
                print(f"   {status_icon} {character_name:<20}: {score['matched']}/{score['total']} conditions ({score['completion']:.1%})")
        
        # Display Animal characters
        if animal_types:
            print("\n🐾 ANIMAL CHARACTERS:")
            for character_type, score in animal_types:
                status_icon = "✅" if score['completion'] == 1.0 else "🔄" if score['completion'] > 0 else "⚪"
                character_name = character_type.replace('_', ' ').title()
                print(f"   {status_icon} {character_name:<20}: {score['matched']}/{score['total']} conditions ({score['completion']:.1%})")
        
        print("=" * 60)
        
        # Collect all conditions that could help with viable character types
        relevant_conditions = set()
        for character_type, score in sorted_types:
            for condition in score['remaining']:
                relevant_conditions.add(condition)
        
        # Strategy: Mix different question types for variety and effectiveness
        question_types = ['yes_no', 'multiple_choice', 'scale']
        current_type_index = 0
        
        # Prioritize questions for character types that are partially matched
        for character_type, score in sorted_types:
            if score['completion'] == 0:
                continue  # Skip types with no matches initially
                
            if score['completion'] == 1.0:
                continue  # Skip completed types
            
            # Add questions for remaining conditions of this character type
            for condition_template in score['remaining']:
                if condition_template in asked_conditions:
                    continue
                
                # Try to use different question types in rotation
                question_type = question_types[current_type_index % len(question_types)]
                
                if condition_template in questions_data[question_type]:
                    strategic_questions.append({
                        'condition': condition_template,
                        'type': question_type,
                        'data': questions_data[question_type][condition_template]
                    })
                    asked_conditions.add(condition_template)
                    current_type_index += 1
                    
                    if len(strategic_questions) >= max_questions:
                        break
            
            if len(strategic_questions) >= max_questions:
                break
        
        # If we still need more questions and have no partial matches, add some general ones
        if len(strategic_questions) < max_questions and len(self.facts) == 0:
            remaining_conditions = list(relevant_conditions - asked_conditions)
            random.shuffle(remaining_conditions)
            
            for condition_template in remaining_conditions:
                question_type = question_types[current_type_index % len(question_types)]
                
                if condition_template in questions_data[question_type]:
                    strategic_questions.append({
                        'condition': condition_template,
                        'type': question_type,
                        'data': questions_data[question_type][condition_template]
                    })
                    asked_conditions.add(condition_template)
                    current_type_index += 1
                    
                    if len(strategic_questions) >= max_questions:
                        break
        
        return strategic_questions
        
    def ask_question(self, question_info):
        """Ask a question based on its type and return the corresponding fact"""
        condition_template = question_info['condition']
        question_type = question_info['type']
        question_data = question_info['data']
        
        print(f"\n[{question_type.upper().replace('_', ' ')} QUESTION]")
        
        if question_type == 'yes_no':
            while True:
                answer = input(f"{question_data} (yes/no): ").lower().strip()
                if answer in ['yes', 'y']:
                    return condition_template.replace('(?x)', self.person_name)
                elif answer in ['no', 'n']:
                    return None
                else:
                    print("Please answer with 'yes' or 'no'.")
                    
        elif question_type == 'multiple_choice':
            print(question_data['question'])
            for key, option in question_data['options'].items():
                print(f"  {key.upper()}) {option}")
            
            while True:
                answer = input("Choose an option (a/b/c/d/e): ").lower().strip()
                if answer in question_data['options']:
                    # Check if this answer should generate a fact
                    if answer in question_data['correct_answers']:
                        fact_template = question_data['fact_mapping'][answer]
                        return fact_template.replace('(?x)', self.person_name)
                    elif answer in question_data.get('skip_options', []):
                        print("   ℹ️  No relevant information extracted from this answer.")
                        return None  # Skip this question - no fact generated
                    else:
                        return None
                else:
                    print("Please choose a valid option (a, b, c, d, or e).")
                    
        elif question_type == 'scale':
            print(question_data['question'])
            print("Scale:")
            for value, label in question_data['labels'].items():
                print(f"  {value} - {label}")
            
            while True:
                try:
                    answer = int(input(f"Enter rating ({question_data['scale_range'][0]}-{question_data['scale_range'][1]}): "))
                    if question_data['scale_range'][0] <= answer <= question_data['scale_range'][1]:
                        if answer >= question_data['threshold']:
                            return condition_template.replace('(?x)', self.person_name)
                        else:
                            return None
                    else:
                        print(f"Please enter a number between {question_data['scale_range'][0]} and {question_data['scale_range'][1]}.")
                except ValueError:
                    print("Please enter a valid number.")
        
        return None
    
    def interactive_session(self):
        """Main interactive session with strategic questioning using 3 question types"""
        print("="*60)
        print("Welcome to the Cyber-City Character Detection Expert System!")
        print("="*60)
        print("\nThis system will help identify what type of character someone is")
        print("in the futuristic Cyber-City environment.")
        print("\n🎯 The system uses 3 types of questions:")
        print("   📝 YES/NO Questions - Simple binary choices")
        print("   🔢 MULTIPLE CHOICE Questions - Select from options (including 'Other/None')")  
        print("   📊 SCALE Questions - Rate on a 1-5 scale")
        print()
        
        self.person_name = input("What is the name of the character you want to analyze? ").strip()
        if not self.person_name:
            self.person_name = "person"
            
        print(f"\nGreat! Now I'll ask you strategic questions about {self.person_name}.")
        print("The system will use different question types based on what's most effective.")
        print("💡 Tip: For multiple choice questions, you can always choose 'Other/None' if no option fits!\n")
        
        max_rounds = 5
        questions_per_round = 3
        
        for round_num in range(1, max_rounds + 1):
            print(f"\n{'='*50}")
            print(f"ROUND {round_num}")
            print(f"{'='*50}")
            
            # Get strategic questions for this round
            strategic_questions = self.get_strategic_questions(questions_per_round)
            
            if not strategic_questions:
                print("No more relevant questions to ask.")
                break
            
            # Ask the strategic questions
            for question_info in strategic_questions:
                fact = self.ask_question(question_info)
                if fact:
                    self.facts.add(fact)
                    print(f"✓ Noted: {fact.replace(self.person_name, self.person_name.title())}")
                    
                    # After adding a fact, re-evaluate immediately
                    self.quick_evaluation_after_fact()
            
            # Analyze current state
            results = self.analyze_person_quick()
            
            # Check if we have a definitive answer
            if results['definitive']:
                print(f"\n🎉 Definitive classification found: {results['types']}")
                break
                
            # Ask if user wants to continue
            if round_num < max_rounds:
                continue_asking = input(f"\nContinue with next round of questions? (yes/no): ").lower().strip()
                if continue_asking in ['no', 'n']:
                    break
        
        return self.analyze_person()
    
    def quick_evaluation_after_fact(self):
        """Quick evaluation after adding a fact to show progress"""
        initial_facts = list(self.facts)
        try:
            derived_facts = forward_chain(self.rules, initial_facts, verbose=False)
            
            # Check if we derived any new character classifications
            character_types = ['cyber_hacker', 'bio_engineer', 'space_mechanic', 
                              'quantum_scientist', 'ice_world_explorer',
                              'cyber_dog', 'hover_bird', 'phase_cat']
            
            for fact in derived_facts:
                for character_type in character_types:
                    if f"{self.person_name} is {character_type}" in fact:
                        character_name = character_type.replace('_', ' ').title()
                        print(f"   🎯 Identified as {character_name}!")
                        return
            
            # Show the top 2 most promising character types
            scores = self.calculate_tourist_scores()
            sorted_scores = sorted(scores.items(), key=lambda x: x[1]['completion'], reverse=True)
            
            if len(sorted_scores) >= 2:
                top_two = sorted_scores[:2]
                if top_two[0][1]['completion'] > 0:
                    print(f"   📈 Most likely: {top_two[0][0].replace('_', ' ').title()} ({top_two[0][1]['completion']:.1%})")
                    if top_two[1][1]['completion'] > 0:
                        print(f"   📊 Second: {top_two[1][0].replace('_', ' ').title()} ({top_two[1][1]['completion']:.1%})")
                        
        except Exception as e:
            pass  # Ignore errors in quick evaluation
    
    def analyze_person_quick(self):
        """Quick analysis without full output"""
        initial_facts = list(self.facts)
        derived_facts = forward_chain(self.rules, initial_facts, verbose=False)
        
        character_types = ['cyber_hacker', 'bio_engineer', 'space_mechanic', 
                          'quantum_scientist', 'ice_world_explorer',
                          'cyber_dog', 'hover_bird', 'phase_cat']
        
        found_types = []
        for fact in derived_facts:
            for character_type in character_types:
                if f"{self.person_name} is {character_type}" in fact:
                    found_types.append(character_type.replace('_', ' ').title())
        
        return {
            'definitive': len(found_types) > 0,
            'types': ', '.join(found_types) if found_types else 'Unknown'
        }
    
    def analyze_person(self):
        """Analyze the person using both forward and backward chaining"""
        print(f"\n{'='*50}")
        print("FINAL ANALYSIS RESULTS")
        print(f"{'='*50}")
        
        # Forward chaining analysis
        print(f"\n🔍 Forward Chaining Analysis for {self.person_name.title()}:")
        print("-" * 40)
        
        initial_facts = list(self.facts)
        derived_facts = forward_chain(self.rules, initial_facts, verbose=False)
        
        results = {}
        character_types = ['cyber_hacker', 'bio_engineer', 'space_mechanic', 
                          'quantum_scientist', 'ice_world_explorer',
                          'cyber_dog', 'hover_bird', 'phase_cat']
        
        found_types = []
        for fact in derived_facts:
            for character_type in character_types:
                if f"{self.person_name} is {character_type}" in fact:
                    found_types.append(character_type.replace('_', ' ').title())
                    
        if found_types:
            print(f"✅ {self.person_name.title()} is identified as: {', '.join(found_types)}")
            for character_type in found_types:
                results[character_type] = "Confirmed"
        else:
            print(f"❓ Could not definitively classify {self.person_name.title()}")
            results["Classification"] = "Unknown"
            
            # Show progress towards each type
            scores = self.calculate_tourist_scores()
            print(f"\n📊 Complete Progress Report:")
            
            # Group and display all character types
            human_types = []
            animal_types = []
            
            for character_type, score in sorted(scores.items(), key=lambda x: x[1]['completion'], reverse=True):
                if character_type in ['cyber_dog', 'hover_bird', 'phase_cat']:
                    animal_types.append((character_type, score))
                else:
                    human_types.append((character_type, score))
            
            if human_types:
                print("\n   🧑 Human Characters:")
                for character_type, score in human_types:
                    status = "✅ IDENTIFIED" if score['completion'] == 1.0 else f"🔄 {score['completion']:.1%}"
                    character_name = character_type.replace('_', ' ').title()
                    print(f"      {character_name:<20}: {score['matched']}/{score['total']} conditions ({status})")
            
            if animal_types:
                print("\n   🐾 Animal Characters:")
                for character_type, score in animal_types:
                    status = "✅ IDENTIFIED" if score['completion'] == 1.0 else f"🔄 {score['completion']:.1%}"
                    character_name = character_type.replace('_', ' ').title()
                    print(f"      {character_name:<20}: {score['matched']}/{score['total']} conditions ({status})")
        
        # Show all facts
        print(f"\n📋 Facts collected about {self.person_name.title()}:")
        for fact in sorted(self.facts):
            if self.person_name in fact:
                print(f"   • {fact}")
        
        # Show derived facts
        new_facts = set(derived_facts) - set(initial_facts)
        if new_facts:
            print(f"\n🧠 Additional facts derived:")
            for fact in sorted(new_facts):
                if self.person_name in fact:
                    print(f"   • {fact}")
        
        # Backward chaining analysis for confirmed types
        if found_types:
            print(f"\n🔄 Backward Chaining Verification:")
            print("-" * 40)
            
            for found_type in found_types:
                goal_template = f"(?x) is {found_type.lower().replace(' ', '_')}"
                goal = goal_template.replace('(?x)', self.person_name)
                try:
                    goal_tree = backward_chain(self.rules, goal, verbose=False)
                    print(f"\n🎯 Verification for {found_type}:")
                    print(f"   Goal: {goal}")
                    print(f"   Tree: {goal_tree}")
                except Exception as e:
                    print(f"   Error verifying {goal}: {e}")
        
        return results
    
    def run_demo(self):
        """Run a demonstration with sample data"""
        print("\n" + "="*60)
        print("DEMONSTRATION MODE - 3 Question Types")
        print("="*60)
        print("Demonstrating all three question types with sample scenarios...\n")
        
        # Demo the three question types
        print("🎯 QUESTION TYPE DEMONSTRATIONS:")
        print("\n1️⃣ YES/NO Question Example:")
        print("   Question: Does the person have digital implants?")
        print("   Answer: yes → Fact: person has digital_implants")
        
        print("\n2️⃣ MULTIPLE CHOICE Question Example:")
        print("   Question: What type of technological enhancement does the person have?")
        print("   Options: a) Digital implants  b) Basic device  c) None  d) Unknown  e) Other")
        print("   Answer: a → Fact: person has digital_implants")
        print("   Answer: e → No fact generated (skipped)")
        
        print("\n3️⃣ SCALE Question Example:")
        print("   Question: How would you rate the person's typing speed? (1-5)")
        print("   Scale: 1-Very slow, 2-Slow, 3-Average, 4-Fast, 5-Extremely fast")
        print("   Answer: 5 → Fact: person types_rapidly")
        
        print(f"\n{'='*60}")
        print("Sample Character Analysis:")
        
        # Test with sample data from the remaining characters
        sample_people = [
            ("Zara (Cyber Hacker)", [
                "zara has glowing_eyes", "zara wears neural_headset", 
                "zara types_rapidly", "zara speaks_in_code"
            ]),
            ("Dr. Kane (Bio Engineer)", [
                "kane has lab_coat", "kane carries_samples", 
                "kane wears safety_goggles"
            ]),
            ("Rex (Space Mechanic)", [
                "rex has oil_stains", "rex carries_plasma_torch", 
                "rex has reinforced_gloves"
            ]),
            ("Byte (Cyber Dog)", [
                "byte has_cyber_fur", "byte emits_electronic_barks", 
                "byte has_data_collar"
            ])
        ]
        
        for person_name, person_facts in sample_people:
            print(f"\n🧑 Analyzing {person_name}:")
            print("-" * 30)
            
            # Forward chaining
            results = forward_chain(self.rules, person_facts, verbose=False)
            
            print("Facts:")
            for fact in person_facts:
                print(f"  • {fact}")
                
            print("Conclusions:")
            for result in results:
                if " is " in result and any(character_type in result for character_type in 
                                         ['cyber_hacker', 'bio_engineer', 'space_mechanic', 
                                          'quantum_scientist', 'ice_world_explorer',
                                          'cyber_dog', 'hover_bird', 'phase_cat']):
                    print(f"  ✅ {result}")


def main():
    system = TouristExpertSystem()
    
    print("Cyber-City Character Detection Expert System")
    print("🎯 Featuring 3 Types of Questions:")
    print("   📝 Yes/No Questions")
    print("   🔢 Multiple Choice Questions (with 'Other/None' option)") 
    print("   📊 Scale/Rating Questions")
    print("\nChoose an option:")
    print("1. Interactive Analysis (Smart Questioning)")
    print("2. Demo Mode (Show Question Types)")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            system.interactive_session()
        elif choice == '2':
            system.run_demo()
        elif choice == '3':
            print("Thank you for using the Character Detection System!")
            break
        else:
            print("Please enter 1, 2, or 3.")
            
        # Ask if user wants to continue
        if choice in ['1', '2']:
            continue_choice = input("\nWould you like to run another analysis? (yes/no): ").lower().strip()
            if continue_choice in ['no', 'n']:
                print("Thank you for using the Character Detection System!")
                break


if __name__ == '__main__':
    main()
