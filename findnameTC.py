import os

def search_files(directory, keyword):
    # Duyệt qua tất cả các tệp trong thư mục
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        # Kiểm tra xem tệp có phải là tệp văn bản không
        if os.path.isfile(filepath) and filename.endswith('.can'):
            # Mặc định không tìm thấy chuỗi trong tệp
            found = False
            # Đọc nội dung của tệp
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                # Kiểm tra xem từ khóa có trong nội dung của tệp không
                if keyword not in content:
                    # Nếu từ khóa không được tìm thấy, đặt biến found thành True
                    found = True
                elif "\\" in content:
                    # Nếu có dấu "\\" trong nội dung, kiểm tra xem từ khóa xuất hiện sau dấu "\\"
                    index = content.find("\\")
                    if index != -1 and keyword in content[index:]:
                        found = True
            # Nếu không tìm thấy từ khóa trong tệp, in ra tên tệp
            if found:
                print("File:", filename)

# Thư mục nhập và từ khóa cần tìm
input_folder = "input"
keyword = "testwaitfortesterconfirmation"

# Gọi hàm search_files với thư mục và từ khóa
search_files(input_folder, keyword)
