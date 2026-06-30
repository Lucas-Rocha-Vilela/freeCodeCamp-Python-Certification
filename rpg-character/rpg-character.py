full_dot = '●'
empty_dot = '○'

def points_count(points):
    points_stats = ''
    points_stats += full_dot * points
    points_stats += empty_dot * (10 - points)
    return points_stats

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    if not len(character_name):
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if character_name.find(' ') >= 0:
        return 'The character name should not contain spaces'
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    
    STR = points_count(strength)
    INT = points_count(intelligence)
    CHA = points_count(charisma)

    return character_name + '\nSTR ' + STR + '\nINT ' + INT + '\nCHA ' + CHA

#print(create_character('ren', 4, 2, 1))


