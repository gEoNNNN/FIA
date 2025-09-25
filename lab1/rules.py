from production import IF, AND, THEN, OR, DELETE, NOT, FAIL

# Character Detection Rules for Cyber-City
TOURIST_RULES = (
    
    # Rules for determining character types based on characteristics
    
    # Cyber Hacker Rules
    IF( AND( '(?x) has digital_implants',         # T1
             '(?x) has glowing_eyes' ),
        THEN( '(?x) is cyber_hacker' )),
    
    IF( AND( '(?x) wears neural_headset',         # T2  
             '(?x) types_rapidly',
             '(?x) speaks_in_code' ),
        THEN( '(?x) has digital_implants' )),
    
    # Bio Engineer Rules  
    IF( AND( '(?x) has lab_coat',                 # T3
             '(?x) carries_samples',
             '(?x) wears safety_goggles' ),
        THEN( '(?x) is bio_engineer' )),
    
    # Space Mechanic Rules
    IF( AND( '(?x) has oil_stains',               # T4
             '(?x) carries_plasma_torch',
             '(?x) has reinforced_gloves' ),
        THEN( '(?x) is space_mechanic' )),
    
    # Quantum Scientist Rules
    IF( AND( '(?x) has energy_scanner',           # T5
             '(?x) wears quantum_suit',
             '(?x) has particle_detector' ),
        THEN( '(?x) is quantum_scientist' )),
    
    # Ice World Explorer Rules
    IF( AND( '(?x) has thermal_gear',             # T6
             '(?x) has frost_crystals',
             '(?x) moves_carefully' ),
        THEN( '(?x) is ice_world_explorer' )),
    
    # Animal-specific rules
    IF( AND( '(?x) has_cyber_fur',                # T7
             '(?x) emits_electronic_barks',
             '(?x) has_data_collar' ),
        THEN( '(?x) is cyber_dog' )),
    
    IF( AND( '(?x) has_metallic_feathers',        # T8
             '(?x) hovers_with_antigrav',
             '(?x) makes_digital_chirps' ),
        THEN( '(?x) is hover_bird' )),
    
    IF( AND( '(?x) has_sensor_whiskers',          # T9
             '(?x) purrs_electronically',
             '(?x) phases_through_walls' ),
        THEN( '(?x) is phase_cat' )),
    
    # Additional characteristic rules
    IF( AND( '(?x) glitches_frequently' ),        # T10
        THEN( '(?x) has digital_implants' )),
    
    IF( AND( '(?x) speaks_binary' ),              # T11
        THEN( '(?x) has_cyber_origins' )),
    
    IF( AND( '(?x) has_cyber_origins',            # T12
             '(?x) has digital_implants' ),
        THEN( '(?x) is cyber_hacker' )),
    
    IF( AND( '(?x) complains_about_system_lag' ), # T13
        THEN( '(?x) has digital_implants' )),
)

# Sample data for testing - 4 humans and 3 animals
TOURIST_DATA = (
    # Zara - Cyber Hacker (Human)
    'zara has glowing_eyes',
    'zara wears neural_headset',
    'zara types_rapidly',
    'zara speaks_in_code',
    'zara glitches_frequently',
    'zara speaks_binary',
    'zara complains_about_system_lag',
    
    # Dr. Kane - Bio Engineer (Human)
    'kane has lab_coat',
    'kane carries_samples', 
    'kane wears safety_goggles',
    
    # Rex - Space Mechanic (Human)
    'rex has oil_stains',
    'rex carries_plasma_torch',
    'rex has reinforced_gloves',
    
    # Dr. Frost - Ice World Explorer (Human)
    'frost has thermal_gear',
    'frost has frost_crystals',
    'frost moves_carefully',
    
    # Byte - Cyber Dog (Animal)
    'byte has_cyber_fur',
    'byte emits_electronic_barks',
    'byte has_data_collar',
    
    # Pixel - Hover Bird (Animal)
    'pixel has_metallic_feathers',
    'pixel hovers_with_antigrav',
    'pixel makes_digital_chirps',
    
    # Ghost - Phase Cat (Animal)
    'ghost has_sensor_whiskers',
    'ghost purrs_electronically',
    'ghost phases_through_walls',
)

# Goal definitions for backward chaining
TOURIST_GOALS = [
    '(?x) is cyber_hacker',
    '(?x) is bio_engineer', 
    '(?x) is space_mechanic',
    '(?x) is quantum_scientist',
    '(?x) is ice_world_explorer',
    '(?x) is cyber_dog',
    '(?x) is hover_bird',
    '(?x) is phase_cat'
]
