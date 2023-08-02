pair={"courseNumber":"RoomNumber","CS101":3004,"CS102":4501,"CS103":6755,"NT110":1244,"CM241":1411}
print(pair)

pair2={'CourseNumber': 'Instructor', 'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

print(pair2)

pair3={'CourseNumber':"meetingTime", 'CS101': "8:00am", 'CS102': "9:00am", 'CS103': "10:00am", 'NT110': "11:00am", 'CM241': "1:00pm"}

print(pair3)

def create_course_room_dict():
    return {
        'CS101': '3004',
        'CS102': '1411',
        'CS103': '4501',
        'NT110': '1244',
        'CM241': '6755',
    }

def create_instructor_dict():
    return {
        'CS101': 'Haynes',
        'CS102': 'Lee',
        'CS103': 'Alvarado Rich',
        'NT110': 'Burke',
        'CM241': 'Lee',
    }

def create_meeting_time_dict():
    return {
        'CS101': '8:00 a.m.',
        'CS102': '9:00 a.m.',
        'CS103': '9:00 a.m.',
        'NT110': '10:00 a.m. / 11:00 a.m.',
        'CM241': '1:00 p.m.',
    }

def main():
    course_room_dict = create_course_room_dict()
    instructor_dict = create_instructor_dict()
    meeting_time_dict = create_meeting_time_dict()

    course_number = input("Enter a course number: ")

    if course_number in course_room_dict:
        room_number = course_room_dict[course_number]
        instructor = instructor_dict[course_number]
        meeting_time = meeting_time_dict[course_number]

        print(f"Course Number: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")
    else:
        print("Course number not found.")

if _name_ == "_main_":
    main()
