from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("****************************** Menu ******************************")
    print("** 1. Thêm sinh viên. **")
    print("** 2. Cập nhật thông tin sinh viên bởi ID. **")
    print("** 3. Xóa sinh viên bởi ID. **")
    print("** 4. Tìm kiếm sinh viên theo tên. **")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình. **")
    print("** 6. Sắp xếp sinh viên theo chuyên ngành. **")
    print("** 7. Hiển thị danh sách sinh viên. **")
    print("** 0. Thoát **")
    print("**********************************************************")

    try:
        key = int(input("Nhập tùy chọn: "))

        if key == 1:
            print("\n1. Thêm sinh viên.")
            qlsv.nhapSinhVien()
            print("\nThêm sinh viên thành công!")
        
        elif key == 2:
            if qlsv.soLuongSinhVien() > 0:
                print("\n2. Cập nhật thông tin sinh viên.")
                id = input("Nhập ID: ").strip()
                if id:
                    qlsv.updateSinhVien(id)
                else:
                    print("ID không được để trống!")
            else:
                print("\nDanh sách sinh viên trống!")
            
        elif key == 3:
            if qlsv.soLuongSinhVien() > 0:
                id = input("Nhập ID: ").strip()
                if id:
                    if qlsv.deleteById(id):
                        print(f"Sinh viên có ID = {id} đã bị xóa.")
                    else:
                        print(f"Sinh viên có ID = {id} không tồn tại.")
                else:
                    print("ID không được để trống!")
            else:
                print("\nDanh sách sinh viên trống!")
    
        elif key == 4:
            if qlsv.soLuongSinhVien() > 0:
                print("\n4. Tìm kiếm sinh viên theo tên.")
                name = input("Nhập tên để tìm kiếm: ").strip()
                if name:
                    search_result = qlsv.findByName(name)
                    qlsv.showSinhVien(search_result)
                else:
                    print("Tên không được để trống!")
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 5:
            if qlsv.soLuongSinhVien() > 0:
                print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA).")
                qlsv.sortByDiemTB()
                qlsv.showSinhVien(qlsv.getListSinhVien())
                print("Sắp xếp thành công!")
            else:
                print("\nDanh sách sinh viên trống!")
            
        elif key == 6:
            if qlsv.soLuongSinhVien() > 0:
                print("\n6. Sắp xếp sinh viên theo chuyên ngành.")
                qlsv.sortByMajor()  # Sửa để dùng sortByMajor
                qlsv.showSinhVien(qlsv.getListSinhVien())
                print("Sắp xếp thành công!")
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 7:
            if qlsv.soLuongSinhVien() > 0:
                print("\n7. Hiển thị danh sách sinh viên.")
                qlsv.showSinhVien(qlsv.getListSinhVien())
            else:
                print("\nDanh sách sinh viên trống!")

        elif key == 0:
            print("\nBạn đã chọn thoát chương trình!")
            break

        else:
            print("\nKhông có chức năng này!")
            print("\nHãy chọn chức năng trong hộp menu.")

    except ValueError:
        print("\nVui lòng nhập một số nguyên hợp lệ!")