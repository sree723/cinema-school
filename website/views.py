from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def department(request, department_name):

    departments = {

        "direction": {
            "number": "01",
            "title": "Direction",
            "subtitle": "THE ART OF SEEING",
            "description": (
                "A director does not simply tell a story. "
                "A director decides how the audience experiences it."
            ),

            "faculty": [
                {
                    "name": "Steven Spielberg",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Storytelling · Blocking · Suspense",
                    "bio": (
                        "Explore story-driven direction, visual emotion, "
                        "character movement and the relationship between "
                        "camera, actor and audience."
                    ),
                },
                {
                    "name": "Akira Kurosawa",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Composition · Movement · Staging",
                    "bio": (
                        "Study composition, staging, movement and the "
                        "construction of powerful cinematic moments."
                    ),
                },
            ],

            "skills": [
                "Visual storytelling",
                "Directing actors",
                "Shot design",
                "Blocking",
                "Mise-en-scène",
                "Camera language",
                "Scene construction",
                "Directing action",
            ],
        },


        "cinematography": {
            "number": "02",
            "title": "Cinematography",
            "subtitle": "PAINT WITH LIGHT",
            "description": (
                "Before the audience understands a scene, "
                "they already feel its light."
            ),

            "faculty": [
                {
                    "name": "Roger Deakins",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Light · Composition · Visual Restraint",
                    "bio": (
                        "Learn how light, framing, lenses and camera movement "
                        "can create emotion without distracting from the story."
                    ),
                },
                {
                    "name": "Santosh Sivan",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Colour · Camera · Indian Visual Language",
                    "bio": (
                        "Explore visual storytelling through colour, landscape, "
                        "camera movement and the distinctive language of Indian cinema."
                    ),
                },
            ],

            "skills": [
                "Lighting design",
                "Camera & lenses",
                "Composition",
                "Colour theory",
                "Exposure",
                "Camera movement",
                "Natural light",
                "Visual storytelling",
            ],
        },


        "screenwriting": {
            "number": "03",
            "title": "Screenwriting",
            "subtitle": "BEFORE THE CAMERA ROLLS",
            "description": (
                "Every great film begins as something "
                "that exists only in words."
            ),

            "faculty": [
                {
                    "name": "Satyajit Ray",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Character · Structure · Observation",
                    "bio": (
                        "Study character-driven storytelling, human observation, "
                        "structure and the subtle details that make stories believable."
                    ),
                },
                {
                    "name": "David Mamet",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Dialogue · Conflict · Scene Construction",
                    "bio": (
                        "Explore dialogue, conflict, scene construction and "
                        "the dramatic architecture of a screenplay."
                    ),
                },
            ],

            "skills": [
                "Story structure",
                "Character development",
                "Dialogue",
                "Scene writing",
                "Screenplay formatting",
                "Conflict",
                "Subtext",
                "Adaptation",
            ],
        },


        "acting": {
            "number": "04",
            "title": "Acting",
            "subtitle": "BECOME THE CHARACTER",
            "description": (
                "The camera sees everything. "
                "There is nowhere for false emotion to hide."
            ),

            "faculty": [
                {
                    "name": "Daniel Day-Lewis",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Transformation · Physicality · Immersion",
                    "bio": (
                        "Explore character transformation, physical preparation, "
                        "emotional commitment and immersive performance."
                    ),
                },
                {
                    "name": "Al Pacino",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Voice · Presence · Emotional Intensity",
                    "bio": (
                        "Study screen presence, voice, emotional intensity, "
                        "character energy and the relationship between actor and camera."
                    ),
                },
            ],

            "skills": [
                "Character creation",
                "Emotional preparation",
                "Screen presence",
                "Voice & movement",
                "Improvisation",
                "Scene study",
                "Camera acting",
                "Character psychology",
            ],
        },


        "editing": {
            "number": "05",
            "title": "Editing",
            "subtitle": "THE INVISIBLE ART",
            "description": (
                "A cut is not simply where one shot ends. "
                "It is where one thought becomes another."
            ),

            "faculty": [
                {
                    "name": "B. Lenin",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Rhythm · Emotion · Narrative Structure",
                    "bio": (
                        "Explore rhythm, emotional editing, narrative structure "
                        "and the invisible decisions that shape a film."
                    ),
                },
                {
                    "name": "V. T. Vijayan",
                    "role": "MASTERCLASS FACULTY",
                    "speciality": "Continuity · Pace · Montage",
                    "bio": (
                        "Study continuity, pacing, montage and the relationship "
                        "between performance, image and rhythm."
                    ),
                },
            ],

            "skills": [
                "Continuity editing",
                "Montage",
                "Cutting on action",
                "Rhythm",
                "Scene construction",
                "Pacing",
                "Sound-image relationship",
                "Emotional editing",
            ],
        },
    }


    department_data = departments.get(department_name)

    if not department_data:
        return render(request, "website/home.html")

    return render(
        request,
        "website/department.html",
        {
            "department": department_data
        }
    )