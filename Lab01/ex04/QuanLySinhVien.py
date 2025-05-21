
from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = max(sv._id for sv in self.listSinhVien)
        return maxId + 1

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ").strip()
        if not name:
            print("Tên không được để trống!")
            return
        sex = input("Nhập giới tính sinh viên: ").strip()
        major = input("Nhập chuyên ngành của sinh viên: ").strip()
        try:
            diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
            if not 0 <= diemTB <= 10:
                raise ValueError("Điểm trung bình phải từ 0 đến 10!")
        except ValueError:
            print("Vui lòng nhập điểm là số hợp lệ (0-10)!")
            return
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            name = input("Nhập tên sinh viên: ").strip()
            if not name:
                print("Tên không được để trống!")
                return
            sex = input("Nhập giới tính sinh viên: ").strip()
            major = input("Nhập chuyên ngành của sinh viên: ").strip()
            try:
                diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
                if not 0 <= diemTB <= 10:
                    raise ValueError("Điểm trung bình phải từ 0 đến 10!")
            except ValueError:
                print("Vui lòng nhập điểm là số hợp lệ (0-10)!")
                return
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID {ID} không tồn tại.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def sortByMajor(self):  # Thêm để hỗ trợ sắp xếp theo chuyên ngành
        self.listSinhVien.sort(key=lambda x: x._major, reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        else:
            sv._hocLuc = "Trung bình"

    def showSinhVien(self, listSV):
        if not listSV:
            print("Không tìm thấy sinh viên nào!")
            return
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("ID", "Tên", "Giới tính", "Chuyên ngành", "Điểm TB", "Học lực"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))

    def getListSinhVien(self):
        return self.listSinhVien