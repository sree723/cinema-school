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
def apply(request):
    return render(request, "website/apply.html")


def faculty(request, faculty_name):

    faculty_members = {

        "kamal": {
            "name": "Kamal Haasan",
            "role": "VICE PRINCIPAL",
            "speciality": "Acting · Direction · Screenwriting",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Kamal_Haasan.jpg",
            "about": "Kamal Haasan is one of the most versatile figures in Indian cinema, known for his work as an actor, filmmaker, screenwriter and producer.",
            "films": [
                "Nayakan",
                "Indian",
                "Thevar Magan",
                "Dasavathaaram",
                "Vikram",
            ],
        },

        "balu": {
            "name": "Balu Mahendra",
            "role": "VICE CHANCELLOR",
            "speciality": "Cinematography · Direction",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Balu_Mahendra.JPG",
            "about": "Balu Mahendra was an acclaimed cinematographer, filmmaker and director known for his distinctive visual style and naturalistic storytelling.",
            "films": [
                "Moondram Pirai",
                "Veedu",
                "Sandhya Raagam",
                "Maro Charitra",
            ],
        },

        "kubrick": {
            "name": "Stanley Kubrick",
            "role": "ASSISTANT PROFESSOR",
            "speciality": "Screenplay · Visual Storytelling",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Stanley_Kubrick_(1949_portrait_by_Phillip_Harrington_-_cropped).jpg",
            "about": "Stanley Kubrick was an influential filmmaker known for meticulous visual composition, ambitious storytelling and distinctive cinematic techniques.",
            "films": [
                "2001: A Space Odyssey",
                "A Clockwork Orange",
                "The Shining",
                "Full Metal Jacket",
            ],
        },

        "hitchcock": {
            "name": "Alfred Hitchcock",
            "role": "PROFESSOR",
            "speciality": "Suspense · Camera · Visual Direction",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Alfred_Hitchcock_NYWTSm.jpg",
            "about": "Alfred Hitchcock was a pioneering filmmaker celebrated for suspense, visual storytelling and innovative cinematic techniques.",
            "films": [
                "Psycho",
                "Vertigo",
                "Rear Window",
                "North by Northwest",
            ],
        },

        "spielberg": {
            "name": "Steven Spielberg",
            "role": "VISITING PROFESSOR",
            "speciality": "Direction · Production · Storytelling",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Steven_Spielberg_portrait.jpg",
            "about": "Steven Spielberg is one of the most influential filmmakers in modern cinema, known for combining accessible storytelling with large-scale filmmaking.",
            "films": [
                "Jaws",
                "E.T. the Extra-Terrestrial",
                "Jurassic Park",
                "Saving Private Ryan",
            ],
        },

        "pacino": {
            "name": "Al Pacino",
            "role": "ACTING PROFESSOR",
            "speciality": "Acting · Character · Performance",
            "image": "https://commons.wikimedia.org/wiki/Special:Redirect/file/Al_Pacino.jpg",
            "about": "Al Pacino is an acclaimed actor known for powerful performances, distinctive screen presence and memorable character work.",
            "films": [
                "The Godfather",
                "Serpico",
                "Scarface",
                "Scent of a Woman",
            ],
        },
    }

    faculty_member = faculty_members.get(faculty_name)

    if not faculty_member:
        return render(request, "website/home.html")

    return render(
        request,
        "website/faculty.html",
        {
            "faculty": faculty_member
        }
    )