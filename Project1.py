from os import system,name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def menu():
    global choice
    print("\nเมนู\n    1.เพิ่มรายวิชา \n    2.ถอนรายวิชา\n    3.แสดงจำนวนหน่วยกิต พร้อมจำนวนเงินที่ต้องจ่าย\n    4.ยืนยันการลงทะเบียน\n    5.ออกจากระบบ")
    choice = input("คำตอบ : ")
def place():
    clear()
    for x in range (0,len(A)):
        if choice == "1":
            if A[x] == "001": u[0] += 3
            elif A[x] == "002": u[1] += 3
            elif A[x] == "003": u[2] += 2  
            elif A[x] == "004": u[3] += 2
            elif A[x] == "005": u[4] += 3 
            elif A[x] == "006": u[5] += 2      
            elif A[x] == "007": u[6] += 3
        elif choice == "2":
            if A[x] == "001": u[0] = 0
            elif A[x] == "002": u[1] = 0
            elif A[x] == "003": u[2] = 0 
            elif A[x] == "004": u[3] = 0
            elif A[x] == "005": u[4] = 0
            elif A[x] == "006": u[5] = 0   
            elif A[x] == "007": u[6] = 0
def show():
    clear()
    print("\n{0:-<80}\n{1:<7}{2:<18}{3:<25}{4:<11}{5:}\n{6:-<80}".format("","ลำดับ","รหัสวิชา","ชื่อวิชา","หน่วยกิต","จำนวนหน่วยกิตวิชาที่เลือก",""))
    print("{0:<50}{1:<15}{2:<12}{3:}".format(" [1]    001     วิชาคณิตศาสตร์ (MATH)","3",u[0],"หน่วย"))
    print("{0:<49}{1:<15}{2:<12}{3:}".format(" [2]    002     วิชาภาษาอังกฤษ (ENGLISH)","3",u[1],"หน่วย"))
    print("{0:<49}{1:<15}{2:<12}{3:}".format(" [3]    003     วิชาศิลปะ (ART)","2",u[2],"หน่วย"))
    print("{0:<50}{1:<15}{2:<12}{3:}".format(" [4]    004     วิชาชีววิทยา (BIOLOGY)","2",u[3],"หน่วย"))
    print("{0:<51}{1:<15}{2:<12}{3:}".format(" [5]    005     วิชาฟิสิกส์ (PHYSICS)","3",u[4],"หน่วย"))
    print("{0:<50}{1:<15}{2:<12}{3:}".format(" [6]    006     วิชาคอมพิวเตอร์ (COMPUTER)","2",u[5],"หน่วย"))
    print("{0:<49}{1:<15}{2:<12}{3:}".format(" [7]    007     วิชาเคมี (CHEMICAL)","3",u[6],"หน่วย"))
    print("{0:-<80}\n{1:<66}{2:<12}{3:}\n{4:-<80}".format("","จำนวนหน่วยกิตทั้งหมด",total,"หน่วย",""))
q,total,A,d,real,dat,u,loop,loop2 = 0,0,[],[],[],[],[0,0,0,0,0,0,0],0,0
while loop == 0:
    clear()
    while True:
        u,total,loop,loop2=[0,0,0,0,0,0,0],0,0,0
        print("\n WELCOME TO TT SCHOOL")
        print("\n กรุณากรอกข้อมูล")
        print('\n > รหัสนักเรียน / ชื่อ-สกุล')
        try:
            stu_id,stu_name = input(" กรอกข้อมูล > ").split("/")
            break
        except ValueError:
            print("\nกรุณากรอกใหม่\n")
    while loop2 == 0:
        menu()
        if choice == "1":
            show()
            while True:
                print("เพิ่ม")
                print("\n ตัวอย่าง > รหัสวิชา - รหัสวิชา - ....")    
                A = input(" กรอกรหัสวิชา > ").split("-")
                place()
                total = u[0]+u[1]+u[2]+u[3]+u[4]+u[5]+u[6]
                if (total > 0 and total <= 12) and u[0]<=3 and u[1]<=3 and u[2]<=2 and u[3]<=2 and u[4]<=3 and u[5]<=2 and u[6]<=3 :
                    show()
                    break
                else:
                    print("\nหน่วยกิตเกิน 12 หน่วย กรุณากรอกใหม่อีกครั้ง\n")
                    u = [0,0,0,0,0,0,0]
        elif choice == "2":
            show()
            print("ถอน")
            print("\n > รหัสวิชา - รหัสวิชา - ....")
            A = input(" กรอกรหัสวิชา > ").split("-")   
            place()
            total = u[0]+u[1]+u[2]+u[3]+u[4]+u[5]+u[6]
            show()
        elif choice == "3":
            all_t = total*150
            show()
            print("{0:<65}{1:<12}{2:}\n{3:-<80}".format("จำนวนเงินทั้งหมด",all_t,"บาท",""))
        elif choice == "4":
            total = u[0]+u[1]+u[2]+u[3]+u[4]+u[5]+u[6]
            all_t = total*150
            d = stu_id + ":" + stu_name+":"+str(total)+":"+str(all_t)
            fdata = open('T:\\datatest.txt','a')
            fdata.write('\n[%s/%s] |\n%d %s\n%d %s\n%d %s\n%d %s\n%d %s\n%d %s\n%d %s\n| %d:%d |\n'%(stu_id,stu_name,u[0],"(MATH)",u[1],"(ENGLISH)",u[2],"(ART)",u[3],"(BIOLOGY)",u[4],"(PHYSICS)",u[5],"(COMPUTER)",u[6],"(CHEMICAL)",total,all_t))
            dat.append(d) 
            print("\n{0:=<80}".format(""))
            for x in dat:
                real = x.split(":")
                print("รหัสนักเรียน  {0[0]:<10}ชื่อ-สกุล {0[1]:<20}หน่วยกิต {0[2]:<2} หน่วย   ราคา {0[3]:<4} บาท".format(real))
            print("{0:=<80}".format(""))
            u,total=[0,0,0,0,0,0,0],0
            while loop == 0:
                clear()
                print("\n คุณต้องการทำอีกครั้งหรือไม่\n\t 1.ใช่ \n\t 2.ไม่")
                ans = input("คำตอบ > ")
                if ans == "1":
                    loop = 0
                    loop2 = 1
                    break
                elif ans == "2":
                    loop2 = 1
                    loop = 1
                    print("\nลงทะเบียนสำเร็จ\n")
                    break
                else:
                    print("กรุณากรอกให้ตรงตามเมนู")
        elif choice == "5":
            print("\nลงทะเบียนสำเร็จ\n")
            loop = 1
            break
        else:
            print("\nERROR\n")
