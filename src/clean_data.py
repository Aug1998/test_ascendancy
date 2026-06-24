def clean_data(data: dict):
    people = []
    experiences = []
    educations = []
    companies = []
    schools = []
    
    for person in data["data"]:
        person_id = person.get("id")

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
                    for sm in person.get("social_media", [])
                    if sm.get("network") == "linkedin"
                ),
                None,
            ),
            "connections": next(
                (
                    sm.get("connections")
                    for sm in person.get("social_media", [])
                    if sm.get("network") == "linkedin"
                ),
                None,
            ),
        })

        # Experience table
        for exp in person.get("experience", []):
            experiences.append({
                "person_id": person_id,
                "person_name": person.get("full_name"),
                "company": exp.get("company", {}).get("name"),
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

        # Education table
        for edu in person.get("education", []):
            educations.append({
                "person_id": person_id,
                "school": edu.get("school", {}).get("name"),
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

    # Companies table
    for experience in experiences:
        companies.append(experience.get("company"))
    
    # Schools table
    for education in educations:
        schools.append(education.get("school"))
    
    return {
        "people": people,
        "experiences": experiences,
        "educations": educations,
        "companies": companies,
        "schools": schools
    }