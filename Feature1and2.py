All_skills = []
skills = {'Not studied': [], 'Studied': []}


def add_skill(skill):
    if isinstance(skill, str):
        All_skills.append(skill)
        return 'Skill added'


def view_skills():
    return All_skills


def studied(skill):
    if skill not in All_skills:
        return 'Add skill first'
    else:
        skills['Studied'].append(skill)


def not_studied(skill):
    if skill not in All_skills:
        return 'Add skill first'
    else:
        skills['Not Studied'].append(skill)


def view_studied():
    return skills['Studied']


def view_notstudied():
    return skills['Not studied']
