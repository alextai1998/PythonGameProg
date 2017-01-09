"""
This will serve as the main Python file for HW #15
"""
import stafflib as sl

sl.register("Alex", "Tai", 17, "Nov. 15, 1998", "Student", 1, 100000000)
sl.register("Sabrina", "Ho", 17, "Nov. 7, 1998", "Student", 321, 20)
sl.register("Stephanie", "Chang", 16, "Jun. 22, 2000", "Student", 777, 12345)
sl.register("Cici", "Chen", 16, "May. 30, 2000", "Student", 1717, 500)
sl.register("Willa", "Lin", 15, "Nov. 15, 1998", "Student", 123, 9000000)

sl.show_emp()
sl.days_inc()
sl.show_emp()

sl.delist("Sabrina", "Ho")
sl.show_emp()
