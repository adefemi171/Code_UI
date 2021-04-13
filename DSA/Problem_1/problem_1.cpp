#include<iostream>
#include<ctime>
#include<fstream>
#include<stdlib.h>
#include<bits/stdc++.h>
using namespace std;

// Declare structure for student details
struct student_info 
{
	char first_name[60],middle_name[50],last_name[50],mobile_number[15],email[60];
    int matric_number,age;
};

//A function that sorts structure based on firstname using strcmp 
//that compares two strings together but in this case we comparing an array.
void sort_by_first_name(student_info student_biodata[],int size)
{
    int j;
    student_info temp;
    for(int i=1;i<size;i++){
        j= i-1;
        while(j>=0&&strcmp(student_biodata[j+1].first_name,student_biodata[j].first_name)<0){
            temp=student_biodata[j+1];
            student_biodata[j+1]=student_biodata[j];
            student_biodata[j]= temp;
            j--;
        } // end while
    } // end for
}; // end sort function


// Driver function
int main()
{
    int i,n;
    cout<<"Enter the number of student to process"<<endl;
    cin>>n;
    struct student_info biodata[n];
	
    for(int j=0; j<n; j++){
        cout<<"Enter Student " << (j+1) << " Information" <<endl;
		cout << "----------------------------------------------" << endl;
        cout<<"Enter your First Name: ";
        cin>>biodata[j].first_name;
		
        cout<<"Enter your Middle Name: ";
        cin>>biodata[j].middle_name;

        cout<<"Enter your Last Name: ";
        cin>>biodata[j].last_name;

        cout<<"Enter your Mobile Number: "<<endl;
        cin>>biodata[j].mobile_number;

        cout<<"Enter your Email Address: "<<endl;
        cin>>biodata[j].email;

        srand((unsigned)time(0));
        int lowest = 199354, highest = 200815;
        int range = highest - lowest;
        biodata[j].matric_number=lowest+(range*rand()/RAND_MAX+1);
        cout<<"Student "<<(j+1)<<" assigned matric number is: ";
        cout<<biodata[j].matric_number<<endl;

        cout<<"Enter your Age: ";
        cin>>biodata[j].age;
        cout<<endl;
    }// End for loop

	// Display Student data before sorting
    for(i=0;i<n;i++){
        cout<<"STUDENTS INFORMATION BEFORE SORTING";
		cout << "----------------------------------------------" << endl;
        cout<<"First Name: "<<biodata[i].first_name<<"";
        cout<<"Middle Name: "<<biodata[i].middle_name<<"";        
        cout<<"Last Name: "<<biodata[i].last_name<<"";        
        cout<<"Mobile Number: "<<biodata[i].mobile_number<<"";        
        cout<<"Email: "<<biodata[i].email<<"";
        cout<<"Matric Number: "<<biodata[i].matric_number<<"";
        cout<<"Age: "<<biodata[i].age<<"";        
        
		// Sort student information
        sort_by_first_name(biodata,n);
        printf("\n Student records sorted by First Name : \n");

        for(i=0;i<n;i++){
            printf("First Name= %s, Middle Name = %s, Last Name= %s, Mobile Number= %s, Email= %s, Matric Number= %i, Age= %i,\n",
                   biodata[i].first_name,biodata[i].middle_name,biodata[i].last_name,biodata[i].mobile_number,
                   biodata[i].email,biodata[i].matric_number,biodata[i].age);
        }// print out loop end

		// Writing output to file
        ofstream outfile;
        outfile.open("student_data.txt");
        if(!outfile){
            cout<<"Error: Unable to write record to file"<<endl;
        }
        else{
            cout<<"Writing record to file"<<endl;
            for(i=0;i<n;i++){
                outfile<<"First Name: " << biodata[i].first_name<<" "<<
                        "Middle Name: " << biodata[i].middle_name<<" "<<
                        "Last Name: " << biodata[i].last_name<<" "<<
                        "Mobile Number: " << biodata[i].mobile_number<<" "<<
                        "Email: " <<  biodata[i].email<<" "<<
                        "Matric Number: " << biodata[i].matric_number<<" "<<
                        "Age: " << biodata[i].age<<" "<<endl;
            }
            cout<<"Data successfully created and saved"<<endl;
            outfile.close();
        }
    }
    return 0;
}