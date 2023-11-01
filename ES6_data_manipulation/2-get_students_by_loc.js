export default function getStudentsByLocation(listOfStudent, city) {
    return listOfStudent.filter((citiies) => citiies.location === city);
}