class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient_id, name, age, gender, diagnosis):
        patient = {
            'ID': patient_id,
            'Name': name,
            'Age': age,
            'Gender': gender,
            'Diagnosis': diagnosis
        }
        self.patients.append(patient)

    def display_patients(self):
        if not self.patients:
            print("No patients in the system.")
        else:
            for patient in self.patients:
                self.display_patient_info(patient)

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient['ID'] == patient_id:
                self.display_patient_info(patient)
                return
        print(f"Patient with ID {patient_id} not found.")

    def delete_patient(self, patient_id):
        for patient in self.patients:
            if patient['ID'] == patient_id:
                self.patients.remove(patient)
                print(f"Patient with ID {patient_id} has been deleted.")
                return
        print(f"Patient with ID {patient_id} not found.")

    def update_patient(self, patient_id, name, age, gender, diagnosis):
        for patient in self.patients:
            if patient['ID'] == patient_id:
                patient['Name'] = name
                patient['Age'] = age
                patient['Gender'] = gender
                patient['Diagnosis'] = diagnosis
                print(f"Patient with ID {patient_id} has been updated.")
                return
        print(f"Patient with ID {patient_id} not found.")

    def display_patient_info(self, patient):
        print("Patient ID:", patient['ID'])
        print("Name:", patient['Name'])
        print("Age:", patient['Age'])
        print("Gender:", patient['Gender'])
        print("Diagnosis:", patient['Diagnosis'])
        print("\n")


def main():
    hospital_system = HospitalManagementSystem()

    while True:
        print("Hospital Management System")
        print("1. Add Patient")
        print("2. Display All Patients")
        print("3. Search Patient by ID")
        print("4. Delete Patient by ID")
        print("5. Update Patient by ID")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            patient_id = input("Enter Patient ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            diagnosis = input("Enter Diagnosis: ")
            hospital_system.add_patient(patient_id, name, age, gender, diagnosis)
            print("Patient details added successfully.")

        elif choice == 2:
            hospital_system.display_patients()

        elif choice == 3:
            patient_id = input("Enter Patient ID to search: ")
            hospital_system.search_patient(patient_id)

        elif choice == 4:
            patient_id = input("Enter Patient ID to delete: ")
            hospital_system.delete_patient(patient_id)

        elif choice == 5:
            patient_id = input("Enter Patient ID to update: ")
            name = input("Enter New Name: ")
            age = input("Enter New Age: ")
            gender = input("Enter New Gender: ")
            diagnosis = input("Enter New Diagnosis: ")
            hospital_system.update_patient(patient_id, name, age, gender, diagnosis)

        elif choice == 6:
            print("Exiting Hospital Management System.")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
