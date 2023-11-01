export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
    const students = listOfStudents.filter((student) => student.location === city);

    const updatedStudent = students.map((student) => {
        const grades = newGrades.find((grade) => grade.studentId === student.id);
        const grade = grades ? grades.grade : 'N/A';
        
        return {
        ...student,
        grade,
    };
    });

    return updatedStudent;
}