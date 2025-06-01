import unittest
from source_code.patients import Patients
from source_code.appointment import Appointment

class TestDentistSystem(unittest.TestCase):

    def test_add_patient(self):
        # Test if a Patients object is created correctly
        p = Patients("abf345", "James", "Webb", 25, "F", "01.01.1996", "123456789")
        self.assertEqual(p.first_name, "James")
        self.assertEqual(p.age, 25)
        self.assertEqual(p.to_dict()["last_name"], "Webb")

    def test_book_appointment(self):
        # Test if Appointment object stores correct values
        a = Appointment("app456", "id123", "01.06.2025", "10:00")
        self.assertEqual(a.date, "01.06.2025")
        self.assertEqual(a.status, "booked")
        self.assertEqual(a.to_dict()["patient_id"], "id123")

    def test_cancel_appointment(self):
        # Change status and check
        a = Appointment("app456", "id123", "01.06.2025", "10:00")
        a_dict = a.to_dict()
        a_dict["status"] = "cancelled"
        self.assertEqual(a_dict["status"], "cancelled")




if __name__ == '__main__':
    unittest.main()