class Solution:
    def countStudents(self, students, sandwiches) -> int:
        n =  len(students)
        cnt=0
        while True:
            print(students,sandwiches)
            if students[0]!=sandwiches[0]:
                students.append(students.pop(0))
                cnt+=1            
            else:
                students.pop(0)
                sandwiches.pop(0)
                cnt=0
            if cnt==len(students):
                break 
        return cnt
        