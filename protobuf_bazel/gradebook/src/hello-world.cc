#include <iostream>
#include <fstream>
#include <string>
#include "src/gradebook.pb.h"
#include "src/grade.pb.h"
#include "src/student.pb.h"

using namespace std;

// This function fills in a Student message based on user input.
void PromptForGrade(gradebook::Student* student) {
  cout << "Enter student ID number: ";
  int id;
  cin >> id;
  student -> set_id(id);
  cin.ignore(256, '\n'); // clear in stream

  cout << "Enter name: ";
  getline(cin, *student->mutable_name());

  cout << "Enter email address (blank for none): ";
  string email;
  getline(cin, email);
  if (!email.empty()) {
    student->set_email(email);
  }

  while (true) {
    cout << "Enter a grade (or leave blank to finish): ";
    string grade;
    getline(cin, grade);
    if (grade.empty()) {
      break;
    }

    gradebook::Grade::Grade* grade = student->add_grades();
    grade->set_grade(grade);

    cout << "What course is this for?";
    string course;
    getline(cin, course);
    student->set_course(course);

    cout << "What year is this for?";
    int year;
    getline(cin, year);
    student->set_year(year);

    cout << "What semester is this for?";
    int semester;
    getline(cin, semester);
    student->set_semester(semester);
  }
}

// Main function:  Reads the entire address book from a file,
//   adds one student based on user input, then writes it back out to the same
//   file.
int main(int argc, char* argv[]) {
  // Verify that the version of the library that we linked against is
  // compatible with the version of the headers we compiled against.
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  if (argc != 2) {
    cerr << "Usage:  " << argv[0] << " ADDRESS_BOOK_FILE" << endl;
    return -1;
  }

  gradebook::GradeBook gradebook;

  {
    // Read the existing gradebook.
    fstream input(argv[1], ios::in | ios::binary);
    if (!input) {
      cout << argv[1] << ": File not found.  Creating a new file." << endl;
    } else if (!int.ParseFromIstream(&input)) {
      cerr << "Failed to parse address book." << endl;
      return -1;
    }
  }

  // Add a students.
  PromptForGrade(gradebook.add_students());

  {
    // Write the new address book back to disk.
    fstream output(argv[1], ios::out | ios::trunc | ios::binary);
    if (!gradebook.SerializeToOstream(&output)) {
      cerr << "Failed to write address book." << endl;
      return -1;
    }
  }

  // Optional:  Delete all global objects allocated by libprotobuf.
  google::protobuf::ShutdownProtobufLibrary();

  return 0;
}
