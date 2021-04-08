#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<bits/stdc++.h>
using namespace std;

// Declare structure for student details
struct student_info 
{
	char firstname [30], middlename[30], lastname[30], mobile_num[15], email[30]; int matric_num, age;
};
//A function that sorts structure based on firstname using strcmp 
//that compares two strings together but in this case we comparing an array.
void sort_by_fname(student_info student_data[], int size)
{
	int j;
	student_info temp;
	for(int i= 1; i<=size; i++){
		j=i-1;
		while(j>=0 && strcmp (student_data[j+1].firstname, student_data[j].firstname) < 0){
			temp= student_data[j+1];
			student_data [j+1]= student_data[j];
			student_data[j]= temp;
			j--;
		}// end while
		
	}// end for
	
	
} // end sort function

// Driver function
int main (){
	int i,n;
	cout << "Enter the number of student to process" << endl;
	cin >> n;
	struct student_info biodata[n];
	cout << "Enter information" << endl;

	cout << "----------------------------------------------" << endl;
	
	//Accepting user information
	for(int j=0; j<n; j++){
		cout << "Enter student information" << (j+1) << endl;

		cout << "----------------------------------------------" << endl;

		cout << "input your FirstName ";
		cin >> biodata[j].firstname;

		cout << "input your MiddleName ";
		cin >> biodata[j].middlename;

		cout << "input your LastName ";
		cin >> biodata[j].lastname;

		cout << "input your PhoneNumber ";
		cin >> biodata[j].mobile_num;

		cout << "input your Email Address ";
		cin>>biodata[j].email;
		
		// A function to assign mat_no to students
		srand((unsigned) time (0));
		//int random_number,n;
		int lowest= 18700, highset = 208111;
		int range = highset - lowest;
		biodata[j].matric_num = lowest + (range * rand() / RAND_MAX + 1);
		cout << "student " << (j+1)<<" assigned matric number is: ";
		cout << biodata[j].matric_num << endl;

		cout << "input your Age ";
		cin >> biodata[j].age;
		cout << endl;
	}// End for loop

	/* // string prompt ("Enter the number of mat to generate :");
	// 	cout<<prompt << endl;
	// 	cin>>n;
	// 	cout<<"mat_no you generated are listed:"<<endl;
	// 	for (int index = 0; index<n; index ++){
	// 		biodata[j].random_number;
			
	// 	} cout<<endl;
		
	// } */

	// Display Student data before sorting
	for (i=0; i < n; i++){
		// information received before sorting
		cout<<"/n STUDENTS INFORMATION BEFORE SORTING"<< endl;
		cout << "----------------------------------------------" << endl;
		cout<<"First Name :"<<biodata[i].firstname<<endl;
		cout<<"Middle Name :"<<biodata[i].middlename<<endl;
		cout<<"Last Name :"<<biodata[i].lastname<<endl;
		cout<<"Mobile Number :"<<biodata[i].mobile_num<<endl;
		cout<<"E-Mail :"<<biodata[i].email<<endl;
		cout<<"Matric No :"<<biodata[i].matric_num<<endl;
		cout<<"Age :"<<biodata[i].age<<endl;
		
	}

	// Sort student information
	sort_by_fname(biodata,n);
	printf("\n Student records sorted by First Name :\n");
	for (i=0; i<n; i++){
		printf("First Name=%s,Middle Name=%s,Last Name=%s,Mobile Number=%s,E-Mail=%s,Matric Number=%s,Age=%s \n",biodata[i].firstname,biodata[i].middlename,biodata[i].lastname,biodata[i].mobile_num,biodata[i].email,biodata[i].matric_num,biodata[i].age);
	} // print out loop end

	// Writing output to file
	ofstream outfile;
	outfile.open("student_data.txt");
	if (!outfile){
		cout << "Error: Unable to write record to file" << endl;
	}
	else {
		cout << "Writing record to file" << endl;

		for (i = 0; i < n; i++){
			outfile << biodata[i].firstname << " " << biodata[i].middlename << " " << biodata[i].lastname << " " << biodata[i].mobile_num << " " << biodata[i].email << " " << biodata[i].matric_num << " " << biodata[i].age << " " << endl;
		}
	cout << "Data successfully created and saved" << endl;
	outfile.close();
	}

	return 0;
}
