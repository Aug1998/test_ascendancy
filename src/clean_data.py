def clean_data(data: dict):
    people = []
    experiences = []
    educations = []
    companies = []
    schools = []

    records = data.get("data", []) if isinstance(data, dict) else []
    valid_people = (person for person in records if isinstance(person, dict))

    for person in valid_people:

        person_id = person.get("id")
        social_media = person.get("social_media")
        social_media = social_media if isinstance(social_media, list) else []

        # Person table
        people.append({
            "person_id": person_id,
            "full_name": person.get("full_name"),
            "current_title": person.get("current_title"),
            "current_company": person.get("current_company_name"),
            "current_location": person.get("current_location"),
            "followers": next(
                (
                    sm.get("followers")
                    for sm in social_media
                    if isinstance(sm, dict) and sm.get("network") == "linkedin"
                ),
                None,
            ),
            "connections": next(
                (
                    sm.get("connections")
                    for sm in social_media
                    if isinstance(sm, dict) and sm.get("network") == "linkedin"
                ),
                None,
            ),
        })

        # Experience table
        experience_items = person.get("experience")
        experience_items = experience_items if isinstance(experience_items, list) else []
        for exp in experience_items:
            if not isinstance(exp, dict):
                continue

            company = exp.get("company")
            company = company if isinstance(company, dict) else {}
            experiences.append({
                "person_id": person_id,
                "person_name": person.get("full_name"),
                "company": company.get("name"),
                "title": exp.get("title"),
                "status": exp.get("status"),
                "start_date": exp.get("start_date"),
                "end_date": exp.get("end_date"),
                "is_current": exp.get("is_current", False),
                "seniority": (
                    exp.get("seniority", [None])[0]
                    if exp.get("seniority")
                    else None
                ),
            })
            companies.append(company.get("name"))

        # Education table
        education_items = person.get("education")
        education_items = education_items if isinstance(education_items, list) else []
        for edu in education_items:
            if not isinstance(edu, dict):
                continue

            school = edu.get("school")
            school = school if isinstance(school, dict) else {}
            educations.append({
                "person_id": person_id,
                "school": school.get("name"),
                "degree": (
                    edu.get("degrees", [None])[0]
                    if edu.get("degrees")
                    else None
                ),
                "major": (
                    edu.get("majors", [None])[0]
                    if edu.get("majors")
                    else None
                ),
                "start_date": edu.get("start_date"),
                "end_date": edu.get("end_date"),
            })
            schools.append(school.get("name"))
    
    return {
        "people": people,
        "experiences": experiences,
        "educations": educations,
        "companies": companies,
        "schools": schools
    }